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
    },

    {
      "title": "Holidays on the Point",
      "description": "Come to Place Royale in the heart of Old Montreal to set your sights on our seasonal decor that conjures up the coziness of ski chalets while paying tribute to winter sports. Take a break from the holiday hubbub and get comfy on our stools surrounded by light-adorned trees. The only thing missing may be a mug of hot chocolate!",
      "date": "Annually in December",
      "website": "https://pacmusee.qc.ca/en/calendar/collection/holidays-on-the-point-2022/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/holidays-on-the-point.jpg"
    },

    {
      "title": "Holiday Market - Collectif Créatif Montréal",
      "description": "The perfect occasion to shop local, support your makers and get one of a kind presents for this Holiday season!",
      "date": "Annually in December",
      "website": "https://www.collectifcreatifmtl.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/collectif-creatif.jpg"
    },

    {
      "title": "Jean-Talon Christmas Market",
      "description": "Merchants of the Jean-Talon Market suggests relaxation for a warm holiday season with the family.",
      "date": "Annually in December",
      "website": "https://noelmontreal.ca/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/jean-talon-christmas-market.jpg"
    },

]

json_data = json.dumps(data, indent=2)
print(json_data)
