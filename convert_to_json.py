import json

data = [
  {
     "title": "Birth of Planet Earth",
      "description": "How did Earth become a living planet as a result of the violent birth of our solar system?",
      "website": "Website"
  },

  {
    "title": "Montreal Bach Festival",
     "description": "Revel in the works of this musical giant in some of the swankiest spots in the city.",
     "website": "Website"
  }
]

json_data = json.dumps(data, indent=2)
print(json_data)
