import requests


def get_json():
    url = "http://api.open-notify.org/iss-now.json"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        return RuntimeError("Unable to access Open Notify API")


# print(get_coordinates())

def get_coordinates():
    ts_la_lo = {}

    resp = get_json()

    if resp['message'] == "success":
        ts_la_lo["timestamp"] = resp["timestamp"]
        ts_la_lo["latitude"] = float(resp["iss_position"]["latitude"])
        ts_la_lo["longitude"] = float(resp["iss_position"]["longitude"])

    else:
        return RuntimeError("Unable to access Open Notify API")

    return ts_la_lo

# def distance_between_coordinate(geoloc1, geoloc2, R=6367):
#     """
#     Compute distance between geographic coordinate pairs in kilometers.
#
#     Parameters
#     ----------
#     geoloc1: tuple or list
#         (lat1, lon1) of first geolocation.
#     geoloc2: tuple or list
#         (lat2, lon2) of second geolocation.
#     R: float
#         Radius of the Earth (est).
#
#     Returns
#     -------
#     float
#         Distance in kilometers between geoloc1 and geoloc2.
#     """
#     rlat1, rlon1 = [i * math.pi / 180 for i in geoloc1]
#     rlat2, rlon2 = [i * math.pi / 180 for i in geoloc2]
#     drlat, drlon = (rlat2 - rlat1), (rlon2 - rlon1)
#
#     init = (math.sin(drlat / 2.)) ** 2 + (math.cos(rlat1)) * \
#            (math.cos(rlat2)) * (math.sin(drlon / 2.)) ** 2
#     return 2.0 * R * math.asin(min(1., math.sqrt(init)))
#
#
# def get_avg_speed(dloc1, dloc2):
#     """
#     Compute speed of ISS relative to Earth's surface using
#     a pair of coordinates.
#
#     Parameters
#     ----------
#     dloc1: dict
#         Dictionary with keys "latitude", "longitude" "timestamp"
#         associated with the first position.
#     dloc2: dict
#         Dictionary with keys "latitude", "longitude" "timestamp"
#         associated with the second position.
#
#     Returns
#     -------
#     float
#         Average speed of the International Space Station relative to the Earth.
#     """
#     ts1 = datetime.datetime.fromtimestamp(dloc1['timestamp'])
#     ts2 = datetime.datetime.fromtimestamp(dloc2['timestamp'])
#     secs = abs((ts2 - ts1).total_seconds())
#     loc1 = (dloc1["latitude"], dloc1["longitude"])
#     loc2 = (dloc2["latitude"], dloc2["longitude"])
#     dist = distance_between_coordinate(geoloc1=loc1, geoloc2=loc2)
#     vinit = (dist / secs)  # kilometers per second
#     return vinit * 3600
#
