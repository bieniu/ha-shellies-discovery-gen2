"""This script adds MQTT discovery support for Shellies Gen2 devices."""

ATTR_BUTTON = "button"
ATTR_BUTTONS = "buttons"
ATTR_FW_ID = "fw_id"
ATTR_ID = "id"
ATTR_INPUT_BINARY_SENSORS = "inputs_binary_sensors"
ATTR_INPUT_EVENTS = "input_events"
ATTR_INPUTS = "inputs"
ATTR_LIGHT = "light"
ATTR_MAC = "mac"
ATTR_MANUFACTURER = "Allterco Robotics"
ATTR_MODEL = "model"
ATTR_NAME = "name"
ATTR_RELAY_BINARY_SENSORS = "binary_sensors"
ATTR_RELAY_SENSORS = "sensors"
ATTR_RELAYS = "relays"
ATTR_SWITCH = "switch"

BUTTON_RESTART = "restart"
BUTTON_UPDATE_FIRMWARE = "update_firmware"

CONF_DISCOVERY_PREFIX = "discovery_prefix"
CONF_QOS = "qos"

DEFAULT_DISC_PREFIX = "homeassistant"

DEVICE_CLASS_CURRENT = "current"
DEVICE_CLASS_ENERGY = "energy"
DEVICE_CLASS_POWER = "power"
DEVICE_CLASS_POWER_FACTOR = "power_factor"
DEVICE_CLASS_PROBLEM = "problem"
DEVICE_CLASS_RESTART = "restart"
DEVICE_CLASS_TEMPERATURE = "temperature"
DEVICE_CLASS_UPDATE = "update"
DEVICE_CLASS_VOLTAGE = "voltage"

ENTITY_CATEGORY_CONFIG = "config"
ENTITY_CATEGORY_DIAGNOSTIC = "diagnostic"

EVENT_DOUBLE_PUSH = "double_push"
EVENT_LONG_PUSH = "long_push"
EVENT_SINGLE_PUSH = "single_push"

KEY_AUTOMATION_TYPE = "atype"
KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_COMMAND_OFF_TEMPLATE = "cmd_off_tpl"
KEY_COMMAND_ON_TEMPLATE = "cmd_on_tpl"
KEY_COMMAND_TOPIC = "cmd_t"
KEY_CONFIGURATION_URL = "cu"
KEY_CONNECTIONS = "cns"
KEY_DEVICE = "dev"
KEY_DEVICE_CLASS = "dev_cla"
KEY_ENABLED_BY_DEFAULT = "en"
KEY_ENTITY_CATEGORY = "entity_category"
KEY_ICON = "icon"
KEY_MAC = "mac"
KEY_MANUFACTURER = "mf"
KEY_MODEL = "mdl"
KEY_NAME = "name"
KEY_PAYLOAD = "pl"
KEY_PAYLOAD_AVAILABLE = "pl_avail"
KEY_PAYLOAD_NOT_AVAILABLE = "pl_not_avail"
KEY_PAYLOAD_OFF = "pl_off"
KEY_PAYLOAD_ON = "pl_on"
KEY_PAYLOAD_PRESS = "payload_press"
KEY_QOS = "qos"
KEY_SCHEMA = "schema"
KEY_STATE_CLASS = "stat_cla"
KEY_STATE_OFF = "stat_off"
KEY_STATE_ON = "stat_on"
KEY_STATE_TEMPLATE = "stat_tpl"
KEY_STATE_TOPIC = "stat_t"
KEY_SUBTYPE = "stype"
KEY_SW_VERSION = "sw"
KEY_TOPIC = "t"
KEY_TYPE = "type"
KEY_UNIQUE_ID = "uniq_id"
KEY_UNIT = "unit_of_meas"
KEY_VALUE_TEMPLATE = "val_tpl"

MODEL_PLUS_1 = "shellyplus1"
MODEL_PLUS_1PM = "shellyplus1pm"
MODEL_PLUS_I4 = "shellyplusi4"
MODEL_PRO_1 = "shellypro1"
MODEL_PRO_1PM = "shellypro1pm"
MODEL_PRO_2 = "shellypro2"
MODEL_PRO_2PM = "shellypro2pm"
MODEL_PRO_4PM = "shellypro4pm"

SENSOR_CURRENT = "current"
SENSOR_ENERGY = "energy"
SENSOR_INPUT = "input"
SENSOR_OVERPOWER = "overpower"
SENSOR_OVERTEMP = "overtemp"
SENSOR_OVERVOLTAGE = "overvoltage"
SENSOR_POWER = "power"
SENSOR_POWER_FACTOR = "power_factor"
SENSOR_TEMPERATURE = "temperature"
SENSOR_VOLTAGE = "voltage"

