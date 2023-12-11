import smbus
import time

from typing import Tuple

import jsonFuncs

bus = smbus.SMBus(1)


def convertToNumber(data: Tuple[float, float]) -> float:
    result = (data[1] - (256 * data[0])) / 1.2
    return result


def readLight(addr=0x23) -> float:
    data = bus.read_i2c_block_data(addr, 0x10)
    jsonFuncs.storeData("lightLevels.JSON", {"time": time.time(), "lightLevel": convertToNumber(data)})
    return convertToNumber(data)
