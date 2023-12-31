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
      "date": "Annually in December",
      "website": "https://espacepourlavie.ca/en/planetarium",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/birth-of-planet-earth.jpg"
    },

    {
      "title": "Montreal Bach Festival",
      "description": "Revel in the works of this musical giant in some of the swankiest spots in the city.",
      "date": "Annually in December",
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

    {
      "title": "Illumi",
      "description": "Illumi is a magical, captivating and extraordinary nocturnal outdoor journey created from thousands of monumental light sculptures.",
      "date": "Annually in December",
      "website": "https://illumi.com/en/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/illumi.jpg"
    },

    {
      "title": "International Digital Art Biennial",
      "description": "This exhibition offers a reflection on the transition that we must accomplish in this post-pandemic era disrupted both geopolitically and climatically. By taking a look at our time while trying to anticipate the consequences of our past and future decisions, these artists are in a way pathfinders, messengers.",
      "date": "Annually in December",
      "website": "https://www.elektramontreal.ca/biennale2022",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/bian.jpg"
    },

    {
      "title": "LUMINOTHÉRAPIE",
      "description": "This winter, the heart of the city is the place to be, Luminothérapie is here to get you moving and enjoying the outdoors! With an all-new interactive experience on the Esplanade Tranquille skating rink, a series of six colourful installations on Sainte-Catherine St. extending to Phillips Square and original video projections, everyone is invited to take a break and have some fun.",
      "date": "Annually in December",
      "website": "https://www.quartierdesspectacles.com/en/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/luminotherapie.jpg"
    },

    {
      "title": "Noël sur l'Avenue",
      "description": "Make the most of the holiday season by participating in festive activities. On the program, the famous Marche de Noël aux flambeaux and the carriole contes et légendes. In addition, Noël dans le parc recreates a small village of yesteryear with many activities and concerts in the heart of the Avenue.",
      "date": "Annually in December",
      "website": "https://www.mont-royal.net/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/noel-sur-lavenue.jpg"
    },

    {
      "title": "Noël dans le Parc",
      "description": "The Christmas in the park festival welcomes Montrealers to experience the magic of Christmas village. Visitors will find free entertainment in the form of live music, poetry, bonfires, and many surprises.",
      "date": "Annually in December",
      "website": "https://festivalnoel.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/noel-dans-le-parc.jpg"
    },

    {
      "title": "Salon des métiers d'art du Québec (SMAQ)",
      "description": "The SMAQ is 11 days to discover nearly 190 outstanding exhibiting craftsmen offering exceptional objects that carry stories. Focus on this flagship event and its 66th edition which will definitely be festive, urban and eco-responsible.",
      "date": "Annually in December",
      "website": "https://festivalnoel.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/smaq.jpg"
    },

    {
      "title": "Odyssée",
      "description": "Downtown Montréal comes to life this holiday season with interactive installations and plenty to do and see in the heart of the city.",
      "date": "Annually in December",
      "website": "https://xpmtl.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/odyssee.jpg"
    },

     {
      "title": "Nutcracker",
      "description": "The traditional Christmas tale of Clara's journey to the Land of Snow and the Kingdom of Sweets, but given a fresh appeal with multimedia projections. See the magic unfold as over 80 young dancers join 40 members of the company's corps de ballet on stage.",
      "date": "Annually in December",
      "website": "https://grandsballets.com/en/performances/detail/nutcracker/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/nutcracker.jpg"
    },

    {
      "title": "Merry Montréal",
      "description": "Experience the festivities of the holiday season in a unique and magical setting filled with beautiful attractions and a multitude of restaurants, shops, and specialty boutiques.",
      "date": "Annually in December",
      "website": "https://montrealenfetes.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/merry-montreal.jpg"
    },

    {
      "title": "New Year's Eve Party",
      "description": "Experience the festivities of the holiday season in a unique and magical setting filled with beautiful attractions and a multitude of restaurants, shops, and specialty boutiques.",
      "date": "Annually in December",
      "website": "",
      "imageURL": ""
    },

     {
      "title": "Merry Montréal",
      "description": "Experience the festivities of the holiday season in a unique and magical setting filled with beautiful attractions and a multitude of restaurants, shops, and specialty boutiques.",
      "date": "Annually in December",
      "website": "https://montrealenfetes.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/merry-montreal.jpg"
    },

     {
      "title": "",
      "description": "",
      "date": "Annually in December",
      "website": "",
      "imageURL": ""
    },

    {
      "title": "New Year's Eve Party",
      "description": "Get down and warm yourself up with the whole family at the hottest party of the season! At 7 p.m., the Old Port and Place Jacques-Cartier will come alive with Montreal’s biggest New Year’s Eve party. At the stroke of midnight, marvel at the fireworks and dance the night away until 2 AM to the sounds of our DJ.",
      "date": "Annually in December",
      "website": "https://montrealenfetes.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/new-years-eve-party.jpg"
    },

    {
      "title": "Nutcracker Market",
      "description": "Annually at the end of November - The Nutcracker Market offers values such as originality and rarity as far as the selection of merchants, products and services, with a magical setting inspiring a sense of wonder so typical of the holiday spirit. Exhibitor categories include, among others, jewellery, dinnerware, local products, interior and outdoor décor items, body-care products and toys.",
      "date": "Annually in December",
      "website": "https://www.marchecassenoisette.com/en/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/nutcracker-market.jpg"
    },

    {
      "title": "Salon du jeu de société de Montréal",
      "description": "The Salon du jeu de société de Montréal is a board game convention for beginners and experienced gamers. Try the latest games releases, talk to designers and play their prototypes, include new games to your collection and much more! The SJSM is an event to discover the amazing world of board games with your family or friends!",
      "date": "Annually in December",
      "website": "",
      "imageURL": ""
    },

    {
      "title": "",
      "description": "",
      "date": "Annually in December",
      "website": "https://www.salonjdsmtl.ca/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/salon-du-jeu-de-societe.jpg"
    },

    {
      "title": "Who Is the Real Santa Claus?",
      "description": "December is the time to meet Santa Clauses from around the world, accompanied by our interpreter-guides. During the month of December, young and old alike are invited to come see Babushka, Melchior, Black Peter and Santa Claus.",
      "date": "Annually in December",
      "website": "https://pacmusee.qc.ca/en/calendar/event/who-is-the-real-santa-claus/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/who-is-the-real-santa-claus.jpg"
    },

    {
      "title": "Fire on Ice",
      "description": "The Holidays start with a bang when these musical fireworks light up the sky over the the Old Port. Magical, spectacular fireworks -a unique, innovative show every time- burst over the St. Lawrence to create a thoroughly original urban winter experience.",
      "date": "Annttps://www.oldportofmontreal.com/",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/fire-on-ice.jpg"
    },

    {
      "title": "Skating Events at the Old Port",
      "description": "Being festive is the Old Port’s guiding principle, and no efforts are spared to live up to it. Each season brings new and exclusive events, festivals, shows, celebrations, and more. With marvellous music and glorious gastronomy to cater to all tastes and cultures, you’ll find here a cordial atmosphere to delight and nourish, and so much more.",
      "date": "Annually in December",
      "website": "https://www.oldportofmontreal.com/skating-events",
      "imageURL": "http://www.go-montreal.com/images/attractions/listings/festivals-events/dj-on-ice.jpg"
    },

]

json_data = json.dumps(data, indent=2)
print(json_data)