STATE_CLASS_MEASUREMENT = "measurement"
STATE_CLASS_TOTAL_INCREASING = "total_increasing"

TOPIC_INPUT = "~status/input:{relay}"
TOPIC_SWITCH_RELAY = "~status/switch:{relay}"

TPL_CURRENT = "{{value_json.current|round(1)}}"
TPL_ENERGY = "{{value_json.aenergy.total|round(2)}}"
TPL_INPUT = "{%if value_json.state%}ON{%else%}OFF{%endif%}"
TPL_POWER = "{{value_json.apower|round(1)}}"
TPL_POWER_FACTOR = "{{value_json.pf*100|round}}"
TPL_RELAY_OVERPOWER = (
    "{%if ^overpower^ in value_json.get(^errors^,[])%}ON{%else%}OFF{%endif%}"
)
TPL_RELAY_OVERTEMP = (
    "{%if ^overtemp^ in value_json.get(^errors^,[])%}ON{%else%}OFF{%endif%}"
)
TPL_RELAY_OVERVOLTAGE = (
    "{%if ^overvoltage^ in value_json.get(^errors^,[])%}ON{%else%}OFF{%endif%}"
)
TPL_TEMPERATURE = "{{value_json.temperature.tC|round(1)}}"
TPL_VOLTAGE = "{{value_json.voltage|round(1)}}"

TRIGGER_BUTTON_DOUBLE_PRESS = "button_double_press"
TRIGGER_BUTTON_LONG_PRESS = "button_long_press"
TRIGGER_BUTTON_SHORT_PRESS = "button_short_press"

UNIT_AMPERE = "A"
UNIT_CELSIUS = "°C"
UNIT_PERCENT = "%"
UNIT_VOLT = "V"
UNIT_WATT = "W"
UNIT_WATTH = "Wh"

VALUE_OFF = "off"
VALUE_ON = "on"
VALUE_TRIGGER = "trigger"

DEVICE_TRIGGER_MAP = {
    EVENT_DOUBLE_PUSH: TRIGGER_BUTTON_DOUBLE_PRESS,
    EVENT_LONG_PUSH: TRIGGER_BUTTON_LONG_PRESS,
    EVENT_SINGLE_PUSH: TRIGGER_BUTTON_SHORT_PRESS,
}

DESCRIPTION_BUTTON_RESTART = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_RESTART,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Restart",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{device_id}^,^method^:^Shelly.Reboot^}}",
}
DESCRIPTION_UPDATE_FIRMWARE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_UPDATE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Update Firmware",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{device_id}^,^method^:^Shelly.Update^,^params^:{{^stage^:^stable^}}}}",
}
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
DESCRIPTION_SENSOR_INPUT = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_VALUE_TEMPLATE: TPL_INPUT,
}
DESCRIPTION_SENSOR_OVERPOWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_PROBLEM,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Overpower",
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_VALUE_TEMPLATE: TPL_RELAY_OVERPOWER,
}
DESCRIPTION_SENSOR_OVERTEMP = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_PROBLEM,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Overtemperature",
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_VALUE_TEMPLATE: TPL_RELAY_OVERTEMP,
}
DESCRIPTION_SENSOR_OVERVOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_PROBLEM,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Overvoltage",
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_VALUE_TEMPLATE: TPL_RELAY_OVERVOLTAGE,
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
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 1,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
    },
    MODEL_PLUS_1PM: {
        ATTR_NAME: "Shelly Plus 1PM",
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 1,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
    },
    MODEL_PLUS_I4: {
        ATTR_NAME: "Shelly Plus i4",
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 4,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
    },
    MODEL_PRO_1: {
        ATTR_NAME: "Shelly Pro 1",
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 1,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
    },
    MODEL_PRO_1PM: {
        ATTR_NAME: "Shelly Pro 1PM",
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 1,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
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
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 2,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
    },
    MODEL_PRO_2PM: {
        ATTR_NAME: "Shelly Pro 2PM",
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 2,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
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
        ATTR_BUTTONS: {
            BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART,
            BUTTON_UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
        },
        ATTR_INPUTS: 4,
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [EVENT_SINGLE_PUSH, EVENT_DOUBLE_PUSH, EVENT_LONG_PUSH],
        ATTR_RELAYS: 4,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
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


def mqtt_publish(topic, payload):
    """Publish data to MQTT broker."""
    payload_str = str(payload).replace("'", '"').replace("^", '\\"')
    service_data = {
        "topic": topic,
        "payload": payload_str,
        "retain": True,
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


def get_switch(relay_id, relay_type):
    """Create configuration for Shelly switch entity."""
    topic = encode_config_topic(f"{disc_prefix}/switch/{device_id}-{relay_id}/config")

    if relay_type != ATTR_SWITCH:
        payload = ""
        return topic, payload

    relay_name = (
        device_config[f"switch:{relay_id}"][ATTR_NAME]
        or f"{device_name} Relay {relay_id}"
    )
    payload = {
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: "~rpc",
        KEY_PAYLOAD_OFF: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:false}}}}",
        KEY_PAYLOAD_ON: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:true}}}}",
        KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY.format(relay=relay_id),
        KEY_VALUE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        KEY_STATE_OFF: VALUE_OFF,
        KEY_STATE_ON: VALUE_ON,
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: f"{device_id}-{relay_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": default_topic,
    }
    return topic, payload


