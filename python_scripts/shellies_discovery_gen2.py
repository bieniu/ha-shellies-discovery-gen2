"""Adds MQTT discovery support for Shellies Gen2+ devices."""

VERSION = "0.0.0"

ATTR_BATTERY_POWERED = "battery_powered"
ATTR_BINARY_SENSORS = "binary_sensors"
ATTR_BRAND = "brand"
ATTR_BUTTON = "button"
ATTR_BUTTONS = "buttons"
ATTR_CCT = "cct"
ATTR_CCT_SENSORS = "cct_sensors"
ATTR_COVER = "cover"
ATTR_COVER_SENSORS = "cover_sensors"
ATTR_COVERS = "covers"
ATTR_REMOVAL_CONDITION = "removal_condition"
ATTR_EMETER_PHASES = "emeter_phases"
ATTR_EMETER_SENSORS = "emeter_sensors"
ATTR_EMETERS = "emeters"
ATTR_FAN = "fan"
ATTR_FW_ID = "fw_id"
ATTR_GEN = "gen"
ATTR_ID = "id"
ATTR_INPUT = "input"
ATTR_INPUTS = "inputs"
ATTR_INPUT_BINARY_SENSORS = "inputs_binary_sensors"
ATTR_INPUT_EVENTS = "input_events"
ATTR_INPUT_SENSORS = "input_sensors"
ATTR_KEY = "key"
ATTR_LIGHT = "light"
ATTR_LIGHT_SENSORS = "light_sensors"
ATTR_MAC = "mac"
ATTR_MANUFACTURER = "Shelly"
ATTR_MIN_FIRMWARE_DATE = "min_firmware_date"
ATTR_MODEL = "model"
ATTR_MODEL_ID = "model_id"
ATTR_NAME = "name"
ATTR_NUMBERS = "numbers"
ATTR_PROFILE = "profile"
ATTR_RELAY_BINARY_SENSORS = "relay_binary_sensors"
ATTR_RELAY_SENSORS = "relay_sensors"
ATTR_RELAYS = "relays"
ATTR_RGB = "rgb"
ATTR_RGB_SENSORS = "rgb_sensors"
ATTR_SENSORS = "sensors"
ATTR_SWITCH = "switch"
ATTR_SWITCHES = "switches"
ATTR_TEMPERATURE_MAX = "temperature_max"
ATTR_TEMPERATURE_MIN = "temperature_min"
ATTR_HUMIDITY_MAX = "humidity_max"
ATTR_HUMIDITY_MIN = "humidity_min"
ATTR_TEMPERATURE_STEP = "temperature_step"
ATTR_THERMOSTATS = "thermostats"
ATTR_UPDATES = "updates"
ATTR_VALVES = "valves"
ATTR_WAKEUP_PERIOD = "wakeup_period"

BUTTON_CALIBRATE = "calibrate"
BUTTON_MUTE_ALARM = "mute_alarm"
BUTTON_RESTART = "restart"
BUTTON_START_BOOST = "start_boost"
BUTTON_STOP_BOOST = "stop_boost"
BUTTON_UPDATE_FIRMWARE = "update_firmware"

CONF_DISCOVERY_PREFIX = "discovery_prefix"
CONF_QOS = "qos"
CONF_SCRIPT_PREFIX = "script_prefix"

DEFAULT_DISC_PREFIX = "homeassistant"

DEVICE_CLASS_APPARENT_POWER = "apparent_power"
DEVICE_CLASS_BATTERY = "battery"
DEVICE_CLASS_BUTTON = "button"
DEVICE_CLASS_CONNECTIVITY = "connectivity"
DEVICE_CLASS_CURRENT = "current"
DEVICE_CLASS_ENERGY = "energy"
DEVICE_CLASS_ENUM = "enum"
DEVICE_CLASS_FREQUENCY = "frequency"
DEVICE_CLASS_HUMIDITY = "humidity"
DEVICE_CLASS_ILLUMINANCE = "illuminance"
DEVICE_CLASS_MOISTURE = "moisture"
DEVICE_CLASS_MOTION = "motion"
DEVICE_CLASS_OCCUPANCY = "occupancy"
DEVICE_CLASS_PLUG = "plug"
DEVICE_CLASS_POWER = "power"
DEVICE_CLASS_POWER_FACTOR = "power_factor"
DEVICE_CLASS_PROBLEM = "problem"
DEVICE_CLASS_RESTART = "restart"
DEVICE_CLASS_SIGNAL_STRENGTH = "signal_strength"
DEVICE_CLASS_SMOKE = "smoke"
DEVICE_CLASS_TEMPERATURE = "temperature"
DEVICE_CLASS_TIMESTAMP = "timestamp"
DEVICE_CLASS_UPDATE = "update"
DEVICE_CLASS_VOLTAGE = "voltage"
DEVICE_CLASS_WATER = "water"

ENTITY_CATEGORY_CONFIG = "config"
ENTITY_CATEGORY_DIAGNOSTIC = "diagnostic"

EVENT_BUTTON_DOWN = "btn_down"
EVENT_BUTTON_UP = "btn_up"
EVENT_DOUBLE_PUSH = "double_push"
EVENT_LONG_PUSH = "long_push"
EVENT_SINGLE_PUSH = "single_push"
EVENT_TRIPLE_PUSH = "triple_push"


HOME_ASSISTANT = "home-assistant"

MIN_LIGHT_TRANSITION = 1

KEY_ACTION_TEMPLATE = "act_tpl"
KEY_CURRENT_HUMIDITY_TOPIC = "curr_hum_t"
KEY_CURRENT_HUMIDITY_TEMPLATE = "curr_hum_tpl"
KEY_CURRENT_TEMPERATURE_TOPIC = "curr_temp_t"
KEY_CURRENT_TEMPERATURE_TEMPLATE = "curr_temp_tpl"
KEY_FAN_MODES = "fan_modes"
KEY_FAN_MODE_STATE_TOPIC = "fan_mode_stat_t"
KEY_FAN_MODE_STATE_TEMPLATE = "fan_mode_stat_tpl"
KEY_FAN_MODE_COMMAND_TOPIC = "fan_mode_cmd_t"
KEY_FAN_MODE_COMMAND_TEMPLATE = "fan_mode_cmd_tpl"
KEY_TARGET_HUMIDITY_COMMAND_TOPIC = "hum_cmd_t"
KEY_TARGET_HUMIDITY_COMMAND_TEMPLATE = "hum_cmd_tpl"
KEY_TARGET_HUMIDITY_STATE_TEMPLATE = "hum_state_tpl"
KEY_TARGET_HUMIDITY_STATE_TOPIC = "hum_stat_t"
KEY_TEMPERATURE_STATE_TEMPLATE = "temp_stat_tpl"
KEY_TEMPERATURE_STATE_TOPIC = "temp_stat_t"
KEY_TEMPERATURE_COMMAND_TEMPLATE = "temp_cmd_tpl"
KEY_TEMPERATURE_COMMAND_TOPIC = "temp_cmd_t"
KEY_TEMP_STEP = "temp_step"
KEY_MIN_TEMP = "min_temp"
KEY_MAX_TEMP = "max_temp"
KEY_MIN_HUMIDITY = "min_hum"
KEY_MAX_HUMIDITY = "max_hum"
KEY_MODES = "modes"
KEY_MODE_STATE_TOPIC = "mode_stat_t"
KEY_ACTION_TOPIC = "act_t"
KEY_MAX_MIREDS = "max_mirs"
KEY_MIN_MIREDS = "min_mirs"
KEY_MODE_COMMAND_TOPIC = "mode_cmd_t"
KEY_MODE_COMMAND_TEMPLATE = "mode_cmd_tpl"
KEY_MODE_STATE_TEMPLATE = "mode_stat_tpl"
KEY_AUTOMATION_TYPE = "atype"
KEY_AVAILABILITY = "avty"
KEY_AVAILABILITY_MODE = "avty_mode"
KEY_AVAILABILITY_TEMPLATE = "avty_tpl"
KEY_AVAILABILITY_TOPIC = "avty_t"
KEY_BLUE_TEMPLATE = "b_tpl"
KEY_GREEN_TEMPLATE = "g_tpl"
KEY_RED_TEMPLATE = "r_tpl"
KEY_BRIGHTNESS_TEMPLATE = "bri_tpl"
KEY_COLOR_TEMP_TEMPLATE = "clr_temp_tpl"
KEY_COMMAND_OFF_TEMPLATE = "cmd_off_tpl"
KEY_COMMAND_ON_TEMPLATE = "cmd_on_tpl"
KEY_COMMAND_TEMPLATE = "cmd_tpl"
KEY_COMMAND_TOPIC = "cmd_t"
KEY_CONFIGURATION_URL = "cu"
KEY_CONNECTIONS = "cns"
KEY_DEFAULT_TOPIC = "~"
KEY_DEVICE = "dev"
KEY_DEVICE_CLASS = "dev_cla"
KEY_ENABLED_BY_DEFAULT = "en"
KEY_ENTITY_CATEGORY = "ent_cat"
KEY_ENTITY_PICTURE = "ent_pic"
KEY_EVENT_TYPES = "evt_typ"
KEY_EXPIRE_AFTER = "expire_after"
KEY_HW_VERSION = "hw"
KEY_ICON = "icon"
KEY_IDENTIFIERS = "ids"
KEY_JSON_ATTRIBUTES_TEMPLATE = "json_attr_tpl"
KEY_JSON_ATTRIBUTES_TOPIC = "json_attr_t"
KEY_LATEST_VERSION_TEMPLATE = "l_ver_tpl"
KEY_LATEST_VERSION_TOPIC = "l_ver_t"
KEY_MAC = "mac"
KEY_MANUFACTURER = "mf"
KEY_MAX = "max"
KEY_MIN = "min"
KEY_MODE = "mode"
KEY_MODEL = "mdl"
KEY_MODEL_ID = "mdl_id"
KEY_NAME = "name"
KEY_OPTIONS = "ops"
KEY_ORIGIN = "o"
KEY_PAYLOAD = "pl"
KEY_PAYLOAD_AVAILABLE = "pl_avail"
KEY_PAYLOAD_CLOSE = "pl_cls"
KEY_PAYLOAD_INSTALL = "pl_inst"
KEY_PAYLOAD_NOT_AVAILABLE = "pl_not_avail"
KEY_PAYLOAD_OFF = "pl_off"
KEY_PAYLOAD_ON = "pl_on"
KEY_PAYLOAD_OPEN = "pl_open"
KEY_PAYLOAD_PRESS = "pl_prs"
KEY_PAYLOAD_STOP = "pl_stop"
KEY_POSITION_TEMPLATE = "pos_tpl"
KEY_POSITION_TOPIC = "pos_t"
KEY_REPORTS_POSITION = "pos"
KEY_QOS = "qos"
KEY_RELEASE_URL = "rel_u"
KEY_SCHEMA = "schema"
KEY_SET_POSITION_TEMPLATE = "set_pos_tpl"
KEY_SET_POSITION_TOPIC = "set_pos_t"
KEY_STATE_CLASS = "stat_cla"
KEY_STATE_CLOSING = "stat_closing"
KEY_STATE_OFF = "stat_off"
KEY_STATE_ON = "stat_on"
KEY_STATE_OPENING = "stat_opening"
KEY_STATE_STOPPED = "stat_stopped"
KEY_STATE_TEMPLATE = "stat_tpl"
KEY_STATE_TOPIC = "stat_t"
KEY_STATE_VALUE_TEMPLATE = "stat_val_tpl"
KEY_STEP = "step"
KEY_SUBTYPE = "stype"
KEY_SUGGESTED_DISPLAY_PRECISION = "sug_dsp_prc"
KEY_SUPPORT_URL = "url"
KEY_SW_VERSION = "sw"
KEY_TILT_COMMAND_TEMPLATE = "tilt_cmd_tpl"
KEY_TILT_COMMAND_TOPIC = "tilt_cmd_t"
KEY_TILT_STATUS_TEMPLATE = "tilt_status_tpl"
KEY_TILT_STATUS_TOPIC = "tilt_status_t"
KEY_TITLE = "tit"
KEY_TOPIC = "t"
KEY_TYPE = "type"
KEY_UNIQUE_ID = "uniq_id"
KEY_UNIT = "unit_of_meas"
KEY_VALUE_TEMPLATE = "val_tpl"
KEY_VIA_DEVICE = "via_device"

# Gen2 devices
MODEL_BLU_GATEWAY = "shellyblugw"
MODEL_PLUS_1 = "shellyplus1"
MODEL_PLUS_1_MINI = "shelly1mini"
MODEL_PLUS_1PM = "shellyplus1pm"
MODEL_PLUS_1PM_MINI = "shelly1pmmini"
MODEL_PLUS_2PM = "shellyplus2pm"
MODEL_PLUS_DIMMER_10V = "shellyplus010v"
MODEL_PLUS_HT = "shellyplusht"
MODEL_PLUS_I4 = "shellyplusi4"
MODEL_PLUS_PLUG_IT = "shellyplusplugit"
MODEL_PLUS_PLUG_S = "shellyplusplugs"
MODEL_PLUS_PLUG_UK = "shellypluspluguk"
MODEL_PLUS_PLUG_US = "shellyplugus"
MODEL_PLUS_RGBW_PM = "shellyplusrgbwpm"
MODEL_PLUS_UNI = "shellyplusuni"
MODEL_PLUS_PM_MINI = "shellypmmini"
MODEL_PLUS_SMOKE = "shellyplussmoke"
MODEL_PLUS_WALL_DIMMER = "shellypluswdus"
MODEL_PRO_1 = "shellypro1"
MODEL_PRO_1PM = "shellypro1pm"
MODEL_PRO_2 = "shellypro2"
MODEL_PRO_2PM = "shellypro2pm"
MODEL_PRO_3 = "shellypro3"
MODEL_PRO_3EM = "shellypro3em"
MODEL_PRO_3EM_3CT63 = "shellypro3em63"
MODEL_PRO_3EM_3CT63_MONOPHASE = "shellypro3em63-monophase"
MODEL_PRO_3EM_400 = "shellypro3em400"
MODEL_PRO_3EM_MONOPHASE = "shellypro3em-monophase"
MODEL_PRO_4PM = "shellypro4pm"
MODEL_PRO_DIMMER_1PM = "shellyprodm1pm"
MODEL_PRO_DIMMER_2PM = "shellyprodm2pm"
MODEL_PRO_DUAL_COVER_PM = "shellypro2cover"
MODEL_PRO_EM = "shellyproem50"
MODEL_WALL_DISPLAY = "ShellyWallDisplay"
MODEL_PRO_RGBWW_PM = "shellyprorgbwwpm"
# Gen3 devices
MODEL_1_G3 = "shelly1g3"
MODEL_1L_G3 = "shelly1lg3"
MODEL_1PM_G3 = "shelly1pmg3"
MODEL_1_MINI_G3 = "shelly1minig3"
MODEL_1PM_MINI_G3 = "shelly1pmminig3"
MODEL_2L_G3 = "shelly2lg3"
MODEL_2PM_G3 = "shelly2pmg3"
MODEL_3EM_63_G3 = "shelly3em63g3"
MODEL_AZ_PLUG = "shellyazplug"
MODEL_BLU_GATEWAY_G3 = "shellyblugwg3"
MODEL_DUO_BULB_G3 = "shellyduobulbg3"
MODEL_EM_G3 = "shellyemg3"
MODEL_HT_G3 = "shellyhtg3"
MODEL_I4_G3 = "shellyi4g3"
MODEL_OUTDOOR_PLUG_S_G3 = "shellyoutdoorsg3"
MODEL_PLUG_S_G3 = "shellyplugsg3"
MODEL_PM_MINI_G3 = "shellypmminig3"
MODEL_DALI_DIMMER_G3 = "shellyddimmerg3"
MODEL_DIMMER_10V_G3 = "shelly0110dimg3"
MODEL_DIMMER_G3 = "shellydimmerg3"
MODEL_X_MOD1 = "shellyxmod1"
# Gen4 devices
MODEL_1_G4 = "shelly1g4"
MODEL_1_MINI_G4 = "shelly1minig4"
MODEL_1PM_G4 = "shelly1pmg4"
MODEL_1PM_MINI_G4 = "shelly1pmminig4"
MODEL_2PM_G4 = "shelly2pmg4"
MODEL_I4_G4 = "shellyi4g4"
MODEL_FLOOD_G4 = "shellyfloodg4"
MODEL_POWER_STRIP_G4 = "shellypstripg4"
MODEL_PRESENCE_G4 = "shellypresence"
# BLU devices
MODEL_BLU_BUTTON1 = "SBBT-002C"
MODEL_BLU_HT = "SBHT-003C"
MODEL_BLU_MOTION = "SBMO-003Z"
MODEL_BLU_RC_BUTTON_4 = "SBBT-004CUS"
MODEL_BLU_TRV = "SBTR-001AEU"
MODEL_BLU_WALL_SWITCH_4 = "SBBT-004CEU"
MODEL_GENERIC_BTHOME_DEVICE = "Generic BTHome Device"
# Powered by Shelly devices
MODEL_OGEMRAY_25A = "ogemray25a"
MODEL_ST1820 = "st1820"
MODEL_ST802_B = "st-802"
MODEL_WATER_VALVE = "watervalve"

NUMBER_EXTERNAL_TEMPERATURE = "external_temperature"
NUMBER_BOOST_TIME = "boost_time"
NUMBER_VALVE_POSITION = "valve_position"

SENSOR_ACTIVE_POWER = "active_power"
SENSOR_ALARM_SOUND = "alarm_sound"
SENSOR_ANALOG_INPUT = "analog_input"
SENSOR_ANALOG_VALUE = "analog_value"
SENSOR_APPARENT_POWER = "apparent_power"
SENSOR_BATTERY = "battery"
SENSOR_CABLE_UNPLUGGED = "cable_unplugged"
SENSOR_CALIBRATION = "calibration"
SENSOR_CLOUD = "cloud"
SENSOR_COUNTER = "counter"
SENSOR_COUNTER_VALUE = "counter_value"
SENSOR_CURRENT = "current"
SENSOR_DETECTED = "detected"
SENSOR_DEVICE_TEMPERATURE = "device_temperature"
SENSOR_ENERGY = "energy"
SENSOR_ETH_IP = "eth_ip"
SENSOR_EXTERNAL_POWER = "external_power"
SENSOR_FIRMWARE = "firmware"
SENSOR_FLOOD = "flood"
SENSOR_FREQUENCY = "frequency"
SENSOR_HUMIDITY = "humidity"
SENSOR_ILLUMINANCE = "illuminance"
SENSOR_ILLUMINANCE_LEVEL = "illuminance_level"
SENSOR_INPUT = "input"
SENSOR_LAST_RESTART = "last_restart"
SENSOR_MOTION = "motion"
SENSOR_N_CURRENT = "n_current"
SENSOR_OVERPOWER = "overpower"
SENSOR_OVERTEMP = "overtemp"
SENSOR_OVERVOLTAGE = "overvoltage"
SENSOR_POWER = "power"
SENSOR_POWER_FACTOR = "power_factor"
SENSOR_POWER_SUPPLY = "power_supply"
SENSOR_PRESENCE = "presence"
SENSOR_RETURNED_ENERGY = "returned_energy"
SENSOR_SIGNAL_STRENGTH = "signal_strength"
SENSOR_SMOKE = "smoke"
SENSOR_SSID = "ssid"
SENSOR_TEMPERATURE = "temperature"
SENSOR_TOTAL_ACTIVE_ENERGY = "total_active_energy"
SENSOR_TOTAL_ACTIVE_POWER = "total_active_power"
SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY = "total_active_returned_energy"
SENSOR_TOTAL_APPARENT_POWER = "total_apparent_power"
SENSOR_TOTAL_CURRENT = "total_current"
SENSOR_VALVE_POSITION = "valve_position"
SENSOR_VOLTAGE = "voltage"
SENSOR_WIFI_IP = "wifi_ip"
SENSOR_WIFI_SIGNAL = "wifi_signal"

SWITCH_ANTI_FREEZE = "anti_freeze"
SWITCH_THERMOSTAT = "thermostat"
SWITCH_CHILD_LOCK = "child_lock"

UPDATE_FIRMWARE = "firmware"
UPDATE_FIRMWARE_BETA = "firmware_beta"

