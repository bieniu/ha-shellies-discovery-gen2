"""Tests for shellies_discovery_gen2.py."""

import json
import runpy
from pathlib import Path
from unittest.mock import Mock

import pytest


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "python_scripts"
    / "shellies_discovery_gen2.py"
)
FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "shelly_1_gen4.json"


def test_none_device_id() -> None:
    """Test that the script raises a ValueError when the device id is None."""
    logger = Mock()
    data = {"id": None}

    with pytest.raises(
        ValueError, match="id value None is not valid, check script configuration"
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_unsupported_model() -> None:
    """Test that the script raises a ValueError for unsupported models."""
    logger = Mock()
    data = {"id": "unsupported-1234"}

    with pytest.raises(
        ValueError, match="model unsupported is not supported, please open a feature request"
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_script_prefix_with_trailing_slash() -> None:
    """Test that the script rejects a script prefix ending with '/'."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {},
        "script_prefix": "bad/prefix/",
    }

    with pytest.raises(
        ValueError,
        match="Script prefix value bad/prefix/ is not valid, check script configuration",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_invalid_qos() -> None:
    """Test that the script rejects invalid QoS values."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {},
        "qos": 3,
    }

    with pytest.raises(
        ValueError, match="QoS value 3 is not valid, check script configuration"
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_missing_mqtt_component() -> None:
    """Test that the script rejects device configs without MQTT component."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {
            "components": [
                {"key": "bluetooth", "config": {}, "attrs": {}},
            ],
        },
    }

    with pytest.raises(
        ValueError,
        match="Missing MQTT component, probably 'Shelly.GetComponent' pagination problem",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_mqtt_prefix_with_space() -> None:
    """Test that the script rejects MQTT prefix values containing spaces."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {
            "components": [
                {
                    "key": "mqtt",
                    "config": {"topic_prefix": "bad topic"},
                    "attrs": {},
                },
            ],
        },
    }

    with pytest.raises(
        ValueError,
        match="MQTT prefix value bad topic/ is not valid, check device configuration",
    ):
        runpy.run_path(str(SCRIPT_PATH), init_globals={"logger": logger, "data": data})


def test_shelly_1_gen4() -> None:
    """Test for Shelly 1 Gen4."""
    logger = Mock()
    hass = Mock()
    hass.services = Mock()
    data = json.loads(FIXTURE_PATH.read_text())

    result = runpy.run_path(
        str(SCRIPT_PATH), init_globals={"logger": logger, "data": data, "hass": hass}
    )

    assert result["config_data"]
    assert hass.services.call.called

    assert hass.services.call.call_args_list[0][0][2] == {
           'payload': '{"id": 1, "src": "shellies_discovery_script", "method": '
           '"Script.Create", "params": {"name": '
           '"shellies_discovery_gen2_script_20250114"}}',
           'qos': 0,
           'retain': True,
           'topic': 'shelly1g4-aabbccddeeff/rpc',
       }

    assert hass.services.call.call_args_list[1][0][2] == {
           'payload': '{"id": 1, "src": "shellies_discovery_script", "method": '
           '"Script.PutCode", "params": {"id": 1, "code": "let topicPrefix = '
           'null;\\nlet updateTimer = null;\\n\\nfunction sendDeviceStatus() '
           '{\\n  try {\\n    let installedVersion = '
           'Shelly.getDeviceInfo().ver;\\n    Shelly.call(\\"Shelly.GetStatus\\", '
           '{}, function (status) {\\n      status.sys.installed_version = '
           'installedVersion;\\n      MQTT.publish(topicPrefix + '
           '\\"/status/rpc\\", JSON.stringify(status));\\n    });\\n  } catch (e) '
           '{\\n    console.log(\\"sendDeviceStatus has failed: \\", e);\\n  '
           '}\\n}\\n\\nfunction onMQTTConfigReceived(config) {\\n  topicPrefix = '
           'config.topic_prefix;\\n  console.log(\\"Using topic prefix: \\", '
           'topicPrefix);\\n\\n  if (!updateTimer) {\\n    updateTimer = '
           'Timer.set(30000, true, sendDeviceStatus);\\n  }\\n}\\n\\nfunction '
           'initScript() {\\n  console.log(\\"Starting '
           'shellies_discovery_gen2_script\\");\\n  try {\\n    '
           'Shelly.call(\\"MQTT.GetConfig\\", {}, onMQTTConfigReceived);\\n  } '
           'catch (e) {\\n    console.log(\\"initScript has failed: \\", e);\\n  '
           '}\\n}\\n\\ninitScript();\\n"}}',
           'qos': 0,
           'retain': True,
           'topic': 'shelly1g4-aabbccddeeff/rpc',
       }

    assert hass.services.call.call_args_list[2][0][2] == {
           'payload': '{"id": 1, "src": "shellies_discovery_script", "method": '
           '"Script.Start", "params": {"id": 1}}',
           'qos': 0,
           'retain': True,
           'topic': 'shelly1g4-aabbccddeeff/rpc',
       }

    assert hass.services.call.call_args_list[3][0][2] == {
       'payload': '{"id":1,"src":"shellies_discovery_script","method":"Script.SetConfig","params":{"id":1,"config":{"enable":true}}}',
       'qos': 0,
       'retain': True,
       'topic': 'shelly1g4-aabbccddeeff/rpc',
   }

    assert hass.services.call.call_args_list[4][0][2] == {
       'payload': '',
       'qos': 0,
       'retain': True,
       'topic': 'homeassistant/switch/shelly1g4-aabbccddeeff-0/config',
   }

    assert hass.services.call.call_args_list[5][0][2] == {
       'payload': '{"schema": "template", "name": "Mirror light", "cmd_t": "~rpc", '
       '"cmd_off_tpl": '
       '"{\\"id\\":1,\\"src\\":\\"home-assistant\\",\\"method\\":\\"Switch.Set\\",\\"params\\":{\\"id\\":0,\\"on\\":false}}", '
       '"cmd_on_tpl": '
       '"{\\"id\\":1,\\"src\\":\\"home-assistant\\",\\"method\\":\\"Switch.Set\\",\\"params\\":{\\"id\\":0,\\"on\\":true}}", '
       '"stat_t": "~status/switch:0", "stat_tpl": "{%if '
       'value_json.output%}on{%else%}off{%endif%}", "avty": [{"t": "~online", '
       '"pl_avail": "true", "pl_not_avail": "false"}, {"t": "~status/rpc", '
       '"val_tpl": "{%if '
       'value_json.mqtt.connected%}online{%else%}offline{%endif%}"}], "uniq_id": '
       '"shelly1g4-aabbccddeeff-0", "qos": 0, "dev": {"cns": [["mac", '
       '"aa:bb:cc:dd:ee:ff"]], "ids": ["aa:bb:cc:dd:ee:ff"], "name": "Shelly 1 '
       'Gen4 [DDEEFF]", "mdl": "Shelly 1 Gen4", "mdl_id": "S4SW-001X16EU", "sw": '
       '"20260120-145311/1.7.4-gf9878b6", "hw": "gen4", "mf": "Shelly", "cu": '
       '"http://shelly1g4-aabbccddeeff.local/"}, "o": {"name": "Shellies '
       'Discovery Gen2", "sw": "0.0.0", "url": '
       '"https://github.com/bieniu/ha-shellies-discovery-gen2"}, "~": '
       '"shelly1g4-aabbccddeeff/"}',
       'qos': 0,
       'retain': True,
       'topic': 'homeassistant/light/shelly1g4-aabbccddeeff-0/config',
   }
