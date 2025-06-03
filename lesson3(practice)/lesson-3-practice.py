from user import User
from card import Card
daria = User('Daria')

daria.sayName()
daria.setAge(18)
daria.sayAge()

Card = Card('4444 5555 6666 1111', '11/99', 'Daria Ch')

daria.addCard(Card)
daria.getCard().pay(100)