Unitymedia Connect box (Compal CH7465LG) Wifi Enabler / Disabler 
=============================================

With this project I want to toggle the 2.4 Ghz Wifi of my Connect box with ease.

Setup
-----


1. Clone & install project and dependencies somewhere eg. on a Raspberry Pi
2. Run the flask server by running ``python3 api.py``
3. Access the flask api service via:
    - Check if Wi-Fi is enabled: ``/wifi/status?ip=<connectbox-ip>&password=<connectbox-pw>``
    - Enable Wi-Fi: ``/wifi/on?ip=<connectbox-ip>&password=<connectbox-pw>``
    - Disable Wi-Fi: ``/wifi/off?ip=<connectbox-ip>&password=<connectbox-pw>``
4. [OPTIONAL] Create a Siri Shourtcut to run it.
5. [OPTIONAL] Create a service to run the flask server on startup:

a) Create service file:
```bash
    sudo vi /lib/systemd/system/flask.service
```

b) Add this to the new service file:
```text
 [Unit]
 Description=Flask Unitymedia Server
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python3 /home/<your-user>/compal_CH7465LG_py/api.py > /home/<your-user>/flask.log 2>&1

 [Install]
 WantedBy=multi-user.target
```

c) Adjust file permissions:
```bash
sudo chmod 644 /lib/systemd/system/flask.servic
```

d) Reload and enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable flask.service
```

e) Reboot
```bash
sudo reboot
```

