
voted = {}

def check_voter(name):
    if voted.get(name):
        print ("refuse vote")
    else:
        voted[name] = True
        print ("allow voting")

check_voter("Shola")
check_voter("Shola")
check_voter("Baxton")