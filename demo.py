

with open("cafe-data.csv", "r") as cafe:
    data = cafe.readlines()
    for line in data:
        
        with open("example.csv", 'a') as ex:
            ex.write(line)