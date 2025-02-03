import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})

class User:
    pass


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == hotel_id, 'name'].squeeze()

    def book(self):
        # Book a hotel by changing its availability to no
        df.loc[df['id'] == hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def see_hotels(self):
        pass

    def available(self):
        # Check if hotel is available
        availability = df.loc[df['id'] == hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self):
        content = f"""
        Thank you for you reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation = Reservation(customer_name=name, hotel_object=hotel)
    print(reservation.generate())
else:
    print("Hotel is not free")

