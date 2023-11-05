from db import Db


class User(Db):
    def register(self, firstname, lastname, phone):
        '''
        register user to customer table, take 3 paramaters firstname, lastname, phone
        '''
        sql_register = "INSERT INTO customer (cus_firstname, cus_lastname, cus_ph, created_on) VALUES (%s, %s, %s, %s)"
        value = (firstname, lastname, phone, self.now)

        self.cursor.execute(sql_register, value)
        self.cnx.commit()

    def is_member(self, phone):
        '''
        check if user is a valid member, if they are return their information {cus_id, firstname, lastname, discount}
        if not return False
        '''
        sql_search_user = f"SELECT * FROM customer WHERE cus_ph={phone}"
        self.cursor.execute(sql_search_user)
        self.cnx.commit()
        result = self.cursor.fetchone()
        if result:
            return {"cus_id": result[0], "firstname": result[1], "lastname": result[2], "discount": 0.1}
        else:
            return False

    def get_user(self, user_id):
        '''
        get individual user account from customer table
        '''
        sql_get_user = f"SELECT * FROM customer WHERE cus_id={user_id}"
        self.cursor.execute(sql_get_user)
        self.cnx.commit()
        result = self.cursor.fetchone()
        return {"cus_id": result[0], "firstname": result[1], "lastname": result[2]}

    def get_users(self):
        '''
        get all user account from customer table
        '''
        sql_get_users = f"SELECT * FROM customer"
        self.cursor.execute(sql_get_users)
        self.cnx.commit()
        result = self.cursor.fetchall()
        count = self.cursor.rowcount
        return result, count

    def checkout(self, user, coffee_id):
        '''
        this function handle financial transaction, and brew the coffee.
        '''

        sql_sell = "INSERT INTO sell (coffee_id, cus_id, sell_total, sell_date) VALUES (%s,%s,%s,%s)"
        purchased_coffee = self.get_cof_resource(coffee_id)

        total = purchased_coffee[3] - (purchased_coffee[3] * user["discount"])

        value = (coffee_id, user["cus_id"], total, self.now)
        self.cursor.execute(sql_sell, value)
        self.make_coffee(coffee_id)
        self.cnx.commit()

        return {"firstname": user["firstname"], "total": total}
