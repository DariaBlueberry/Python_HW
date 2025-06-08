from address import Address
from mailing import Mailing

to_addr = Address(410003, "Saratov", "Aviacionnaya", "41", "145")
from_addr = Address(410007, "Saratov", "Prospect", "28", "13")

mailing = Mailing(to_address=to_addr, from_address=from_addr,
                  cost=250, track="AB123654789")

print(f'Отправление {mailing.track} из {mailing.from_address.index}, '
      f'{mailing.from_address.city}, {mailing.from_address.street}, '
      f'{mailing.from_address.house} - {mailing.from_address.apartment} '
      f'в {mailing.to_address.index}, {mailing.to_address.city}, '
      f'{mailing.to_address.street}, {mailing.to_address.house} - '
      f'{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.)')
