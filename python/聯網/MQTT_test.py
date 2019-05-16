import paho.mqtt.client as mqtt
import time,os

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))
  
# If broker asks client ID.
client_id = "Asus_notebook_X550V"
client = mqtt.Client(client_id=client_id)
client.on_connect = on_connect
client.on_message = on_message
# If broker asks user/password.
user = "Way"
password = "ga34825971"
client.username_pw_set(user, password)
client.connect("192.168.43.97", 1883, 600)

topic = ["Way/temp" ,"Way/test2" ,"Way/humi"]

payload = 40
for i in range(1,10):
    client.publish(topic[0], "%d" %(payload),qos = 2)
    client.publish(topic[1], "1",qos = 2)
    client.publish(topic[2], "%d" %(payload),qos = 2)
    time.sleep(1)
    payload =payload-2
    client.loop_start()
    # 當 qos = 0, 若訊息間隔太短，就可能會漏發訊息。這是正常現象。

