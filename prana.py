latitude_mx = []
longitude_mx = []


def plottr():
    dloc1 = {'timestamp': 1643317244, 'latitude': 31.7377, 'longitude': -101.5348}
    dloc2 = {'timestamp': 1643317259, 'latitude': 32.4222, 'longitude': -100.7308}

    # latitude = float(str([value for key, value in dloc1.items() if key == "latitude"])[1:-1])
    # latitude_mx.append(latitude)

    latitude = [value for key, value in dloc1.items() if key != "timestamp"]
    latitude_mx.append(latitude[0])
    longitude_mx.append(latitude[1])

    longtitude =[value for key, value in dloc2.items() if key != "timestamp"]
    latitude_mx.append(longtitude[0])
    longitude_mx.append(longtitude[1])



plottr()

print(longitude_mx)
print(latitude_mx)
