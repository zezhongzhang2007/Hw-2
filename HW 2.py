
def create_entry(number,name,type_1,type_2,health_points,attack,defense,special_attack,special_defense,speed,generation,is_legendary):
    print("number:",number)
    print("name:", name)
    if type_2 == " ":
        print("Types:",(type_1))
    else:
        print("Types:", (type_1, type_2))
    dict2 = {"health_points":health_points,"attack":attack,"defense":defense,"Sp.Atk":special_attack,"Sp.Def":special_defense,"Speed":speed}
    print("Battle_States:",dict2)
    print("generation:",generation)
    print("legendary:",is_legendary)


a_random_pokemon = create_entry(81, "Magnemite","Steel"," ",25, 35, 70, 95, 55, 45, 1, False)
