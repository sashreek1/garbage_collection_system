import urllib.request, json
import webbrowser
url=''

#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = "Your_api_key"

# set the required location inputs either 'name of the place' or 'lat,long'
origin= 'kolkata'
destination='mumbai'
waypoints=['delhi','rajasthan','goa','bihar']

    
#Building the URL for the request
nav_request = 'origin={}&destination={}&waypoints=optimize:true|{}|{}|{}|{}&key={}'.format(origin,destination,waypoints[0],waypoints[1],waypoints[2],waypoints[3],api_key)
request = endpoint + nav_request

#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()

#Loads response as JSON
directions = json.loads(response)
routes=directions["routes"]

# get the order for route planning
waypoint_order=routes[0]["waypoint_order"]

# url part  without optimisation
part1='https://www.google.co.in/maps/dir/'
part2=part1+'{}/{}/{}/{}/{}/{}/'.format(origin,waypoints[0],waypoints[1],waypoints[2],waypoints[3],destination)
webbrowser.open(part2)

# url part  with optimisation (using index values stored in waypoint_order)
part2=part1+'{}/{}/{}/{}/{}/{}/'.format(origin,waypoints[waypoint_order[0]],waypoints[waypoint_order[1]],waypoints[waypoint_order[2]],waypoints[waypoint_order[3]],destination)
webbrowser.open(part2)
