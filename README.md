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

# Parcel-V0.1
