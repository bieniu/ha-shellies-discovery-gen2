[![Community Forum][forum-shield]][forum]  [![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]  [![PayPal_Me][paypal-me-shield]][paypal-me]

This script adds MQTT discovery support for Shelly Gen2 devices in the [Home Assistant](https://home-assistant.io/).

![image](https://user-images.githubusercontent.com/478555/151068134-eac574ac-60c9-4e19-8ff1-cefa5046177d.png)

## Prerequisites

This script needs Home Assistant `python_script` component so, if you never used it, I strongly suggest you to follow the [official instruction](https://www.home-assistant.io/integrations/python_script#writing-your-first-script) and check that `python_script` is properly configured and it's working.

For the device to work with the script, it must have MQTT configured and options `RPC status notifications over MQTT` and `Generic status update over MQTT` enabled.

## Installation

You can download `shellies_discovery_gen2.py` file and save it in `<config>/python_scripts` folder.

## Supported devices

- Shelly Plus 1
- Shelly Plus 1PM
- Shelly Plus i4
- Shelly Pro 1
- Shelly Pro 1PM
- Shelly Pro 2
- Shelly Pro 2PM
- Shelly Pro 4PM

## How to debug

To debug the script add this to your `logger` configuration:

```yaml
# configuration.yaml file
logger:
  default: warning
  logs:
    homeassistant.components.python_script: debug
    homeassistant.components.automation: info
```

## Supported platforms

- switch
- light
- sensor

## Supported features

- the device name is taken from the device configuration
- the relay name is taken from the device configuration
- the relay consumption type is taken from the device configuration
- if the input type is set to button, device automation triggers are available
- custom MQTT prefixes are supported

## Known problems

- availability doesn’t work (firmware change is needed)

## Script arguments

key | optional | type | default | description
-- | -- | -- | -- | --
`discovery_prefix` | True | string | `homeassistant` | MQTT discovery prefix
`qos` | True | integer | `0` | MQTT QoS, you can use `0`, `1` or `2`

## Minimal configuration

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
  action:
    - service: mqtt.publish
      data:
        topic: "shellypro4pm-aabbcc/rpc"  # shellypro4pm-aabbccddeeff is a device ID
        payload: "{{ device_info_payload }}"
    - service: mqtt.publish
      data:
        topic: "shellyplus1pm-112233/rpc"  # shellyplus1pm-112233445566 is a device ID
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
```

[forum]: https://community.home-assistant.io/t/shellies-discovery-gen2-script/384479
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=popout
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
[paypal-me-shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal-me]: https://www.paypal.me/bieniu79
