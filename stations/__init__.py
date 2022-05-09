from .station import FillingStation
from .wog import WOG

STATIONS = {
    'wog': WOG
}


def get_filling_station(name: str) -> FillingStation:
    s = STATIONS[name]
    return s()
