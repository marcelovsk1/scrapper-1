import json

data = [
    {
      "Go Montreal Events": {
      "webPage": "Montreal December Festival & Events",
      "pageURL": "http://www.go-montreal.com/attraction_events_dec.htm"
      }
    },

    {
      "title": "Birth of Planet Earth",
        "description": "How did Earth become a living planet as a result of the violent birth of our solar system?",
        "date": "ANNUALLY IN DECEMBER",
        "website": "https://espacepourlavie.ca/en/planetarium",
        "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/birth-of-planet-earth.jpg"
    },

    {
      "title": "Montreal Bach Festival",
      "description": "Revel in the works of this musical giant in some of the swankiest spots in the city.",
      "date": "ANNUALLY IN DECEMBER",
      "website": "https://festivalbachmontreal.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/montreal-bach-festival.jpg"
    }
]

json_data = json.dumps(data, indent=2)
print(json_data)
