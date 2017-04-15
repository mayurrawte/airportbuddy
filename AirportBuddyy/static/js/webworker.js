



 client = new Paho.MQTT.Client("139.59.79.221",Number(1884),"/ws","cluebt");
// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});

// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("del");
  client.subscribe("del/lostandfound");
  message = new Paho.MQTT.Message("Hello");
  message.destinationName = "test";
  client.send(message);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message)
{
    var ms = "";
    for(var i in message)
    {
        ms = ms+ " : " + i;
    }
    var data = ' <div class="msga">'+message.destinationName +":"+ message.payloadString+'</div>';

    console.log("onMessageArrived:"+message.payloadString);
  $('#chat_message').append(data);



}

