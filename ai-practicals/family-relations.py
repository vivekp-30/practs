# Basic predicates
def male(person):
    return person in ['John', 'Mike', 'David', 'Steve', 'Tom']

def female(person):
    return person in ['Mary', 'Sara', 'Kate', 'Anna', 'Linda']

def parent(parent, child):
    family_relations = {
        'John': ['Mike', 'Sara'],
        'Mary': ['Mike', 'Sara'],
        'David': ['Kate', 'Steve'],
        'Anna': ['Kate', 'Steve'],
        'Tom': ['Linda'],
        'Kate': ['Linda'],
    }
    return child in family_relations.get(parent, [])


# Derived family relations
def father(father, child):
    return male(father) and parent(father, child)

def mother(mother, child):
    return female(mother) and parent(mother, child)

def grandfather(grandfather, grandchild):
    for parent_person in ['Mike', 'Sara', 'Kate', 'Steve', 'Linda']:
        if father(grandfather, parent_person) and parent(parent_person, grandchild):
            return True
    return False

def grandmother(grandmother, grandchild):
    for parent_person in ['Mike', 'Sara', 'Kate', 'Steve', 'Linda']:
        if mother(grandmother, parent_person) and parent(parent_person, grandchild):
            return True
    return False

def brother(brother, sibling):
    for parent_person in ['John', 'David', 'Tom']:
        if male(brother) and parent(parent_person, brother) and parent(parent_person, sibling) and brother != sibling:
            return True
    return False

def sister(sister, sibling):
    for parent_person in ['Mary', 'Anna', 'Kate']:
        if female(sister) and parent(parent_person, sister) and parent(parent_person, sibling) and sister != sibling:
            return True
    return False

def uncle(uncle, nephew_niece):
    for parent_person in ['Mike', 'Sara', 'Kate', 'Steve', 'Linda']:
        if brother(uncle, parent_person) and parent(parent_person, nephew_niece):
            return True
    return False

def aunt(aunt, nephew_niece):
    for parent_person in ['Mike', 'Sara', 'Kate', 'Steve', 'Linda']:
        if sister(aunt, parent_person) and parent(parent_person, nephew_niece):
            return True
    return False

def nephew(nephew, uncle_aunt):
    return male(nephew) and (uncle(uncle_aunt, nephew) or aunt(uncle_aunt, nephew))

def niece(niece, uncle_aunt):
    return female(niece) and (uncle(uncle_aunt, niece) or aunt(uncle_aunt, niece))

def cousin(cousin1, cousin2):
    for parent1 in ['John', 'David', 'Tom']:
        for parent2 in ['Mary', 'Anna', 'Kate']:
            if parent(parent1, cousin1) and parent(parent2, cousin2) and parent1 != parent2:
                return True
    return False


# Test the family relations
print(f"Is John the father of Mike? {father('John', 'Mike')}")
print(f"Is Mary the mother of Sara? {mother('Mary', 'Sara')}")
print(f"Is John the grandfather of Linda? {grandfather('John', 'Linda')}")
print(f"Is Anna the grandmother of Linda? {grandmother('Anna', 'Linda')}")
print(f"Is Mike the brother of Sara? {brother('Mike', 'Sara')}")
print(f"Is Sara the sister of Mike? {sister('Sara', 'Mike')}")
print(f"Is David the uncle of Linda? {uncle('David', 'Linda')}")
print(f"Is Kate the aunt of Linda? {aunt('Kate', 'Linda')}")
print(f"Is Steve the nephew of Kate? {nephew('Steve', 'Kate')}")
print(f"Is Linda the niece of Tom? {niece('Linda', 'Tom')}")
print(f"Is Linda a cousin of Steve? {cousin('Linda', 'Steve')}")
