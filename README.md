Unitymedia Connect box (Compal CH7465LG) Wifi Enabler / Disabler 
=============================================

With this project I want to toggle the 2.4 Ghz Wifi of my Connect box with ease.

Usage
-----

Set the ip to the connect box and the password in config.py
The file ``toggle-wifi.py`` contains the code to toggle the 2.4ghz wifi signal.

Or

1. Install project and dependencies on Raspberry Pi
2. Set your Connectbox ip and password in config.py
3. User Siri Shortcut for iOS to toggle Wifi: https://www.icloud.com/shortcuts/436cf7b5e1a14bcfa8709561b4406595

Development
-----------

For development is recommended to use a ``venv``.

.. code:: bash

    $ python3 -m venv .
    $ source bin/activate
    $ python3 setup.py develop
