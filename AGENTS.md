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
    [https://www.home-assistant.io/integrations/python_script/](https://www.home-assistant.io/integrations/python_script/)
  - MQTT discovery documentation:
    [https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery)

## Python Version

The script runs in the Python environment bundled with Home Assistant. Always write
code compatible with **Python 3.14**. Do not use features or syntax from newer
versions without verifying Home Assistant support. Avoid type annotations in runtime
code — the `python_script` sandbox evaluates the script directly without a type
checker.

## Repository Layout

- `python_scripts/` — Home Assistant python scripts. The discovery generator lives
  here.
- `tests/` — pytest test suite.
- `tests/fixtures/` — full-device JSON fixtures used by device snapshot tests.
- `tests/snapshots/` — Syrupy snapshot output for MQTT topics and payloads.
- `scripts/` — helper scripts and documentation for Shelly-side scripts.
- `ruff.toml` — Ruff lint and formatting configuration.
- `.github/workflows/ci.yml` — CI lint and test commands.

## Script Architecture

The script receives device data through the `data` object injected by Home Assistant.
Understanding this flow is essential before modifying the script:

1. **Input (`data`)** — a dict containing device status, config, and component
   information retrieved from the Shelly device's RPC API. Key fields include:
   - `id` — device identifier (MAC-based)
   - `model` — Shelly model string (e.g., `"SNSW-001P16EU"`)
   - `components` — list of component dicts, each describing a sensor, switch, etc.

2. **Processing** — the script iterates over components and maps each to one or more
   Home Assistant MQTT discovery payloads using model constants and component
   definitions.

3. **Output** — MQTT discovery messages published via `hass.services.call()` to the
   `mqtt.publish` service. Each message targets a unique discovery topic.

### Supported Component Types (Platforms)

Each component type maps to a Home Assistant platform. Current supported platforms:

`binary_sensor`, `button`, `climate`, `cover`, `device_trigger`, `event`, `light`,
`number`, `select`, `sensor`, `switch`, `text`, `update`

When adding a new platform type, follow the pattern of an existing similar platform
and add tests covering the new component's discovery payload.

### BLU Device Architecture

BLU devices (e.g., Shelly BLU Button, BLU DW) differ from Gen2/Gen3/Gen4 devices:

- They do **not** communicate via direct MQTT. They use Bluetooth Low Energy and
  rely on a **Shelly gateway device** to relay their data over MQTT.
- The script generates discovery for BLU devices through the gateway's topics, not
  directly from the BLU device.
- When adding BLU device support, identify the gateway model that relays the device
  and ensure the fixture reflects the gateway + BLU component relationship.

## Development Setup

Install test dependencies using `uv` (required — do not use plain `pip`):

```bash
uv pip install -r requirements-test.txt
```

`uv` ensures reproducible environments consistent with CI. If `uv` is not installed:

```bash
pip install uv
```

## Development Commands

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

Run tests for a single device model only:

```bash
pytest tests/test_main.py -k "<fixture_name>"
```

Update Syrupy snapshots after an intentional behavior change:

```bash
pytest tests --snapshot-update
```

Always review the snapshot diff after `--snapshot-update` before committing.

Pre-commit-style repository hygiene is handled with `prek` and the hooks in
`.pre-commit-config.yaml`.

## Coding Guidelines

- Ruff is the linter and formatter. Follow `ruff.toml`; do not introduce local
  formatting styles that fight Ruff.
- Keep generated MQTT discovery payloads compact.
- Use Home Assistant MQTT discovery abbreviations for payload keys whenever an
  abbreviation exists:
  [https://www.home-assistant.io/integrations/mqtt/#supported-abbreviations-in-mqtt-discovery-messages](https://www.home-assistant.io/integrations/mqtt/#supported-abbreviations-in-mqtt-discovery-messages)
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

1. Add the model constant (e.g., `MODEL_SHELLYPLUS2PM = "SPLUS2PM"`) and the
   device definition/update logic in `python_scripts/shellies_discovery_gen2.py`.
2. Add a complete fixture JSON file under `tests/fixtures/`. The fixture must
   represent the full `data` dict passed to the script for that device, including
   all component information needed to generate discovery.

   Minimal fixture structure:
   ```json
   {
     "id": "shellyplusht-aabbccddeeff",
     "model": "SNSW-001P16EU",
     "fw_ver": "1.0.0",
     "components": [
       {
         "key": "switch:0",
         "status": { ... },
         "config": { ... }
       }
     ]
   }
   ```
   Keep fixtures complete enough to exercise the real discovery output, not just
   the minimal fields needed to avoid errors.

3. Add the fixture name to the `device_fixture` parameter list in `test_device` in
   `tests/test_main.py`.
4. Run the device test and generate initial snapshots:
   ```bash
   pytest tests/test_main.py -k "<fixture_name>" --snapshot-update
   ```
5. Review the generated snapshot carefully. Verify that all MQTT topics and
   payloads match Home Assistant MQTT discovery rules before committing.
6. Update `README.md` and `info.md` to include the new model in the supported devices
   list.

### Checklist for a New Device

- [ ] Model constant added
- [ ] Device definition logic added to `shellies_discovery_gen2.py`
- [ ] Fixture JSON added under `tests/fixtures/`
- [ ] Fixture name added to `test_device` parameter list
- [ ] Snapshot generated and reviewed
- [ ] `ruff check` and `ruff format --check` pass
- [ ] All existing snapshot tests still pass
- [ ] `README.md` and `info.md` updated with new model

## Snapshot Changes

Snapshot changes are part of the public behavior of this repository. Review them
carefully; unexpected topic, unique ID, or payload key changes are usually bugs.

When a snapshot change is intentional (e.g., a bugfix or discovery improvement):

- Run `pytest --snapshot-update` to regenerate affected snapshots.
- Describe the reason for the change explicitly in the PR/commit message.
- Never accept snapshot changes without reading the diff.

## Testing Notes

- `tests/test_main.py` loads `python_scripts/shellies_discovery_gen2.py` as a
  module and injects the Home Assistant-style globals used by `python_script`.
- `test_device` is the required full-device regression test path for supported
  models.
- The snapshots assert both MQTT config topics and JSON payloads.
- To run only a specific device test:
  ```bash
  pytest tests/test_main.py -k "shellyplus2pm"
  ```

## Versioning

This project follows **Semantic Versioning** (SemVer: `MAJOR.MINOR.PATCH`):

- `PATCH` — bug fixes, no behavior change visible to users
- `MINOR` — new device support or new non-breaking features
- `MAJOR` — breaking changes to MQTT topics, unique IDs, or script arguments

Versioning is managed by the repository's CI. The new version number is based
on the tags of individual PRs, which are manually added by the repository's
maintainer. Changing the version number in the VERSION constant in the script
 is prohibited!

## Documentation Notes

- Update `README.md` and `info.md` when supported devices, script arguments,
  installation behavior, or user-visible MQTT discovery behavior changes.
- Keep Home Assistant-specific wording aligned with current official
  documentation, especially around `python_script` and MQTT discovery.
- The supported devices table in `README.md` and `info.md` is user-facing; keep model
  names and links accurate.

## Contribution Checklist

Before submitting any change, verify:

- [ ] `ruff check` and `ruff format --check` pass with zero errors
- [ ] All existing snapshot tests pass without unexpected changes
- [ ] New device: fixture added, snapshot generated and reviewed
- [ ] `README.md` and `info.md` updated if supported devices or script arguments changed
- [ ] No new runtime imports added to `shellies_discovery_gen2.py`
- [ ] Snapshot diff reviewed — no unexpected topic, unique ID, or payload changes
- [ ] Commit message describes the reason for any intentional snapshot update
