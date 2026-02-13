"""Tests for shellies_discovery_gen2.py."""

import json
import re
import sys
import types
from importlib import util
from pathlib import Path
from unittest.mock import Mock

import pytest
from syrupy import SnapshotAssertion

SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "python_scripts"
    / "shellies_discovery_gen2.py"
)
FIXTURES_PATH = Path(__file__).resolve().parent / "fixtures"
MODULE_NAME = "python_scripts.shellies_discovery_gen2"


def run_script(*, data, logger, hass=None):
    """Load and execute the script as a module for coverage."""
    if MODULE_NAME in sys.modules:
        del sys.modules[MODULE_NAME]

    if "python_scripts" not in sys.modules:
        package = types.ModuleType("python_scripts")
        package.__path__ = [str(SCRIPT_PATH.parent)]
        sys.modules["python_scripts"] = package

    spec = util.spec_from_file_location(MODULE_NAME, SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load module spec for shellies_discovery_gen2")

    module = util.module_from_spec(spec)
    module.data = data
    module.logger = logger
    if hass is not None:
        module.hass = hass
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


def test_none_device_id() -> None:
    """Test that the script raises a ValueError when the device id is None."""
    logger = Mock()
    data = {"id": None}

    with pytest.raises(
        ValueError,
        match=re.escape("id value None is not valid, check script configuration"),
    ):
        run_script(logger=logger, data=data)


def test_unsupported_model() -> None:
    """Test that the script raises a ValueError for unsupported models."""
    logger = Mock()
    data = {"id": "unsupported-1234"}

    with pytest.raises(
        ValueError,
        match=re.escape(
            "model unsupported is not supported, please open a feature request"
        ),
    ):
        run_script(logger=logger, data=data)


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
        match=re.escape(
            "Script prefix value bad/prefix/ is not valid, check script configuration"
        ),
    ):
        run_script(logger=logger, data=data)


def test_invalid_qos() -> None:
    """Test that the script rejects invalid QoS values."""
    logger = Mock()
    data = {
        "id": "shellyplus1-123456",
        "device_config": {},
        "qos": 3,
    }

    with pytest.raises(
        ValueError,
        match=re.escape("QoS value 3 is not valid, check script configuration"),
    ):
        run_script(logger=logger, data=data)


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
        match=re.escape(
            "Missing MQTT component, probably 'Shelly.GetComponent' pagination problem"
        ),
    ):
        run_script(logger=logger, data=data)


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
        match=re.escape(
            "MQTT prefix value bad topic/ is not valid, check device configuration"
        ),
    ):
        run_script(logger=logger, data=data)


@pytest.mark.parametrize(
    "device_fixture",
    [
        "shelly_1_gen4",
        "shelly_plug_m_gen3",
        "shelly_plug_pm_gen3",
        "shelly_blu_rc_button_4_zb",
        "shelly_blu_ht_display_zb",
    ],
)
def test_device(snapshot: SnapshotAssertion, device_fixture: str) -> None:
    """Test for Shelly devices."""
    logger = Mock()
    hass = Mock()
    hass.services = Mock()
    fixture_path = FIXTURES_PATH / f"{device_fixture}.json"
    data = json.loads(fixture_path.read_text())

    result = run_script(logger=logger, data=data, hass=hass)

    assert result.config_data
    assert hass.services.call.called

    for call in range(len(hass.services.call.call_args_list)):
        topic = hass.services.call.call_args_list[call][0][2]["topic"]
        payload = hass.services.call.call_args_list[call][0][2].get("payload")
        if not payload:
            continue
        assert topic == snapshot(name=f"{call}-topic")
        assert json.loads(payload) == snapshot(name=f"{call}-payload")
