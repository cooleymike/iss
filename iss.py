import requests, json, turtle

iss = turtle.Turtle()

def setup(window):
    

    window.setup(1000,500)
    window.bgpic(r"C:/LTC/CH10/earth.gif")
    window.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape(r"C:/LTC/CH10/iss.gif")
    iss.shape(r"C:/LTC/CH10/iss.gif")

def move_iss(lat,long):
   

    iss.penup()
    iss.goto(long,lat)
    iss.pendown()


def track_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    if(response.status_code == 200):
        response.dictionary = json.loads(response.text)
        position = response.dictionary['iss_position']
        lat = float(position['latitude'])
        long = float(position['longitude'])
        move_iss(lat,long)
    else:
        print('Houston, we have a problem', response.status_code)
    widget = turtle.getcanvas()
    widget.after(500,track_iss)

def main():
   
    screen = turtle.Screen()
    setup(screen)
    track_iss()

if __name__ == "__main__":
    main()
    turtle.mainloop()
