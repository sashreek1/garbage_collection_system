import urllib.request, json
import webbrowser


def opt_route(origin, waypoints, destination):

    #Google MapsDdirections API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    # please set your api_key below
    api_key = "api_key"

    #adding mode of routing
    mode='driving'
       
    #Building the URL for the request
    nav_request = 'origin={}&destination={}&waypoints=optimize:true|{}|{}|{}|{}&mode={}&key={}'.format(origin,destination,waypoints[0],waypoints[1],waypoints[2],waypoints[3],mode,api_key)
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

    # url part  with optimisation (using index values stored in waypoint_order)
    part2='{}/{}/{}/{}/{}/{}/'.format(origin,waypoints[waypoint_order[0]],waypoints[waypoint_order[1]],waypoints[waypoint_order[2]],waypoints[waypoint_order[3]],destination)
    url=part1+part2

    #webbrowser.open(url)

    return url


#url=opt_route('-28.5588,29.77523', ['-29.778758,31.043515','-28.757862,31.902001','-27.769209,30.79068899999999','-30.154131,30.058675'], '-29.595413,30.3799223')
