import shodan

from options import Options
from colors import Colors
from file import File


class Shodan_cmd(object):
    """
    The Shodan_cmd class is used for all connection operations to Shodan API.
    """

    def __init__(self, API_KEY):
        self.api = shodan.Shodan(API_KEY)

    def host(self, ip, is_printed, is_saved, is_compared):
        """
        Get all available information from an IP and display/save them.
        :param ip: ip whose information we want to retrieve
        :param is_saved: determines whether the function saves the collected data or just displays it in the console
        """
        try:
            datas = self.api.host(ip)

            if is_printed:
                print(Options.LIST_TITLE + Colors.INFO + "IP: " + Colors.ENDC + datas.get('ip_str'))
                print(Options.LIST_SUB + Colors.INFO + "Country: " + Colors.ENDC + datas.get('country_name', 'Unknown'))
                print(Options.LIST_SUB + Colors.INFO + "City: " + Colors.ENDC + str(datas.get('city', 'Unknown')))
                print(Options.LIST_SUB + Colors.INFO + "Latitude: " + Colors.ENDC + str(datas.get('latitude')))
                print(Options.LIST_SUB + Colors.INFO + "Longitude: " + Colors.ENDC + str(datas.get('longitude')))
                print(Options.LIST_SUB + Colors.INFO + "Hostnames: " + Colors.ENDC + str(datas.get('hostnames')))
                for data in datas['data']:
                    print()
                    print(Options.LIST_SUB + Colors.INFO + "Port: " + Colors.ENDC + str(data.get('port')))
                    print(
                        Options.LIST_SUB + Colors.INFO + "Service: " + Colors.ENDC + data.get('_shodan').get('module'))
                    print(Options.LIST_SUB + Colors.INFO + "Protocol: " + Colors.ENDC + data.get('transport'))
                print()

            if is_saved or is_compared:
                content = {}
                ports = []
                services = []
                transports = []
                content['ip_str'] = str(datas.get('ip_str'))
                content['country_name'] = str(datas.get('country_name', 'Unknown'))
                content['city'] = str(datas.get('city', 'Unknown'))
                content['latitude'] = str(datas.get('latitude'))
                content['longitude'] = str(datas.get('longitude'))
                content['hostnames'] = str(datas.get('hostnames'))

                for data in datas['data']:
                    ports.append(str(data.get('port')))
                    services.append(str(data.get('_shodan').get('module')))
                    transports.append(str(data.get('transport')))

                content['ports'] = ports
                content['services'] = services
                content['transports'] = transports

                if is_saved:
                    File(content).save()
                else:
                    File(content).compare()

        except Exception as e:
            print(Colors.FAIL + Colors.BOLD + "\n" + Options.LIST_ERROR + "ERROR: " + Colors.ENDC + str(e) + "\n")

    def services(self):
        """
        Print a list of services that Shodan crawls.
        """
        services = self.api.services()

        for port, service in services.items():
            print(Options.LIST_SUB + Colors.GREEN + port + ": " + Colors.ENDC + service)

    def protocols(self):
        """
        Print a list of protocols that the Shodan on-demand scanning API supports.
        """
        protocols = self.api.protocols()

        for title, description in protocols.items():
            print(Options.LIST_SUB + Colors.GREEN + title + ": " + Colors.ENDC + description)

    def api_info(self):
        """
        Print API information.
        """
        infos = self.api.info()

        print(Options.LIST_INFO + Colors.INFO + "API Information:" + Colors.ENDC)

        for title, value in infos.items():
            print(Options.LIST_SUB + Colors.GREEN + str(title).capitalize() + ": " + Colors.ENDC + str(value))
