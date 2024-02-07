from fastapi import FastAPI

app = FastAPI()

data = [
  {
    "name": "John Doe",
    "occupation": "Software Engineer",
    "address": "123 Main St"
  },
  {
    "name": "Jane Smith",
    "occupation": "Data Scientist",
    "address": "456 Elm St"
  },
  {
    "name": "Michael Johnson",
    "occupation": "Web Developer",
    "address": "789 Oak St"
  },
  {
    "name": "Emily Brown",
    "occupation": "UX Designer",
    "address": "101 Maple Ave"
  },
  {
    "name": "David Lee",
    "occupation": "Product Manager",
    "address": "202 Pine St"
  },
  {
    "name": "Sarah Taylor",
    "occupation": "Marketing Specialist",
    "address": "303 Cedar St"
  },
  {
    "name": "Chris Evans",
    "occupation": "Graphic Designer",
    "address": "404 Walnut St"
  },
  {
    "name": "Jessica White",
    "occupation": "Financial Analyst",
    "address": "505 Birch St"
  },
  {
    "name": "Matthew Miller",
    "occupation": "Systems Administrator",
    "address": "606 Spruce St"
  },
  {
    "name": "Amanda Martinez",
    "occupation": "HR Coordinator",
    "address": "707 Chestnut St"
  }
]


@app.get("/name")

def get_names():
    names=[]
    for datum in data:
        names.append(datum["name"])
    return names

@app.get("/occupation")
def get_occu():
    occu=[]
    for datum2 in data:
        occu.append(datum2["occupation"])
    return occu


@app.get("/address")
def get_add():
    add=[]
    for datum2 in data:
        add.append(datum2["address"])
    return add


# post request is to add new data 
# and a put or patch request is to add new data
    
  


