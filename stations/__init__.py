from .station import FillingStation

STATIONS = {
}


def get_filling_station(name: str) -> FillingStation:
    s = STATIONS[name]
    return s()
