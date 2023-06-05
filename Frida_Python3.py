paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]

#Modifying paintings to include dates
paintings = list(zip(paintings, dates))

paintings += [('The Broken Column', 1944), ('The Wounded Deer', 1946), ('Me and My Doll', 1937)]
#print(len(paintings))

#Creating a number for audio tour
audio_tour_number = [num for num in range(1, len(paintings)+1)]

#Final list including paintings, dates and audio list
master_list = list(zip(paintings, audio_tour_number))
print(master_list)