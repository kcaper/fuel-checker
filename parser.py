import argparse

parser = argparse.ArgumentParser(
    description='cli',
    epilog='...'
)

parser.add_argument(
    '-c', '--city',
    action='store', type=str,
    help='City name'
)
parser.add_argument(
    '-f', '--fuel',
    action='store', type=str,
    help='Fuel query, ie: 95, A95, M95'
)
parser.add_argument(
    '-s', '--station',
    action='append', type=str,
    help='Filling station, ie: wog'
)
