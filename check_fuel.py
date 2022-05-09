from parser import parser
from stations import get_filling_station


if __name__ == '__main__':
    args = parser.parse_args()
    if not (args.city and args.fuel):
        raise KeyError('Indicate city and fuel.')

    stations = [get_filling_station(s) for s in args.station]

    for station in stations:
        print(station.check(args.fuel, args.city))
