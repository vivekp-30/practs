# Define predicates
def is_batsman(person):
    return person == "Sachin"

def is_cricketer(person):
    # If a person is a batsman, they are a cricketer
    if is_batsman(person):
        return True
    return False

# Define the entities
person = "Sachin"

# Applying logic
if is_cricketer(person):
    print(f"{person} is a Cricketer")
else:
    print(f"{person} is not a Cricketer")
