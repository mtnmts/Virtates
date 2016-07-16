# In the world of machines
# - virtual machines -
# Dominated by software
# Everything is cold
# Cold as ice.

import logging
from threading import Lock
from enum import Enum


class VMState(Enum):
    On = 1
    Off = 2
    Paused = 3
    Busy = 4
    Unknown = 5
    Error = 6


class VM(object):
    def __init__(self, cloud, friendly_name, uuid, status, cs_data):
        self._uuid = uuid
        self._cloud = cloud
        self._friendly_name = friendly_name
        self._cs_data = cs_data
        self._status = status
        self._lock = Lock()
