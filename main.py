from argparse import ArgumentParser

from options import Options
from shodan_cmd import Shodan_cmd
from user_input import ask_string, ask_number


def main():
    # again = True
    # while again:
    #     print("")
    #
    #     # On enregistre les traces d'exécution
    #     file = f'Baseline_{numero}_{depart}.txt'
    #     with open(file, mode='w', encoding='utf-8') as f:
    #         print(resultat, file=f)
    #
    #     print(f"Enregistrement des traces d'exécution dans le fichier \"{file}\" effectué.")
    #
    #     again = ask_string('Voulez-vous tester une autre recherche ?')

    argument_parser = ArgumentParser(
        description="Cyberwatch - Shodan",
        usage="./cyberwatch.py [options] \nSamples: ./cyberwatch.py -H")

    argument_parser.add_argument('-I', '--info', dest='info', type=str,
                                 help='Get info about: services, protocols, queries and api')

    argument_parser.add_argument('-H', '--host', dest='host', type=str,
                                 help='Search host in Shodan')

    argument_parser.add_argument('-s', '--save', dest='save', action="store_true",
                                 help='Save results')

    argument_parser.add_argument('-r', '--report', dest='report', type=str,
                                 help='Show a report with selected field/s')

    args = argument_parser.parse_args()

    cyberwatch = Shodan_cmd(Options.API)

    if args.info:
        if args.info.lower() == "services":
            cyberwatch.services(args.save)
        elif args.info.lower() == "protocols":
            cyberwatch.protocols(args.save)
        elif args.info.lower() == "api":
            cyberwatch.api_info()
        # else:
        #     print(SAMPLES)

    elif args.host:
        cyberwatch.host(args.host, args.save)

    # elif args.report:  # REPORT
    #     res = cyberwatch.search(args.search, args.page)
    #     print("\n [i] " + Colors.GREEN + "Total results: " + colors.ENDC + str(res['total']))
    #     shd.report(res, args.report, args.output)
    #
    # else:
    #     print(SAMPLES)

    # print(shodan.Shodan(Options.API).host('8.8.8.8'))


if __name__ == '__main__':
    main()
