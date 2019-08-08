import talkpython_search_api

if __name__ == "__main__":
    guest1_name= input("Please type the name of a TalkPython guest:")
    guest1_hits = talkpython_search_api.search_episodes(guest1_name)
    guest2_name= input("Please type the name of a second TalkPython guest:")
    guest2_hits = talkpython_search_api.search_episodes(guest2_name)

    guest1_total_episodes = len(guest1_hits['results'])
    guest2_total_episodes = len(guest2_hits['results'])

    if guest1_total_episodes > guest2_total_episodes:
        print(f"Guest 1 wins with {guest1_total_episodes} episodes versus Guest 2's {guest2_total_episodes}!")
    else:
        print(f"Guest 2 wins with {guest2_total_episodes} episodes versus Guest 1's {guest1_total_episodes}!")

