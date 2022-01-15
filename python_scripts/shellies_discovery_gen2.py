ATTR_FW_ID = "fw_id"
ATTR_FW_VER = "fw_ver"
ATTR_ID = "id"
ATTR_MAC = "mac"
ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_MODEL = "model"
ATTR_NAME = "name"

KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_COMMAND_TOPIC = "cmd_t"
KEY_CONNECTIONS = "cns"
KEY_DEVICE = "dev"
KEY_MAC = "mac"
KEY_MANUFACTURER = "mf"
KEY_MODEL = "mdl"
KEY_NAME = "name"
KEY_PAYLOAD_AVAILABLE = "pl_avail"
KEY_PAYLOAD_NOT_AVAILABLE = "pl_not_avail"
KEY_PAYLOAD_OFF = "pl_off"
KEY_PAYLOAD_ON = "pl_on"
KEY_QOS = "qos"
KEY_STATE_OFF = "stat_off"
KEY_STATE_ON = "stat_on"
KEY_STATE_TOPIC = "stat_t"
KEY_SW_VERSION = "sw"
KEY_UNIQUE_ID = "uniq_id"
KEY_VALUE_TEMPLATE = "val_tpl"

VALUE_FALSE = "false"
VALUE_TRUE = "true"

SUPPORTED_MODELS = {"SHPSW04P": "Shelly Pro 4PM", "SNSW-001P16EU": "Shelly Plus 1PM"}

def mqtt_publish(topic, payload, retain):
    """Publish data to MQTT broker."""
    payload_str = str(payload).replace("'", '"').replace("^", '\\"')
    service_data = {
        "topic": topic,
        "payload": payload_str,
        "retain": retain,
        "qos": 0,
    }
    logger.debug(service_data)  # noqa: F821
    logger.debug("Sending to MQTT broker: %s %s", topic, payload_str)  # noqa: F821
    hass.services.call("mqtt", "publish", service_data, False)  # noqa: F821

def format_mac(mac):
    """Format the mac address string."""
    return ":".join(mac[i : i + 2] for i in range(0, 12, 2))

def encode_config_topic(string):
    """Encode a config topic to UTF-8."""
    return string.encode("ascii", "ignore").decode("utf-8")

def configure_pro4pm():
    """Create configuration for Shelly Pro 4PM."""
    device_config = {}

    relays = 4

    for relay in range(relays):
        config_topic = encode_config_topic(f"{disc_prefix}/switch/{device_id}-{relay}/config")
        payload = {
            KEY_NAME: f"{device_name} Relay {relay}",
            KEY_COMMAND_TOPIC: f"~rpc",
            KEY_PAYLOAD_OFF: f"{{^id^: 1, ^src^:^{device_id}^, ^method^: ^Switch.Set^, ^params^: {{^id^: {relay}, ^on^: false}}}}",
            KEY_PAYLOAD_ON: f"{{^id^: 1, ^src^:^{device_id}^, ^method^: ^Switch.Set^, ^params^: {{^id^: {relay}, ^on^: true}}}}",
            KEY_STATE_TOPIC: f"~status/switch:{relay}",
            KEY_VALUE_TEMPLATE: "{{ value_json.output }}",
            KEY_STATE_ON: VALUE_TRUE,
            KEY_STATE_OFF: VALUE_FALSE,
            KEY_AVAILABILITY_TOPIC: f"~online",
            KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
            KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
            KEY_UNIQUE_ID: f"{device_id}-{relay}".lower(),
            KEY_QOS: qos,
            KEY_DEVICE: device_info,
            "~": f"{device_id}/",
        }
        device_config.update({config_topic: payload})

    return device_config

def configure_plus1pm():
    """Create configuration for Shelly Plus 1PM."""
    device_config = {}

    relays = 1

    for relay in range(relays):
        config_topic = encode_config_topic(f"{disc_prefix}/switch/{device_id}-{relay}/config")
        payload = {
            KEY_NAME: f"{device_name} Relay {relay}",
            KEY_COMMAND_TOPIC: f"~rpc",
            KEY_PAYLOAD_OFF: f"{{^id^: 1, ^src^:^{device_id}^, ^method^: ^Switch.Set^, ^params^: {{^id^: {relay}, ^on^: false}}}}",
            KEY_PAYLOAD_ON: f"{{^id^: 1, ^src^:^{device_id}^, ^method^: ^Switch.Set^, ^params^: {{^id^: {relay}, ^on^: true}}}}",
            KEY_STATE_TOPIC: f"~status/switch:{relay}",
            KEY_VALUE_TEMPLATE: "{{ value_json.output }}",
            KEY_STATE_ON: VALUE_TRUE,
            KEY_STATE_OFF: VALUE_FALSE,
            KEY_AVAILABILITY_TOPIC: f"~online",
            KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
            KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
            KEY_UNIQUE_ID: f"{device_id}-{relay}".lower(),
            KEY_QOS: qos,
            KEY_DEVICE: device_info,
            "~": f"{device_id}/",
        }
        device_config.update({config_topic: payload})

    return device_config

device_id = data.get(ATTR_ID)  # noqa: F821
firmware_id = data.get(ATTR_FW_ID)  # noqa: F821
firmware_ver = data.get(ATTR_FW_VER)  # noqa: F821
mac = data.get(ATTR_MAC)  # noqa: F821
model = data.get(ATTR_MODEL)  # noqa: F821
device_name = data.get(ATTR_NAME)  # noqa: F821

if device_id is None:
    raise ValueError("id value None is not valid, check script configuration")
if mac is None:
    raise ValueError("mac value None is not valid, check script configuration")
if model is None:
    raise ValueError("model value None is not valid, check script configuration")
if model not in SUPPORTED_MODELS:
    raise ValueError(f"model {model} is not supported")

qos = 0
retain = True
disc_prefix = "homeassistant"

device_info = {
    KEY_CONNECTIONS: [[KEY_MAC, format_mac(mac)]],
    KEY_NAME: device_name,
    KEY_MODEL: SUPPORTED_MODELS[model],
    KEY_SW_VERSION: firmware_ver,
    KEY_MANUFACTURER: ATTR_MANUFACTURER,
}

if model == "SHPSW04P":
    config_data = configure_pro4pm()
if model == "SNSW-001P16EU":
    config_data = configure_plus1pm()

if config_data:
    for topic, payload in config_data.items():
        mqtt_publish(topic, payload, retain)
