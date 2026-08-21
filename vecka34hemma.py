
device_1 = "SW-Emil-Ek-1"
model_1 = "WS-1991"
role_1 = "Switch, access"

device_2 = "R-Emil-Ek-1"
model_2 = "CISCO2960"
role_2 = "Router, lager 3"

device_3 = "SW-Emil-Ek-3"
model_3 = "EE1991"
role_3 = "Switch, core"

device_4 = "AP-01"
model_4 = "Cisco2702"
role_4 = "Kontor"

print ("UTRUSTNINGSLISTA")
print ("-" * 52)


print (f"{device_1:<16}{model_1:<20}{role_1}")
print (f"{device_2:<16}{model_2:<20}{role_2}")
print (f"{device_3:<16}{model_3:<20}{role_3}")
print (f"{device_4:<16}{model_4:<20}{role_4}")

print ("-" * 52)
print("Antal enheter: 4")
