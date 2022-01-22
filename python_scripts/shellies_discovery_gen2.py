"""This script adds MQTT discovery support for Shellies Gen2 devices."""

ATTR_FW_ID = "fw_id"
ATTR_ID = "id"
ATTR_LIGHT = "light"
ATTR_MAC = "mac"
ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_MODEL = "model"
ATTR_NAME = "name"
ATTR_RELAY_SENSORS = "sensors"
ATTR_RELAYS = "relays"
ATTR_SWITCH = "switch"

DEVICE_CLASS_CURRENT = "current"
DEVICE_CLASS_ENERGY = "energy"
DEVICE_CLASS_POWER = "power"
DEVICE_CLASS_POWER_FACTOR = "power_factor"
DEVICE_CLASS_TEMPERATURE = "temperature"
DEVICE_CLASS_VOLTAGE = "voltage"

KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_COMMAND_OFF_TEMPLATE = "cmd_off_tpl"
KEY_COMMAND_ON_TEMPLATE = "cmd_on_tpl"
KEY_COMMAND_TOPIC = "cmd_t"
KEY_CONNECTIONS = "cns"
KEY_DEVICE = "dev"
KEY_DEVICE_CLASS = "dev_cla"
KEY_ENABLED_BY_DEFAULT = "en"
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
KEY_STATE_CLASS = "stat_cla"
KEY_STATE_OFF = "stat_off"
KEY_STATE_ON = "stat_on"
KEY_STATE_TEMPLATE = "stat_tpl"
KEY_STATE_TOPIC = "stat_t"
KEY_SW_VERSION = "sw"
KEY_UNIQUE_ID = "uniq_id"
KEY_UNIT = "unit_of_meas"
KEY_VALUE_TEMPLATE = "val_tpl"

MODEL_PLUS_1 = "shellyplus1"
MODEL_PLUS_1PM = "shellyplus1pm"
MODEL_PRO_1 = "shellypro1"
MODEL_PRO_1PM = "shellypro1pm"
MODEL_PRO_2 = "shellypro2"
MODEL_PRO_2PM = "shellypro2pm"
MODEL_PRO_4PM = "shellypro4pm"

SENSOR_CURRENT = "current"
SENSOR_ENERGY = "energy"
SENSOR_POWER = "power"
SENSOR_POWER_FACTOR = "power_factor"
SENSOR_TEMPERATURE = "temperature"
SENSOR_VOLTAGE = "voltage"

STATE_CLASS_MEASUREMENT = "measurement"
STATE_CLASS_TOTAL_INCREASING = "total_increasing"

TOPIC_SWITCH_RELAY = "~status/switch:{relay}"

TPL_CURRENT = "{{value_json.current|round(1)}}"
TPL_ENERGY = "{{value_json.aenergy.total|round(2)}}"
TPL_POWER = "{{value_json.apower|round(1)}}"
TPL_POWER_FACTOR = "{{value_json.pf*100|round}}"
TPL_TEMPERATURE = "{{value_json.temperature.tC|round(1)}}"
TPL_VOLTAGE = "{{value_json.voltage|round(1)}}"

UNIT_AMPERE = "A"
UNIT_CELSIUS = "°C"
UNIT_PERCENT = "%"
UNIT_VOLT = "V"
UNIT_WATT = "W"
UNIT_WATTH = "Wh"

VALUE_OFF = "off"
VALUE_ON = "on"

DESCRIPTION_SENSOR_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_POWER_FACTOR = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER_FACTOR,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Power Factor",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_POWER_FACTOR,
}
DESCRIPTION_SENSOR_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE,
}
DESCRIPTION_SENSOR_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}

SUPPORTED_MODELS = {
    MODEL_PLUS_1: {
        ATTR_NAME: "Shelly Plus 1",
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {},
    },
    MODEL_PLUS_1PM: {
        ATTR_NAME: "Shelly Plus 1PM",
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
    },
    MODEL_PRO_1: {
        ATTR_NAME: "Shelly Pro 1",
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {},
    },
    MODEL_PRO_1PM: {
        ATTR_NAME: "Shelly Pro 1PM",
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
    },
    MODEL_PRO_2: {
        ATTR_NAME: "Shelly Pro 2",
        ATTR_RELAYS: 2,
        ATTR_RELAY_SENSORS: {},
    },
    MODEL_PRO_2PM: {
        ATTR_NAME: "Shelly Pro 2PM",
        ATTR_RELAYS: 2,
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
    },
    MODEL_PRO_4PM: {
        ATTR_NAME: "Shelly Pro 4PM",
        ATTR_RELAYS: 4,
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
    },
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
        KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY.format(relay=relay),
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
        KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY.format(relay=relay),
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


def get_sensor(sensor, description, relay=None):
    """Create configuration for Shelly sensor."""
    switch_name = (
        device_config[f"switch:{relay}"][ATTR_NAME] or f"{device_name} Relay {relay}"
    )
    if relay is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{relay}-{sensor}/config"
        )
        unique_id = f"{device_id}-{relay}-{sensor}".lower()
        sensor_name = f"{switch_name} {description[KEY_NAME]}"
    else:
        topic = encode_config_topic(f"{disc_prefix}/sensor/{device_id}-{sensor}/config")
        unique_id = f"{device_id}-{sensor}".lower()
        sensor_name = f"{device_name} {description[KEY_NAME]}"

    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: description[KEY_STATE_TOPIC].format(relay=relay),
        KEY_VALUE_TEMPLATE: description[KEY_VALUE_TEMPLATE],
        KEY_UNIT: description[KEY_UNIT],
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": f"{device_id}/",
    }

    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_STATE_CLASS):
        payload[KEY_STATE_CLASS] = description[KEY_STATE_CLASS]

    return topic, payload


def configure_device(relays, relay_sensors):
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

        for sensor, description in relay_sensors.items():
            topic, payload = get_sensor(sensor, description, relay)
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
relay_sensors = SUPPORTED_MODELS[model][ATTR_RELAY_SENSORS]

config_data = configure_device(relays, relay_sensors)

if config_data:
    for config_topic, config_payload in config_data.items():
        mqtt_publish(config_topic, config_payload, retain)