SCRIPT_CODE = """let topicPrefix = null;
let updateTimer = null;

function sendDeviceStatus() {
  try {
    let installedVersion = Shelly.getDeviceInfo().ver;
    Shelly.call(^Shelly.GetStatus^, {}, function (status) {
      status.sys.installed_version = installedVersion;
      MQTT.publish(topicPrefix + ^/status/rpc^, JSON.stringify(status));
    });
  } catch (e) {
    console.log(^sendDeviceStatus has failed: ^, e);
  }
}

function onMQTTConfigReceived(config) {
  topicPrefix = config.topic_prefix;
  console.log(^Using topic prefix: ^, topicPrefix);

  if (!updateTimer) {
    updateTimer = Timer.set(30000, true, sendDeviceStatus);
  }
}

function initScript() {
  console.log(^Starting shellies_discovery_gen2_script^);
  try {
    Shelly.call(^MQTT.GetConfig^, {}, onMQTTConfigReceived);
  } catch (e) {
    console.log(^initScript has failed: ^, e);
  }
}

initScript();
"""
SCRIPT_CURRENT_NAME = "shellies_discovery_gen2_script_20250114"
SCRIPT_OLD_NAMES = [
    "Send Device Status",
    "send_device_status",
    "send_device_status.js",
    "shellies_discovery_gen2_script_20221116",
    "shellies_discovery_gen2_script_20240216",
    "shellies_discovery_gen2_script_20241123",
]

STATE_CLASS_MEASUREMENT = "measurement"
STATE_CLASS_TOTAL_INCREASING = "total_increasing"

TOPIC_COVER = "~status/cover:{id}"
TOPIC_EMDATA = "~status/emdata:{id}"
TOPIC_EMDATA1 = "~status/em1data:{id}"
TOPIC_EMETER = "~status/em:{id}"
TOPIC_EMETER1 = "~status/em1:{id}"
TOPIC_EVENTS_RPC = "~events/rpc"
TOPIC_HUMIDITY = "~status/humidity:{id}"
TOPIC_ILLUMINANCE = "~status/illuminance:{id}"
TOPIC_INPUT = "~status/input:{id}"
TOPIC_LIGHT = "~status/light:{id}"
TOPIC_ONLINE = "~online"
TOPIC_RPC = "~rpc"
TOPIC_SHELLIES_DISCOVERY_SCRIPT = "shellies_discovery_script"
TOPIC_STATUS_BLU_TRV = "~status/blutrv:{id}"
TOPIC_STATUS_BTH_DEVICE = "~status/bthomedevice:{id}"
TOPIC_STATUS_BTH_SENSOR = "~status/bthomesensor:{id}"
TOPIC_STATUS_CLOUD = "~status/cloud"
TOPIC_STATUS_DEVICE_POWER = "~status/devicepower:0"
TOPIC_STATUS_FLOOD = "~status/flood:0"
TOPIC_STATUS_PM1 = "~status/pm1:0"
TOPIC_STATUS_CCT = "~status/cct:{id}"
TOPIC_STATUS_RGB = "~status/rgb:{id}"
TOPIC_STATUS_PRESENCE = "~status/presence"
TOPIC_STATUS_RPC = "~status/rpc"
TOPIC_STATUS_SMOKE = "~status/smoke:0"
TOPIC_STATUS_SYS = "~status/sys"
TOPIC_STATUS_WIFI = "~status/wifi"
TOPIC_SWITCH_RELAY = "~status/switch:{id}"
TOPIC_TEMPERATURE = "~status/temperature:{id}"
TOPIC_THERMOSTAT = "~status/thermostat:{id}"
TOPIC_VOLTMETER = "~status/voltmeter:{id}"

TPL_ACTION_TEMPLATE = "{{%if value_json.output%}}{action}{{%else%}}idle{{%endif%}}"
TPL_ANALOG_INPUT = "{{value_json.percent}}"
TPL_ANALOG_VALUE = "{{value_json.xpercent}}"
TPL_BATTERY = "{{value_json.battery}}"
TPL_BATTERY_PERCENT = "{{value_json.battery.percent}}"
TPL_BLU_TRV_REPORT_EXTERNAL_TEMPERATURE = "{{{{{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^TRV.SetExternalTemperature^,^params^:{{^id^:0,^t_C^:value}}}}}}|to_json}}}}"
TPL_BLU_TRV_SET_BOOST_TIME = "{{{{{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^Trv.SetConfig^,^params^:{{^id^:0,^config^:{{^default_boost_duration^:value*60}}}}}}}}|to_json}}}}"
TPL_BLU_TRV_SET_VALVE_POSITION = "{{{{{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^Trv.SetPosition^,^params^:{{^id^:0,^pos^:value}}}}}}|to_json}}}}"
TPL_BLU_TRV_VALVE_POSITION = "{{value_json.pos}}"
TPL_BLU_TRV_CALIBRATION = (
    "{{^ON^ if ^not_calibrated^ in value_json.get(^errors^,[]) else ^OFF^}}"
)
TPL_COUNTER = "{{value_json.counts.total}}"
TPL_COUNTER_VALUE = "{{value_json.counts.xtotal}}"
TPL_CLOUD = "{%if value_json.cloud.connected%}ON{%else%}OFF{%endif%}"
TPL_CLOUD_INDEPENDENT = "{%if value_json.connected%}ON{%else%}OFF{%endif%}"
TPL_CURRENT = "{{value_json.current}}"
TPL_CURRENT_TEMPERATURE = "{{value_json.current_C}}"
TPL_DETECTED_OBJECTS = "{{value_json.num_objects}}"
TPL_EMETER_ACTIVE_POWER = "{{value_json.act_power}}"
TPL_EMETER_PHASE_ACTIVE_POWER = "{{{{value_json.{phase}_act_power}}}}"
TPL_EMETER_APPARENT_POWER = "{{value_json.aprt_power}}"
TPL_EMETER_PHASE_APPARENT_POWER = "{{{{value_json.{phase}_aprt_power}}}}"
TPL_EMETER_PHASE_CURRENT = "{{{{value_json.{phase}_current}}}}"
TPL_EMETER_PHASE_FREQUENCY = "{{{{value_json.{phase}_freq}}}}"
TPL_EMETER_N_CURRENT = "{{value_json.n_current}}"
TPL_EMETER_PHASE_TOTAL_ACTIVE_ENERGY = "{{{{value_json.{phase}_total_act_energy}}}}"
TPL_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY = (
    "{{{{value_json.{phase}_total_act_ret_energy}}}}"
)
TPL_EMETER_POWER_FACTOR = "{{value_json.pf}}"
TPL_EMETER_PHASE_POWER_FACTOR = "{{{{value_json.{phase}_pf}}}}"
TPL_EMETER_TOTAL_ACTIVE_ENERGY = "{{value_json.total_act}}"
TPL_EMETER1_TOTAL_ACTIVE_ENERGY = "{{value_json.total_act_energy}}"
TPL_EMETER_TOTAL_ACTIVE_POWER = "{{value_json.total_act_power}}"
TPL_EMETER_TOTAL_ACTIVE_RETURNED_ENERGY = "{{value_json.total_act_ret}}"
TPL_EMETER1_TOTAL_ACTIVE_RETURNED_ENERGY = "{{value_json.total_act_ret_energy}}"
TPL_EMETER_TOTAL_APPARENT_POWER = "{{value_json.total_aprt_power}}"
TPL_EMETER_TOTAL_CURRENT = "{{value_json.total_current}}"
TPL_EMETER_PHASE_VOLTAGE = "{{{{value_json.{phase}_voltage}}}}"
TPL_EVENT = "{{%if value_json.params.events.0.id=={input_id}%}}{{{{{{^event_type^:value_json.params.events.0.event}}|to_json}}}}{{%endif%}}"
TPL_FREQUENCY = "{{value_json.freq}}"
TPL_ENERGY = "{{value_json.aenergy.total}}"
TPL_RETURNED_ENERGY = "{{value_json.ret_aenergy.total}}"
TPL_ETH_IP = "{{value_json.eth.ip}}"
TPL_EXTERNAL_POWER = "{%if value_json.external.present%}ON{%else%}OFF{%endif%}"
TPL_FIRMWARE_BETA = "{%if value_json.sys.available_updates.beta is defined%}{{value_json.sys.available_updates.beta.version}}{%else%}{{value_json.sys.installed_version}}{%endif%}"
TPL_FIRMWARE_BETA_SYS = "{%if value_json.available_updates.beta is defined%}{{value_json.available_updates.beta.version}}{%else%}{{value_json.ver}}{%endif%}"
TPL_FIRMWARE_STABLE = "{%if value_json.sys.available_updates.stable is defined%}{{value_json.sys.available_updates.stable.version}}{%else%}{{value_json.sys.installed_version}}{%endif%}"
TPL_FIRMWARE_STABLE_SYS = "{%if value_json.available_updates.stable is defined%}{{value_json.available_updates.stable.version}}{%else%}{{value_json.ver}}{%endif%}"
TPL_FIRMWARE_STABLE_INDEPENDENT = (
    "{%if value_json.available_updates.stable is defined%}ON{%else%}OFF{%endif%}"
)
TPL_FIRMWARE_STABLE_ATTRS = "{{value_json.available_updates.get(^stable^,{})|to_json}}"
TPL_FIRMWARE_STABLE_ATTRS_INDEPENDENT = (
    "{{value_json.available_updates.get(^stable^,{})|to_json}}"
)
TPL_HUMIDITY = "{{value_json.rh}}"
TPL_ILLUMINANCE = "{{value_json.lux}}"
TPL_ILLUMINANCE_LEVEL = "{{value_json.illumination}}"
TPL_INPUT = "{%if value_json.state%}ON{%else%}OFF{%endif%}"
TPL_INSTALLED_FIRMWARE = "{{value_json.sys.installed_version}}"
TPL_INSTALLED_FIRMWARE_SYS = "{{value_json.ver}}"
TPL_MQTT_CONNECTED = "{%if value_json.mqtt.connected%}online{%else%}offline{%endif%}"
TPL_VALUE_ONLINE = "{%if value_json.value%}online{%else%}offline{%endif%}"
TPL_POWER = "{{value_json.apower}}"
TPL_POWER_FACTOR = "{{value_json.pf*100}}"
TPL_PRESENCE = "{%if value_json.num_objects > 0%}ON{%else%}OFF{%endif%}"
TPL_RELAY_OVERPOWER = (
    "{%if ^overpower^ in value_json.get(^errors^,[])%}ON{%else%}OFF{%endif%}"
)
TPL_RELAY_OVERTEMP = (
    "{%if ^overtemp^ in value_json.get(^errors^,[])%}ON{%else%}OFF{%endif%}"
)
TPL_RELAY_OVERVOLTAGE = (
    "{%if ^overvoltage^ in value_json.get(^errors^,[])%}ON{%else%}OFF{%endif%}"
)
TPL_RELAY_TEMPERATURE = "{{{{value_json[^switch:{relay}^].temperature.tC}}}}"
TPL_SET_BLU_TARGET_TEMPERATURE = "{{{{{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^TRV.SetTarget^,^params^:{{^id^:0,^target_C^:value|round(1)}}}}}}|tojson}}}}"
TPL_SET_BLU_THERMOSTAT_MODE = "{{%set target=4 if value==^off^ else 21%}}{{{{{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^TRV.SetTarget^,^params^:{{^id^:0,^target_C^:target}}}}}}|to_json}}}}"
TPL_SET_TARGET_TEMPERATURE = "{{{{{{^id^:1,^src^:^{source}^,^method^:^Thermostat.SetConfig^,^params^:{{^config^:{{^id^:{thermostat},^target_C^:value}}}}}}|tojson}}}}"
TPL_SET_THERMOSTAT_MODE = "{{%if value==^off^%}}{{%set enable=false%}}{{%else%}}{{%set enable=true%}}{{%endif%}}{{{{{{^id^:1,^src^:^{source}^,^method^:^Thermostat.SetConfig^,^params^:{{^config^:{{^id^:{thermostat},^enable^:enable}}}}}}|tojson}}}}"
TPL_ALARM = "{%if value_json.alarm%}ON{%else%}OFF{%endif%}"
TPL_MUTE = "{%if value_json.mute%}OFF{%else%}ON{%endif%}"
TPL_CABLE_UNPLUGGED = (
    "{%if ^cable_unplugged^ in value_json.get(^errors^)%}ON{%else%}OFF{%endif%}"
)
TPL_TARGET_TEMPERATURE = "{{value_json.target_C}}"
TPL_TEMPERATURE = "{{value_json.temperature.tC}}"
TPL_TEMPERATURE_0 = "{{value_json[^temperature:0^].tC}}"
TPL_TEMPERATURE_INDEPENDENT = "{{value_json.tC}}"
TPL_BTH_SENSOR = "{{value_json.value}}"
TPL_BTH_BINARY_SENSOR = "{{^ON^ if value_json.value else ^OFF^}}"
TPL_BLU_THERMOSTAT_ACTION = "{%if value_json.pos>0%}heating{%else%}idle{%endif%}"
TPL_BLU_THERMOSTAT_MODE = "{{^off^ if value_json.target_C==4 else ^heat^}}"
TPL_THERMOSTAT_MODE = "{{%if value_json.enable%}}{action}{{%else%}}off{{%endif%}}"
TPL_UPTIME = "{{(as_timestamp(now())-value_json.sys.uptime)|timestamp_local}}"
TPL_UPTIME_INDEPENDENT = "{{(as_timestamp(now())-value_json.uptime)|timestamp_local}}"
TPL_VALUE = "{{value_json.value}}"
TPL_VALUE_BOOLEAN = "{%if value_json.value%}ON{%else%}OFF{%endif%}"
TPL_VALUE_SWITCH = "{%if value_json.value%}on{%else%}off{%endif%}"
TPL_HVAC_MODE = (
    "{{^fan_only^ if value_json.value == ^ventilation^ else value_json.value}}"
)
TPL_VOLTAGE = "{{value_json.voltage}}"
TPL_WIFI_IP = "{{value_json.wifi.sta_ip}}"
TPL_WIFI_IP_INDEPENDENT = "{{value_json.sta_ip}}"
TPL_WIFI_RSSI = "{{value_json.wifi.rssi}}"
TPL_WIFI_SSID = "{{value_json.wifi.ssid}}"
TPL_WIFI_SSID_INDEPENDENT = "{{value_json.ssid}}"
TPL_RSSI = "{{value_json.rssi}}"
TPL_SWITCH_PAYLOAD_OFF = "{{^id^:1,^src^:^{source}^,^method^:^Switch.Set^,^params^:{{^id^:{id},^on^:false}}}}"
TPL_SWITCH_PAYLOAD_ON = (
    "{{^id^:1,^src^:^{source}^,^method^:^Switch.Set^,^params^:{{^id^:{id},^on^:true}}}}"
)
TPL_SWITCH_OUTPUT = "{%if value_json.output%}on{%else%}off{%endif%}"

TRIGGER_BUTTON_DOUBLE_PRESS = "button_double_press"
TRIGGER_BUTTON_DOWN = "button_down"
TRIGGER_BUTTON_LONG_PRESS = "button_long_press"
TRIGGER_BUTTON_SHORT_PRESS = "button_short_press"
TRIGGER_BUTTON_TRIPLE_PRESS = "button_triple_press"
TRIGGER_BUTTON_UP = "button_up"

UNIT_AMPERE = "A"
UNIT_CELSIUS = "°C"
UNIT_DBM = "dBm"
UNIT_HERTZ = "Hz"
UNIT_LUX = "lx"
UNIT_MINUTES = "min"
UNIT_PERCENT = "%"
UNIT_PULSE = "pulse"
UNIT_VOLT = "V"
UNIT_VA = "VA"
UNIT_WATT = "W"
UNIT_WATTH = "Wh"

VALUE_OFF = "off"
VALUE_ON = "on"
VALUE_TRIGGER = "trigger"

BTH_HUMIDITY = 46
BTH_MOTION = 33
BTH_TEMPERATURE = 69
GENERIC_BTH_HUMIDITY = 3
GENERIC_BTH_BATTERY = 1
GENERIC_BTH_TEMPERATURE = 2

BTH_DEV_MAP = {
    0: MODEL_GENERIC_BTHOME_DEVICE,
    1: MODEL_BLU_BUTTON1,
    3: MODEL_BLU_HT,
    5: MODEL_BLU_MOTION,
    6: MODEL_BLU_WALL_SWITCH_4,
    7: MODEL_BLU_RC_BUTTON_4,
    8: MODEL_BLU_TRV,
}

BTH_IDX_MAP = {
    BTH_HUMIDITY: SENSOR_HUMIDITY,
    BTH_MOTION: SENSOR_MOTION,
    BTH_TEMPERATURE: SENSOR_TEMPERATURE,
    GENERIC_BTH_HUMIDITY: SENSOR_HUMIDITY,
    GENERIC_BTH_BATTERY: SENSOR_BATTERY,
    GENERIC_BTH_TEMPERATURE: SENSOR_TEMPERATURE,
}

DEVICE_TRIGGER_MAP = {
    EVENT_DOUBLE_PUSH: TRIGGER_BUTTON_DOUBLE_PRESS,
    EVENT_LONG_PUSH: TRIGGER_BUTTON_LONG_PRESS,
    EVENT_SINGLE_PUSH: TRIGGER_BUTTON_SHORT_PRESS,
    EVENT_TRIPLE_PUSH: TRIGGER_BUTTON_TRIPLE_PRESS,
    EVENT_BUTTON_UP: TRIGGER_BUTTON_UP,
    EVENT_BUTTON_DOWN: TRIGGER_BUTTON_DOWN,
}

