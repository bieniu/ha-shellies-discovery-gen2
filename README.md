# ha-shellies-discovery-gen2

## Supported devices

- Shelly Plus 1
- Shelly Plus 1PM
- Shelly Pro 1
- Shelly Pro 1PM
- Shelly Pro 2
- Shelly Pro 2PM
- Shelly Pro 4PM

## Required automations

```yaml
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
        topic: "shellypro4pm-aabbcc/rpc"
        payload: "{{ device_info_payload }}"
    - service: mqtt.publish
      data:
        topic: "shellyplus1pm-112233/rpc"
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
