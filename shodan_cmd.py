import shodan

from options import Options
from colors import Colors
from file import File


class Shodan_cmd(object):
    def __init__(self, API_KEY):
        self.api = shodan.Shodan(API_KEY)

    def host(self, ip, is_save):
        try:
            datas = self.api.host(ip)
            if is_save is False:
                print(Options.LIST_TITLE + Colors.INFO + "IP: " + Colors.ENDC + datas.get('ip_str'))
                print(Options.LIST_SUB + Colors.INFO + "Country: " + Colors.ENDC + datas.get('country_name', 'Unknown'))
                print(Options.LIST_SUB + Colors.INFO + "City: " + Colors.ENDC + str(datas.get('city', 'Unknown')))
                print(Options.LIST_SUB + Colors.INFO + "Latitude: " + Colors.ENDC + str(datas.get('latitude')))
                print(Options.LIST_SUB + Colors.INFO + "Longitude: " + Colors.ENDC + str(datas.get('longitude')))
                print(Options.LIST_SUB + Colors.INFO + "Hostnames: " + Colors.ENDC + str(datas.get('hostnames')))
                for data in datas['data']:
                    print()
                    print(Options.LIST_SUB + Colors.INFO + "Port: " + Colors.ENDC + str(data['port']))
                    print(Options.LIST_SUB + Colors.INFO + "Service: " + Colors.ENDC + data['_shodan']['module'])
                    print(Options.LIST_SUB + Colors.INFO + "Protocol: " + Colors.ENDC + data['transport'])
            else:
                content = ""
                content += "IP: " + datas.get('ip_str')
                content += "\nCountry: " + datas.get('country_name', 'Unknown')
                content += "\nCity: " + str(datas.get('city', 'Unknown'))
                content += "\nLatitude: " + str(datas.get('latitude'))
                content += "\nLongitude: " + str(datas.get('longitude'))
                content += "\nHostnames: " + str(datas.get('hostnames'))
                for data in datas['data']:
                    content += "\n\nPort: " + str(data['port'])
                    content += "\nService: " + data['_shodan']['module']
                    content += "\nProtocol: " + data['transport']

                File(content).save()

        except Exception as e:
            print(Colors.FAIL + Colors.BOLD + "\n" + Options.LIST_ERROR + "ERROR: " + Colors.ENDC + str(e) + "\n")


def services(self, sfile):
    result = self.api.services()
    if sfile is None:
        for x, y in result.items():
            print(" [-] " + Colors.GREEN + x + ": " + Colors.ENDC + y)
    else:
        with open(sfile, 'w') as f:
            for x, y in result.items():
                f.write("\n [-] %s: %s" % (x, y))
        print(" [i] " + Colors.GREEN + "File saved!!\n" + Colors.ENDC)


def protocols(self, sfile):
    result = self.api.protocols()
    if sfile is None:
        for x, y in result.items():
            print(" [-] " + Colors.GREEN + x + ": " + Colors.ENDC + y)
    else:
        with open(sfile, 'w') as f:
            for x, y in result.items():
                f.write("\n [-] %s: %s" % (x, y))
        print(" [i] " + Colors.GREEN + "File saved!!\n" + Colors.ENDC)


def api_info(self):
    result = self.api.info()
    print(Options.LIST_INFO + Colors.INFO + "API Information:" + Colors.ENDC)
    for x, y in result.items():
        print(Options.LIST_SUB + Colors.GREEN + str(x).capitalize() + ": " + Colors.ENDC + str(y))

# def report(self, datas, fields, sfile):
#     location = ['longitude', 'latitude', 'country_name', 'city']
#     if sfile is None:
#         for data in datas['data']:
#             if ',' in fields:
#                 list_fields = fields.split(',')
#                 for field in list_fields:
#                     if field in location:
#                         print(str(data['location'][field])),
#                     else:
#                         print(str(data.get(field))),
#                 print("\n")
#             else:
#                 if fields in location:
#                     print(str(data['location'][fields]))
#                 else:
#                     print(str(data.get(fields)))
#     else:
#         with open(sfile, 'w') as f:
#             for r in res['matches']:
#                 if "," in field:
#                     lfield = field.split(",")
#                     for fl in lfield:
#                         if fl in loc:
#                             f.write(str(r['location'][fl]))
#                             f.write(",")
#                         else:
#                             f.write(str(r.get(fl)))
#                             f.write(",")
#                     f.write("\n")
#                 else:
#                     if field in loc:
#                         f.write("\n " + str(r['location'][field]))
#                     else:
#                         f.write("\n " + str(r.get(field)))
#         print("\n [i] " + Colors.GREEN + "File saved!!\n" + Colors.ENDC)
