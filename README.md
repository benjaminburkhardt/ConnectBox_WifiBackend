Unitymedia Connect box (Compal CH7465LG) Wifi Enabler / Disabler 
=============================================

With this project I want to toggle the 2.4 Ghz Wifi of my Connect box with ease.

Usage
-----

Set the ip to the connect box and the password in config.py
The file ``toggle-wifi.py`` contains the code to toggle the 2.4ghz wifi signal.

Development
-----------

For development is recommended to use a ``venv``.

.. code:: bash

    $ python3 -m venv .
    $ source bin/activate
    $ python3 setup.py develop
