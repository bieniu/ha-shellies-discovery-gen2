let topic_prefix = null;
let installed_version = null;

Shelly.call("MQTT.GetConfig", {}, function (config) {
    topic_prefix = config.topic_prefix;
});

function SendDeviceStatus() {
    let _device_info = Shelly.getDeviceInfo();
    installed_version = _device_info.ver;
    Shelly.call("Shelly.GetStatus", {}, function (status) {
        status.sys.installed_version = installed_version;
        status.sys.model = model;
        MQTT.publish(topic_prefix + "/status/rpc", JSON.stringify(status));
    });
}


MQTT.setConnectHandler(SendDeviceStatus)
let UpdateTimer = Timer.set(30000, true, SendDeviceStatus);