def get_light(relay_id, relay_type):
    """Create configuration for Shelly relay as light entity."""
    topic = encode_config_topic(f"{disc_prefix}/light/{device_id}-{relay_id}/config")

    if relay_type != ATTR_LIGHT:
        payload = ""
        return topic, payload

    relay_name = (
        device_config[f"switch:{relay_id}"][ATTR_NAME]
        or f"{device_name} Relay {relay_id}"
    )
    payload = {
        KEY_SCHEMA: "template",
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: "~rpc",
        KEY_COMMAND_OFF_TEMPLATE: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:false}}}}",
        KEY_COMMAND_ON_TEMPLATE: f"{{^id^:1,^src^:^{device_id}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:true}}}}",
        KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY.format(relay=relay_id),
        KEY_STATE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: f"{device_id}-{relay_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": default_topic,
    }
    return topic, payload


def get_sensor(sensor, description, relay_id=None):
    """Create configuration for Shelly sensor entity."""
    switch_name = (
        device_config[f"switch:{relay_id}"][ATTR_NAME]
        or f"{device_name} Relay {relay_id}"
    )
    if relay_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{relay_id}-{sensor}/config"
        )
        unique_id = f"{device_id}-{relay_id}-{sensor}".lower()
        sensor_name = f"{switch_name} {description[KEY_NAME]}"
    else:
        topic = encode_config_topic(f"{disc_prefix}/sensor/{device_id}-{sensor}/config")
        unique_id = f"{device_id}-{sensor}".lower()
        sensor_name = f"{device_name} {description[KEY_NAME]}"

    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: description[KEY_STATE_TOPIC].format(relay=relay_id),
        KEY_VALUE_TEMPLATE: description[KEY_VALUE_TEMPLATE],
        KEY_UNIT: description[KEY_UNIT],
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": default_topic,
    }

    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_STATE_CLASS):
        payload[KEY_STATE_CLASS] = description[KEY_STATE_CLASS]

    return topic, payload


def get_binary_sensor(
    sensor, description, entity_id=None, is_input=False, input_type=None
):
    """Create configuration for Shelly binary sensor entity."""
    if is_input:
        name = (
            device_config[f"input:{entity_id}"][ATTR_NAME]
            or f"{device_name} Input {entity_id}"
        )
    else:
        name = (
            device_config[f"switch:{entity_id}"][ATTR_NAME]
            or f"{device_name} Relay {entity_id}"
        )
    if entity_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/binary_sensor/{device_id}-{entity_id}-{sensor}/config"
        )
        unique_id = f"{device_id}-{entity_id}-{sensor}".lower()
        sensor_name = (
            f"{name} {description[KEY_NAME]}" if description.get(KEY_NAME) else name
        )
    else:
        topic = encode_config_topic(
            f"{disc_prefix}/binary_sensor/{device_id}-{sensor}/config"
        )
        unique_id = f"{device_id}-{sensor}".lower()
        sensor_name = f"{device_name} {description[KEY_NAME]}"

    if is_input and input_type != ATTR_SWITCH:
        payload = ""
        return topic, payload

    payload = {
        KEY_NAME: sensor_name,
        KEY_STATE_TOPIC: description[KEY_STATE_TOPIC].format(relay=entity_id),
        KEY_VALUE_TEMPLATE: description[KEY_VALUE_TEMPLATE],
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        "~": default_topic,
    }

    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_STATE_CLASS):
        payload[KEY_STATE_CLASS] = description[KEY_STATE_CLASS]

    return topic, payload


def get_input(input_id, input_type, event):
    """Create configuration for Shelly input event."""
    topic = encode_config_topic(
        f"{disc_prefix}/device_automation/{device_id}-input-{input_id}/{event}/config"
    )

    if input_type != ATTR_BUTTON:
        payload = ""
        return topic, payload

    payload = {
        KEY_AUTOMATION_TYPE: VALUE_TRIGGER,
        KEY_TOPIC: f"{device_id}/events/rpc",
        KEY_PAYLOAD: f"{input_id}_{event}",
        KEY_VALUE_TEMPLATE: "{{value_json.params.events.0.id}}_{{value_json.params.events.0.event}}",
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_TYPE: DEVICE_TRIGGER_MAP[event],
        KEY_SUBTYPE: f"button_{input_id + 1}",
    }

    return topic, payload


