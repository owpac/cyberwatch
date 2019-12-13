from argparse import ArgumentParser

from options import Options
from colors import Colors
from shodan_cmd import Shodan_cmd


def main():
    argument_parser = ArgumentParser(
        description="Cyberwatch - Shodan",
        usage="./cyberwatch.py [options]\n\n" + Options.SAMPLE)

    argument_parser.add_argument('-I', '--info', dest='info', type=str,
                                 help='Get info about: services, protocols and api')

    argument_parser.add_argument('-H', '--host', dest='host', type=str,
                                 help='Search host in Shodan')

    argument_parser.add_argument('-p', '--print', dest='print', action="store_true",
                                 help='Print results in command line')

    argument_parser.add_argument('-s', '--save', dest='save', action="store_true",
                                 help='Save results')

    argument_parser.add_argument('-c', '--compare', dest='compare', action="store_true",
                                 help='Compare results with baseline')

    args = argument_parser.parse_args()

    cyberwatch = Shodan_cmd(Options.SHODAN_API)

    if args.info:
        if args.info.lower() == "services":
            cyberwatch.services()
        elif args.info.lower() == "protocols":
            cyberwatch.protocols()
        elif args.info.lower() == "api":
            cyberwatch.api_info()
        else:
            msg = "Wrong option. Please choose from : Services, Protocols, Api"
            print(Colors.FAIL + Colors.BOLD + "\n" + Options.LIST_ERROR + "ERROR: " + Colors.ENDC + msg + "\n")

    elif args.host:
        cyberwatch.host(args.host, args.print, args.save, args.compare)

    else:
        msg = "Wrong option."
        print(Colors.FAIL + Colors.BOLD + "\n" + Options.LIST_ERROR + "ERROR: " + Colors.ENDC + msg + "\n")


if __name__ == '__main__':
    main()
