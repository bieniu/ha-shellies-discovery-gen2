# ha-shellies-discovery-gen2

## Supported devices

- Shelly Pro 4PM
- Shelly Plus 1PM

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
      fw_id: "{{ trigger.payload_json.result.sys.device.fw_id }}"
      id: "{{ trigger.payload_json.src }}"
      mac: "{{ trigger.payload_json.result.sys.device.mac }}"
      name: "{{ trigger.payload_json.result.sys.device.name }}"
```