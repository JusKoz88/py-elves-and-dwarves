def calculate_team_total_rating(list_of_players: list) -> int:
    return sum(elem.get_rating() for elem in list_of_players)


def elves_concert(list_of_elves: list) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
