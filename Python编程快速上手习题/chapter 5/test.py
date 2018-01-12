stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('Inventory:')
    items = 0
    for k,v in inventory.items():
        print(str(v), k, sep="\t")
        items += v
    print(items)


# def addToInventory(inventory, addedItems):
#     addingItem={}
#     for k,v in inventory.items():
#         if k in addedItems:
#             addingItem[k]=v+addedItems.count(k)
#         else :
#             addingItem[k]=v
#     for i in addedItems:
#         if i in addingItem.keys():
#             continue
#         else :
#             addingItem[i]=addedItems.count(i)
#     for k,v in addingItem.items():
#         inventory[k]=v
#     del addingItem
#     return inventory

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory



#displayInventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

