class Train:
    def __init__(self, train_id, train_name, source, destination, departure_time, available_seats, train_type, price_per_ticket, total_distance):
        self.train_id = train_id
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.available_seats = available_seats
        self.train_type = train_type  # e.g., Express, Local, etc.
        self.price_per_ticket = price_per_ticket  # Price per ticket
        self.total_distance = total_distance  # Distance in kilometers

    def book_ticket(self, num_seats):
        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            return True
        return False

    def cancel_ticket(self, num_seats):
        self.available_seats += num_seats


class RailwayBookingSystem:
    def __init__(self):
        self.trains = []
        self.bookings = {}

    def add_train(self, train):
        self.trains.append(train)

    def view_trains(self):
        print("\nAvailable Trains:")
        for train in self.trains:
            print(f"Train ID: {train.train_id}, Train Name: {train.train_name}, "
                  f"Source: {train.source}, Destination: {train.destination}, "
                  f"Departure Time: {train.departure_time}, Available Seats: {train.available_seats}, "
                  f"Train Type: {train.train_type}, Price per Ticket: ${train.price_per_ticket}, "
                  f"Total Distance: {train.total_distance} km")

    def book_ticket(self, train_id, num_seats, user_name):
        for train in self.trains:
            if train.train_id == train_id:
                if train.book_ticket(num_seats):
                    if user_name not in self.bookings:
                        self.bookings[user_name] = []
                    self.bookings[user_name].append((train.train_id, num_seats))
                    total_price = num_seats * train.price_per_ticket
                    print(f"Successfully booked {num_seats} tickets for {train.train_name}. Total price: ${total_price}.")
                    return
                else:
                    print("Not enough available seats.")
                    return
        print("Train not found.")

    def cancel_ticket(self, train_id, num_seats, user_name):
        if user_name in self.bookings:
            for booking in self.bookings[user_name]:
                if booking[0] == train_id:
                    if booking[1] >= num_seats:
                        self.update_booking(user_name, train_id, num_seats, booking)
                        return
                    else:
                        print("You have not booked enough tickets for this train.")
                        return
        print("No bookings found for this user.")

    def update_booking(self, user_name, train_id, num_seats, booking):
        booking_index = self.bookings[user_name].index(booking)
        self.bookings[user_name][booking_index] = (train_id, booking[1] - num_seats)
        for train in self.trains:
            if train.train_id == train_id:
                train.cancel_ticket(num_seats)
                total_refund = num_seats * train.price_per_ticket
                print(f"Successfully canceled {num_seats} tickets for {train.train_name}. Total refund: ${total_refund}.")
                return

    def view_bookings(self, user_name):
        if user_name in self.bookings:
            print(f"\nBookings for {user_name}:")
            for train_id, num_seats in self.bookings[user_name]:
                print(f"Train ID: {train_id}, Seats Booked: {num_seats}")
        else:
            print("No bookings found for this user.")


def main():
    system = RailwayBookingSystem()

    # Adding some trains with complete details
    system.add_train(Train(1, "Express Train", "City A", "City B", "10:00 AM", 100, "Express", 50, 150))
    system.add_train(Train(2, "Local Train", "City A", "City C", "11:00 AM", 50, "Local", 30, 80))
    system.add_train(Train(3, "Rapid Train", "City B", "City D", "12:00 PM", 75, "Rapid", 70, 200))
    system.add_train(Train(4, "Intercity Train", "City C", "City D", "01:00 PM", 60, "Intercity", 60, 120))

    while True:
        print("\nRailway Ticket Booking System")
        print("1. View Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View My Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.view_trains()
        elif choice == '2':
            try:
                train_id = int(input("Enter Train ID: "))
                num_seats = int(input("Enter number of seats to book: "))
                user_name = input("Enter your name: ")
                system.book_ticket(train_id, num_seats, user_name)
            except ValueError:
                print("Please enter valid numerical values for Train ID and number of seats.")
        elif choice == '3':
            try:
                train_id = int(input("Enter Train ID: "))
                num_seats = int(input("Enter number of seats to cancel: "))
                user_name = input("Enter your name: ")
                system.cancel_ticket(train_id, num_seats, user_name)
            except ValueError:
                print("Please enter valid numerical values for Train ID and number of seats.")
        elif choice == '4':
            user_name = input("Enter your name: ")
            system.view_bookings(user_name)
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
