let topicPrefix = null;
let updateTimer = null;
let installedVersion = null;
let statusTopic = null;

function onStatusReceived(result, error_code) {
  try {
    if (error_code !== 0 || !result) {
      return;
    }
    result.sys.installed_version = installedVersion;
    MQTT.publish(statusTopic, JSON.stringify(result));
  } catch (e) {
    console.log("sendDeviceStatus has failed: ", e);
  }
}

function sendDeviceStatus() {
  if (!MQTT.isConnected()) {
    return;
  }
  Shelly.call("Shelly.GetStatus", {}, onStatusReceived);
}

function onMQTTConfigReceived(config) {
  topicPrefix = config.topic_prefix;
  statusTopic = topicPrefix + "/status/rpc";
  console.log("Using topic prefix: ", topicPrefix);

  if (!updateTimer) {
    updateTimer = Timer.set(30000, true, sendDeviceStatus);
  }
}

function initScript() {
  console.log("Starting shellies_discovery_gen2_script");
  try {
    installedVersion = Shelly.getDeviceInfo().ver;
    Shelly.call("MQTT.GetConfig", {}, onMQTTConfigReceived);
  } catch (e) {
    console.log("initScript has failed: ", e);
  }
}

initScript();
