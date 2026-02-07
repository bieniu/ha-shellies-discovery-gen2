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
        ValueError,
        match="model unsupported is not supported, please open a feature request",
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

    assert json.loads(hass.services.call.call_args_list[5][0][2]["payload"]) == {
        "avty": [
            {
                "pl_avail": "true",
                "pl_not_avail": "false",
                "t": "~online",
            },
            {
                "t": "~status/rpc",
                "val_tpl": "{%if value_json.mqtt.connected%}online{%else%}offline{%endif%}",
            },
        ],
        "cmd_off_tpl": '{"id":1,"src":"home-assistant","method":"Switch.Set","params":{"id":0,"on":false}}',
        "cmd_on_tpl": '{"id":1,"src":"home-assistant","method":"Switch.Set","params":{"id":0,"on":true}}',
        "cmd_t": "~rpc",
        "dev": {
            "cns": [
                [
                    "mac",
                    "aa:bb:cc:dd:ee:ff",
                ],
            ],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": [
                "aa:bb:cc:dd:ee:ff",
            ],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "name": "Mirror light",
        "o": {
            "name": "Shellies Discovery Gen2",
            "sw": "0.0.0",
            "url": "https://github.com/bieniu/ha-shellies-discovery-gen2",
        },
        "qos": 0,
        "schema": "template",
        "stat_t": "~status/switch:0",
        "stat_tpl": "{%if value_json.output%}on{%else%}off{%endif%}",
        "uniq_id": "shelly1g4-aabbccddeeff-0",
        "~": "shelly1g4-aabbccddeeff/",
    }

    assert json.loads(hass.services.call.call_args_list[7][0][2]["payload"]) == {
        "avty": [
            {
                "pl_avail": "true",
                "pl_not_avail": "false",
                "t": "~online",
            },
            {
                "t": "~status/rpc",
                "val_tpl": "{%if value_json.mqtt.connected%}online{%else%}offline{%endif%}",
            },
        ],
        "dev": {
            "cns": [
                [
                    "mac",
                    "aa:bb:cc:dd:ee:ff",
                ],
            ],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": [
                "aa:bb:cc:dd:ee:ff",
            ],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "dev_cla": "temperature",
        "en": "false",
        "ent_cat": "diagnostic",
        "name": "Mirror light Temperature",
        "o": {
            "name": "Shellies Discovery Gen2",
            "sw": "0.0.0",
            "url": "https://github.com/bieniu/ha-shellies-discovery-gen2",
        },
        "qos": 0,
        "stat_cla": "measurement",
        "stat_t": "~status/rpc",
        "sug_dsp_prc": 1,
        "uniq_id": "shelly1g4-aabbccddeeff-0-temperature",
        "unit_of_meas": "°C",
        "val_tpl": '{{value_json["switch:0"].temperature.tC}}',
        "~": "shelly1g4-aabbccddeeff/",
    }
    assert json.loads(hass.services.call.call_args_list[8][0][2]["payload"]) == {
        "avty": [
            {"pl_avail": "true", "pl_not_avail": "false", "t": "~online"},
            {
                "t": "~status/rpc",
                "val_tpl": "{%if "
                "value_json.mqtt.connected%}online{%else%}offline{%endif%}",
            },
        ],
        "dev": {
            "cns": [["mac", "aa:bb:cc:dd:ee:ff"]],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": ["aa:bb:cc:dd:ee:ff"],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "dev_cla": "problem",
        "en": "true",
        "ent_cat": "diagnostic",
        "name": "Mirror light Overtemperature",
        "o": {
            "name": "Shellies Discovery Gen2",
            "sw": "0.0.0",
            "url": "https://github.com/bieniu/ha-shellies-discovery-gen2",
        },
        "qos": 0,
        "stat_t": "~status/switch:0",
        "uniq_id": "shelly1g4-aabbccddeeff-0-overtemp",
        "val_tpl": '{%if "overtemp" in '
        'value_json.get("errors",[])%}ON{%else%}OFF{%endif%}',
        "~": "shelly1g4-aabbccddeeff/",
    }

    assert json.loads(hass.services.call.call_args_list[8][0][2]["payload"]) == {
        "avty": [
            {"pl_avail": "true", "pl_not_avail": "false", "t": "~online"},
            {
                "t": "~status/rpc",
                "val_tpl": "{%if "
                "value_json.mqtt.connected%}online{%else%}offline{%endif%}",
            },
        ],
        "dev": {
            "cns": [["mac", "aa:bb:cc:dd:ee:ff"]],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": ["aa:bb:cc:dd:ee:ff"],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "dev_cla": "problem",
        "en": "true",
        "ent_cat": "diagnostic",
        "name": "Mirror light Overtemperature",
        "o": {
            "name": "Shellies Discovery Gen2",
            "sw": "0.0.0",
            "url": "https://github.com/bieniu/ha-shellies-discovery-gen2",
        },
        "qos": 0,
        "stat_t": "~status/switch:0",
        "uniq_id": "shelly1g4-aabbccddeeff-0-overtemp",
        "val_tpl": '{%if "overtemp" in '
        'value_json.get("errors",[])%}ON{%else%}OFF{%endif%}',
        "~": "shelly1g4-aabbccddeeff/",
    }
    assert json.loads(hass.services.call.call_args_list[9][0][2]["payload"]) == {
        "avty": [
            {"pl_avail": "true", "pl_not_avail": "false", "t": "~online"},
            {
                "t": "~status/rpc",
                "val_tpl": "{%if "
                "value_json.mqtt.connected%}online{%else%}offline{%endif%}",
            },
        ],
        "dev": {
            "cns": [["mac", "aa:bb:cc:dd:ee:ff"]],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": ["aa:bb:cc:dd:ee:ff"],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "dev_cla": "button",
        "evt_typ": [
            "btn_down",
            "btn_up",
            "double_push",
            "long_push",
            "single_push",
            "triple_push",
        ],
        "name": "Button 0",
        "o": {
            "name": "Shellies Discovery Gen2",
            "sw": "0.0.0",
            "url": "https://github.com/bieniu/ha-shellies-discovery-gen2",
        },
        "qos": 0,
        "stat_t": "~events/rpc",
        "uniq_id": "shelly1g4-aabbccddeeff-0",
        "val_tpl": "{%if "
        'value_json.params.events.0.id==0%}{{{"event_type":value_json.params.events.0.event}|to_json}}{%endif%}',
        "~": "shelly1g4-aabbccddeeff/",
    }

    assert json.loads(hass.services.call.call_args_list[10][0][2]["payload"]) == {
        "atype": "trigger",
        "dev": {
            "cns": [["mac", "aa:bb:cc:dd:ee:ff"]],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": ["aa:bb:cc:dd:ee:ff"],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "pl": "0_btn_down",
        "qos": 0,
        "stype": "button_1",
        "t": "shelly1g4-aabbccddeeff/events/rpc",
        "type": "button_down",
        "val_tpl": "{{value_json.params.events.0.id}}_{{value_json.params.events.0.event}}",
    }

    assert json.loads(hass.services.call.call_args_list[11][0][2]["payload"]) == {
        "atype": "trigger",
        "dev": {
            "cns": [["mac", "aa:bb:cc:dd:ee:ff"]],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": ["aa:bb:cc:dd:ee:ff"],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "pl": "0_btn_up",
        "qos": 0,
        "stype": "button_1",
        "t": "shelly1g4-aabbccddeeff/events/rpc",
        "type": "button_up",
        "val_tpl": "{{value_json.params.events.0.id}}_{{value_json.params.events.0.event}}",
    }

    assert json.loads(hass.services.call.call_args_list[12][0][2]["payload"]) == {
        "atype": "trigger",
        "dev": {
            "cns": [["mac", "aa:bb:cc:dd:ee:ff"]],
            "cu": "http://shelly1g4-aabbccddeeff.local/",
            "hw": "gen4",
            "ids": ["aa:bb:cc:dd:ee:ff"],
            "mdl": "Shelly 1 Gen4",
            "mdl_id": "S4SW-001X16EU",
            "mf": "Shelly",
            "name": "Shelly 1 Gen4 [DDEEFF]",
            "sw": "20260120-145311/1.7.4-gf9878b6",
        },
        "pl": "0_double_push",
        "qos": 0,
        "stype": "button_1",
        "t": "shelly1g4-aabbccddeeff/events/rpc",
        "type": "button_double_press",
        "val_tpl": "{{value_json.params.events.0.id}}_{{value_json.params.events.0.event}}",
    }
