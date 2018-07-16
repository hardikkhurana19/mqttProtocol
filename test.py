import paho.mqtt.client as mqtt
import re
name = ""
friend = ""
client = mqtt.Client()
print("Let's Get Started!!")

def name2():
        global name
        global friend
        spy_name = input("What's your name------>\n")
        while spy_name.isalpha() == False:
            print("name can not contain spaces or numeric values")
            spy_name = input("What's your name------>\n")
        if len(spy_name) > 0 and spy_name != " ":  # logic will be here if condition is true
            spy = input("friend name\n")
            while spy.isalpha() == False:
                print("name can not contain spaces or numeric values")
                spy = input("What's your friend name------>\n")
            if len(spy) > 0 and spy != " ":
                print("Let's get Started Mr. " + spy_name + spy)
                friend = spy
                name = spy_name

                client.on_connect = on_connect
                client.on_message = on_message
                client.on_disconnect = on_disconnect
                client.connect("iot.eclipse.org", 1883)
                client.loop_start()
                while True:
                    var = name+friend
                    msg = input("Enter your message\n")
                    age = "\\bexit\\b"
                    if re.match(age, str(msg)) != None:
                            list = msg.split("/")
                            new = list[1]
                            var = name + new
                            while True:
                                msg = input("Enter your message for" +new +"\n")
                                client.publish(var,msg,2)
                    else:
                        client.publish(var, msg, 2)


            else:
                print("error")

def on_connect(client,userdata,flags,rc):
    global friend
    global name
    var = friend+name
    print("connected")
    client.subscribe(var,2)


def on_message(client,userdata,msg):
    newmsg=str(msg.payload.decode("utf-8"))
    global friend
    print(friend+" says " +newmsg)



def on_disconnect(client,usredata,rc):
    print("Disconnectd from broker")

name2()