def get_button(button, description):
    """Create configuration for Shelly button entity."""
    topic = encode_config_topic(f"{disc_prefix}/button/{device_id}-{button}/config")

    payload = {
        KEY_NAME: f"{device_name} {description[KEY_NAME]}",
        KEY_COMMAND_TOPIC: "~rpc",
        KEY_PAYLOAD_PRESS: description[KEY_PAYLOAD_PRESS].format(device_id=device_id),
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_UNIQUE_ID: f"{device_id}-{button}".lower(),
        KEY_QOS: qos,
        # KEY_AVAILABILITY_TOPIC: f"~online",
        # KEY_PAYLOAD_AVAILABLE: VALUE_TRUE,
        # KEY_PAYLOAD_NOT_AVAILABLE: VALUE_FALSE,
        KEY_DEVICE: device_info,
        "~": default_topic,
    }

    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_ICON):
        payload[KEY_ICON] = description[KEY_ICON]

    return topic, payload


def configure_device():
    """Create configuration for the device."""
    config = {}

    for relay_id in range(relays):
        relay_type = (
            ATTR_LIGHT
            if ATTR_LIGHT
            in device_config["sys"]["ui_data"]["consumption_types"][relay_id].lower()
            else ATTR_SWITCH
        )

        topic, payload = get_switch(relay_id, relay_type)
        config[topic] = payload

        topic, payload = get_light(relay_id, relay_type)
        config[topic] = payload

        for sensor, description in relay_sensors.items():
            topic, payload = get_sensor(sensor, description, relay_id)
            config[topic] = payload

        for binary_sensor, description in relay_binary_sensors.items():
            topic, payload = get_binary_sensor(binary_sensor, description, relay_id)
            config[topic] = payload

    for input_id in range(inputs):
        input_type = device_config[f"input:{input_id}"]["type"]

        for event in input_events:
            topic, payload = get_input(input_id, input_type, event)
            config[topic] = payload

        for binary_sensor, description in input_binary_sensors.items():
            topic, payload = get_binary_sensor(
                binary_sensor,
                description,
                input_id,
                is_input=True,
                input_type=input_type,
            )
            config[topic] = payload

    for button, descripton in buttons.items():
        topic, payload = get_button(button, descripton)
        config[topic] = payload

    return config


device_id = data[ATTR_ID]  # noqa: F821
device_config = data["device_config"]  # noqa: F821
firmware_id = device_config["sys"]["device"][ATTR_FW_ID]
mac = device_config["sys"]["device"][ATTR_MAC]
device_name = device_config["sys"]["device"][ATTR_NAME]
device_url = f"http://{device_config['mqtt']['topic_prefix']}.local/"
default_topic = f"{device_config['mqtt']['topic_prefix']}/"

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

qos = data.get(CONF_QOS, 0)  # noqa: F821
if qos not in (0, 1, 2):
    raise ValueError(f"QoS value {qos} is not valid, check script configuration")

disc_prefix = data.get(CONF_DISCOVERY_PREFIX, DEFAULT_DISC_PREFIX)  # noqa: F821

device_info = {
    KEY_CONNECTIONS: [[KEY_MAC, format_mac(mac)]],
    KEY_NAME: device_name,
    KEY_MODEL: SUPPORTED_MODELS[model][ATTR_NAME],
    KEY_SW_VERSION: firmware_id,
    KEY_MANUFACTURER: ATTR_MANUFACTURER,
    KEY_CONFIGURATION_URL: device_url,
}

inputs = SUPPORTED_MODELS[model].get(ATTR_INPUTS, 0)
input_events = SUPPORTED_MODELS[model].get(ATTR_INPUT_EVENTS, [])
input_binary_sensors = SUPPORTED_MODELS[model].get(ATTR_INPUT_BINARY_SENSORS, {})

relays = SUPPORTED_MODELS[model].get(ATTR_RELAYS, 0)
relay_sensors = SUPPORTED_MODELS[model].get(ATTR_RELAY_SENSORS, {})
relay_binary_sensors = SUPPORTED_MODELS[model].get(ATTR_RELAY_BINARY_SENSORS, {})

buttons = SUPPORTED_MODELS[model].get(ATTR_BUTTONS, {})

config_data = configure_device()

if config_data:
    for config_topic, config_payload in config_data.items():
        mqtt_publish(config_topic, config_payload)
