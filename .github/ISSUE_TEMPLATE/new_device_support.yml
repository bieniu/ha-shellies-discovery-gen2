name: New device suport
description: Suggest support for a new device
labels: new-device-support
body:
  - type: textarea
    attributes:
      label: Shelly.GetStatus response (JSON)
      description: Paste the full JSON response to `curl http://<DEVICE_IP>/rpc/Shelly.GetStatus`
      placeholder: |
        {
          "sys": {
            "mac": "AABBCCDDEEFF"
          }
        }
      render: json
    validations:
      required: true

  - type: textarea
    attributes:
      label: Shelly.GetConfig response (JSON)
      description: Paste the full JSON response to `curl http://<DEVICE_IP>/rpc/Shelly.GetConfig`
      placeholder: |
        {
          "sys": {
            "device": {
              "name": "Shelly"
            }
          }
        }
      render: json
    validations:
      required: true

  - type: textarea
    attributes:
      label: Shelly.GetDeviceInfo response (JSON)
      description: Paste the full JSON response to `curl http://<DEVICE_IP>/rpc/Shelly.GetDeviceInfo`
      placeholder: |
        {
          "id": "shelly-aabbccddeeff"
        }
      render: json
    validations:
      required: true