DESCRIPTION_BUTTON_MUTE_ALARM = {
    KEY_ICON: "mdi:volume-mute",
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Mute Alarm",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{source}^,^method^:^Smoke.Mute^}}",
    KEY_AVAILABILITY_TOPIC: TOPIC_STATUS_SMOKE,
    KEY_AVAILABILITY_TEMPLATE: "{%if value_json.alarm%}online{%else%}offline{%endif%}",
}
DESCRIPTION_BUTTON_RESTART = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_RESTART,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Restart",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{source}^,^method^:^Shelly.Reboot^}}",
}
DESCRIPTION_BUTTON_BLU_TRV_CALIBRATE = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Calibrate",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^TRV.Calibrate^,^params^:{{^id^:0}}}}}}",
}
DESCRIPTION_BUTTON_BLU_TRV_START_BOOST = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Start boost",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^TRV.SetBoost^,^params^:{{^id^:0}}}}}}",
}
DESCRIPTION_BUTTON_BLU_TRV_STOP_BOOST = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Stop boost",
    KEY_PAYLOAD_PRESS: "{{^id^:1,^src^:^{source}^,^method^:^BluTRV.Call^,^params^:{{^id^:{thermostat},^method^:^TRV.ClearBoost^,^params^:{{^id^:0}}}}}}",
}
DESCRIPTION_NUMBER_BLU_TRV_EXTERNAL_TEMPERATURE = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "External temperature",
    KEY_COMMAND_TOPIC: TOPIC_RPC,
    KEY_COMMAND_TEMPLATE: TPL_BLU_TRV_REPORT_EXTERNAL_TEMPERATURE,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_ICON: "mdi:thermometer-check",
    KEY_MIN: -50,
    KEY_MAX: 50,
    KEY_STEP: 0.1,
    KEY_MODE: "box",
}
DESCRIPTION_NUMBER_BLU_TRV_VALVE_POSITION = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Valve position",
    KEY_STATE_TOPIC: TOPIC_STATUS_BLU_TRV,
    KEY_VALUE_TEMPLATE: TPL_BLU_TRV_VALVE_POSITION,
    KEY_COMMAND_TOPIC: TOPIC_RPC,
    KEY_COMMAND_TEMPLATE: TPL_BLU_TRV_SET_VALVE_POSITION,
    KEY_UNIT: UNIT_PERCENT,
    KEY_ICON: "mdi:valve",
    KEY_MIN: 0,
    KEY_MAX: 100,
}
DESCRIPTION_NUMBER_BLU_TRV_BOOST_TIME = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_NAME: "Boost time",
    KEY_COMMAND_TOPIC: TOPIC_RPC,
    KEY_COMMAND_TEMPLATE: TPL_BLU_TRV_SET_BOOST_TIME,
    KEY_UNIT: UNIT_MINUTES,
    KEY_ICON: "mdi:clock-outline",
    KEY_MIN: 1,
    KEY_MAX: 100,
    KEY_MODE: "box",
}
DESCRIPTION_SENSOR_BATTERY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_BATTERY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Battery",
    KEY_STATE_TOPIC: TOPIC_STATUS_DEVICE_POWER,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_BATTERY_PERCENT,
}
DESCRIPTION_SENSOR_BLU_TRV_VALVE_POSITION = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Valve position",
    KEY_ICON: "mdi:pipe-valve",
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_STATE_TOPIC: TOPIC_STATUS_BLU_TRV,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_BLU_TRV_VALVE_POSITION,
}
DESCRIPTION_SENSOR_BLU_TRV_BATTERY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_BATTERY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Battery",
    KEY_STATE_TOPIC: TOPIC_STATUS_BLU_TRV,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_BATTERY,
}
DESCRIPTION_SENSOR_BTH_DEV_BATTERY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_BATTERY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Battery",
    KEY_STATE_TOPIC: TOPIC_STATUS_BTH_DEVICE,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_BATTERY,
}
DESCRIPTION_SENSOR_GENERIC_BTH_DEV_BATTERY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_BATTERY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Battery",
    KEY_STATE_TOPIC: TOPIC_STATUS_BTH_SENSOR,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_BTH_SENSOR,
}
DESCRIPTION_SENSOR_EXTERNAL_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "External power",
    KEY_STATE_TOPIC: TOPIC_STATUS_DEVICE_POWER,
    KEY_VALUE_TEMPLATE: TPL_EXTERNAL_POWER,
}
DESCRIPTION_SENSOR_CLOUD = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CONNECTIVITY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Cloud",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_CLOUD,
}
DESCRIPTION_SENSOR_PRESENCE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_OCCUPANCY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Occupancy",
    KEY_STATE_TOPIC: TOPIC_STATUS_PRESENCE,
    KEY_VALUE_TEMPLATE: TPL_PRESENCE,
}
DESCRIPTION_SENSOR_POWER_SUPPLY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_PLUG,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Power supply",
    KEY_STATE_TOPIC: "~status/boolean:200",
    KEY_VALUE_TEMPLATE: TPL_VALUE_BOOLEAN,
}
DESCRIPTION_SENSOR_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_CCT_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_CCT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_LIGHT_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_LIGHT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_RGB_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RGB,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_EMETER_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "EM{emeter_id} current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_EMETER_PHASE_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Phase {phase} current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_CURRENT,
}
DESCRIPTION_SENSOR_COUNTER = {
    ATTR_REMOVAL_CONDITION: lambda config, input_id: config.get(
        f"input:{input_id}", {}
    ).get("type")
    != "count",
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Pulse counter {input}",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_UNIT: UNIT_PULSE,
    KEY_VALUE_TEMPLATE: TPL_COUNTER,
}
DESCRIPTION_SENSOR_COUNTER_VALUE = {
    ATTR_REMOVAL_CONDITION: lambda config, input_id: config.get(f"input:{input_id}", {})
    .get("xcounts", {})
    .get("expr")
    is None,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Counter value {input}",
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_VALUE_TEMPLATE: TPL_COUNTER_VALUE,
}
DESCRIPTION_SENSOR_ANALOG_INPUT = {
    ATTR_REMOVAL_CONDITION: lambda config, input_id: config.get(
        f"input:{input_id}", {}
    ).get("type")
    != "percent",
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Analog input {input}",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_ANALOG_INPUT,
}
DESCRIPTION_SENSOR_ANALOG_VALUE = {
    ATTR_REMOVAL_CONDITION: lambda config, input_id: config.get(f"input:{input_id}", {})
    .get("xpercent", {})
    .get("expr")
    is None,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Analog value {input}",
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_VALUE_TEMPLATE: TPL_ANALOG_VALUE,
}
DESCRIPTION_SENSOR_N_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "N current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_EMETER_N_CURRENT,
}
DESCRIPTION_SENSOR_TOTAL_CURRENT = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Total current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_EMETER_TOTAL_CURRENT,
}
DESCRIPTION_SENSOR_CURRENT_PM = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_PM1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_CURRENT_COVER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CURRENT,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Current",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_COVER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_AMPERE,
    KEY_VALUE_TEMPLATE: TPL_CURRENT,
}
DESCRIPTION_SENSOR_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_RETURNED_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Returned energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_RETURNED_ENERGY,
}
DESCRIPTION_SENSOR_CCT_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_STATUS_CCT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_LIGHT_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_LIGHT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_RGB_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_STATUS_RGB,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_ENERGY_PM = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_STATUS_PM1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_RETURNED_ENERGY_PM = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Total active returned energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_STATUS_PM1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_RETURNED_ENERGY,
}
DESCRIPTION_SENSOR_ENERGY_COVER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_COVER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_ENERGY,
}
DESCRIPTION_SENSOR_ETH_IP = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_ICON: "mdi:ip-outline",
    KEY_NAME: "Ethernet IP",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_ETH_IP,
}
DESCRIPTION_SENSOR_INPUT = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_VALUE_TEMPLATE: TPL_INPUT,
}
DESCRIPTION_SENSOR_LAST_RESTART = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TIMESTAMP,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Last restart",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_UPTIME,
}
DESCRIPTION_SENSOR_BLU_TRV_CALIBRATION = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_PROBLEM,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Calibration",
    KEY_STATE_TOPIC: TOPIC_STATUS_BLU_TRV,
    KEY_VALUE_TEMPLATE: TPL_BLU_TRV_CALIBRATION,
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
    KEY_ENABLED_BY_DEFAULT: True,
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
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_CCT_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_CCT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_LIGHT_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_LIGHT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_RGB_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RGB,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_POWER_PM = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_PM1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_EMETER_ACTIVE_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "EM{emeter_id} active power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_EMETER_ACTIVE_POWER,
}
DESCRIPTION_SENSOR_EMETER_PHASE_ACTIVE_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Phase {phase} active power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_ACTIVE_POWER,
}
DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Phase {phase} total active energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_EMDATA,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_TOTAL_ACTIVE_ENERGY,
}
DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Phase {phase} total active returned energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_EMDATA,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY,
}
DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "EM{emeter_id} total active energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_EMDATA1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_EMETER1_TOTAL_ACTIVE_ENERGY,
}
DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Total active energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_EMDATA.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_EMETER_TOTAL_ACTIVE_ENERGY,
}
DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_RETURNED_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "EM{emeter_id} total active returned energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_EMDATA1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_EMETER1_TOTAL_ACTIVE_RETURNED_ENERGY,
}
DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_RETURNED_ENERGY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENERGY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Total active returned energy",
    KEY_STATE_CLASS: STATE_CLASS_TOTAL_INCREASING,
    KEY_STATE_TOPIC: TOPIC_EMDATA.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATTH,
    KEY_VALUE_TEMPLATE: TPL_EMETER_TOTAL_ACTIVE_RETURNED_ENERGY,
}
DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Total active power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_EMETER_TOTAL_ACTIVE_POWER,
}
DESCRIPTION_SENSOR_EMETER_APPARENT_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_APPARENT_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "EM{emeter_id} apparent power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VA,
    KEY_VALUE_TEMPLATE: TPL_EMETER_APPARENT_POWER,
}
DESCRIPTION_SENSOR_EMETER_PHASE_APPARENT_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_APPARENT_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Phase {phase} apparent power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VA,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_APPARENT_POWER,
}
DESCRIPTION_SENSOR_EMETER_TOTAL_APPARENT_POWER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_APPARENT_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Total apparent power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VA,
    KEY_VALUE_TEMPLATE: TPL_EMETER_TOTAL_APPARENT_POWER,
}
DESCRIPTION_SENSOR_POWER_COVER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Power",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_COVER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_WATT,
    KEY_VALUE_TEMPLATE: TPL_POWER,
}
DESCRIPTION_SENSOR_POWER_FACTOR = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER_FACTOR,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Power factor",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_POWER_FACTOR,
}
DESCRIPTION_SENSOR_EMETER_POWER_FACTOR = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER_FACTOR,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "EM{emeter_id} power factor",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER1,
    KEY_VALUE_TEMPLATE: TPL_EMETER_POWER_FACTOR,
}
DESCRIPTION_SENSOR_EMETER_PHASE_POWER_FACTOR = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER_FACTOR,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Phase {phase} power factor",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_POWER_FACTOR,
}
DESCRIPTION_SENSOR_POWER_FACTOR_COVER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_POWER_FACTOR,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Power factor",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_COVER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_POWER_FACTOR,
}
DESCRIPTION_SENSOR_SSID = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_ICON: "mdi:wifi-settings",
    KEY_NAME: "SSID",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_WIFI_SSID,
}
DESCRIPTION_SENSOR_RELAY_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE,
}
DESCRIPTION_SENSOR_CCT_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_CCT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE,
}
DESCRIPTION_SENSOR_LIGHT_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_LIGHT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE,
}
DESCRIPTION_SENSOR_RGB_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RGB,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE,
}
DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_RELAY_TEMPERATURE,
}
DESCRIPTION_SENSOR_COVER_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_COVER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE,
}
DESCRIPTION_SENSOR_DEVICE_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Device temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE_0,
}
DESCRIPTION_SENSOR_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_CCT_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_CCT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_LIGHT_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_LIGHT,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_RGB_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RGB,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_VOLTAGE_PM = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_PM1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_FREQUENCY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_FREQUENCY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Frequency",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_HERTZ,
    KEY_VALUE_TEMPLATE: TPL_FREQUENCY,
}
DESCRIPTION_SENSOR_FREQUENCY_PM = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_FREQUENCY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Frequency",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_PM1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_HERTZ,
    KEY_VALUE_TEMPLATE: TPL_FREQUENCY,
}
DESCRIPTION_SENSOR_EMETER_FREQUENCY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_FREQUENCY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "EM{emeter_id} frequency",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_HERTZ,
    KEY_VALUE_TEMPLATE: TPL_FREQUENCY,
}
DESCRIPTION_SENSOR_EMETER_PHASE_FREQUENCY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_FREQUENCY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Phase {phase} frequency",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_HERTZ,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_FREQUENCY,
}
DESCRIPTION_SENSOR_EMETER_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "EM{emeter_id} voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER1,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_EMETER_PHASE_VOLTAGE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Phase {phase} voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_EMETER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_EMETER_PHASE_VOLTAGE,
}
DESCRIPTION_SENSOR_VOLTAGE_COVER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_NAME: "Voltage",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_COVER,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SENSOR_WIFI_IP = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_ICON: "mdi:ip-outline",
    KEY_NAME: "WiFi IP",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_WIFI_IP,
}
DESCRIPTION_SENSOR_WIFI_SIGNAL = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_SIGNAL_STRENGTH,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Signal strength",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_UNIT: UNIT_DBM,
    KEY_VALUE_TEMPLATE: TPL_WIFI_RSSI,
}
DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_SIGNAL_STRENGTH,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Signal strength",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_BTH_DEVICE,
    KEY_UNIT: UNIT_DBM,
    KEY_VALUE_TEMPLATE: TPL_RSSI,
}
DESCRIPTION_SENSOR_BLU_TRV_SIGNAL_STRENGTH = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_SIGNAL_STRENGTH,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Signal strength",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_BLU_TRV,
    KEY_UNIT: UNIT_DBM,
    KEY_VALUE_TEMPLATE: TPL_RSSI,
}
DESCRIPTION_SLEEPING_SENSOR_CLOUD = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_CONNECTIVITY,
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Cloud",
    KEY_STATE_TOPIC: TOPIC_STATUS_CLOUD,
    KEY_VALUE_TEMPLATE: TPL_CLOUD_INDEPENDENT,
}
DESCRIPTION_SENSOR_SMOKE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_SMOKE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Smoke",
    KEY_STATE_TOPIC: TOPIC_STATUS_SMOKE,
    KEY_VALUE_TEMPLATE: TPL_ALARM,
}
DESCRIPTION_SENSOR_SMOKE_ALARM_SOUND = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Alarm sound",
    KEY_STATE_TOPIC: TOPIC_STATUS_SMOKE,
    KEY_VALUE_TEMPLATE: TPL_MUTE,
}
DESCRIPTION_SENSOR_CABLE_UNPLUGGED = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_PROBLEM,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Cable unplugged",
    KEY_STATE_TOPIC: TOPIC_STATUS_FLOOD,
    KEY_VALUE_TEMPLATE: TPL_CABLE_UNPLUGGED,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
}
DESCRIPTION_SENSOR_FLOOD_ALARM_SOUND = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Alarm sound",
    KEY_STATE_TOPIC: TOPIC_STATUS_FLOOD,
    KEY_VALUE_TEMPLATE: TPL_MUTE,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
}
DESCRIPTION_SENSOR_FLOOD = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_MOISTURE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Flood",
    KEY_STATE_TOPIC: TOPIC_STATUS_FLOOD,
    KEY_VALUE_TEMPLATE: TPL_ALARM,
}
DESCRIPTION_SLEEPING_SENSOR_FIRMWARE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_UPDATE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Firmware",
    KEY_STATE_TOPIC: TOPIC_STATUS_SYS,
    KEY_VALUE_TEMPLATE: TPL_FIRMWARE_STABLE_INDEPENDENT,
    KEY_JSON_ATTRIBUTES_TOPIC: TOPIC_STATUS_SYS,
    KEY_JSON_ATTRIBUTES_TEMPLATE: TPL_FIRMWARE_STABLE_ATTRS_INDEPENDENT,
}
DESCRIPTION_SENSOR_ILLUMINANCE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ILLUMINANCE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Illuminance",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_ILLUMINANCE.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 0,
    KEY_UNIT: UNIT_LUX,
    KEY_VALUE_TEMPLATE: TPL_ILLUMINANCE,
}
DESCRIPTION_SENSOR_DETECTED = {
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Detected",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_PRESENCE,
    KEY_VALUE_TEMPLATE: TPL_DETECTED_OBJECTS,
    KEY_ICON: "mdi:account-group",
    KEY_UNIT: "objects",
}
DESCRIPTION_SENSOR_ILLUMINANCE_LEVEL = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_ENUM,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Illuminance level",
    KEY_STATE_TOPIC: TOPIC_ILLUMINANCE.format(id=0),
    KEY_VALUE_TEMPLATE: TPL_ILLUMINANCE_LEVEL,
    KEY_OPTIONS: ["dark", "twilight", "bright"],
    KEY_ICON: "mdi:brightness-5",
}
DESCRIPTION_SENSOR_HUMIDITY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Humidity",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_HUMIDITY.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_HUMIDITY,
}
DESCRIPTION_SENSOR_HUMIDITY_200 = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Humidity",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: "~status/number:200",
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_VALUE,
}
DESCRIPTION_SENSOR_BTH_HUMIDITY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Humidity",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_BTH_SENSOR,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_BTH_SENSOR,
}
DESCRIPTION_SENSOR_BTH_MOTION = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_MOTION,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Motion",
    KEY_STATE_TOPIC: TOPIC_STATUS_BTH_SENSOR,
    KEY_VALUE_TEMPLATE: TPL_BTH_BINARY_SENSOR,
}
DESCRIPTION_SENSOR_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_TEMPERATURE.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE_INDEPENDENT,
}
DESCRIPTION_SENSOR_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_TEMPERATURE.format(id=0),
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE_INDEPENDENT,
}
DESCRIPTION_SENSOR_TEMPERATURE_201 = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: "~status/number:201",
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_VALUE,
}
DESCRIPTION_SENSOR_BTH_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Temperature",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_BTH_SENSOR,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_BTH_SENSOR,
}
DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TIMESTAMP,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Last restart",
    KEY_STATE_TOPIC: TOPIC_STATUS_SYS,
    KEY_VALUE_TEMPLATE: TPL_UPTIME_INDEPENDENT,
}
DESCRIPTION_SLEEPING_SENSOR_SSID = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_ICON: "mdi:wifi-settings",
    KEY_NAME: "SSID",
    KEY_STATE_TOPIC: TOPIC_STATUS_WIFI,
    KEY_VALUE_TEMPLATE: TPL_WIFI_SSID_INDEPENDENT,
}
DESCRIPTION_SLEEPING_SENSOR_WIFI_IP = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_ICON: "mdi:ip-outline",
    KEY_NAME: "WiFi IP",
    KEY_STATE_TOPIC: TOPIC_STATUS_WIFI,
    KEY_VALUE_TEMPLATE: TPL_WIFI_IP_INDEPENDENT,
}
DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_SIGNAL_STRENGTH,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_DIAGNOSTIC,
    KEY_NAME: "Signal strength",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_STATUS_WIFI,
    KEY_UNIT: UNIT_DBM,
    KEY_VALUE_TEMPLATE: TPL_RSSI,
}
DESCRIPTION_UPDATE_FIRMWARE = {
    KEY_DEVICE_CLASS: "firmware",
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_LATEST_VERSION_TEMPLATE: TPL_FIRMWARE_STABLE,
    KEY_LATEST_VERSION_TOPIC: TOPIC_STATUS_RPC,
    KEY_NAME: "Firmware",
    KEY_PAYLOAD_INSTALL: "{{^id^:1,^src^:^{source}^,^method^:^Shelly.Update^,^params^:{{^stage^:^stable^}}}}",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_INSTALLED_FIRMWARE,
}
DESCRIPTION_UPDATE_FIRMWARE_SYS = {
    KEY_DEVICE_CLASS: "firmware",
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_LATEST_VERSION_TEMPLATE: TPL_FIRMWARE_STABLE_SYS,
    KEY_LATEST_VERSION_TOPIC: TOPIC_STATUS_SYS,
    KEY_NAME: "Firmware",
    KEY_PAYLOAD_INSTALL: "{{^id^:1,^src^:^{source}^,^method^:^Shelly.Update^,^params^:{{^stage^:^stable^}}}}",
    KEY_STATE_TOPIC: TOPIC_STATUS_SYS,
    KEY_VALUE_TEMPLATE: TPL_INSTALLED_FIRMWARE_SYS,
}
DESCRIPTION_UPDATE_FIRMWARE_BETA = {
    KEY_DEVICE_CLASS: "firmware",
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_LATEST_VERSION_TEMPLATE: TPL_FIRMWARE_BETA,
    KEY_LATEST_VERSION_TOPIC: TOPIC_STATUS_RPC,
    KEY_NAME: "Firmware beta",
    KEY_PAYLOAD_INSTALL: "{{^id^:1,^src^:^{source}^,^method^:^Shelly.Update^,^params^:{{^stage^:^beta^}}}}",
    KEY_STATE_TOPIC: TOPIC_STATUS_RPC,
    KEY_VALUE_TEMPLATE: TPL_INSTALLED_FIRMWARE,
}
DESCRIPTION_VALVE_FRANKEVER = {
    ATTR_KEY: "service",
    KEY_DEVICE_CLASS: DEVICE_CLASS_WATER,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_STATE_TOPIC: "~status/number:200",
    KEY_VALUE_TEMPLATE: TPL_VALUE,
    KEY_COMMAND_TOPIC: TOPIC_RPC,
    KEY_COMMAND_TEMPLATE: "{{{{{{^id^:1,^src^:^{source}^,^method^:^Number.Set^,^params^:{{^id^:200,^value^:value}}}}|tojson}}}}",
    KEY_REPORTS_POSITION: True,
}
DESCRIPTION_UPDATE_FIRMWARE_BETA_SYS = {
    KEY_DEVICE_CLASS: "firmware",
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_LATEST_VERSION_TEMPLATE: TPL_FIRMWARE_BETA_SYS,
    KEY_LATEST_VERSION_TOPIC: TOPIC_STATUS_SYS,
    KEY_NAME: "Firmware beta",
    KEY_PAYLOAD_INSTALL: "{{^id^:1,^src^:^{source}^,^method^:^Shelly.Update^,^params^:{{^stage^:^beta^}}}}",
    KEY_STATE_TOPIC: TOPIC_STATUS_SYS,
    KEY_VALUE_TEMPLATE: TPL_INSTALLED_FIRMWARE_SYS,
}
DESCRIPTION_EXTERNAL_SENSOR_TEMPERATURE = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Temperature {sensor}",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_TEMPERATURE,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_CELSIUS,
    KEY_VALUE_TEMPLATE: TPL_TEMPERATURE_INDEPENDENT,
}
DESCRIPTION_EXTERNAL_SENSOR_HUMIDITY = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Humidity {sensor}",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_HUMIDITY,
    KEY_SUGGESTED_DISPLAY_PRECISION: 1,
    KEY_UNIT: UNIT_PERCENT,
    KEY_VALUE_TEMPLATE: TPL_HUMIDITY,
}
DESCRIPTION_EXTERNAL_SENSOR_INPUT = {
    KEY_ENABLED_BY_DEFAULT: False,
    KEY_STATE_TOPIC: TOPIC_INPUT,
    KEY_VALUE_TEMPLATE: TPL_INPUT,
}
DESCRIPTION_EXTERNAL_SENSOR_VOLTMETER = {
    KEY_DEVICE_CLASS: DEVICE_CLASS_VOLTAGE,
    KEY_ENABLED_BY_DEFAULT: True,
    KEY_NAME: "Voltmeter {sensor}",
    KEY_STATE_CLASS: STATE_CLASS_MEASUREMENT,
    KEY_STATE_TOPIC: TOPIC_VOLTMETER,
    KEY_UNIT: UNIT_VOLT,
    KEY_VALUE_TEMPLATE: TPL_VOLTAGE,
}
DESCRIPTION_SWITCH_CHILD_LOCK = {
    ATTR_ID: 201,
    KEY_NAME: "Child lock",
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_PAYLOAD_OFF: "{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:{id},^value^:false}}}}",
    KEY_PAYLOAD_ON: "{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:{id},^value^:true}}}}",
    KEY_STATE_TOPIC: "~status/boolean:{id}",
    KEY_VALUE_TEMPLATE: TPL_VALUE_SWITCH,
}
DESCRIPTION_SWITCH_ANTI_FREEZE = {
    ATTR_ID: 200,
    KEY_NAME: "Anti-freeze",
    KEY_ICON: "mdi:snowflake-off",
    KEY_ENTITY_CATEGORY: ENTITY_CATEGORY_CONFIG,
    KEY_PAYLOAD_OFF: "{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:{id},^value^:false}}}}",
    KEY_PAYLOAD_ON: "{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:{id},^value^:true}}}}",
    KEY_STATE_TOPIC: "~status/boolean:{id}",
    KEY_VALUE_TEMPLATE: TPL_VALUE_SWITCH,
}
DESCRIPTION_SWITCH_THERMOSTAT = {
    ATTR_ID: 201,
    KEY_NAME: "Thermostat",
    KEY_ICON: "mdi:thermostat",
    KEY_PAYLOAD_OFF: "{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:{id},^value^:false}}}}",
    KEY_PAYLOAD_ON: "{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:{id},^value^:true}}}}",
    KEY_STATE_TOPIC: "~status/boolean:{id}",
    KEY_VALUE_TEMPLATE: TPL_VALUE_SWITCH,
}
DESCRIPTION_THERMOSTAT = {
    ATTR_TEMPERATURE_MIN: 5,
    ATTR_TEMPERATURE_MAX: 35,
    ATTR_TEMPERATURE_STEP: 0.5,
}
DESCRIPTION_THERMOSTAT_ST1820 = {
    ATTR_KEY: "service",
    ATTR_TEMPERATURE_STEP: 0.5,
    KEY_CURRENT_HUMIDITY_TEMPLATE: TPL_VALUE,
    KEY_CURRENT_HUMIDITY_TOPIC: "~status/number:200",
    KEY_CURRENT_TEMPERATURE_TEMPLATE: TPL_VALUE,
    KEY_CURRENT_TEMPERATURE_TOPIC: "~status/number:201",
    KEY_MODE_COMMAND_TEMPLATE: "{{%if value==^off^%}}{{%set output=false%}}{{%else%}}{{%set output=true%}}{{%endif%}}{{{{{{^id^:1,^src^:^{source}^,^method^:^Boolean.Set^,^params^:{{^id^:202,^value^:output}}}}|tojson}}}}",
    KEY_MODE_STATE_TEMPLATE: "{{%if value_json.value%}}{action}{{%else%}}off{{%endif%}}",
    KEY_MODE_STATE_TOPIC: "~status/boolean:202",
    KEY_TEMPERATURE_COMMAND_TEMPLATE: "{{{{{{^id^:1,^src^:^{source}^,^method^:^Number.Set^,^params^:{{^id^:202,^value^:value}}}}|tojson}}}}",
    KEY_TEMPERATURE_STATE_TEMPLATE: TPL_VALUE,
    KEY_TEMPERATURE_STATE_TOPIC: "~status/number:202",
}
DESCRIPTION_THERMOSTAT_ST802_B = {
    ATTR_KEY: "service",
    ATTR_TEMPERATURE_STEP: 0.5,
    ATTR_TEMPERATURE_MIN: 5,
    ATTR_TEMPERATURE_MAX: 35,
    ATTR_HUMIDITY_MAX: 75,
    ATTR_HUMIDITY_MIN: 40,
    KEY_CURRENT_HUMIDITY_TEMPLATE: TPL_VALUE,
    KEY_CURRENT_HUMIDITY_TOPIC: "~status/number:200",
    KEY_CURRENT_TEMPERATURE_TEMPLATE: TPL_VALUE,
    KEY_CURRENT_TEMPERATURE_TOPIC: "~status/number:201",
    KEY_MODES: ["cool", "dry", "fan_only", "heat"],
    KEY_MODE_COMMAND_TEMPLATE: "{{%if value==^fan_only^%}}{{%set value=^ventilation^%}}{{%endif%}}{{{{{{^id^:1,^src^:^{source}^,^method^:^Enum.Set^,^params^:{{^id^:201,^value^:value}}}}|tojson}}}}",
    KEY_MODE_STATE_TEMPLATE: TPL_HVAC_MODE,
    KEY_MODE_STATE_TOPIC: "~status/enum:201",
    KEY_TEMPERATURE_COMMAND_TEMPLATE: "{{{{{{^id^:1,^src^:^{source}^,^method^:^Number.Set^,^params^:{{^id^:203,^value^:value}}}}|tojson}}}}",
    KEY_TEMPERATURE_STATE_TEMPLATE: TPL_VALUE,
    KEY_TEMPERATURE_STATE_TOPIC: "~status/number:203",
    KEY_FAN_MODES: ["auto", "low", "medium", "high"],
    KEY_FAN_MODE_STATE_TOPIC: "~status/enum:200",
    KEY_FAN_MODE_STATE_TEMPLATE: TPL_VALUE,
    KEY_FAN_MODE_COMMAND_TEMPLATE: "{{{{{{^id^:1,^src^:^{source}^,^method^:^Enum.Set^,^params^:{{^id^:200,^value^:value}}}}|tojson}}}}",
    KEY_TARGET_HUMIDITY_COMMAND_TEMPLATE: "{{{{{{^id^:1,^src^:^{source}^,^method^:^Number.Set^,^params^:{{^id^:202,^value^:value}}}}|tojson}}}}",
    KEY_TARGET_HUMIDITY_STATE_TEMPLATE: TPL_VALUE,
    KEY_TARGET_HUMIDITY_STATE_TOPIC: "~status/number:202",
}
DESCRIPTION_BLU_TRV_THERMOSTAT = {
    ATTR_TEMPERATURE_MIN: 4,
    ATTR_TEMPERATURE_MAX: 30,
    ATTR_TEMPERATURE_STEP: 0.1,
}


