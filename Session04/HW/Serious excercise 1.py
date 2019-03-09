inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# # add key "pocket"
# inventory['pocket'] = ''
# print(inventory)

# # set the value of "pocket"
# pocket_list = ["seashell", "strange berry", "lint"]
# inventory['pocket'] = ["seashell", "strange berry", "lint"]
# print(inventory)

# Then .remove('dagger')
inventory["backpack"].remove('dagger')
print(inventory)

# Add 50 to the number
inventory['gold'] += 50
print(inventory)