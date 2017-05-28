import paho.mqtt.publish as publish 
# This is the Publisher.
# Car publishes its location to the Traffic Light
def publish_location(lattitude,longitude,typ,accuracy):
    if lattitude and longitude and typ and accuracy:
        msgs=[{'topic':"/location",'payload':lattitude},{'topic':"/location",'payload':longitude},{'topic':"/location",'payload':typ},{'topic':"/location",'payload':accuracy}]
        publish.multiple(msgs,hostname="192.168.178.33")
        print("Published Location data to the Traffic Light") 
    else:
        print("Location information not received from Geo API")  
        msgs="No information received from Geo API" 
    return msgs 