def get_component_number(component: str, config):
    """Return the number of components."""
    return len([key for key in config if key.startswith(f"{component}:")])


def get_component_ids(component: str, config):
    """Return the list of IDs for component."""
    return [
        int(key.split(":")[-1]) for key in config if key.startswith(f"{component}:")
    ]


SUPPORTED_MODELS = {
    MODEL_BLU_TRV: {
        ATTR_NAME: "Shelly BLU TRV",
        ATTR_MODEL_ID: "SBTR-001AEU",
        ATTR_BINARY_SENSORS: {
            SENSOR_CALIBRATION: DESCRIPTION_SENSOR_BLU_TRV_CALIBRATION
        },
        ATTR_SENSORS: {
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BLU_TRV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BLU_TRV_BATTERY,
            SENSOR_VALVE_POSITION: DESCRIPTION_SENSOR_BLU_TRV_VALVE_POSITION,
        },
        ATTR_BUTTONS: {
            BUTTON_CALIBRATE: DESCRIPTION_BUTTON_BLU_TRV_CALIBRATE,
            BUTTON_START_BOOST: DESCRIPTION_BUTTON_BLU_TRV_START_BOOST,
            BUTTON_STOP_BOOST: DESCRIPTION_BUTTON_BLU_TRV_STOP_BOOST,
        },
        ATTR_NUMBERS: {
            "report_eternal_temperature": {},
            "report_external_temperature": {},
            NUMBER_EXTERNAL_TEMPERATURE: DESCRIPTION_NUMBER_BLU_TRV_EXTERNAL_TEMPERATURE,
            NUMBER_BOOST_TIME: DESCRIPTION_NUMBER_BLU_TRV_BOOST_TIME,
            NUMBER_VALVE_POSITION: DESCRIPTION_NUMBER_BLU_TRV_VALVE_POSITION,
        },
    },
    MODEL_BLU_BUTTON1: {
        ATTR_NAME: "Shelly BLU Button1",
        ATTR_MODEL_ID: MODEL_BLU_BUTTON1,
        ATTR_SENSORS: {
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BTH_DEV_BATTERY,
        },
        ATTR_INPUTS: 1,
    },
    MODEL_BLU_RC_BUTTON_4: {
        ATTR_NAME: "Shelly BLU RC Button 4",
        ATTR_MODEL_ID: MODEL_BLU_RC_BUTTON_4,
        ATTR_SENSORS: {
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BTH_DEV_BATTERY,
        },
        ATTR_INPUTS: 4,
    },
    MODEL_BLU_WALL_SWITCH_4: {
        ATTR_NAME: "Shelly BLU Wall Switch 4",
        ATTR_MODEL_ID: MODEL_BLU_WALL_SWITCH_4,
        ATTR_SENSORS: {
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BTH_DEV_BATTERY,
        },
        ATTR_INPUTS: 4,
    },
    MODEL_GENERIC_BTHOME_DEVICE: {
        ATTR_NAME: MODEL_GENERIC_BTHOME_DEVICE,
        ATTR_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_BTH_TEMPERATURE,
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_BTH_HUMIDITY,
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_GENERIC_BTH_DEV_BATTERY,
        },
    },
    MODEL_BLU_HT: {
        ATTR_NAME: "Shelly BLU H&T",
        ATTR_MODEL_ID: "SBHT-003C",
        ATTR_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_BTH_TEMPERATURE,
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_BTH_HUMIDITY,
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BTH_DEV_BATTERY,
        },
        ATTR_INPUTS: 1,
    },
    MODEL_BLU_MOTION: {
        ATTR_NAME: "Shelly BLU Motion",
        ATTR_MODEL_ID: "SBMO-003Z",
        ATTR_SENSORS: {
            SENSOR_SIGNAL_STRENGTH: DESCRIPTION_SENSOR_BTH_DEV_SIGNAL_STRENGTH,
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BTH_DEV_BATTERY,
        },
        ATTR_BINARY_SENSORS: {
            SENSOR_MOTION: DESCRIPTION_SENSOR_BTH_MOTION,
        },
    },
    MODEL_EM_G3: {
        ATTR_NAME: "Shelly EM Gen3",
        ATTR_MODEL_ID: "S3EM-002CXCEU",
        ATTR_GEN: 3,
        ATTR_EMETERS: 2,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241029,
    },
    MODEL_1_G3: {
        ATTR_NAME: "Shelly 1 Gen3",
        ATTR_MODEL_ID: "S3SW-001X16EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240331,
    },
    MODEL_1L_G3: {
        ATTR_NAME: "Shelly 1L Gen3",
        ATTR_MODEL_ID: "S3SW-0A1X1EUL",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250319,
    },
    MODEL_1_G4: {
        ATTR_NAME: "Shelly 1 Gen4",
        ATTR_MODEL_ID: "S4SW-001X16EU",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240902,
    },
    MODEL_1PM_G3: {
        ATTR_NAME: "Shelly 1PM Gen3",
        ATTR_MODEL_ID: "S3SW-001P16EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240331,
    },
    MODEL_1PM_G4: {
        ATTR_NAME: "Shelly 1PM Gen4",
        ATTR_MODEL_ID: "S4SW-001P16EU",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240902,
    },
    MODEL_PLUS_DIMMER_10V: {
        ATTR_NAME: "Shelly Plus 0-10V Dimmer",
        ATTR_MODEL_ID: "SNDM-00100WW",
        ATTR_GEN: 2,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_LIGHT_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240331,
    },
    MODEL_DALI_DIMMER_G3: {
        ATTR_NAME: "Shelly DALI Dimmer Gen3",
        ATTR_MODEL_ID: "S3DM-0A1WW",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_LIGHT_SENSORS: {SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240813,
    },
    MODEL_DIMMER_10V_G3: {
        ATTR_NAME: "Shelly Dimmer 0/1-10V PM Gen3",
        ATTR_MODEL_ID: "S3DM-0010WW",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_LIGHT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_LIGHT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_LIGHT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_LIGHT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_LIGHT_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240331,
    },
    MODEL_DIMMER_G3: {
        ATTR_NAME: "Shelly Dimmer Gen3",
        ATTR_MODEL_ID: "S3DM-0A101WWL",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_LIGHT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_LIGHT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_LIGHT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_LIGHT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_LIGHT_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240912,
    },
    MODEL_BLU_GATEWAY: {
        ATTR_NAME: "Shelly BLU Gateway",
        ATTR_MODEL_ID: "SNGW-BT01",
        ATTR_GEN: 2,
        ATTR_BINARY_SENSORS: {
            SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD,
        },
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241011,
    },
    MODEL_BLU_GATEWAY_G3: {
        ATTR_NAME: "Shelly BLU Gateway Gen3",
        ATTR_MODEL_ID: "S3GW-1DBT001",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {
            SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD,
            SENSOR_FIRMWARE: {},
        },
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250109,
    },
    MODEL_HT_G3: {
        ATTR_BATTERY_POWERED: True,
        ATTR_NAME: "Shelly H&T Gen3",
        ATTR_MODEL_ID: "S3SN-0U12A",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {
            SENSOR_EXTERNAL_POWER: DESCRIPTION_SENSOR_EXTERNAL_POWER,
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
        },
        ATTR_SENSORS: {
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BATTERY,
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_HUMIDITY,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
        ATTR_WAKEUP_PERIOD: 7200,
    },
    MODEL_I4_G3: {
        ATTR_NAME: "Shelly i4 Gen3",
        ATTR_MODEL_ID: "S3SN-0024X",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240331,
    },
    MODEL_I4_G4: {
        ATTR_NAME: "Shelly i4 Gen4",
        ATTR_MODEL_ID: "S4SN-0A24X",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240902,
    },
    MODEL_PLUS_1: {
        ATTR_NAME: "Shelly Plus 1",
        ATTR_MODEL_ID: "SNSW-001X16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_1_MINI: {
        ATTR_NAME: "Shelly Plus 1 Mini",
        ATTR_MODEL_ID: "SNSW-001X8EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_1_MINI_G3: {
        ATTR_NAME: "Shelly 1 Mini Gen3",
        ATTR_MODEL_ID: "S3SW-001X8EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_1_MINI_G4: {
        ATTR_NAME: "Shelly 1 Mini Gen4",
        ATTR_MODEL_ID: "S4SW-001X8EU",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240902,
    },
    MODEL_PLUS_1PM: {
        ATTR_NAME: "Shelly Plus 1PM",
        ATTR_MODEL_ID: "SNSW-001P16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_1PM_MINI: {
        ATTR_NAME: "Shelly Plus 1PM Mini",
        ATTR_MODEL_ID: "SNSW-001P8EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_1PM_MINI_G3: {
        ATTR_NAME: "Shelly 1PM Mini Gen3",
        ATTR_MODEL_ID: "S3SW-001P8EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231102,
    },
    MODEL_1PM_MINI_G4: {
        ATTR_NAME: "Shelly 1PM Mini Gen4",
        ATTR_MODEL_ID: "S4SW-001P8EU",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240902,
    },
    MODEL_PLUS_2PM: {
        ATTR_NAME: "Shelly Plus 2PM",
        ATTR_MODEL_ID: "SNSW-002P16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_COVERS: 1,
        ATTR_COVER_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_COVER,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_COVER,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_COVER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR_COVER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_COVER_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_COVER,
        },
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_2L_G3: {
        ATTR_NAME: "Shelly 2L Gen3",
        ATTR_MODEL_ID: "S3SW-0A2X4EUL",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_RELAY_SENSORS: {SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250319,
    },
    MODEL_2PM_G3: {
        ATTR_NAME: "Shelly 2PM Gen3",
        ATTR_MODEL_ID: "S3SW-002P16EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_COVERS: 1,
        ATTR_COVER_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_COVER,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_COVER,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_COVER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR_COVER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_COVER_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_COVER,
        },
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240712,
    },
    MODEL_2PM_G4: {
        ATTR_NAME: "Shelly 2PM Gen4",
        ATTR_MODEL_ID: "S4SW-002P16EU",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_COVERS: 1,
        ATTR_COVER_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_COVER,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_COVER,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_COVER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR_COVER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_COVER_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_COVER,
        },
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241028,
    },
    MODEL_PLUS_HT: {
        ATTR_BATTERY_POWERED: True,
        ATTR_NAME: "Shelly Plus H&T",
        ATTR_MODEL_ID: "SNSN-0013A",
        ATTR_BINARY_SENSORS: {
            SENSOR_EXTERNAL_POWER: DESCRIPTION_SENSOR_EXTERNAL_POWER,
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
        },
        ATTR_SENSORS: {
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BATTERY,
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_HUMIDITY,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
        ATTR_WAKEUP_PERIOD: 7200,
    },
    MODEL_PLUS_I4: {
        ATTR_NAME: "Shelly Plus i4",
        ATTR_MODEL_ID: "SNSW-0024X",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_PLUG_IT: {
        ATTR_NAME: "Shelly Plus Plug IT",
        ATTR_MODEL_ID: "SNPL-00110IT",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
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
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_PLUG_S: {
        ATTR_NAME: "Shelly Plus Plug S",
        ATTR_MODEL_ID: "SNPL-00112EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
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
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_OUTDOOR_PLUG_S_G3: {
        ATTR_NAME: "Shelly Outdoor Plug S Gen3",
        ATTR_MODEL_ID: "S3PL-20112EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_RETURNED_ENERGY: DESCRIPTION_SENSOR_RETURNED_ENERGY,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241128,
    },
    MODEL_AZ_PLUG: {
        ATTR_NAME: "Shelly AZ Plug",
        ATTR_MODEL_ID: "S3PL-10112EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_RETURNED_ENERGY: DESCRIPTION_SENSOR_RETURNED_ENERGY,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241011,
    },
    MODEL_PLUG_S_G3: {
        ATTR_NAME: "Shelly Plug S Gen3",
        ATTR_MODEL_ID: "S3PL-00112EU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_RETURNED_ENERGY: DESCRIPTION_SENSOR_RETURNED_ENERGY,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240820,
    },
    MODEL_PLUS_PLUG_UK: {
        ATTR_NAME: "Shelly Plus Plug UK",
        ATTR_MODEL_ID: "SNPL-00112UK",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
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
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_PLUG_US: {
        ATTR_NAME: "Shelly Plus Plug US",
        ATTR_MODEL_ID: "SNPL-00116US",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
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
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_PM_MINI: {
        ATTR_NAME: "Shelly Plus PM Mini",
        ATTR_MODEL_ID: "SNPM-001PCEU16",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_PM,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_PM,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY_PM,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_PM,
            SENSOR_RETURNED_ENERGY: DESCRIPTION_SENSOR_RETURNED_ENERGY_PM,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_PM,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_UNI: {
        ATTR_NAME: "Shelly Plus Uni",
        ATTR_MODEL_ID: "SNSX-0043X",
        ATTR_GEN: 2,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_SENSORS: {
            SENSOR_COUNTER: DESCRIPTION_SENSOR_COUNTER,
            SENSOR_COUNTER_VALUE: DESCRIPTION_SENSOR_COUNTER_VALUE,
            SENSOR_ANALOG_INPUT: DESCRIPTION_SENSOR_ANALOG_INPUT,
            SENSOR_ANALOG_VALUE: DESCRIPTION_SENSOR_ANALOG_VALUE,
        },
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231219,
    },
    MODEL_PLUS_RGBW_PM: {
        ATTR_NAME: "Shelly Plus RGBW PM",
        ATTR_MODEL_ID: "SNDC-0D4P10WW",
        ATTR_GEN: 2,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_LIGHT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_LIGHT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_LIGHT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_LIGHT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_LIGHT_VOLTAGE,
        },
        ATTR_RGB_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_RGB_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_RGB_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_RGB_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RGB_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_RGB_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240208,
    },
    MODEL_PM_MINI_G3: {
        ATTR_NAME: "Shelly PM Mini Gen3",
        ATTR_MODEL_ID: "S3PM-001PCEU16",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_PM,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_PM,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY_PM,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_PM,
            SENSOR_RETURNED_ENERGY: DESCRIPTION_SENSOR_RETURNED_ENERGY_PM,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_PM,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PLUS_SMOKE: {
        ATTR_BATTERY_POWERED: True,
        ATTR_NAME: "Shelly Plus Smoke",
        ATTR_MODEL_ID: "SNSN-0031Z",
        ATTR_BINARY_SENSORS: {
            SENSOR_ALARM_SOUND: DESCRIPTION_SENSOR_SMOKE_ALARM_SOUND,
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
            SENSOR_SMOKE: DESCRIPTION_SENSOR_SMOKE,
        },
        ATTR_BUTTONS: {BUTTON_MUTE_ALARM: DESCRIPTION_BUTTON_MUTE_ALARM},
        ATTR_SENSORS: {
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BATTERY,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
        ATTR_WAKEUP_PERIOD: 86400,
    },
    MODEL_PLUS_WALL_DIMMER: {
        ATTR_NAME: "Shelly Plus Wall Dimmer",
        ATTR_MODEL_ID: "SNDM-0013US",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_POWER_STRIP_G4: {
        ATTR_NAME: "Shelly Power Strip Gen4",
        ATTR_MODEL_ID: "S4PL-00416EU",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_RELAYS: 4,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_RETURNED_ENERGY: DESCRIPTION_SENSOR_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250804,
    },
    MODEL_PRESENCE_G4: {
        ATTR_NAME: "Shelly Presence Gen4",
        ATTR_MODEL_ID: "S4SN-0U61X",
        ATTR_GEN: 4,
        ATTR_BINARY_SENSORS: {
            SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD,
            SENSOR_PRESENCE: DESCRIPTION_SENSOR_PRESENCE,
        },
        ATTR_SENSORS: {
            SENSOR_DETECTED: DESCRIPTION_SENSOR_DETECTED,
            SENSOR_ILLUMINANCE_LEVEL: DESCRIPTION_SENSOR_ILLUMINANCE_LEVEL,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250915,
    },
    MODEL_PRO_1: {
        ATTR_NAME: "Shelly Pro 1",
        ATTR_MODEL_ID: "SPSW-001XE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_1PM: {
        ATTR_NAME: "Shelly Pro 1PM",
        ATTR_MODEL_ID: "SPSW-x01PE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_2: {
        ATTR_NAME: "Shelly Pro 2",
        ATTR_MODEL_ID: "SPSW-x02XE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_2PM: {
        ATTR_NAME: "Shelly Pro 2PM",
        ATTR_MODEL_ID: "SPSW-x02PE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_COVERS: 1,
        ATTR_COVER_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_COVER,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_COVER,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_COVER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR_COVER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_COVER_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_COVER,
        },
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 2,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_3: {
        ATTR_NAME: "Shelly Pro 3",
        ATTR_MODEL_ID: "SPSW-003XE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 3,
        ATTR_RELAY_BINARY_SENSORS: {SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP},
        ATTR_RELAY_SENSORS: {
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE_STATUS
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_DIMMER_1PM: {
        ATTR_NAME: "Shelly Pro Dimmer 1PM",
        ATTR_MODEL_ID: "SPDM-001PE01EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_LIGHT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_LIGHT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_LIGHT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_LIGHT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_LIGHT_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231005,
    },
    MODEL_PRO_DIMMER_2PM: {
        ATTR_NAME: "Shelly Pro Dimmer 2PM",
        ATTR_MODEL_ID: "SPDM-002PE01EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_LIGHT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_LIGHT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_LIGHT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_LIGHT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_LIGHT_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231005,
    },
    MODEL_PRO_DUAL_COVER_PM: {
        ATTR_NAME: "Shelly Pro Dual Cover PM",
        ATTR_MODEL_ID: "SPSH-002PE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_COVERS: 2,
        ATTR_COVER_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT_COVER,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY_COVER,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER_COVER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR_COVER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_COVER_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE_COVER,
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_EM: {
        ATTR_NAME: "Shelly Pro EM",
        ATTR_MODEL_ID: "SPEM-002CEBEU50",
        ATTR_EMETERS: 2,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_RELAYS: 1,
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_3EM: {
        ATTR_NAME: "Shelly Pro 3EM",
        ATTR_MODEL_ID: "SPEM-003CEBEU",
        ATTR_EMETERS: 1,
        ATTR_EMETER_PHASES: ["a", "b", "c"],
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_N_CURRENT: DESCRIPTION_SENSOR_N_CURRENT,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
            SENSOR_TOTAL_CURRENT: DESCRIPTION_SENSOR_TOTAL_CURRENT,
            SENSOR_TOTAL_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_POWER,
            SENSOR_TOTAL_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_APPARENT_POWER,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_RETURNED_ENERGY,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_PHASE_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_PHASE_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_PHASE_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_PHASE_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231219,
    },
    MODEL_PRO_3EM_3CT63: {
        ATTR_NAME: "Shelly Pro 3EM-3CT63",
        ATTR_MODEL_ID: "SPEM-003CEBEU63",
        ATTR_EMETERS: 1,
        ATTR_EMETER_PHASES: ["a", "b", "c"],
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_N_CURRENT: DESCRIPTION_SENSOR_N_CURRENT,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
            SENSOR_TOTAL_CURRENT: DESCRIPTION_SENSOR_TOTAL_CURRENT,
            SENSOR_TOTAL_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_POWER,
            SENSOR_TOTAL_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_APPARENT_POWER,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_RETURNED_ENERGY,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_PHASE_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_PHASE_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_PHASE_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_PHASE_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241011,
    },
    MODEL_3EM_63_G3: {
        ATTR_NAME: "Shelly 3EM-63 G3",
        ATTR_MODEL_ID: "S3EM-003CXCEU63",
        ATTR_EMETERS: 1,
        ATTR_EMETER_PHASES: ["a", "b", "c"],
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_N_CURRENT: DESCRIPTION_SENSOR_N_CURRENT,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
            SENSOR_TOTAL_CURRENT: DESCRIPTION_SENSOR_TOTAL_CURRENT,
            SENSOR_TOTAL_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_POWER,
            SENSOR_TOTAL_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_APPARENT_POWER,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_RETURNED_ENERGY,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_PHASE_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_PHASE_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_PHASE_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_PHASE_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250520,
    },
    MODEL_PRO_3EM_3CT63_MONOPHASE: {
        ATTR_NAME: "Shelly Pro 3EM-3CT63",
        ATTR_MODEL_ID: "SPEM-003CEBEU63",
        ATTR_EMETERS: 1,
        ATTR_EMETER_PHASES: ["a", "b", "c"],
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_N_CURRENT: DESCRIPTION_SENSOR_N_CURRENT,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
            SENSOR_TOTAL_CURRENT: DESCRIPTION_SENSOR_TOTAL_CURRENT,
            SENSOR_TOTAL_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_POWER,
            SENSOR_TOTAL_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_APPARENT_POWER,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_RETURNED_ENERGY,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_PHASE_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_PHASE_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_PHASE_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_PHASE_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241011,
    },
    MODEL_PRO_3EM_400: {
        ATTR_NAME: "Shelly Pro 3EM-400",
        ATTR_MODEL_ID: "SPEM-003CEBEU400",
        ATTR_EMETERS: 1,
        ATTR_EMETER_PHASES: ["a", "b", "c"],
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_N_CURRENT: DESCRIPTION_SENSOR_N_CURRENT,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
            SENSOR_TOTAL_CURRENT: DESCRIPTION_SENSOR_TOTAL_CURRENT,
            SENSOR_TOTAL_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_POWER,
            SENSOR_TOTAL_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_TOTAL_APPARENT_POWER,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER0_TOTAL_ACTIVE_RETURNED_ENERGY,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_PHASE_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_PHASE_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_PHASE_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_PHASE_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_PHASE_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_PHASE_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231219,
    },
    MODEL_PRO_3EM_MONOPHASE: {
        ATTR_NAME: "Shelly Pro 3EM",
        ATTR_MODEL_ID: "SPEM-003CEBEU",
        ATTR_EMETERS: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
            SENSOR_DEVICE_TEMPERATURE: DESCRIPTION_SENSOR_DEVICE_TEMPERATURE,
        },
        ATTR_EMETER_SENSORS: {
            SENSOR_ACTIVE_POWER: DESCRIPTION_SENSOR_EMETER_ACTIVE_POWER,
            SENSOR_APPARENT_POWER: DESCRIPTION_SENSOR_EMETER_APPARENT_POWER,
            SENSOR_CURRENT: DESCRIPTION_SENSOR_EMETER_CURRENT,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_EMETER_POWER_FACTOR,
            SENSOR_TOTAL_ACTIVE_ENERGY: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_ENERGY,
            SENSOR_TOTAT_ACTIVE_RETURNED_ENERGY: DESCRIPTION_SENSOR_EMETER_TOTAL_ACTIVE_RETURNED_ENERGY,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_EMETER_VOLTAGE,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_EMETER_FREQUENCY,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231219,
    },
    MODEL_PRO_4PM: {
        ATTR_NAME: "Shelly Pro 4PM",
        ATTR_MODEL_ID: "SPSW-x04PE16EU",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 4,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_POWER_FACTOR: DESCRIPTION_SENSOR_POWER_FACTOR,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_ETH_IP: DESCRIPTION_SENSOR_ETH_IP,
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20230803,
    },
    MODEL_PRO_RGBWW_PM: {
        ATTR_NAME: "Shelly Pro RGBWW PM",
        ATTR_MODEL_ID: "SPDC-0D5PE16EU",
        ATTR_GEN: 2,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_CCT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CCT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_CCT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_CCT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_CCT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_CCT_VOLTAGE,
        },
        ATTR_LIGHT_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_LIGHT_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_LIGHT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_LIGHT_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_LIGHT_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_LIGHT_VOLTAGE,
        },
        ATTR_RGB_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_RGB_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_RGB_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_RGB_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RGB_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_RGB_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240816,
    },
    MODEL_DUO_BULB_G3: {
        ATTR_NAME: "Shelly Duo Bulb Gen3",
        ATTR_MODEL_ID: "S3BL-D010009AEU",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_CCT_SENSORS: {
            SENSOR_ENERGY: DESCRIPTION_SENSOR_CCT_ENERGY,
            SENSOR_POWER: DESCRIPTION_SENSOR_CCT_POWER,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250909,
    },
    MODEL_WALL_DISPLAY: {
        ATTR_NAME: "Shelly Wall Display",
        ATTR_MODEL_ID: "SAWD-xA1XX10EU1",
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_HUMIDITY,
            SENSOR_ILLUMINANCE: DESCRIPTION_SENSOR_ILLUMINANCE,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_THERMOSTATS: {0: DESCRIPTION_THERMOSTAT},
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE_SYS,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA_SYS,
        },
        ATTR_MIN_FIRMWARE_DATE: 20231117,
    },
    MODEL_X_MOD1: {
        ATTR_NAME: "Shelly X MOD1",
        ATTR_MODEL_ID: "S3MX-0A",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 4,
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20240520,
    },
    MODEL_FLOOD_G4: {
        ATTR_BATTERY_POWERED: True,
        ATTR_NAME: "Shelly Flood Gen4",
        ATTR_MODEL_ID: "S4SN-0071A",
        ATTR_BINARY_SENSORS: {
            SENSOR_ALARM_SOUND: DESCRIPTION_SENSOR_FLOOD_ALARM_SOUND,
            SENSOR_CABLE_UNPLUGGED: DESCRIPTION_SENSOR_CABLE_UNPLUGGED,
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
            SENSOR_FLOOD: DESCRIPTION_SENSOR_FLOOD,
        },
        ATTR_SENSORS: {
            SENSOR_BATTERY: DESCRIPTION_SENSOR_BATTERY,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_MIN_FIRMWARE_DATE: 20250129,
        ATTR_WAKEUP_PERIOD: 43200,
    },
    MODEL_ST1820: {
        ATTR_NAME: "LinkedGo Smart Thermostat ST1820",
        ATTR_MODEL_ID: "ST1820",
        ATTR_BRAND: "LinkedGo",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
        },
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_HUMIDITY_200,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE_201,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_SWITCHES: {
            SWITCH_ANTI_FREEZE: DESCRIPTION_SWITCH_ANTI_FREEZE,
            SWITCH_CHILD_LOCK: DESCRIPTION_SWITCH_CHILD_LOCK,
        },
        ATTR_THERMOSTATS: {0: DESCRIPTION_THERMOSTAT_ST1820},
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: {},
            UPDATE_FIRMWARE_BETA: {},
        },
        ATTR_MIN_FIRMWARE_DATE: 20241121,
    },
    MODEL_ST802_B: {
        ATTR_NAME: "LinkedGo Smart Thermostat ST802-B",
        ATTR_MODEL_ID: "ST802-B",
        ATTR_BRAND: "LinkedGo",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
        },
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_HUMIDITY: DESCRIPTION_SENSOR_HUMIDITY_200,
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_TEMPERATURE_201,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_SWITCHES: {
            SWITCH_THERMOSTAT: DESCRIPTION_SWITCH_THERMOSTAT,
            SWITCH_ANTI_FREEZE: DESCRIPTION_SWITCH_ANTI_FREEZE,
        },
        ATTR_THERMOSTATS: {0: DESCRIPTION_THERMOSTAT_ST802_B},
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: {},
            UPDATE_FIRMWARE_BETA: {},
        },
        ATTR_MIN_FIRMWARE_DATE: 20241121,
    },
    MODEL_WATER_VALVE: {
        ATTR_NAME: "FrankEver Smart Water Valve",
        ATTR_MODEL_ID: "WaterValve",
        ATTR_BRAND: "FrankEver",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {
            SENSOR_CLOUD: DESCRIPTION_SLEEPING_SENSOR_CLOUD,
            SENSOR_POWER_SUPPLY: DESCRIPTION_SENSOR_POWER_SUPPLY,
            SENSOR_FIRMWARE: DESCRIPTION_SLEEPING_SENSOR_FIRMWARE,
        },
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SLEEPING_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SLEEPING_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SLEEPING_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SLEEPING_SENSOR_WIFI_SIGNAL,
        },
        ATTR_VALVES: {0: DESCRIPTION_VALVE_FRANKEVER},
        ATTR_MIN_FIRMWARE_DATE: 20241121,
    },
    MODEL_OGEMRAY_25A: {
        ATTR_NAME: "Ogemray 25A Smart Switch",
        ATTR_MODEL_ID: "Ogemray25A",
        ATTR_BRAND: "Ogemray",
        ATTR_GEN: 3,
        ATTR_BINARY_SENSORS: {SENSOR_CLOUD: DESCRIPTION_SENSOR_CLOUD},
        ATTR_BUTTONS: {BUTTON_RESTART: DESCRIPTION_BUTTON_RESTART},
        ATTR_INPUT_BINARY_SENSORS: {SENSOR_INPUT: DESCRIPTION_SENSOR_INPUT},
        ATTR_INPUT_EVENTS: [
            EVENT_BUTTON_DOWN,
            EVENT_BUTTON_UP,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_SINGLE_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        ATTR_RELAYS: 1,
        ATTR_RELAY_BINARY_SENSORS: {
            SENSOR_OVERPOWER: DESCRIPTION_SENSOR_OVERPOWER,
            SENSOR_OVERTEMP: DESCRIPTION_SENSOR_OVERTEMP,
            SENSOR_OVERVOLTAGE: DESCRIPTION_SENSOR_OVERVOLTAGE,
        },
        ATTR_RELAY_SENSORS: {
            SENSOR_CURRENT: DESCRIPTION_SENSOR_CURRENT,
            SENSOR_ENERGY: DESCRIPTION_SENSOR_ENERGY,
            SENSOR_FREQUENCY: DESCRIPTION_SENSOR_FREQUENCY,
            SENSOR_POWER: DESCRIPTION_SENSOR_POWER,
            SENSOR_TEMPERATURE: DESCRIPTION_SENSOR_RELAY_TEMPERATURE,
            SENSOR_VOLTAGE: DESCRIPTION_SENSOR_VOLTAGE,
        },
        ATTR_SENSORS: {
            SENSOR_LAST_RESTART: DESCRIPTION_SENSOR_LAST_RESTART,
            SENSOR_SSID: DESCRIPTION_SENSOR_SSID,
            SENSOR_WIFI_IP: DESCRIPTION_SENSOR_WIFI_IP,
            SENSOR_WIFI_SIGNAL: DESCRIPTION_SENSOR_WIFI_SIGNAL,
        },
        ATTR_UPDATES: {
            UPDATE_FIRMWARE: DESCRIPTION_UPDATE_FIRMWARE,
            UPDATE_FIRMWARE_BETA: DESCRIPTION_UPDATE_FIRMWARE_BETA,
        },
        ATTR_MIN_FIRMWARE_DATE: 20241128,
    },
}


def get_consumption_type(consumption_list, relay_id):
    """Return consumption type for relay."""
    try:
        consumption_type = consumption_list[relay_id]
    except IndexError:
        return ATTR_SWITCH

    if "light" in consumption_type.lower():
        return ATTR_LIGHT

    if "fan" in consumption_type.lower():
        return ATTR_FAN

    return ATTR_SWITCH


def mqtt_publish(topic, payload):
    """Publish data to MQTT broker."""
    payload_str = str(payload).replace("'", '"').replace("^", '\\"')
    service_data = {
        "topic": topic,
        "payload": payload_str,
        "retain": True,
        "qos": 0,
    }
    logger.debug("Sending to MQTT broker: %s %s", topic, payload_str)  # noqa: F821
    hass.services.call("mqtt", "publish", service_data, False)  # noqa: F821


def format_mac(mac):
    """Format the mac address string."""
    return ":".join(mac[i : i + 2] for i in range(0, 12, 2))


def encode_config_topic(string):
    """Encode a config topic to UTF-8."""
    return string.encode("ascii", "ignore").decode("utf-8")


def get_cover(cover_id, profile):
    """Create configuration for Shelly cover entity."""
    topic = encode_config_topic(f"{disc_prefix}/cover/{device_id}-{cover_id}/config")

    if profile != ATTR_COVER:
        return topic, ""

    cover_name = (
        device_config[f"cover:{cover_id}"][ATTR_NAME] or f"Cover {cover_id}"
    ).replace("'", "_")
    payload = {
        KEY_NAME: cover_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_POSITION_TOPIC: TOPIC_COVER.format(id=cover_id),
        KEY_STATE_TOPIC: TOPIC_COVER.format(id=cover_id),
        KEY_VALUE_TEMPLATE: "{%if value_json.state!=^calibrating^%}{{value_json.state}}{%endif%}",
        KEY_POSITION_TEMPLATE: "{%if is_number(value_json.get(^current_pos^))%}{{value_json.current_pos}}{%endif%}",
        KEY_SET_POSITION_TOPIC: TOPIC_RPC,
        KEY_SET_POSITION_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Cover.GoToPosition^,^params^:{{^id^:{cover_id},^pos^:{{{{position}}}}}}}}",
        KEY_PAYLOAD_OPEN: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Cover.Open^,^params^:{{^id^:{cover_id}}}}}",
        KEY_PAYLOAD_CLOSE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Cover.Close^,^params^:{{^id^:{cover_id}}}}}",
        KEY_PAYLOAD_STOP: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Cover.Stop^,^params^:{{^id^:{cover_id}}}}}",
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-{cover_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    if device_config[f"cover:{cover_id}"].get("slat", {}).get("enable", False):
        payload[KEY_TILT_COMMAND_TEMPLATE] = (
            f"{{^id^:1,^src^:^{source_topic}^,^method^:^Cover.GoToPosition^,^params^:{{^id^:{cover_id},^slat_pos^:{{{{tilt_position}}}}}}}}"
        )
        payload[KEY_TILT_COMMAND_TOPIC] = TOPIC_RPC
        payload[KEY_TILT_STATUS_TEMPLATE] = (
            "{%if is_number(value_json.get(^slat_pos^))%}{{value_json.slat_pos}}{%endif%}"
        )
        payload[KEY_TILT_STATUS_TOPIC] = TOPIC_COVER.format(id=cover_id)

    return topic, payload


def get_valve(valve_id, description):
    """Create configuration for Shelly valve entity."""
    key = description.get(ATTR_KEY, "valve")

    topic = encode_config_topic(f"{disc_prefix}/valve/{device_id}-{valve_id}/config")

    if f"{key}:{valve_id}" not in device_config:
        return topic, ""

    valve_name = "Valve"

    payload = {
        KEY_NAME: valve_name,
        KEY_UNIQUE_ID: f"{device_id}-{valve_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
        KEY_AVAILABILITY: availability,
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_COMMAND_TOPIC: description[KEY_COMMAND_TOPIC],
        KEY_COMMAND_TEMPLATE: description[KEY_COMMAND_TEMPLATE].format(
            source=source_topic
        ),
        KEY_STATE_TOPIC: description[KEY_STATE_TOPIC],
        KEY_VALUE_TEMPLATE: description[KEY_VALUE_TEMPLATE],
        KEY_REPORTS_POSITION: str(description[KEY_REPORTS_POSITION]).lower(),
    }

    return topic, payload


def get_climate(thermostat_id, description):
    """Create configuration for Shelly climate entity."""
    key = description.get(ATTR_KEY, "thermostat")

    topic = encode_config_topic(
        f"{disc_prefix}/climate/{device_id}-{thermostat_id}/config"
    )

    if f"{key}:{thermostat_id}" not in device_config:
        return topic, ""

    thermostat_type = device_config.get(f"{key}:{thermostat_id}", {}).get(
        "type", "heating"
    )
    thermostat_default_mode = "cool" if thermostat_type == "cooling" else "heat"

    thermostat_name = (
        device_config.get(f"{key}:{thermostat_id}", {}).get(ATTR_NAME) or "Thermostat"
    ).replace("'", "_")

    thermostat_topic = TOPIC_THERMOSTAT.format(id=thermostat_id)
    current_temp_topic = (
        description.get(KEY_CURRENT_TEMPERATURE_TOPIC) or thermostat_topic
    )
    temp_state_topic = description.get(KEY_TEMPERATURE_STATE_TOPIC) or thermostat_topic
    mode_state_topic = description.get(KEY_MODE_STATE_TOPIC) or thermostat_topic

    min_temp = (
        description.get(ATTR_TEMPERATURE_MIN)
        or device_config[f"{key}:{thermostat_id}"]["temp_range"][0]
    )
    max_temp = (
        description.get(ATTR_TEMPERATURE_MAX)
        or device_config[f"{key}:{thermostat_id}"]["temp_range"][1]
    )
    mode_state_tpl = description.get(KEY_MODE_STATE_TEMPLATE) or TPL_THERMOSTAT_MODE
    mode_command_tpl = (
        description.get(KEY_MODE_COMMAND_TEMPLATE) or TPL_SET_THERMOSTAT_MODE
    )
    temp_command_tpl = (
        description.get(KEY_TEMPERATURE_COMMAND_TEMPLATE) or TPL_SET_TARGET_TEMPERATURE
    )

    payload = {
        KEY_NAME: thermostat_name,
        KEY_CURRENT_TEMPERATURE_TOPIC: current_temp_topic,
        KEY_CURRENT_TEMPERATURE_TEMPLATE: description.get(
            KEY_CURRENT_TEMPERATURE_TEMPLATE
        )
        or TPL_CURRENT_TEMPERATURE,
        KEY_TEMPERATURE_STATE_TOPIC: temp_state_topic,
        KEY_TEMPERATURE_STATE_TEMPLATE: description.get(KEY_TEMPERATURE_STATE_TEMPLATE)
        or TPL_TARGET_TEMPERATURE,
        KEY_TEMPERATURE_COMMAND_TOPIC: TOPIC_RPC,
        KEY_TEMPERATURE_COMMAND_TEMPLATE: temp_command_tpl.format(
            source=source_topic, thermostat=thermostat_id
        ),
        KEY_TEMP_STEP: description[ATTR_TEMPERATURE_STEP],
        KEY_MIN_TEMP: min_temp,
        KEY_MAX_TEMP: max_temp,
        KEY_MODE_STATE_TOPIC: mode_state_topic,
        KEY_MODE_COMMAND_TOPIC: TOPIC_RPC,
        KEY_MODE_COMMAND_TEMPLATE: mode_command_tpl.format(
            source=source_topic, thermostat=thermostat_id
        ),
        KEY_UNIQUE_ID: f"{device_id}-{thermostat_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    if model == MODEL_ST802_B:
        payload[KEY_AVAILABILITY] = [
            {
                KEY_TOPIC: "~status/boolean:201",
                KEY_VALUE_TEMPLATE: TPL_VALUE_ONLINE,
            }
        ]
    else:
        payload[KEY_AVAILABILITY] = availability

    if fan_modes := description.get(KEY_FAN_MODES):
        payload[KEY_FAN_MODES] = fan_modes
        payload[KEY_FAN_MODE_STATE_TOPIC] = description[KEY_FAN_MODE_STATE_TOPIC]
        payload[KEY_FAN_MODE_STATE_TEMPLATE] = description[KEY_FAN_MODE_STATE_TEMPLATE]
        payload[KEY_FAN_MODE_COMMAND_TOPIC] = TOPIC_RPC
        payload[KEY_FAN_MODE_COMMAND_TEMPLATE] = description[
            KEY_FAN_MODE_COMMAND_TEMPLATE
        ].format(source=source_topic)

    if target_humidity_state_topic := description.get(KEY_TARGET_HUMIDITY_STATE_TOPIC):
        payload[KEY_TARGET_HUMIDITY_STATE_TOPIC] = target_humidity_state_topic
        payload[KEY_TARGET_HUMIDITY_STATE_TEMPLATE] = description[
            KEY_TARGET_HUMIDITY_STATE_TEMPLATE
        ]
        payload[KEY_TARGET_HUMIDITY_COMMAND_TEMPLATE] = description[
            KEY_TARGET_HUMIDITY_COMMAND_TEMPLATE
        ].format(source=source_topic)
        payload[KEY_TARGET_HUMIDITY_COMMAND_TOPIC] = TOPIC_RPC
        payload[KEY_MAX_HUMIDITY] = description[ATTR_HUMIDITY_MAX]
        payload[KEY_MIN_HUMIDITY] = description[ATTR_HUMIDITY_MIN]

    if model != MODEL_ST802_B:
        payload[KEY_MODE_STATE_TEMPLATE] = mode_state_tpl.format(
            action=thermostat_default_mode
        )
    else:
        payload[KEY_MODE_STATE_TEMPLATE] = mode_state_tpl

    if model not in (MODEL_ST1820, MODEL_ST802_B):
        payload[KEY_ACTION_TOPIC] = thermostat_topic
        payload[KEY_ACTION_TEMPLATE] = TPL_ACTION_TEMPLATE.format(
            action=thermostat_type
        )

    if f"humidity:{thermostat_id}" in device_config:
        payload[KEY_CURRENT_HUMIDITY_TOPIC] = TOPIC_HUMIDITY.format(id=thermostat_id)
        payload[KEY_CURRENT_HUMIDITY_TEMPLATE] = TPL_HUMIDITY
    elif humidity_topic := description.get(KEY_CURRENT_HUMIDITY_TOPIC):
        payload[KEY_CURRENT_HUMIDITY_TOPIC] = humidity_topic
        payload[KEY_CURRENT_HUMIDITY_TEMPLATE] = description[
            KEY_CURRENT_HUMIDITY_TEMPLATE
        ]

    if modes := description.get(KEY_MODES):
        payload[KEY_MODES] = modes
    else:
        payload[KEY_MODES] = ["off", thermostat_default_mode]

    return topic, payload


def get_blu_climate(thermostat_id: str, description) -> tuple:
    """Create configuration for Shelly BLU climate entity."""
    topic = encode_config_topic(
        f"{disc_prefix}/climate/{device_id}-{thermostat_id}/config"
    )
    payload = {
        KEY_NAME: "",
        KEY_ACTION_TOPIC: TOPIC_STATUS_BLU_TRV.format(id=thermostat_id),
        KEY_ACTION_TEMPLATE: TPL_BLU_THERMOSTAT_ACTION,
        KEY_CURRENT_TEMPERATURE_TOPIC: TOPIC_STATUS_BLU_TRV.format(id=thermostat_id),
        KEY_CURRENT_TEMPERATURE_TEMPLATE: TPL_CURRENT_TEMPERATURE,
        KEY_TEMPERATURE_STATE_TOPIC: TOPIC_STATUS_BLU_TRV.format(id=thermostat_id),
        KEY_TEMPERATURE_STATE_TEMPLATE: TPL_TARGET_TEMPERATURE,
        KEY_TEMPERATURE_COMMAND_TOPIC: TOPIC_RPC,
        KEY_TEMPERATURE_COMMAND_TEMPLATE: TPL_SET_BLU_TARGET_TEMPERATURE.format(
            source=source_topic, thermostat=thermostat_id
        ),
        KEY_TEMP_STEP: description[ATTR_TEMPERATURE_STEP],
        KEY_MIN_TEMP: description[ATTR_TEMPERATURE_MIN],
        KEY_MAX_TEMP: description[ATTR_TEMPERATURE_MAX],
        KEY_MODES: ["heat"],
        KEY_MODE_STATE_TOPIC: TOPIC_STATUS_BLU_TRV.format(id=thermostat_id),
        KEY_MODE_STATE_TEMPLATE: "heat",
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-{thermostat_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    return topic, payload


def get_switch(relay_id, relay_type, profile, description={}):
    """Create configuration for Shelly switch entity."""
    topic = encode_config_topic(f"{disc_prefix}/switch/{device_id}-{relay_id}/config")

    key = description.get(ATTR_KEY) or ATTR_SWITCH

    if f"{device_id}/c/switch:{relay_id}".lower() in device_config.get(
        f"thermostat:{relay_id}", {}
    ).get("actuator", ""):
        return topic, ""

    if relay_type != ATTR_SWITCH or profile == ATTR_COVER:
        return topic, ""

    if name := description.get(ATTR_NAME):
        relay_name = name
    else:
        relay_name = (
            device_config.get(f"{key}:{relay_id}", {}).get(ATTR_NAME)
            or f"Relay {relay_id}"
        ).replace("'", "_")
    payload_off_tpl = description.get(KEY_PAYLOAD_OFF) or TPL_SWITCH_PAYLOAD_OFF
    payload_on_tpl = description.get(KEY_PAYLOAD_ON) or TPL_SWITCH_PAYLOAD_ON
    topic_switch = description.get(KEY_STATE_TOPIC) or TOPIC_SWITCH_RELAY
    value_template = description.get(KEY_VALUE_TEMPLATE) or TPL_SWITCH_OUTPUT

    payload = {
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_PAYLOAD_OFF: payload_off_tpl.format(source=source_topic, id=relay_id),
        KEY_PAYLOAD_ON: payload_on_tpl.format(source=source_topic, id=relay_id),
        KEY_STATE_TOPIC: topic_switch.format(id=relay_id),
        KEY_VALUE_TEMPLATE: value_template,
        KEY_STATE_OFF: VALUE_OFF,
        KEY_STATE_ON: VALUE_ON,
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-{relay_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    if entity_category := description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = entity_category

    if icon := description.get(KEY_ICON):
        payload[KEY_ICON] = icon

    return topic, payload


def get_relay_light(relay_id, relay_type, profile):
    """Create configuration for Shelly relay as light entity."""
    topic = encode_config_topic(f"{disc_prefix}/light/{device_id}-{relay_id}/config")

    if relay_type != ATTR_LIGHT or profile == ATTR_COVER:
        return topic, ""

    relay_name = (
        device_config[f"switch:{relay_id}"][ATTR_NAME] or f"Relay {relay_id}"
    ).replace("'", "_")
    payload = {
        KEY_SCHEMA: "template",
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_COMMAND_OFF_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:false}}}}",
        KEY_COMMAND_ON_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:true}}}}",
        KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY.format(id=relay_id),
        KEY_STATE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-{relay_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }
    return topic, payload


def get_relay_fan(relay_id, relay_type, profile):
    """Create configuration for Shelly relay as fan entity."""
    topic = encode_config_topic(f"{disc_prefix}/fan/{device_id}-{relay_id}/config")

    if relay_type != ATTR_FAN or profile == ATTR_COVER:
        return topic, ""

    relay_name = (
        device_config[f"switch:{relay_id}"][ATTR_NAME] or f"Relay {relay_id}"
    ).replace("'", "_")
    payload = {
        KEY_NAME: relay_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_COMMAND_TEMPLATE: f"{{%if value==^ON^%}}{{^id^:1,^src^:^{source_topic}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:true}}}}{{%else%}}{{^id^:1,^src^:^{source_topic}^,^method^:^Switch.Set^,^params^:{{^id^:{relay_id},^on^:false}}}}{{%endif%}}",
        KEY_STATE_TOPIC: TOPIC_SWITCH_RELAY.format(id=relay_id),
        KEY_STATE_VALUE_TEMPLATE: "{%if value_json.output%}ON{%else%}OFF{%endif%}",
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-{relay_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }
    return topic, payload


def get_light(light_id: int):
    """Create configuration for Shelly light entity."""
    topic = encode_config_topic(f"{disc_prefix}/light/{device_id}-{light_id}/config")

    light_name = (
        device_config[f"light:{light_id}"][ATTR_NAME] or f"Light {light_id}"
    ).replace("'", "_")
    payload = {
        KEY_SCHEMA: "template",
        KEY_NAME: light_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_COMMAND_OFF_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Light.Set^,^params^:{{^id^:{light_id},^on^:false{{%if transition is defined%}},^transition_duration^:{{{{max(transition|int,{MIN_LIGHT_TRANSITION})}}}}{{%endif%}}}}}}",
        KEY_COMMAND_ON_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^Light.Set^,^params^:{{^id^:{light_id},^on^:true{{%if transition is defined%}},^transition_duration^:{{{{max(transition|int,{MIN_LIGHT_TRANSITION})}}}}{{%endif%}}{{%if brightness is defined%}},^brightness^:{{{{brightness|float|multiply(0.3922)|round}}}}{{%endif%}}}}}}",
        KEY_STATE_TOPIC: TOPIC_LIGHT.format(id=light_id),
        KEY_STATE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        KEY_BRIGHTNESS_TEMPLATE: "{{value_json.brightness|float|multiply(2.55)|round}}",
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-{light_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }
    return topic, payload


