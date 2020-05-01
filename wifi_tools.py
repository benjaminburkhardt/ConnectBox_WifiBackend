"""
ENABLE WIFI

Set router ip and password in config.py

"""
import argparse
import os
import pprint
import sys
import threading


from compal import (Compal,  # noqa
                    WifiSettings)

lock = threading.Lock()


# Push the parent directory onto PYTHONPATH before compal module is imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



def change_wifi_to(ip, password, enableWifi):
    lock.acquire()
    modem = Compal(ip, password)
    modem.login()

    # And/or change wifi settings
    wifi = WifiSettings(modem)
    settings = wifi.wifi_settings

    if enableWifi:
        if settings.radio_2g.bss_enable == 2:
            # ENABLE 2.4Ghz
            settings.radio_2g.bss_enable = 1
        else:
            modem.logout()
            lock.release()
            return "WIFI was already ON"

    if not enableWifi:
        if settings.radio_2g.bss_enable == 1:
            # DISABLE 2.4Ghz
            settings.radio_2g.bss_enable = 2
        else:
            modem.logout()
            lock.release()
            return "WIFI was already OFF"

    wifi.update_wifi_settings(settings, False)

    wifi = WifiSettings(modem)
    settings = wifi.wifi_settings

    # pprint.pprint(settings)
    if enableWifi and settings.radio_2g.bss_enable == 1:
        to_return = "WIFI (" + str(wifi.wifi_settings.radio_2g.ssid) + ") is now ON!"
    elif not enableWifi and settings.radio_2g.bss_enable == 2:
        to_return = "WIFI (" + str(wifi.wifi_settings.radio_2g.ssid) + ") is now OFF!"
    else:
        to_return = "\nERROR! Something went wrong... :("

    modem.logout()
    lock.release()
    return to_return

def toggle_wifi(ip, password):
    modem = Compal(ip, password)
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
        return "WIFI ("+ str(wifi.wifi_settings.radio_2g.ssid) + ") is now ON!"
    elif settings.radio_2g.bss_enable == 2:
        return "WIFI ("+ str(wifi.wifi_settings.radio_2g.ssid) + ") is now OFF!"
    else:
        return "ERROR! Something went wrong... :("


def wifi_enabled(ip, password):
    modem = Compal(ip, password)
    modem.login()
    wifi = WifiSettings(modem)
    enabled = wifi.wifi_settings.radio_2g.bss_enable == 1
    modem.logout()
    return enabled


if __name__ == "__main__":
    print("Disabled...")
    # parser = argparse.ArgumentParser(description="Connect Box WiFi configuration")
    #
    # parser.add_argument("ip", help="ConnectBox ip",
    #                     type=str)
    # parser.add_argument("password", help="ConnectBox password",
    #                     type=str)
    # parser.add_argument("enableWifi", help="Enable WiFi", type=int)
    #
    # args, unknown = parser.parse_known_args()
    #
    # change_wifi_to(args.ip, args.password, args.enableWifi == 1)
