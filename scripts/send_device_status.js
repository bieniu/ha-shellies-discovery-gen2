let CONFIG = { topic_prefix: null };

Shelly.call("MQTT.GetConfig", {}, function (config) {
    CONFIG.topic_prefix = config.topic_prefix;
});

function SendDeviceStatus() {
    Shelly.call("Shelly.GetStatus", {}, function (status) {
        MQTT.publish(CONFIG.topic_prefix + "/status/rpc", JSON.stringify({ "result": status }));
    });
}

let UpdateTimer = Timer.set(300000, true, SendDeviceStatus);