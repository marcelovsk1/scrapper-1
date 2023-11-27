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
    },
    {
      "title": "Le Grand Marché de Noël de Montréal",
      "description": "Inspired by the charming Christmas traditions from around the world, this event offers a Christmas market and village with many free outdoor activities. Imagine a fairy-tale setting in the heart of Quartier Latin in downtown Montreal, bustling with life day and night, traditional log cabins, illuminated christmas trees, tasty delights and much more.",
      "date": "Annually in December",
      "website": "https://noelmontreal.ca/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/le-grand-marche-de-noel-de-montreal.jpg"
    },

    {
     "title": "Montreal's Christmas Village",
      "description": "Take part in the cultural, festive and culinary activities that will take place in Montreal during the holiday season and celebrate in total safety, the delicious northern charm of the city.",
      "date": "Annually in December",
      "website": "https://noelmontreal.ca/en/montreal-christmas-markets/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/christmas-village.jpg"

    },

    {
      "title": "Railway Christmas",
      "description": "Exporail, the Canadian Railway Museum will transport its visitors into the Magic of Christmas. Many vehicles will be decorated and illuminated in the Grand Gallery, activities will be offered and Santa will meet the visitors! Railway Christmas is a must-see event for the whole family!",
      "date": "Annually in December",
      "website": "https://exporail.org/en/activities/railway-christmas/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/railway-christmas.jpg"
    }
]

json_data = json.dumps(data, indent=2)
print(json_data)
