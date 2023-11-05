from db import Db
from user import User
from report import Report
from inventory import Inventory
from prettytable import PrettyTable
import os

# ------------------------------UI-------------------------------------#

# Declare main menu switch
sell_coffee_menu = False
report_coffee_menu = False
inventory_coffee_menu = False

user = User()
my_db = Db()
report = Report()
inv = Inventory()


def clear():
    '''clear screen function'''
    os.system('cls||clear')


def coffee_list_menu(user_list):
    '''retreive coffee from coffee table and display as a menu item
    take one input, user information {firstname, total}'''
    coffees = my_db.get_coffees()
    catalog = "select coffee"

    select_coffee_state = True

    for index, coffee in enumerate(coffees, 1):
        catalog += f"\n{index}. {coffee[1]} - {coffee[2]}"

    while select_coffee_state:

        coffee_menu = input(catalog + "\ne to exit\nKey in: ")

        if coffee_menu == "e":
            clear()
            break

        clear()

        # if not enough material to make coffee
        if not my_db.check_mat(int(coffee_menu)):
            print("not enough resource to make coffee")
            av_resource = my_db.get_resource()

            input(
                f"available resource in stock:\ncoffee bean: {av_resource[0]}\nwater: {av_resource[1]}\nsugar: {av_resource[2]}")

            clear()
        else:
            # make coffee and check out user, user.checkout method call make coffee method.
            checkout = user.checkout(
                user=user_list, coffee_id=coffee_menu)
            input(
                f"Thank {checkout['firstname']} \nTotal: ${checkout['total']}\nYour coffee will be ready in 2 minutes ")
            clear()
            break


# ------------------------Start UI-------------------------#
main_menu = True

while main_menu:

    # Main menu listed
    print("-----Welcome to CS111 Coffee Shope-----")
    first_menu = input(
        "Key in number to get started...\n1. Sell Coffee\n2. Report\n3. Inventory\ne. Exit\nKey in: ")

    clear()

    if first_menu == "1":
        sell_coffee_menu = True

    elif first_menu == "2":
        report_coffee_menu = True

    elif first_menu == "3":
        inventory_coffee_menu = True

    elif first_menu == "e":
        main_menu = False


#------------ Sell Coffee Menu UI -------------------#

    while sell_coffee_menu:
        clear()
        ck1 = input(
            "for member or guest\n1. guest\n2. member\n3. register\ne to exit\nKey in: ")

        if ck1 == "2":
            phone_num = input("type member phone number: ")
            verify_member = user.is_member(phone=phone_num)

            clear()

            # verify if customer is indeed a member, if they are store their information in verify_member
            if verify_member:
                coffee_list_menu(verify_member)
            else:
                input("member not found!")
                clear()

        elif ck1 == "3":
            clear()
            print("register user menu: ")
            firstname = input("input firstname: ")
            lastname = input("input lastname: ")
            phone_num = input("input phone_number: ")

            user.register(firstname=firstname,
                          lastname=lastname, phone=phone_num)

            input("register successfully")

        elif ck1 == "e":
            sell_coffee_menu = False
            clear()

        else:
            clear()
            guest = user.get_user(1)
            guest["discount"] = 0
            coffee_list_menu(user_list=guest)

#------------ Report Coffee Menu UI -------------------#
    while report_coffee_menu:

        ck2 = input(
            "report menu option listed:\n1. resource report\n2. sale report\n3. member report\ne. exit\nKey in: ")

        if ck2 == "1":
            report.gen_resource()
            clear()

        elif ck2 == "2":
            r_sale_menu = True
            while r_sale_menu:

                clear()
                r_sale_op = input(
                    "select sale report:\n1. get all\n2. from specific date\ne. exit\nKey in: ")

                if r_sale_op == "e":
                    r_sale_menu = False

                elif r_sale_op == "1":
                    report.gen_sale()
                    clear()

                elif r_sale_op == "2":
                    start_date = input(
                        "enter start date (YYYY-MM-DD) require: ")
                    end_date = input("enter end date (YYYY-MM-DD): ")

                    if not end_date:
                        report.gen_sale(start_date=start_date)
                        clear()

                    else:
                        report.gen_sale(start_date=start_date,
                                        end_date=end_date)
                        clear()

            clear()

        elif ck2 == "3":
            report.gen_member()
            clear()

        elif ck2 == "e":
            report_coffee_menu = False
            clear()

#------------ Inventory Menu UI -------------------#
    while inventory_coffee_menu:
        clear()
        inv_op = input(
            "select item to refill\n1. coffee bean\n2. water\n3. sugar\ne. exit\nKey in: ")

        if inv_op == "1" or inv_op == "2" or inv_op == "3":
            to_refill = int(input("input amount to refill: "))

            if inv_op == "1":
                inv.refill(item="cof_bean", to_refill=to_refill)
            elif inv_op == "2":
                inv.refill(item="water", to_refill=to_refill)
            elif inv_op == "3":
                inv.refill(item="sugar", to_refill=to_refill)

            input("successfully refilled, check report!")

            clear()

        elif inv_op == "e":
            inventory_coffee_menu = False
            clear()

        else:
            input("invalid option")
