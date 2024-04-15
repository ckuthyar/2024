class Auditorium:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

    def display_auditorium(self):
        print("Auditorium Layout:")
        print("   " + " ".join([str(i) for i in range(1, self.seats_per_row + 1)]))
        for i in range(self.rows):
            print(f"{i + 1}: " + " ".join(self.seats[i]))

    def book_seat(self, row, seat):
        if 1 <= row <= self.rows and 1 <= seat <= self.seats_per_row:
            if self.seats[row - 1][seat - 1] == 'X':
                print("Sorry, this seat is already booked.")
            else:
                self.seats[row - 1][seat - 1] = 'X'
                print(f"Seat {row}-{seat} booked successfully!")
        else:
            print("Invalid seat selection.")

if __name__ == "__main__":
    rows = int(input("Enter the number of rows in the auditorium: "))
    seats_per_row = int(input("Enter the number of seats per row: "))
    auditorium = Auditorium(rows, seats_per_row)
    
    while True:
        print("\n1. View Auditorium Layout")
        print("2. Book a Seat")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            auditorium.display_auditorium()
        elif choice == '2':
            row = int(input("Enter row number: "))
            seat = int(input("Enter seat number: "))
            auditorium.book_seat(row, seat)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

