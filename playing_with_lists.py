def print_list(names: list):
    for name in names:
        print(name.title() + ", I hope you can join me for dinner tonight.")


def guest_sequence() -> None:
    guests = ['albert einstein', 'edsger dijkstra', 'elon musk']

    print_list(guests)

    print('\n')
    print(guests.pop(0).title() + " can't make it tonight.")

    guests.insert(0, 'richard feynman')

    print('\n')
    print_list(guests)

    print('\n')
    print("I found a larger table.")
    guests.append('bill nye')

    print_list(guests)

if __name__ == "__main__":
    guest_sequence()