def get_cct_light(cct_id: int):
    """Create configuration for Shelly CCT light entity."""
    topic = encode_config_topic(f"{disc_prefix}/light/{device_id}-cct-{cct_id}/config")

    light_name = (
        device_config[f"cct:{cct_id}"][ATTR_NAME] or f"CCT light {cct_id}"
    ).replace("'", "_")

    min_ct = 2700
    max_ct = 6500
    if "ct_range" in device_config[f"cct:{cct_id}"]:
        min_ct = device_config[f"cct:{cct_id}"]["ct_range"][0]
        max_ct = device_config[f"cct:{cct_id}"]["ct_range"][1]

    payload = {
        KEY_SCHEMA: "template",
        KEY_NAME: light_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_COMMAND_OFF_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^CCT.Set^,^params^:{{^id^:{cct_id},^on^:false}}{{%if transition is defined%}},^transition_duration^:{{{{max(transition|int,{MIN_LIGHT_TRANSITION})}}}}{{%endif%}}}}",
        KEY_COMMAND_ON_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^CCT.Set^,^params^:{{^id^:{cct_id},^on^:true{{%if transition is defined%}},^transition_duration^:{{{{max(transition|int,{MIN_LIGHT_TRANSITION})}}}}{{%endif%}}{{%if brightness is defined%}},^brightness^:{{{{brightness|float|multiply(0.3922)|round}}}}{{%endif%}}{{%if color_temp is defined%}},^ct^:{{{{(1000000/color_temp)|round}}}}{{%endif%}}}}}}",
        KEY_STATE_TOPIC: TOPIC_STATUS_CCT.format(id=cct_id),
        KEY_STATE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        KEY_BRIGHTNESS_TEMPLATE: "{{value_json.brightness|float|multiply(2.55)|round}}",
        KEY_COLOR_TEMP_TEMPLATE: "{{(1000000/value_json.ct)|round}}",
        KEY_MAX_MIREDS: round(1000000 / min_ct),
        KEY_MIN_MIREDS: round(1000000 / max_ct),
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-cct-{cct_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }
    return topic, payload


