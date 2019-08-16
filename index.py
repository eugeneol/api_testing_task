import requests

url = "https://api.nasa.gov/neo/rest/v1/feed?api_key=jjTg5nDgDLFhdckWGzOnqs6D8uT4L0FkZmSrcvFd"

r = requests.get(url)
re = r.json()

res = []
count_asteroids = 0
is_potentially_hazardous_asteroid_counter = 0
diameter_counter = 0
near_earth_objects = re['near_earth_objects'].values()
for earth_object in near_earth_objects:
    for obj in earth_object:
        res.append(obj['name'])
        count_asteroids += 1
        if obj['is_potentially_hazardous_asteroid']:
            is_potentially_hazardous_asteroid_counter += 1
            if obj['estimated_diameter']['kilometers']['estimated_diameter_max'] >= 1:
                diameter_counter += 1

print("1) List of asteroids:" + str(res))
print("2) Asteroids counted by me: " + str(count_asteroids) + " Element count: " + str(re["element_count"]))
print("3) Potentially hazardous asteroids: " + str(is_potentially_hazardous_asteroid_counter))
print("4) Potentially hazardous asteroids with diameter +1km: " + str(diameter_counter))
