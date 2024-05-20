from .admin import CheckAdmin
from .Check import Check
from loader import dp

if __name__ == 'filters':
    dp.filters_factory.bind(CheckAdmin)



# my_list = []
# new = (input("Listga qoshish uchun ma'lumot kirting:"))
# my_list = new.split()
# way = (input(""))
#
# # my_list.split
# # my_list.extend
# print(my_list)