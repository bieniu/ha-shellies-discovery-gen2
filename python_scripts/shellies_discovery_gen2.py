"""This script adds MQTT discovery support for Shellies Gen2 devices."""

ATTR_FW_ID = "fw_id"
ATTR_ID = "id"
ATTR_LIGHT = "light"
ATTR_MAC = "mac"
ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_MODEL = "model"
ATTR_NAME = "name"
ATTR_RELAYS = "relays"
ATTR_SWITCH = "switch"

KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_COMMAND_OFF_TEMPLATE = "cmd_off_tpl"
KEY_COMMAND_ON_TEMPLATE = "cmd_on_tpl"
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
KEY_SCHEMA = "schema"
KEY_STATE_OFF = "stat_off"
KEY_STATE_ON = "stat_on"
KEY_STATE_TOPIC = "stat_t"
KEY_STATE_TEMPLATE = "stat_tpl"
KEY_SW_VERSION = "sw"
KEY_UNIQUE_ID = "uniq_id"
KEY_VALUE_TEMPLATE = "val_tpl"

MODEL_PLUS_1 = "shellyplus1"
MODEL_PLUS_1PM = "shellyplus1pm"
MODEL_PRO_1 = "shellypro1"
MODEL_PRO_1PM = "shellypro1pm"
MODEL_PRO_2 = "shellypro2"
MODEL_PRO_2PM = "shellypro2pm"
MODEL_PRO_4PM = "shellypro4pm"

VALUE_OFF = "off"
VALUE_ON = "on"

SUPPORTED_MODELS = {
    MODEL_PLUS_1: {ATTR_NAME: "Shelly Plus 1", ATTR_RELAYS: 1},
    MODEL_PLUS_1PM: {ATTR_NAME: "Shelly Plus 1PM", ATTR_RELAYS: 1},
    MODEL_PRO_1: {ATTR_NAME: "Shelly Pro 1", ATTR_RELAYS: 1},
    MODEL_PRO_1PM: {ATTR_NAME: "Shelly Pro 1PM", ATTR_RELAYS: 1},
    MODEL_PRO_2: {ATTR_NAME: "Shelly Pro 2", ATTR_RELAYS: 2},
    MODEL_PRO_2PM: {ATTR_NAME: "Shelly Pro 2PM", ATTR_RELAYS: 2},
    MODEL_PRO_4PM: {ATTR_NAME: "Shelly Pro 4PM", ATTR_RELAYS: 4},
}


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


def get_switch(relay, relay_type):
    """Create configuration for Shelly as switch."""
    topic = encode_config_topic(f"{disc_prefix}/switch/{device_id}-{relay}/config")

    if relay_type != ATTR_SWITCH:
        payload = ""
        return topic, payload

    relay_name = (
        device_config[f"switch:{relay}"][ATTR_NAME] or f"{device_name} Relay {relay}"
    )
    payload = {
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: "~rpc",
        KEY_PAYLOAD_OFF: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay},^on^:false}}}}",
        KEY_PAYLOAD_ON: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay},^on^:true}}}}",
        KEY_STATE_TOPIC: f"~status/switch:{relay}",
        KEY_VALUE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        KEY_STATE_OFF: VALUE_OFF,
        KEY_STATE_ON: VALUE_ON,
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: f"{device_id}-{relay}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": f"{device_id}/",
    }
    return topic, payload


def get_light(relay, relay_type):
    """Create configuration for Shelly relay as light."""
    topic = encode_config_topic(f"{disc_prefix}/light/{device_id}-{relay}/config")

    if relay_type != ATTR_LIGHT:
        payload = ""
        return topic, payload

    relay_name = (
        device_config[f"switch:{relay}"][ATTR_NAME] or f"{device_name} Relay {relay}"
    )
    payload = {
        KEY_SCHEMA: "template",
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: "~rpc",
        KEY_COMMAND_OFF_TEMPLATE: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay},^on^:false}}}}",
        KEY_COMMAND_ON_TEMPLATE: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay},^on^:true}}}}",
        KEY_STATE_TOPIC: f"~status/switch:{relay}",
        KEY_STATE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: f"{device_id}-{relay}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": f"{device_id}/",
    }
    return topic, payload


def configure_device(relays):
    """Create configuration for the device."""
    config = {}

    for relay in range(relays):
        relay_type = (
            ATTR_LIGHT
            if ATTR_LIGHT
            in device_config["sys"]["ui_data"]["consumption_types"][relay].lower()
            else ATTR_SWITCH
        )

        topic, payload = get_switch(relay, relay_type)
        config[topic] = payload

        topic, payload = get_light(relay, relay_type)
        config[topic] = payload

    return config


device_id = data[ATTR_ID]  # noqa: F821
device_config = data["device_config"]  # noqa: F821
firmware_id = device_config["sys"]["device"][ATTR_FW_ID]
mac = device_config["sys"]["device"][ATTR_MAC]
device_name = device_config["sys"]["device"][ATTR_NAME]

model = device_id.rsplit("-", 1)[0]

if model not in SUPPORTED_MODELS:
    raise ValueError(
        f"model {model} is not supported, please open an issue here https://github.com/bieniu/ha-shellies-discovery-gen2/issues"
    )

if not device_name:
    device_name = SUPPORTED_MODELS[model][ATTR_NAME]

if device_id is None:
    raise ValueError("id value None is not valid, check script configuration")
if mac is None:
    raise ValueError("mac value None is not valid, check script configuration")

qos = 0
retain = True
disc_prefix = "homeassistant"

device_info = {
    KEY_CONNECTIONS: [[KEY_MAC, format_mac(mac)]],
    KEY_NAME: device_name,
    KEY_MODEL: SUPPORTED_MODELS[model][ATTR_NAME],
    KEY_SW_VERSION: firmware_id,
    KEY_MANUFACTURER: ATTR_MANUFACTURER,
}

relays = SUPPORTED_MODELS[model][ATTR_RELAYS]

config_data = configure_device(relays)

if config_data:
    for config_topic, config_payload in config_data.items():
        mqtt_publish(config_topic, config_payload, retain)
