class Ticket:
    def __init__(self, price, destination):
        self.price = price
        self.destination = destination

class Passenger:
    def __init__(self, name, money, destination):
        self.name = name
        self.money = money
        self.destination = destination

    def info(self):
        print(f"{self.name} хочет купить билет до {self.destination}, имеет с собой {self.money} и")


    def buy_ticket(self, ticket):
        if ticket.destination == self.destination and self.money >= ticket.price:
            self.money = self.money - ticket.price
            print(f"Сдача {self.money}")
        else:
            print(f"{self.name} не может купить билет в {ticket.destination} за {ticket.price}!")

passenger1 = Passenger('Маша', 1500, "Красноярск")
ticket1 = Ticket(5000, "Анапа")
ticket2 = Ticket(1000, "Красноярск")

passenger1.info()
passenger1.buy_ticket(ticket2)
