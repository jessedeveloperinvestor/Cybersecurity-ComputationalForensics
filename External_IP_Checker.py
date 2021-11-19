from urllib.request import urlopen
url='https://ipinfo.io/json'
answer=urlopen(url)
data=json.load(answer)
ip=data['ip']
org=data['org']
cit=data['city']
country=data['country']
region=data['region']
print('Details of External IP:\n')
print('IP: {4}\nRegion: {1}\nCountry: {2}\nCity: {3} \nOrg.: {0}'.format(org,region,country,cit,ip))