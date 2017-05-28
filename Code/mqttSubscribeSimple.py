import paho.mqtt.subscribe as subscribe 

#This is the subscriber.
#Traffic Light subscribes to the location information from car
def subscribe_location():
    topics=['/location']
    m=subscribe.simple(topics,hostname="192.168.178.33",msg_count=4)
    loc=list()
    topic=list() 
    for a in m:
        topic.append(a.topic) 
        temp_loc=str(a.payload.decode("utf-8"))
        loc.append(temp_loc) 
    topic.reverse()
    loc.reverse() 
    return loc 
