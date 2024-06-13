# Shellies Discovery Gen2

[![GitHub Release][releases-shield]][releases]
[![GitHub All Releases][downloads-total-shield]][releases]
[![Community Forum][forum-shield]][forum]
[![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]
[![PayPal_Me][paypal-me-shield]][paypal-me]


This script adds MQTT discovery support for Shelly Gen2 and Gen3 devices in the [Home Assistant](https://home-assistant.io/).

![image](https://user-images.githubusercontent.com/478555/151659020-a6181434-ae19-42bb-9dbe-fed8002ee730.png)

## Prerequisites

This script needs Home Assistant `python_script` component so, if you never used it, I strongly suggest you to follow the [official instruction](https://www.home-assistant.io/integrations/python_script#writing-your-first-script) and check that `python_script` is properly configured and it's working.

For the device to work with the script, it must have MQTT configured and options **Enable "MQTT Control"**, **RPC status notifications over MQTT** and **Generic status update over MQTT** enabled.

MQTT integration must be configured in Home Assistant.

## Installation

You can download `shellies_discovery_gen2.py` file and save it in `<config>/python_scripts` folder or install the script via [HACS](https://hacs.xyz/).
You won't find **Shellies Discovery Gen2** in the HACS **Integrations** section, nor add it as a custom repository. You must have a properly configured `python_script` component to be able to install the script from the HACS **Automations** section.

Shellies Discovery Gen2 will automatically install/update the script on your Shelly device. Due to `python_scripts` integration limitations, updating the device script requires the `announce` automation to run twice.

## Supported devices

- Shelly 1 Gen3
- Shelly 1PM Gen3
- Shelly 1 Mini Gen3
- Shelly 1PM Mini Gen3
- Shelly Dimmer 0/1-10V PM Gen3
- Shelly H&T Gen3
- Shelly I4 Gen3
- Shelly PM Mini Gen3
- Shelly Plus 1
- Shelly Plus 1 Mini
- Shelly Plus 1PM
- Shelly Plus 1PM Mini
- Shelly Plus 2PM
- Shelly Plus Add-on
- Shelly Plus H&T
- Shelly Plus I4
- Shelly Plus Plug IT
- Shelly Plus Plug S
- Shelly Plus Plug UK
- Shelly Plus Plug US
- Shelly Plus PM Mini
- Shelly Plus RGBW PM (RGBW profile is not supported)
- Shelly Plus Smoke
- Shelly Plus Wall Dimmer
- Shelly Pro 1
- Shelly Pro 1PM
- Shelly Pro 2
- Shelly Pro 2PM
- Shelly Pro 3
- Shelly Pro 3EM
- Shelly Pro 3EM Switch Add-on
- Shelly Pro 4PM
- Shelly Pro Dimmer 2
- Shelly Pro Dual Cover PM
- Shelly Pro EM
- Shelly Wall Display (relay and thermostat mode)
- Shelly X MOD1

## Battery powered devices

Battery powered devices like Plus H&T are put to sleep most of the time. For this reason, adding/updating entities configuration for a device should be done as follows:

- enter the device into setup mode (press the button on the device)
- manually run `Shellies Announce Gen2` automation

## How to debug

To debug the script add this to your `logger` configuration:

```yaml
# configuration.yaml file
logger:
  default: error
  logs:
    homeassistant.components.python_script: debug
    homeassistant.components.automation: info
    homeassistant.components.mqtt.discovery: info
```

## Supported platforms

- binary sensor
- button
- climate
- cover
- device trigger
- event
- fan
- light
- sensor
- switch
- update

## Supported features

- the device name is taken from the device configuration
- the relay name is taken from the device configuration
- the relay consumption type is taken from the device configuration (consumption type must contain `light` or `fan` to configure light or fan platform)
- if the input type is set to button, device automation triggers are available
- custom MQTT prefixes are supported

## Script arguments

key | optional | type | default | description
-- | -- | -- | -- | --
`discovery_prefix` | True | string | `homeassistant` | MQTT discovery prefix
`script_prefix` | True | string | | MQTT prefix to install the script in the device
`qos` | True | integer | `0` | MQTT QoS, you can use `0`, `1` or `2`

## Configuration

```yaml
# configuration.yaml file
python_script:

# automations.yaml file
- id: shellies_announce_gen2
  alias: "Shellies Announce Gen2"
  trigger:
    - platform: homeassistant
      event: start
  variables:
    device_info_payload:  "{{ {'id': 1, 'src':'shellies_discovery', 'method':'Shelly.GetConfig'} | to_json }}"
    device_ids:  # enter the list of device IDs (MQTT prefixes) here
      - shellyplus2pm-485519a1ff8c
      - custom-prefix/shelly-kitchen
  action:
    - repeat:
        for_each: "{{ device_ids }}"
        sequence:
          - service: mqtt.publish
            data:
              topic: "{{ repeat.item }}/rpc"
              payload: "{{ device_info_payload }}"

- id: shellies_discovery_gen2
  alias: "Shellies Discovery Gen2"
  mode: queued
  max: 999
  trigger:
  - platform: mqtt
    topic: shellies_discovery/rpc
  action:
  - service: python_script.shellies_discovery_gen2
    data:
      id: "{{ trigger.payload_json.src }}"
      device_config: "{{ trigger.payload_json.result }}"
  - service: mqtt.publish
    data:
      topic: "{{ trigger.payload_json.result.mqtt.topic_prefix }}/command"
      payload: "status_update"
```

[releases]: https://github.com/bieniu/ha-shellies-discovery-gen2/releases
[releases-shield]: https://img.shields.io/github/release/bieniu/ha-shellies-discovery-gen2.svg?style=popout
[downloads-total-shield]: https://img.shields.io/github/downloads/bieniu/ha-shellies-discovery-gen2/total
[forum]: https://community.home-assistant.io/t/shellies-discovery-gen2-script/384479
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=popout
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
[paypal-me-shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal-me]: https://www.paypal.me/bieniu79
