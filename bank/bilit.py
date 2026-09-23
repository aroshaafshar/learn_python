seats = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
    10: None
}

while True:
     print("\nAvailable seats:")

     for seat, name in seats.items():
        if name is None:
            print(seat, end=" ")

     print()

     reserved = 0

     for name in seats.values():
        if name is not None:
            reserved += 1

     remaining = 10 - reserved

     print("Seats remaining:", remaining)

     if remaining == 0:
        print("All seats are reserved.")
        break

     choice = input("Choose an option (reserve/release/exit): ")

     if choice == "reserve":
        seat = int(input("Choose seat: "))

        if seat not in seats:
            print("Invalid seat.")

        elif seats[seat] is not None:
            print("Seat", seat, "is already reserved.")

        else:
            name = input("Enter your name: ")
            seats[seat] = name
            print("Seat", seat, "reserved successfully.")

     elif choice == "release":
        seat = int(input("Choose seat to release: "))

        if seat not in seats:
            print("Invalid seat.")

        elif seats[seat] is None:
            print("Seat", seat, "is not reserved.")

        else:
            seats[seat] = None
            print("Seat", seat, "released successfully.")

     elif choice == "exit":
        break

     else:
        print("Invalid option.")