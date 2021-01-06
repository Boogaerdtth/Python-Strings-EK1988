# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
#1
gullit = 'Ruud Gullit'
van_basten = 'Marco van Basten'
#2
goal_0 = 35
goal_1 = 54

#3
scorers = gullit, goal_0, van_basten, goal_1

#4
report = f'{gullit} scored in the {goal_0}th minute, \n {van_basten} scored in the {goal_1}th minute'
print(report)

# Part 2
#1
player = 'Oleksij Mychajlytsjenko'
#2
first_name = player[0:player.find(" ")]
print(first_name)
#3
last_name_len = len(player[player.find(" ")+1:])
print(last_name_len)
space_last_name = last_name_len != (" ")
print(space_last_name)
#4
name_short = f"{player[0]}. {player[8:]}"
print(name_short)
#5
chant = (first_name + "!!! ") * (len(player[0:7])) #(len(first_name))
print(chant)
#6
good_chant = chant != (" ")
print(good_chant)
