let topic_prefix = null;
let installed_version = null;

Shelly.call("MQTT.GetConfig", {}, function (config) {
    topic_prefix = config.topic_prefix;
});

function SendDeviceStatus() {
    Shelly.call("Shelly.GetDeviceInfo", {}, function (device_info) {
        installed_version = device_info.ver;
    });
    Shelly.call("Shelly.GetStatus", {}, function (status) {
        status.sys.installed_version = installed_version;
        MQTT.publish(topic_prefix + "/status/rpc", JSON.stringify({ "result": status }));
    });
}

let UpdateTimer = Timer.set(300000, true, SendDeviceStatus);