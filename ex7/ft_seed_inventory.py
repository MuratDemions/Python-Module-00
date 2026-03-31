def ft_seed_inventory(seed, num, typer):
    seed = seed[0].upper() + seed[1:]
    if typer == "packets":
        print(seed, " seeds:", num, "packets available")
    elif typer == "grams":
        print(seed, " seeds:", num, "grams total")
    elif typer == "area":
        print(seed, " seeds:  covers ", num, " square meters")
    else:
        print("Unknown unit type")