def get_rgb_light(rgb_id: int):
    """Create configuration for Shelly RGB light entity."""
    topic = encode_config_topic(f"{disc_prefix}/light/{device_id}-rgb-{rgb_id}/config")

    light_name = (
        device_config[f"rgb:{rgb_id}"][ATTR_NAME] or f"RGB light {rgb_id}"
    ).replace("'", "_")
    payload = {
        KEY_SCHEMA: "template",
        KEY_NAME: light_name,
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_COMMAND_OFF_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^RGB.Set^,^params^:{{^id^:{rgb_id},^on^:false}}{{%if transition is defined%}},^transition_duration^:{{{{max(transition|int,{MIN_LIGHT_TRANSITION})}}}}{{%endif%}}}}",
        KEY_COMMAND_ON_TEMPLATE: f"{{^id^:1,^src^:^{source_topic}^,^method^:^RGB.Set^,^params^:{{^id^:{rgb_id},^on^:true{{%if transition is defined%}},^transition_duration^:{{{{max(transition|int,{MIN_LIGHT_TRANSITION})}}}}{{%endif%}}{{%if brightness is defined%}},^brightness^:{{{{brightness|float|multiply(0.3922)|round}}}}{{%endif%}}{{%if blue is defined and green is defined and red is defined%}},^rgb^:{{{{[red,green,blue]}}}}{{%elif blue is defined and green is defined%}},^rgb^:{{{{[0,green,blue]}}}}{{%elif red is defined and green is defined%}},^rgb^:{{{{[red,green,0]}}}}{{%elif blue is defined and red is defined%}},^rgb^:{{{{[red,0,blue]}}}}{{%elif blue is defined%}},^rgb^:{{{{[0,0,blue]}}}}{{%elif green is defined%}},^rgb^:{{{{[0,green,0]}}}}{{%elif red is defined%}},^rgb^:{{{{[red,0,0]}}}}{{%endif%}}}}}}",
        KEY_STATE_TOPIC: TOPIC_STATUS_RGB.format(id=rgb_id),
        KEY_STATE_TEMPLATE: "{%if value_json.output%}on{%else%}off{%endif%}",
        KEY_BRIGHTNESS_TEMPLATE: "{{value_json.brightness|float|multiply(2.55)|round}}",
        KEY_BLUE_TEMPLATE: "{{value_json.rgb[2]}}",
        KEY_GREEN_TEMPLATE: "{{value_json.rgb[1]}}",
        KEY_RED_TEMPLATE: "{{value_json.rgb[0]}}",
        KEY_AVAILABILITY: availability,
        KEY_UNIQUE_ID: f"{device_id}-rgb-{rgb_id}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }
    return topic, payload


