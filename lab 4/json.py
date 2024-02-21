import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data['items']:
    dn = item['dn']
    description = item.get('descr', '')
    speed = item.get('speed', 'inherit')
    mtu = item.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))