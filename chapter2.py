# exercise 2.1, 2.2
for line in open("emperors.txt"):
    line = line.split(',')
    name = line[0]
    print(f"-----{name}-----")
    birth_year = int(line[1])
    death_year = int(line[2])
    start_of_reign = int(line[3])
    end_of_reign = int(line[4])
    life = death_year - birth_year
    power = end_of_reign - start_of_reign
    print(f"Reign length = {power}")
    print(f"Lifespan = {life}")
    print(f"Emperor's life in power = {power/life * 100:.2f}%")

