from prettytable import PrettyTable
from db import Db
from user import User
from datetime import datetime, timedelta


class Report(User, Db):

    def gen_resource(self):
        '''
        check for available resource in database
        return table of resource with field Coffee Bean, Water, Sugar
        '''
        resource_table = PrettyTable()
        resource_table.field_names = ["Coffee Bean", "Water", "Sugar"]
        data = self.get_resource()
        formatted_row = [f'{data[0]} kg', f'{data[1]} ml', f'{data[2]} ml']
        resource_table.add_row(formatted_row)
        input(resource_table.get_string())

    def gen_member(self):
        '''
        check for available member in database
        return table of member
        '''

        member_table = PrettyTable()
        total_user, count = self.get_users()

        member_table.field_names = ["ID", "First Name",
                                    "Last Name", "Phone Number", "created_on"]
        member_table.add_rows(total_user)

        print(f"Total Member: {count}")
        input(member_table.get_string(
            fields=["ID", "First Name", "Last Name", "Phone Number"]))

    def gen_sale(self, **kwargs):
        '''
        check for sale report all or within a specific time slot
        take 2 input as optional, start_date and end_date
        return table of sale.
        '''

        # inner join query, sell id, first name, lastname, coffee, total
        sale_table = PrettyTable()
        sql = "SELECT sell.sell_id, customer.cus_firstname, customer.cus_lastname,coffee.coffee_name, sell.sell_total \
            FROM sell \
                INNER JOIN coffee ON sell.coffee_id = coffee.coffee_id \
                    INNER JOIN customer ON sell.cus_id = customer.cus_id"

        if len(kwargs) > 0:
            if 'end_date' not in kwargs:
                # format date without microsecond
                kwargs["end_date"] = self.now.isoformat(' ', 'seconds')

            kwargs["end_date"] += ' 23:59:00'
            sql += f" WHERE sell.sell_date BETWEEN '{kwargs['start_date']}' and '{kwargs['end_date']}'"

        self.cursor.execute(sql)
        self.cnx.commit()
        result = self.cursor.fetchall()

        total = 0
        for n in result:
            total += n[4]

        sale_table.field_names = [
            "ID", "First Name", "Last Name", "Coffee", "Sell"]
        sale_table.add_rows(result)

        print(f"Total Sale: ${round(total, 2)}")
        input(sale_table.get_string(sortby="ID", reversesort=True))
