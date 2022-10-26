team = ["Miami", "Boston", "Milwauke", "Philadelphia", "Toronto", "Chikago", "Brooklin", "Atlant"]

print (team[0], "plays", team[-1])
first = input("Who won? ")
print (team[1], "plays", team[-2])
second = input("Who won? ")
print (team[2], "plays", team[-3])
third = input("Who won? ")
print (team[3], "plays", team[-4])
fourth = input("Who won? ")
print("The first round winners are: ", first, second, third, "and", fourth)

teams = [first, second, third, fourth]
print("The semi-finals are")
print(teams[0], "plays", teams[-1])
first1 = input("Who won? ")
print(teams[1], "plays", teams[-2])
second2 = input("Who won? ")
print("The results for semi-finals are: ", first1, "and", second2)

teamss = [first1, "and", second2]
print("The finals are: ")
print(teams[0], "plays", teamss[-1])
finals = input("Who won? ")
print("The winner of the NBA is ", finals)