def get_sensor(
    sensor,
    description,
    profile=None,
    relay_id=None,
    light_id=None,
    rgb_id=None,
    cct_id=None,
    cover_id=None,
    emeter_id=None,
    emeter_phase=None,
    sensor_id=None,
    input_id=None,
    thermostat_id=None,
    bt_id=None,
):
    """Create configuration for Shelly sensor entity."""
    if emeter_id is not None and emeter_phase is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{emeter_id}-{emeter_phase}-{sensor}/config"
        )
    elif emeter_id is not None and emeter_phase is None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{emeter_id}-{sensor}/config"
        )
    elif cover_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-cover-{cover_id}-{sensor}/config"
        )
    elif relay_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{relay_id}-{sensor}/config"
        )
    elif light_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{light_id}-{sensor}/config"
        )
    elif rgb_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-rgb-{rgb_id}-{sensor}/config"
        )
    elif cct_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-cct-{cct_id}-{sensor}/config"
        )
    elif sensor_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{sensor_id}-{sensor}/config"
        )
    elif bt_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/sensor/{device_id}-{bt_id}-{sensor}/config"
        )
    else:
        topic = encode_config_topic(f"{disc_prefix}/sensor/{device_id}-{sensor}/config")

    if (
        input_id is not None
        and description.get(ATTR_REMOVAL_CONDITION)
        and description[ATTR_REMOVAL_CONDITION](device_config, input_id)
    ):
        return topic, ""

    if profile == ATTR_LIGHT and light_id is None:
        return topic, ""

    if profile == ATTR_RGB and rgb_id is None:
        return topic, ""

    if profile == ATTR_COVER and cover_id is None:
        return topic, ""

    if profile == ATTR_SWITCH and relay_id is None:
        return topic, ""

    if cover_id is not None:
        switch_name = (
            device_config[f"cover:{cover_id}"][ATTR_NAME] or f"Cover {cover_id}"
        ).replace("'", "_")
        unique_id = f"{device_id}-cover-{cover_id}-{sensor}".lower()
        sensor_name = f"{switch_name} {description[KEY_NAME]}"
    elif relay_id is not None:
        switch_name = (
            device_config[f"switch:{relay_id}"].get(ATTR_NAME, {})
            or f"Relay {relay_id}"
        ).replace("'", "_")
        unique_id = f"{device_id}-{relay_id}-{sensor}".lower()
        sensor_name = f"{switch_name} {description[KEY_NAME]}"
    elif light_id is not None:
        light_name = (
            device_config[f"light:{light_id}"].get(ATTR_NAME, {}) or f"Light {light_id}"
        ).replace("'", "_")
        unique_id = f"{device_id}-{light_id}-{sensor}".lower()
        sensor_name = f"{light_name} {description[KEY_NAME]}"
    elif rgb_id is not None:
        rgb_name = (
            device_config[f"rgb:{rgb_id}"].get(ATTR_NAME, {}) or f"RGB light {rgb_id}"
        ).replace("'", "_")
        unique_id = f"{device_id}-rgb-{rgb_id}-{sensor}".lower()
        sensor_name = f"{rgb_name} {description[KEY_NAME]}"
    elif cct_id is not None:
        cct_name = (
            device_config[f"cct:{cct_id}"].get(ATTR_NAME, {}) or f"CCT light {cct_id}"
        ).replace("'", "_")
        unique_id = f"{device_id}-cct-{cct_id}-{sensor}".lower()
        sensor_name = f"{cct_name} {description[KEY_NAME]}"
    elif emeter_id is not None and emeter_phase is not None:
        unique_id = f"{device_id}-{emeter_id}-{emeter_phase}-{sensor}".lower()
        sensor_name = description[KEY_NAME].format(phase=emeter_phase.upper())
    elif emeter_id is not None and emeter_phase is None:
        unique_id = f"{device_id}-{emeter_id}-{sensor}".lower()
        sensor_name = description[KEY_NAME].format(emeter_id=emeter_id)
    elif sensor_id is not None:
        unique_id = f"{device_id}-{sensor_id}-{sensor}".lower()
        sensor_name = device_config[f"{sensor}:{sensor_id}"][ATTR_NAME] or description[
            KEY_NAME
        ].format(sensor=sensor_id).replace("'", "_")
    elif bt_id is not None:
        unique_id = f"{device_id}-{bt_id}-{sensor}".lower()
        sensor_name = description[KEY_NAME]
    elif input_id is not None:
        unique_id = f"{device_id}-{input_id}-{sensor}".lower()
        sensor_name = device_config[f"input:{input_id}"][ATTR_NAME] or description[
            KEY_NAME
        ].format(input=input_id).replace("'", "_")
    else:
        unique_id = f"{device_id}-{sensor}".lower()
        sensor_name = description[KEY_NAME]

    payload = {
        KEY_NAME: sensor_name,
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    if availability:
        payload[KEY_AVAILABILITY] = availability

    if expire_after:
        payload[KEY_EXPIRE_AFTER] = expire_after

    if emeter_id is not None and emeter_phase is not None:
        payload[KEY_VALUE_TEMPLATE] = description[KEY_VALUE_TEMPLATE].format(
            phase=emeter_phase
        )
    elif (
        relay_id is not None
        and description[KEY_VALUE_TEMPLATE] == TPL_RELAY_TEMPERATURE
    ):
        payload[KEY_VALUE_TEMPLATE] = description[KEY_VALUE_TEMPLATE].format(
            relay=relay_id
        )
    else:
        payload[KEY_VALUE_TEMPLATE] = description[KEY_VALUE_TEMPLATE]

    if cover_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=cover_id)
    elif relay_id is not None and description[KEY_STATE_TOPIC] != TOPIC_STATUS_RPC:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=relay_id)
    elif light_id is not None and description[KEY_STATE_TOPIC]:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=light_id)
    elif rgb_id is not None and description[KEY_STATE_TOPIC]:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=rgb_id)
    elif cct_id is not None and description[KEY_STATE_TOPIC]:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=cct_id)
    elif emeter_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=emeter_id)
    elif sensor_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=sensor_id)
    elif input_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=input_id)
    elif thermostat_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=thermostat_id)
    elif bt_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=bt_id)
    else:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC]

    if options := description.get(KEY_OPTIONS):
        payload[KEY_OPTIONS] = options
    if description.get(KEY_UNIT):
        payload[KEY_UNIT] = description[KEY_UNIT]
    if description.get(KEY_ICON):
        payload[KEY_ICON] = description[KEY_ICON]
    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_STATE_CLASS):
        payload[KEY_STATE_CLASS] = description[KEY_STATE_CLASS]
    if description.get(KEY_SUGGESTED_DISPLAY_PRECISION):
        payload[KEY_SUGGESTED_DISPLAY_PRECISION] = description[
            KEY_SUGGESTED_DISPLAY_PRECISION
        ]

    return topic, payload


def get_binary_sensor(
    sensor,
    description,
    entity_id=None,
    is_input=False,
    input_type=None,
    profile=None,
    bt_id=None,
    thermostat_id=None,
):
    """Create configuration for Shelly binary sensor entity."""
    if entity_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/binary_sensor/{device_id}-{entity_id}-{sensor}/config"
        )
    elif bt_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/binary_sensor/{device_id}-{bt_id}-{sensor}/config"
        )
    elif thermostat_id is not None:
        topic = encode_config_topic(
            f"{disc_prefix}/binary_sensor/{device_id}-{thermostat_id}-{sensor}/config"
        )
    else:
        topic = encode_config_topic(
            f"{disc_prefix}/binary_sensor/{device_id}-{sensor}/config"
        )

    if not description:
        return topic, ""

    if profile == ATTR_COVER:
        return topic, ""

    if is_input:
        name = (
            device_config[f"input:{entity_id}"][ATTR_NAME] or f"Input {entity_id}"
        ).replace("'", "_")
    elif entity_id is not None:
        name = (
            device_config[f"switch:{entity_id}"].get(ATTR_NAME, {})
            or f"Relay {entity_id}"
        ).replace("'", "_")
    if entity_id is not None:
        unique_id = f"{device_id}-{entity_id}-{sensor}".lower()
        sensor_name = (
            f"{name} {description[KEY_NAME]}" if description.get(KEY_NAME) else name
        )
    elif bt_id is not None:
        unique_id = f"{device_id}-{bt_id}-{sensor}".lower()
        sensor_name = description[KEY_NAME]
    elif thermostat_id is not None:
        unique_id = f"{device_id}-{thermostat_id}-{sensor}".lower()
        sensor_name = description[KEY_NAME]
    else:
        unique_id = f"{device_id}-{sensor}".lower()
        sensor_name = description[KEY_NAME]

    if is_input and input_type != ATTR_SWITCH:
        return topic, ""

    payload = {
        KEY_NAME: sensor_name,
        KEY_VALUE_TEMPLATE: description[KEY_VALUE_TEMPLATE],
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_UNIQUE_ID: unique_id,
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    if availability:
        payload[KEY_AVAILABILITY] = availability

    if expire_after:
        payload[KEY_EXPIRE_AFTER] = expire_after

    if entity_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=entity_id)
    elif bt_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=bt_id)
    elif thermostat_id is not None:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(id=thermostat_id)
    else:
        payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC]

    if description.get(KEY_JSON_ATTRIBUTES_TOPIC) and description.get(
        KEY_JSON_ATTRIBUTES_TEMPLATE
    ):
        payload[KEY_JSON_ATTRIBUTES_TOPIC] = description[KEY_JSON_ATTRIBUTES_TOPIC]
        payload[KEY_JSON_ATTRIBUTES_TEMPLATE] = description[
            KEY_JSON_ATTRIBUTES_TEMPLATE
        ]
    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_STATE_CLASS):
        payload[KEY_STATE_CLASS] = description[KEY_STATE_CLASS]

    return topic, payload


def get_bthome_event(input_id, bt_id, device_id_prefix):
    """Create configuration for BTHome device event entity."""
    topic = encode_config_topic(
        f"{disc_prefix}/event/{device_id_prefix}-{bt_id}-{input_id}/config"
    )

    payload = {
        KEY_NAME: f"Button {input_id}",
        KEY_STATE_TOPIC: TOPIC_EVENTS_RPC,
        KEY_EVENT_TYPES: [
            EVENT_SINGLE_PUSH,
            EVENT_DOUBLE_PUSH,
            EVENT_LONG_PUSH,
            EVENT_TRIPLE_PUSH,
        ],
        KEY_VALUE_TEMPLATE: f"{{%if value_json.params.events.0.component==^bthomedevice:{bt_id}^ and value_json.params.events.0.idx is defined and value_json.params.events.0.idx=={input_id} and value_json.params.events.0.event is defined%}}{{{{{{^event_type^:value_json.params.events.0.event}}|to_json}}}}{{%endif%}}",
        KEY_UNIQUE_ID: f"{device_id_prefix}-{bt_id}-{input_id}".lower(),
        KEY_QOS: qos,
        KEY_AVAILABILITY: availability,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
        KEY_DEVICE_CLASS: DEVICE_CLASS_BUTTON,
    }

    return topic, payload


def get_bthome_input(input_id, bt_id, device_id_prefix, event):
    """Create configuration for BTHome device input event automation."""
    topic = encode_config_topic(
        f"{disc_prefix}/device_automation/{device_id_prefix}-{bt_id}-{input_id}/{event}/config"
    )

    payload = {
        KEY_AUTOMATION_TYPE: VALUE_TRIGGER,
        KEY_TOPIC: f"{default_topic}events/rpc",
        KEY_PAYLOAD: f"bthomedevice:{bt_id}_{input_id}_{event}",
        KEY_VALUE_TEMPLATE: "{{value_json.params.events.0.component}}_{{value_json.params.events.0.idx}}_{{value_json.params.events.0.event}}",
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_TYPE: DEVICE_TRIGGER_MAP[event],
        KEY_SUBTYPE: f"button_{input_id + 1}",
    }

    return topic, payload


def get_input(input_id, input_type, event):
    """Create configuration for Shelly input event."""
    topic = encode_config_topic(
        f"{disc_prefix}/device_automation/{device_id}-input-{input_id}/{event}/config"
    )

    if input_type != ATTR_BUTTON:
        return topic, ""

    payload = {
        KEY_AUTOMATION_TYPE: VALUE_TRIGGER,
        KEY_TOPIC: f"{default_topic}events/rpc",
        KEY_PAYLOAD: f"{input_id}_{event}",
        KEY_VALUE_TEMPLATE: "{{value_json.params.events.0.id}}_{{value_json.params.events.0.event}}",
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_TYPE: DEVICE_TRIGGER_MAP[event],
        KEY_SUBTYPE: f"button_{input_id + 1}",
    }

    return topic, payload


def get_event(input_id, input_type):
    """Create configuration for Shelly event entity."""
    topic = encode_config_topic(
        f"{disc_prefix}/event/{device_id}-input-{input_id}/config"
    )

    if input_type != ATTR_BUTTON:
        return topic, ""

    input_name = (
        device_config[f"input:{input_id}"].get(ATTR_NAME) or f"Button {input_id}"
    ).replace("'", "_")

    payload = {
        KEY_NAME: input_name,
        KEY_STATE_TOPIC: TOPIC_EVENTS_RPC,
        KEY_EVENT_TYPES: input_events,
        KEY_VALUE_TEMPLATE: TPL_EVENT.format(input_id=input_id),
        KEY_UNIQUE_ID: f"{device_id}-{input_id}".lower(),
        KEY_QOS: qos,
        KEY_AVAILABILITY: availability,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
        KEY_DEVICE_CLASS: DEVICE_CLASS_BUTTON,
    }

    return topic, payload


def get_button(button, description, thermostat_id=None):
    """Create configuration for Shelly button entity."""
    topic = encode_config_topic(f"{disc_prefix}/button/{device_id}-{button}/config")

    payload = {
        KEY_NAME: description[KEY_NAME],
        KEY_COMMAND_TOPIC: TOPIC_RPC,
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_UNIQUE_ID: f"{device_id}-{button}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }

    if thermostat_id is not None:
        payload[KEY_PAYLOAD_PRESS] = description[KEY_PAYLOAD_PRESS].format(
            source=source_topic, thermostat=thermostat_id
        )
    else:
        payload[KEY_PAYLOAD_PRESS] = description[KEY_PAYLOAD_PRESS].format(
            source=source_topic
        )

    if description.get(KEY_AVAILABILITY_TOPIC):
        payload[KEY_AVAILABILITY_TOPIC] = description[KEY_AVAILABILITY_TOPIC]
        payload[KEY_AVAILABILITY_TEMPLATE] = description[KEY_AVAILABILITY_TEMPLATE]
    elif availability:
        payload[KEY_AVAILABILITY] = availability
    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_ICON):
        payload[KEY_ICON] = description[KEY_ICON]

    return topic, payload


def get_number(number: str, description, thermostat_id=None) -> tuple:
    """Create configuration for Shelly number entity."""
    topic = encode_config_topic(f"{disc_prefix}/number/{device_id}-{number}/config")

    if not description:
        return topic, ""

    payload = {
        KEY_NAME: description[KEY_NAME],
        KEY_COMMAND_TOPIC: description[KEY_COMMAND_TOPIC],
        KEY_MIN: description[KEY_MIN],
        KEY_MAX: description[KEY_MAX],
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_UNIQUE_ID: f"{device_id}-{number}".lower(),
        KEY_QOS: qos,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
        KEY_AVAILABILITY: availability,
    }

    if thermostat_id is not None:
        payload[KEY_COMMAND_TEMPLATE] = description[KEY_COMMAND_TEMPLATE].format(
            source=source_topic, thermostat=thermostat_id
        )
        if description.get(KEY_STATE_TOPIC):
            payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC].format(
                id=thermostat_id
            )
    else:
        payload[KEY_COMMAND_TEMPLATE] = description[KEY_COMMAND_TEMPLATE].format(
            source=source_topic
        )
        if description.get(KEY_STATE_TOPIC):
            payload[KEY_STATE_TOPIC] = description[KEY_STATE_TOPIC]

    if description.get(KEY_MODE):
        payload[KEY_MODE] = description[KEY_MODE]
    if description.get(KEY_VALUE_TEMPLATE):
        payload[KEY_VALUE_TEMPLATE] = description[KEY_VALUE_TEMPLATE]
    if description.get(KEY_DEVICE_CLASS):
        payload[KEY_DEVICE_CLASS] = description[KEY_DEVICE_CLASS]
    if description.get(KEY_ENTITY_CATEGORY):
        payload[KEY_ENTITY_CATEGORY] = description[KEY_ENTITY_CATEGORY]
    if description.get(KEY_ICON):
        payload[KEY_ICON] = description[KEY_ICON]
    if description.get(KEY_STEP):
        payload[KEY_STEP] = description[KEY_STEP]
    if description.get(KEY_UNIT):
        payload[KEY_UNIT] = description[KEY_UNIT]

    return topic, payload


def get_update(update, description):
    """Create configuration for Shelly update entity."""
    topic = encode_config_topic(f"{disc_prefix}/update/{device_id}-{update}/config")

    if not description:
        return topic, ""

    payload = {
        KEY_NAME: description[KEY_NAME],
        KEY_ENABLED_BY_DEFAULT: str(description[KEY_ENABLED_BY_DEFAULT]).lower(),
        KEY_UNIQUE_ID: f"{device_id}-{update}".lower(),
        KEY_STATE_TOPIC: description[KEY_STATE_TOPIC],
        KEY_VALUE_TEMPLATE: description[KEY_VALUE_TEMPLATE],
        KEY_LATEST_VERSION_TEMPLATE: description[KEY_LATEST_VERSION_TEMPLATE],
        KEY_LATEST_VERSION_TOPIC: description[KEY_LATEST_VERSION_TOPIC],
        KEY_ENTITY_PICTURE: "https://brands.home-assistant.io/_/shelly/icon.png",
        KEY_RELEASE_URL: "https://shelly-api-docs.shelly.cloud/gen2/changelog",
        KEY_TITLE: f"{device_name} Firmware",
        KEY_QOS: qos,
        KEY_AVAILABILITY: availability,
        KEY_DEVICE: device_info,
        KEY_ORIGIN: origin_info,
        KEY_DEFAULT_TOPIC: default_topic,
    }
    if description.get(KEY_PAYLOAD_INSTALL):
        payload[KEY_COMMAND_TOPIC] = TOPIC_RPC
        payload[KEY_PAYLOAD_INSTALL] = description[KEY_PAYLOAD_INSTALL].format(
            source=source_topic
        )
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

    if model == MODEL_PRO_DUAL_COVER_PM:
        profile = ATTR_COVER
    elif model == MODEL_PLUS_RGBW_PM:
        profile = device_config["sys"]["device"][ATTR_PROFILE]
    elif model in (
        MODEL_DALI_DIMMER_G3,
        MODEL_DIMMER_10V_G3,
        MODEL_DIMMER_G3,
        MODEL_PLUS_DIMMER_10V,
        MODEL_PRO_DIMMER_1PM,
        MODEL_PRO_DIMMER_2PM,
    ):
        profile = ATTR_LIGHT
    else:
        profile = device_config["sys"]["device"].get(ATTR_PROFILE, ATTR_SWITCH)

    for cover_id in range(covers):
        topic, payload = get_cover(cover_id, profile)
        config[topic] = payload

        for sensor, description in cover_sensors.items():
            topic, payload = get_sensor(
                sensor, description, profile=profile, cover_id=cover_id
            )
            config[topic] = payload

    for light_id in range(lights):
        topic, payload = get_light(light_id)
        config[topic] = payload

        for sensor, description in light_sensors.items():
            topic, payload = get_sensor(
                sensor, description, light_id=light_id, profile=profile
            )
            config[topic] = payload

    for cct_id in range(cct_lights):
        topic, payload = get_cct_light(cct_id)
        config[topic] = payload

        for sensor, description in cct_sensors.items():
            topic, payload = get_sensor(
                sensor, description, cct_id=cct_id, profile=profile
            )
            config[topic] = payload

    for rgb_id in range(rgb_lights):
        topic, payload = get_rgb_light(rgb_id)
        config[topic] = payload

        for sensor, description in rgb_sensors.items():
            topic, payload = get_sensor(
                sensor, description, rgb_id=rgb_id, profile=profile
            )
            config[topic] = payload

    for emeter_id in range(emeters):
        if emeter_phases:
            for phase in emeter_phases:
                for sensor, description in emeter_sensors.items():
                    topic, payload = get_sensor(
                        sensor, description, emeter_id=emeter_id, emeter_phase=phase
                    )
                    config[topic] = payload
        else:
            for sensor, description in emeter_sensors.items():
                topic, payload = get_sensor(sensor, description, emeter_id=emeter_id)
                config[topic] = payload

    for thermostat_id, description in thermostats.items():
        topic, payload = get_climate(thermostat_id, description)
        config[topic] = payload

    for valve_id, description in valves.items():
        topic, payload = get_valve(valve_id, description)
        config[topic] = payload

    for relay_id in range(relays):
        consumption_types = [
            item.lower()
            for item in device_config["sys"]
            .get("ui_data", {})
            .get("consumption_types", [])
        ]
        relay_type = get_consumption_type(consumption_types, relay_id)

        topic, payload = get_switch(relay_id, relay_type, profile)
        config[topic] = payload

        topic, payload = get_relay_light(relay_id, relay_type, profile)
        config[topic] = payload

        topic, payload = get_relay_fan(relay_id, relay_type, profile)
        config[topic] = payload

        for sensor, description in relay_sensors.items():
            topic, payload = get_sensor(
                sensor, description, profile=profile, relay_id=relay_id
            )
            config[topic] = payload

        for binary_sensor, description in relay_binary_sensors.items():
            topic, payload = get_binary_sensor(
                binary_sensor, description, relay_id, profile=profile
            )
            config[topic] = payload

    if device_config["sys"]["device"].get("addon_type") == "prooutput":
        for switch_id in range(100, 200):
            if device_config.get(f"switch:{switch_id}"):
                topic, payload = get_switch(switch_id, ATTR_SWITCH, ATTR_SWITCH)
                config[topic] = payload

    for switch, description in switches.items():
        switch_id = description[ATTR_ID]
        topic, payload = get_switch(switch_id, ATTR_SWITCH, switch, description)
        config[topic] = payload

    for input_id in inputs:
        input_type = device_config[f"input:{input_id}"]["type"]

        topic, payload = get_event(input_id, input_type)
        config[topic] = payload

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

        for sensor, description in input_sensors.items():
            topic, payload = get_sensor(
                sensor,
                description,
                input_id=input_id,
            )
            config[topic] = payload

    for button, descripton in buttons.items():
        topic, payload = get_button(button, descripton)
        config[topic] = payload

    for update, descripton in updates.items():
        topic, payload = get_update(update, descripton)
        config[topic] = payload

    for sensor, description in sensors.items():
        topic, payload = get_sensor(sensor, description)
        config[topic] = payload

    for binary_sensor, description in binary_sensors.items():
        topic, payload = get_binary_sensor(binary_sensor, description)
        config[topic] = payload

    if device_config["sys"]["device"].get("addon_type") == "sensor":
        for input_id in range(100, 200):
            if input_config := device_config.get(f"input:{input_id}"):
                input_type = input_config["type"]

                for event in (
                    EVENT_SINGLE_PUSH,
                    EVENT_DOUBLE_PUSH,
                    EVENT_LONG_PUSH,
                    EVENT_TRIPLE_PUSH,
                ):
                    topic, payload = get_input(input_id, input_type, event)
                    config[topic] = payload

                topic, payload = get_binary_sensor(
                    "input",
                    DESCRIPTION_EXTERNAL_SENSOR_INPUT,
                    input_id,
                    is_input=True,
                    input_type=input_type,
                )
                config[topic] = payload

    for sensor_id in range(100, 200):
        if device_config.get(f"temperature:{sensor_id}"):
            topic, payload = get_sensor(
                "temperature",
                DESCRIPTION_EXTERNAL_SENSOR_TEMPERATURE,
                sensor_id=sensor_id,
            )
            config[topic] = payload

        if device_config.get(f"humidity:{sensor_id}"):
            topic, payload = get_sensor(
                "humidity",
                DESCRIPTION_EXTERNAL_SENSOR_HUMIDITY,
                sensor_id=sensor_id,
            )
            config[topic] = payload

        if device_config.get(f"voltmeter:{sensor_id}"):
            topic, payload = get_sensor(
                "voltmeter",
                DESCRIPTION_EXTERNAL_SENSOR_VOLTMETER,
                sensor_id=sensor_id,
            )
            config[topic] = payload

    return config


