# incomplete on purpose - check `final` branch
import datetime
import random
import sys

# fix local imports
# import collection_create
# import db_client



name_choices =  ["Big", "Goat", "Chicken", "Tasty", "Salty", "Fire", "Forest", "Moon", "State", "Texas", "Bear", "California"]
cuisine_choices = ["Pizza", "Bar Food", "Fast Food", "Pasta","Tacos", "Sushi", "Vegetarian", "Steak", "Burgers"]


def get_random_name():
    _name_start = random.choice(name_choices)
    _name_end = random.choice(name_choices)
    return f"{_name_start} {_name_end}"

def get_random_cuisine():
    selected_cuisine = random.choice(cuisine_choices)
    return selected_cuisine
  
def get_random_rating(skew_low=True):
    part_a = list([random.randint(1, 3) for i in range(10)])
    part_b = list([random.randint(3, 4) for i in range(10)])
    if not skew_low:
      part_c = list([random.randint(4, 5) for i in range(25)])
    else:
      part_c = list([random.randint(4, 5) for i in range(5)])
    _ratings =  part_a + part_b +  part_c
    return random.choice(_ratings)

def get_random_timestamp():
    now = datetime.datetime.now()
    delta = now - datetime.timedelta(days=random.randint(0, 5_000), minutes=random.randint(0, 60), seconds=random.randint(0, 60))
    return delta

# create get_or_generate_collection function

def run(collection, iterations=50, skew_results=True):
    completed = 0
    for n in range(0, iterations):
        timestamp = get_random_timestamp()
        name = get_random_name()
        cuisine = get_random_cuisine()
        rating = get_random_rating(skew_low=True)
        if skew_results:
          if cuisine.lower() == "mexican":
              rating = random.choice([4, 5])
          elif cuisine.lower() == "bar food":
              rating = random.choice([1, 2])
          elif cuisine.lower() == "sushi":
              rating = get_random_rating(skew_low=False)              
        data = {
          "metadata": {
            "name": name,
            "cuisine": cuisine
          },
          "rating": rating,
          "timestamp": timestamp
        }
        # send to database
        print(data)
        if n > 0 and n % 1000 == 0:
            print(f"Finished {n} of {iterations} items.")
    print(f"Added {completed} items.")


if __name__ == "__main__":
    iterations = 50
    name="rating_over_time"
    try:
        iterations = int(sys.argv[1])
    except:
        pass
    try:
        name= sys.argv[2]
    except:
        pass
    collection = None
    run(collection, iterations=iterations)