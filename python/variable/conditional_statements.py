units = 250
if units <= 100:
    print("Electricity Bill: ₹500")
elif units <= 200:
    print("Electricity Bill: ₹1000")
else:
    print("Electricity Bill: ₹1500")


is_wifi_connected = False
is_mobile_data_on = True
if is_wifi_connected:
    print("Connected through Wi-Fi")
elif is_mobile_data_on:
    print("Connected through Mobile Data")
else:
    print("No Internet Connection")