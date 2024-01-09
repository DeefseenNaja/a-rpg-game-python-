import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 80
HPMAX = 80
minATK = 1
maxATK = 5
EVD = 5
pot = 1
elix = 0
gold = 50
x = 0
y = 0
equip = []

        #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
       ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],    # y = 1
       ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
       ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
       ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mayor": {
        "t": "MAYOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

e_list = ["Goblin", "Orc", "GreenSlime", "BlueSlime", "RedSlime", "GiantSlime", "Wolf"]

mobs = {
    "Goblin": {
        "hp": 30,
        "atmin": 2,
        "atmax": 4,
        "go": random.randint(10,20)
    },
    "Orc": {
        "hp": 80,
        "atmin": 3,
        "atmax": 7,
        "go": random.randint(30,60)
    },
    "Wolf": {
        "hp": 50,
        "atmin": 2,
        "atmax": 5,
        "go": random.randint(15,25)
    },
    "GreenSlime": {
        "hp": 20,
        "atmin": 1,
        "atmax": 3,
        "go": random.randint(1,10)
    },
    "BlueSlime": {
        "hp": 20,
        "atmin": 1,
        "atmax": 3,
        "go": random.randint(1,10)
    },
    "RedSlime": {
        "hp": 20,
        "atmin": 1,
        "atmax": 3,
        "go": random.randint(1,10)
    },
    "GiantSlime": {
        "hp": 25,
        "atmin": 1,
        "atmax": 3,
        "go": random.randint(5,15)
    },
    "Dragon": {
        "hp": 600,
        "atmin": 5,
        "atmax": 12,
        "go": random.randint(45,100)
    }
}
 

def clear():
    os.system("cls")


def draw():
    print("-------------------------")


def save():
    list = [
        name,
        str(HP),
        str(minATK),
        str(maxATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    file = open("load.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(name + "'s HP refilled to " + str(HP) + "!")


def battle():
    global fight, play, run, HP, pot, elix, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atkmin = mobs[enemy]["atmin"]
    atkmax = mobs[enemy]["atmax"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        print(enemy + "'s HP: " + str(hp) + "/" + str(hpmax))
        print(name + "'s HP: " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        print("4 - FLEE")
        draw()

        choice = input("# ")

        if choice == "1":
            dmg = random.randint(minATK,maxATK)
            hp -= dmg 
            print(name + " dealt " + str(dmg) + " damage to the " + enemy + ".")
     
            if hp > 0:
                evade_chance = random.randint(1,100)
                if evade_chance <= EVD:
                    print("You successfully evaded the attack!")
                else:
                    atk = random.randint(atkmin,atkmax)
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")        
        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                atk = random.randint(atkmin,atkmax)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                atk = random.randint(atkmin,atkmax)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            else:
                print("No elixirs!")
            input("> ")

        elif choice == "4":
            flee_chance = random.randint(1, 100)
            if flee_chance <= 35:
                print("You successfully fled the battle!")
                fight = False
            else:
                atk = random.randint(atkmin,atkmax)
                HP -= atk
                print("You failed to flee the battle.")
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
        input("> ")      
        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("Congratulations, you've finished the game!")
                boss = False
                play = False
                run = False
            input("> ")
            clear()


def shop():
    global buy, gold, pot, elix, minATK, maxATK

    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("ATK: " + str(minATK) + " - " + str(maxATK))
        draw()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - WEAPON ")
        print("4 - LEAVE ")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                if pot >= 5:
                    print("Potion already full!")
                else: 
                    pot += 1
                    gold -= 5
                    print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 1:
               if elix >= 1:
                   print("Elixer already full!")
               else:
                   elix += 1
                   gold -= 8
                   print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            clear()
            draw()
            print("Choose the weapon that you desire!")
            draw()
            print("1 - Iron Sword (ATK 3 - 10) - 200 gold\n2 - Iron Claymore (ATK 3 - 15) - 350 gold\n3 - Mana Blade (ATK 5 - 18) - 600 gold\n4 - Dragon Slayer Spear (ATK 3 - 50) - 1000 gold\n5 - Leave")
            draw()
            
            wep = input("# ")
            
            if wep == "1":
                if "Iron Sword" in equip:
                    print("You've already bought this!")
                else:    
                    if gold >= 200:
                        minATK = 3
                        maxATK = 10
                        gold -= 200
                        equip.append("Iron Sword")
                        print("You've bought an Iron Sword!") 
                    else:
                        print("Not enough gold!")
                input("> ")  
            elif wep == "2":
                if "Iron Claymore" in equip:
                    print("You've already bought this!")     
                else:    
                    if gold >= 350:
                        minATK = 3
                        maxATK = 15
                        gold -= 350
                        equip.append("Iron Claymore")
                        print("You've bought an Iron Claymore!")
                    else:
                        print("Not enough gold!")  
                input("> ")          
            elif wep == "3":
                if "Mana Blade" in equip:
                    print("You've already bought this!")
                else:    
                    if gold >= 600:
                        minATK = 5
                        maxATK = 18
                        gold -= 600
                        equip.append("Mana Blade")
                        print("You've bought a Mana Blade!")
                    else:
                        print("Not enough gold!")
                input("> ") 
            elif wep == "4":
                if "Dragon Slayer Spear" in equip:
                    print("You've already bought this!")
                else:    
                    if gold >= 1000:
                        minATK = 3
                        maxATK = 50
                        gold -= 1000
                        equip.append("Dragon Slayer Spear")
                        print("You've bought a Dragon Slayer Spear!")
                    else:
                        print("Not enough gold!")
                input("> ")
            elif wep == "5":
                input("> ") 
        elif choice == "4":
            buy = False
      
def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if "Dragon Slayer Spear" in equip:
            print("You might want to take on the dragon now! Take this key but be careful with the beast!")
            key = False
        else:
            print("You're not strong enough to face the dragon yet! Keep practicing and come back later!!")
            key = True

        draw()
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False


def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False



while run:
    while menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            print("You have to fight through many type of enemies, getting stronger to become A Mighty Adventurer and defeat a Dragon for the peace of this land!")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("Please enter you name : ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()

        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(minATK) + " - " + str(maxATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(gold))
            print("COORD:", x, y)
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if elix > 0:
                print("6 - USE ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave":
                print("7 - ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("No elixirs!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True