def install_script(script_id, device_topic, script_topic):
    """Install the script on the device."""
    logger.info("Installing the script %s, ID: %s", SCRIPT_CURRENT_NAME, script_id)  # noqa: F821

    payload = {
        "id": 1,
        "src": script_topic,
        "method": "Script.Create",
        "params": {ATTR_NAME: SCRIPT_CURRENT_NAME},
    }
    mqtt_publish(device_topic, payload)
    payload = {
        "id": 1,
        "src": script_topic,
        "method": "Script.PutCode",
        "params": {"id": script_id, "code": SCRIPT_CODE},
    }
    mqtt_publish(device_topic, payload)
    payload = {
        "id": 1,
        "src": script_topic,
        "method": "Script.Start",
        "params": {"id": script_id},
    }
    mqtt_publish(device_topic, payload)
    payload = f"{{'id':1,'src':'{script_topic}','method':'Script.SetConfig','params':{{'id':{script_id},'config':{{'enable':true}}}}}}"
    mqtt_publish(device_topic, payload)


def current_script_installed():
    """Return True if the current version of the script is installed."""
    script_id = 1

    while True:
        if f"script:{script_id}" in device_config:
            if device_config[f"script:{script_id}"][ATTR_NAME] == SCRIPT_CURRENT_NAME:
                return True
        else:
            return False

        script_id = script_id + 1


def get_script_id():
    """Return the script ID."""
    script_id = 1

    while True:
        if f"script:{script_id}" in device_config:
            script_id = script_id + 1
        else:
            return script_id


def remove_old_script_versions(device_topic, script_topic):
    """Remove old script versions."""
    for script_id in range(1, 100):
        if f"script:{script_id}" in device_config:
            script_name = device_config[f"script:{script_id}"][ATTR_NAME]
            if script_name in SCRIPT_OLD_NAMES:
                logger.info(  # noqa: F821
                    "Removing the old script %s, ID: %s", script_name, script_id
                )
                payload = {
                    "id": 1,
                    "src": script_topic,
                    "method": "Script.Stop",
                    "params": {"id": script_id},
                }
                mqtt_publish(device_topic, payload)
                payload = {
                    "id": 1,
                    "src": script_topic,
                    "method": "Script.Delete",
                    "params": {"id": script_id},
                }
                mqtt_publish(device_topic, payload)


logger.info("Shellies Discovery Gen2 version: %s", VERSION)  # noqa: F821
device_id = data[ATTR_ID]  # noqa: F821
if device_id is None:
    raise ValueError("id value None is not valid, check script configuration")

model = device_id.rsplit("-", 1)[0]
if model not in SUPPORTED_MODELS:
    raise ValueError(
        f"model {model} is not supported, please open a feature request here https://github.com/bieniu/ha-shellies-discovery-gen2/issues"
    )

device_config = data["device_config"]  # noqa: F821

origin_info = {
    KEY_NAME: "Shellies Discovery Gen2",
    KEY_SW_VERSION: VERSION,
    KEY_SUPPORT_URL: "https://github.com/bieniu/ha-shellies-discovery-gen2",
}

wakeup_period = SUPPORTED_MODELS[model].get(ATTR_WAKEUP_PERIOD, 0)
if wakeup_period > 0:
    availability = None
    expire_after = wakeup_period * 1.2
else:
    availability = [
        {
            KEY_TOPIC: TOPIC_ONLINE,
            KEY_PAYLOAD_AVAILABLE: "true",
            KEY_PAYLOAD_NOT_AVAILABLE: "false",
        }
    ]
    if model not in (
        MODEL_FLOOD_G4,
        MODEL_HT_G3,
        MODEL_PLUS_HT,
        MODEL_PLUS_SMOKE,
        MODEL_WALL_DISPLAY,
    ):
        availability.append(
            {
                KEY_TOPIC: TOPIC_STATUS_RPC,
                KEY_VALUE_TEMPLATE: TPL_MQTT_CONNECTED,
            }
        )
    expire_after = None

disc_prefix = data.get(CONF_DISCOVERY_PREFIX, DEFAULT_DISC_PREFIX)  # noqa: F821

script_prefix = data.get(CONF_SCRIPT_PREFIX, None)  # noqa: F821
if script_prefix and (script_prefix[-1] == "/" or " " in script_prefix):
    raise ValueError(
        f"Script prefix value {script_prefix} is not valid, check script configuration"
    )

source_topic = f"{script_prefix}/{HOME_ASSISTANT}" if script_prefix else HOME_ASSISTANT

qos = data.get(CONF_QOS, 0)  # noqa: F821
if qos not in (0, 1, 2):
    raise ValueError(f"QoS value {qos} is not valid, check script configuration")

if "components" in device_config:
    components = {
        comp["key"]: {**comp["config"], **comp.get("attrs", {})}
        for comp in device_config["components"]
        if comp["key"].startswith(("blu", "bt", "mqtt"))
    }

    if "mqtt" not in components:
        raise ValueError(
            "Missing MQTT component, probably 'Shelly.GetComponent' pagination problem"
        )

    default_topic = f"{components['mqtt']['topic_prefix']}/"
    if " " in default_topic:
        raise ValueError(
            f"MQTT prefix value {default_topic} is not valid, check device configuration"
        )

    bthome_devices = {
        key: {**conf, "components": []}
        for key, conf in components.items()
        if key.startswith("bthomedevice")
    }
    for dev in bthome_devices.values():
        for comp, config in components.items():
            if (
                dev["addr"] == config.get("addr")
                and config.get("obj_id") in BTH_IDX_MAP
            ):
                dev["components"].append({BTH_IDX_MAP[config["obj_id"]]: comp})

    blutrv_devices = {
        key: {**conf, "components": []}
        for key, conf in components.items()
        if key.startswith("blutrv")
    }

    for dev in blutrv_devices.values():
        for comp, config in components.items():
            if (
                dev["addr"] == config.get("addr")
                and config.get("obj_id") == BTH_TEMPERATURE
            ):
                dev["components"].append(comp)

    config_data = {}

    via_device = format_mac(device_id.rsplit("-", 1)[-1])

    original_device_id = device_id

    for device, config in bthome_devices.items():
        btdevice_id = device.split(":")[-1]
        if f"blutrv:{btdevice_id}" in blutrv_devices:
            continue

        if not (model := config["meta"]["ui"].get("local_name")):
            model = BTH_DEV_MAP.get(config.get("model_id", MODEL_GENERIC_BTHOME_DEVICE))

        if model not in SUPPORTED_MODELS:
            logger.warning(  # noqa: F821
                "device %s is not supported, please open a feature request here "
                "https://github.com/bieniu/ha-shellies-discovery-gen2/issues",
                device,
            )
            continue

        logger.debug("Found BTHome devices: %s", bthome_devices)  # noqa: F821

        mac = config["addr"].lower()
        device_name = (
            config[ATTR_NAME]
            or f"{SUPPORTED_MODELS[model][ATTR_NAME]} {mac.upper().replace(':', '')}"
        ).replace("'", "_")

        device_id = f"{original_device_id}-{mac.replace(':', '')}"
        device_info = {
            KEY_CONNECTIONS: [["bluetooth", mac]],
            KEY_IDENTIFIERS: [mac],
            KEY_NAME: device_name,
            KEY_MODEL: SUPPORTED_MODELS[model][ATTR_NAME],
            KEY_MANUFACTURER: ATTR_MANUFACTURER,
            KEY_VIA_DEVICE: via_device,
        }
        if model_id := SUPPORTED_MODELS[model].get(ATTR_MODEL_ID):
            device_info[KEY_MODEL_ID] = model_id

        binary_sensors = SUPPORTED_MODELS[model].get(ATTR_BINARY_SENSORS, {})
        sensors = SUPPORTED_MODELS[model].get(ATTR_SENSORS, {})

        for sensor, description in sensors.items():
            btsensor_id = None
            for component in config["components"]:
                if comp_id := component.get(sensor):
                    btsensor_id = comp_id.split(":")[-1]
                    break

            topic, payload = get_sensor(
                sensor, description, bt_id=btsensor_id or btdevice_id
            )
            config_data[topic] = payload

        for binary_sensor, description in binary_sensors.items():
            btsensor_id = None
            for component in config["components"]:
                if comp_id := component.get(binary_sensor):
                    btsensor_id = comp_id.split(":")[-1]
                    break

            topic, payload = get_binary_sensor(
                binary_sensor, description, bt_id=btsensor_id or btdevice_id
            )
            config_data[topic] = payload

        bth_inputs = SUPPORTED_MODELS[model].get(ATTR_INPUTS, 0)

        for input_id in range(bth_inputs):
            # Create event entity for button presses
            topic, payload = get_bthome_event(input_id, btdevice_id, device_id)
            config_data[topic] = payload

            # Create device automation triggers for each supported event type
            for event in [
                EVENT_SINGLE_PUSH,
                EVENT_DOUBLE_PUSH,
                EVENT_LONG_PUSH,
                EVENT_TRIPLE_PUSH,
            ]:
                topic, payload = get_bthome_input(
                    input_id, btdevice_id, device_id, event
                )
                config_data[topic] = payload

    for thermostat, config in blutrv_devices.items():
        model = BTH_DEV_MAP.get(config.get("model_id"))
        mac = config["addr"].lower()
        device_name = (
            config[ATTR_NAME]
            or f"{SUPPORTED_MODELS[model][ATTR_NAME]} {mac.upper().replace(':', '')}"
        ).replace("'", "_")
        device_id += f"-{mac.replace(':', '')}"
        device_info = {
            KEY_CONNECTIONS: [["bluetooth", mac]],
            KEY_IDENTIFIERS: [mac],
            KEY_NAME: device_name,
            KEY_MODEL: SUPPORTED_MODELS[model][ATTR_NAME],
            KEY_MODEL_ID: SUPPORTED_MODELS[model][ATTR_MODEL_ID],
            KEY_MANUFACTURER: ATTR_MANUFACTURER,
            KEY_VIA_DEVICE: via_device,
        }
        thermostat_id = thermostat.split(":")[-1]
        topic, payload = get_blu_climate(thermostat_id, DESCRIPTION_BLU_TRV_THERMOSTAT)
        config_data[topic] = payload

        sensors = SUPPORTED_MODELS[model].get(ATTR_SENSORS, {})

        for sensor, description in sensors.items():
            topic, payload = get_sensor(
                sensor, description, thermostat_id=thermostat_id
            )
            config_data[topic] = payload

        binary_sensors = SUPPORTED_MODELS[model].get(ATTR_BINARY_SENSORS, {})

        for sensor, description in binary_sensors.items():
            topic, payload = get_binary_sensor(
                sensor, description, thermostat_id=thermostat_id
            )
            config_data[topic] = payload

        buttons = SUPPORTED_MODELS[model].get(ATTR_BUTTONS, {})

        for button, description in buttons.items():
            topic, payload = get_button(
                button, description, thermostat_id=thermostat_id
            )
            config_data[topic] = payload

        numbers = SUPPORTED_MODELS[model].get(ATTR_NUMBERS, {})

        for number, description in numbers.items():
            topic, payload = get_number(
                number, description, thermostat_id=thermostat_id
            )
            config_data[topic] = payload

else:
    if (
        model == MODEL_PRO_3EM
        and device_config["sys"]["device"].get(ATTR_PROFILE) == "monophase"
    ):
        model = MODEL_PRO_3EM_MONOPHASE
    if (
        model == MODEL_PRO_3EM_3CT63
        and device_config["sys"]["device"].get(ATTR_PROFILE) == "monophase"
    ):
        model = MODEL_PRO_3EM_3CT63_MONOPHASE

    default_topic = f"{device_config['mqtt']['topic_prefix']}/"
    if " " in default_topic:
        raise ValueError(
            f"MQTT prefix value {default_topic} is not valid, check device configuration"
        )
    firmware_id = device_config["sys"]["device"][ATTR_FW_ID]

    if (
        model
        not in (
            MODEL_FLOOD_G4,
            MODEL_HT_G3,
            MODEL_PLUS_HT,
            MODEL_PLUS_SMOKE,
            MODEL_WALL_DISPLAY,
        )
        and not current_script_installed()
    ):
        device_topic = encode_config_topic(f"{default_topic}rpc")
        if script_prefix:
            script_topic = f"{script_prefix}/{TOPIC_SHELLIES_DISCOVERY_SCRIPT}"
        else:
            script_topic = TOPIC_SHELLIES_DISCOVERY_SCRIPT

        script_id = get_script_id()
        install_script(script_id, device_topic, script_topic)
        remove_old_script_versions(device_topic, script_topic)

    min_firmware_date = SUPPORTED_MODELS[model][ATTR_MIN_FIRMWARE_DATE]
    try:
        firmware_date = int(firmware_id.split("-", 1)[0])
    except ValueError as exc:
        raise ValueError(
            f"firmware version {min_firmware_date} is not supported, update your device {device_id}"
        ) from exc
    if firmware_date < min_firmware_date:
        raise ValueError(
            f"firmware dated {min_firmware_date} is required, update your device {device_id}"
        )

    mac = device_config["sys"]["device"][ATTR_MAC]
    if mac is None:
        raise ValueError("mac value None is not valid, check script configuration")

    mac = format_mac(mac).lower()

    device_name = (
        device_config["sys"]["device"].get(ATTR_NAME)
        or f"{SUPPORTED_MODELS[model][ATTR_NAME]} {mac.upper().replace(':', '')}"
    ).replace("'", "_")
    device_url = f"http://{device_id}.local/"

    gen = SUPPORTED_MODELS[model].get(ATTR_GEN, 2)
    device_info = {
        KEY_CONNECTIONS: [[KEY_MAC, mac]],
        KEY_IDENTIFIERS: [mac],
        KEY_NAME: device_name,
        KEY_MODEL: SUPPORTED_MODELS[model][ATTR_NAME],
        KEY_MODEL_ID: SUPPORTED_MODELS[model].get(ATTR_MODEL_ID),
        KEY_SW_VERSION: firmware_id,
        KEY_HW_VERSION: f"gen{gen}",
        KEY_MANUFACTURER: ATTR_MANUFACTURER,
        KEY_CONFIGURATION_URL: device_url,
    }
    if brand := SUPPORTED_MODELS[model].get(ATTR_BRAND):
        device_info[KEY_MANUFACTURER] = f"{brand} (Powered by {ATTR_MANUFACTURER})"

    inputs = get_component_ids(ATTR_INPUT, device_config)
    input_events = SUPPORTED_MODELS[model].get(ATTR_INPUT_EVENTS, [])
    input_binary_sensors = SUPPORTED_MODELS[model].get(ATTR_INPUT_BINARY_SENSORS, {})
    input_sensors = SUPPORTED_MODELS[model].get(ATTR_INPUT_SENSORS, {})

    emeters = SUPPORTED_MODELS[model].get(ATTR_EMETERS, 0)
    emeter_phases = SUPPORTED_MODELS[model].get(ATTR_EMETER_PHASES, [])
    emeter_sensors = SUPPORTED_MODELS[model].get(ATTR_EMETER_SENSORS, {})

    relays = SUPPORTED_MODELS[model].get(ATTR_RELAYS, 0)
    relay_sensors = SUPPORTED_MODELS[model].get(ATTR_RELAY_SENSORS, {})
    relay_binary_sensors = SUPPORTED_MODELS[model].get(ATTR_RELAY_BINARY_SENSORS, {})

    thermostats = SUPPORTED_MODELS[model].get(ATTR_THERMOSTATS, {})

    lights = get_component_number(ATTR_LIGHT, device_config)
    light_sensors = SUPPORTED_MODELS[model].get(ATTR_LIGHT_SENSORS, {})

    cct_lights = get_component_number(ATTR_CCT, device_config)
    cct_sensors = SUPPORTED_MODELS[model].get(ATTR_CCT_SENSORS, {})

    rgb_lights = get_component_number(ATTR_RGB, device_config)
    rgb_sensors = SUPPORTED_MODELS[model].get(ATTR_RGB_SENSORS, {})

    buttons = SUPPORTED_MODELS[model].get(ATTR_BUTTONS, {})
    sensors = SUPPORTED_MODELS[model].get(ATTR_SENSORS, {})
    binary_sensors = SUPPORTED_MODELS[model].get(ATTR_BINARY_SENSORS, {})
    updates = SUPPORTED_MODELS[model].get(ATTR_UPDATES, {})

    covers = SUPPORTED_MODELS[model].get(ATTR_COVERS, 0)
    cover_sensors = SUPPORTED_MODELS[model].get(ATTR_COVER_SENSORS, {})

    switches = SUPPORTED_MODELS[model].get(ATTR_SWITCHES, {})

    valves = SUPPORTED_MODELS[model].get(ATTR_VALVES, {})

    config_data = configure_device()

if config_data:
    for config_topic, config_payload in config_data.items():
        mqtt_publish(config_topic, config_payload)
