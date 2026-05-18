# Repository Instructions

## Project Overview

This repository contains **Shellies Discovery Gen2**, a Home Assistant `python_script`
that generates MQTT discovery configuration for Shelly Gen2, Gen3, Gen4, and BLU
devices.

The main script is:

- `python_scripts/shellies_discovery_gen2.py`

It is intended to run inside Home Assistant's `python_script` integration, not as a
normal Python package. Keep the implementation compatible with that sandbox:

- Do not add runtime imports to `shellies_discovery_gen2.py`; Home Assistant
  `python_script` does not allow Python imports.
- Use the injected `data`, `hass`, and `logger` objects as the script interface.
- Keep helper code in the same script file unless it is test-only code.
- Treat Home Assistant behavior as the source of truth:
  - Python Script documentation:
    https://www.home-assistant.io/integrations/python_script/
  - MQTT discovery documentation:
    https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery

## Repository Layout

- `python_scripts/` - Home Assistant python scripts. The discovery generator lives
  here.
- `tests/` - pytest test suite.
- `tests/fixtures/` - full-device JSON fixtures used by device snapshot tests.
- `tests/snapshots/` - Syrupy snapshot output for MQTT topics and payloads.
- `scripts/` - helper scripts and documentation for Shelly-side scripts.
- `ruff.toml` - Ruff lint and formatting configuration.
- `.github/workflows/ci.yml` - CI lint and test commands.

## Development Commands

Install test dependencies in your active environment:

```bash
uv pip install -r requirements-test.txt
```

Run the same checks as CI:

```bash
ruff check python_scripts tests
ruff format --check python_scripts tests
pytest tests --timeout=30 --cov --cov-branch --cov-report=xml --error-for-skips
```

For local fixes:

```bash
ruff check --fix python_scripts tests
ruff format python_scripts tests
```

Pre-commit-style repository hygiene is handled with `prek` and the hooks in
`.pre-commit-config.yaml`.

## Coding Guidelines

- Ruff is the linter and formatter. Follow `ruff.toml`; do not introduce local
  formatting styles that fight Ruff.
- Keep generated MQTT discovery payloads compact.
- Use Home Assistant MQTT discovery abbreviations for payload keys whenever an
  abbreviation exists:
  https://www.home-assistant.io/integrations/mqtt/#supported-abbreviations-in-mqtt-discovery-messages
- Prefer existing constants such as `KEY_STATE_TOPIC`, `KEY_DEVICE`, and
  `KEY_UNIQUE_ID` over string literals for discovery keys.
- Preserve stable MQTT topics, unique IDs, entity names, and device identifiers
  unless a behavior change is intentional and covered by snapshot updates.
- Be careful with retained discovery/state behavior and availability topics; these
  affect how entities appear after Home Assistant or MQTT restarts.
- Keep changes scoped. This project intentionally concentrates most runtime logic
  in `shellies_discovery_gen2.py` because of Home Assistant `python_script`
  restrictions.

## Adding Support for a New Device Model

Support for a new Shelly model must include a full-device fixture test.

1. Add the model constants and device definition/update logic in
   `python_scripts/shellies_discovery_gen2.py`.
2. Add a complete fixture JSON file under `tests/fixtures/`. The fixture should
   represent the data passed to the script for that device, including device
   status/config/component information needed to generate discovery.
3. Add the fixture name to the `device_fixture` parameter list in
   `test_device` in `tests/test_main.py`.
4. Run the device test and update Syrupy snapshots only after verifying that the
   generated MQTT topics and payloads match Home Assistant MQTT discovery rules.

Snapshot changes are part of the public behavior of this repository. Review them
carefully; unexpected topic, unique ID, or payload key changes are usually bugs.

## Testing Notes

- `tests/test_main.py` loads `python_scripts/shellies_discovery_gen2.py` as a
  module and injects the Home Assistant-style globals used by `python_script`.
- `test_device` is the required full-device regression test path for supported
  models.
- The snapshots assert both MQTT config topics and JSON payloads. If a behavior
  change is intentional, update snapshots explicitly and explain why.
- Keep fixtures complete enough to exercise the real discovery output for the
  device, not only the minimal fields needed to avoid errors.

## Documentation Notes

- Update `README.md` when supported devices, script arguments, installation
  behavior, or user-visible MQTT discovery behavior changes.
- Keep Home Assistant-specific wording aligned with current official
  documentation, especially around `python_script` and MQTT discovery.
