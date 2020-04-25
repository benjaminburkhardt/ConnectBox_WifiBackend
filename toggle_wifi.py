"""
ENABLE WIFI

Set router ip and password in config.py

"""
import argparse
import os
import pprint
import sys
import config

from compal import (Compal, DHCPSettings, PortForwards, Proto,  # noqa
                    WifiSettings)

# Push the parent directory onto PYTHONPATH before compal module is imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def toggle_wifi(enable_wifi):
    modem = Compal(config.host, config.interface_passwd)
    modem.login()

    # And/or change wifi settings
    wifi = WifiSettings(modem)
    settings = wifi.wifi_settings

    if enable_wifi:
        # ENABLE 2.4Ghz
        settings.radio_2g.bss_enable = 1
    else:
        # DISABLE 2.4Ghz
        settings.radio_2g.bss_enable = 2

    wifi.update_wifi_settings(settings, False)

    wifi = WifiSettings(modem)
    settings = wifi.wifi_settings

    # pprint.pprint(settings)
    if enable_wifi and settings.radio_2g.bss_enable == 1:
        print("\nWIFI is now ON!")
    elif not enable_wifi and settings.radio_2g.bss_enable == 2:
        print("\nWIFI is now OFF!")
    else:
        print("\nERROR! Something went wrong... :(")

    modem.logout()

def switch_wifi():
    modem = Compal(config.host, config.interface_passwd)
    modem.login()

    # And/or change wifi settings
    wifi = WifiSettings(modem)
    settings = wifi.wifi_settings

    if settings.radio_2g.bss_enable == 2:
        # ENABLE 2.4Ghz
        settings.radio_2g.bss_enable = 1
    else:
        # DISABLE 2.4Ghz
        settings.radio_2g.bss_enable = 2

    wifi.update_wifi_settings(settings)

    wifi = WifiSettings(modem)
    settings = wifi.wifi_settings

    pprint.pprint(settings)

    modem.logout()

    if settings.radio_2g.bss_enable == 1:
        return "WIFI is now ON!"
    elif settings.radio_2g.bss_enable == 2:
        return "WIFI is now OFF!"
    else:
        return "ERROR! Something went wrong... :("




if __name__ == "__main__":

    if len(sys.argv) >= 2:
        if str(sys.argv[1]) == "1":
            toggle_wifi(True)
        elif str(sys.argv[1]) == "0":
            toggle_wifi(False)
        else:
            print("Wrong parameter 0=disable 1=enable !!!")
    else:
        print("Parameter missing !!!")