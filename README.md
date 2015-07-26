# Install raspian on raspberry
Install airmon-ng and airodump-ng and screen

mkdir /home/pi/parcel/     <<<<<<<Here install the script
mkdir /home/pi/parcel/arc/
and add in /etc/rc.local

sudo /usr/local/sbin/airmon-ng stop wlan0 &
sudo /usr/local/sbin/airmon-ng start wlan0 &
rm  /home/pi/parcel/arc/1* &

When your pi start, run twice commands

screen -S air -d -m -L airodump-ng mon0 -w /home/pi/parcel/arc/1 --output-format csv
sh /home/pi/parcel/arc/filtering.sh &

Modify the script with your information about server idas

# Mount Broker and IDAs.

#Mount Services and Devices

-----------Create Service------------------------

curl -X POST http://<Ip Idas>:<Port>/iot/services \
-i \
-H "X-Auth-Token: $SMARTCITY_ALICE_TOKEN" \
-H "Content-Type: application/json" \
-H "Fiware-Service: smartcity" \
-H "Fiware-ServicePath: /wifi" \
-d '{"services": [{ "apikey": "apikey2", "cbroker": "http://<IP BROKER>:<Port broker>", "entity_type": "thing", "resource": "/iot/d" }]}'


---------Create Device------------------
curl -X POST http://<Ip Idas>:<Port>/iot/devices \
-i \
-H "X-Auth-Token: $SMARTCITY_ALICE_TOKEN" \
-H "Content-Type: application/json" \
-H "Fiware-Service: smartcity" \
-H "Fiware-ServicePath: /wifi" \
-d ' { "devices": [ { "device_id": "dev_1", "protocol": "PDI-IoTA-UltraLight", "entity_name": "entity_1", "entity_type": "thing", "timezone": "America/Santiago", "commands": [ { "name": "ping", "type": "command", "value": "device_id@ping|%s"} ], "attributes": [ { "object_id": "source_data", "name": "Device_Detected", "type": "int" } ], "static_attributes": [ { "name": "att_name", "type": "string", "value": "value" } ] } ] }'



-----------------------Update information ---------------------

curl -X GET "http://<Ip Idas>:<Port>/iot/d?i=dev_1&d=source_data|15&k=apikey2" -i

----------------Request--------------------------

(curl 172.17.0.10:10026/v1/queryContext -s -S --header 'Content-Type: application/json' --header 'Accept: application/json' \
-H "Fiware-Service: smartcity" \
-H "Fiware-ServicePath: /wifi" \
-d @- | python -mjson.tool) <<EOF
{
    "entities": [
        {
            "type": "thing",
            "isPattern": "false",
            "id": "entity_1"
        }
    ]
}
EOF


# Parcel-V0.1
