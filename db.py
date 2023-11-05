import mysql.connector
from os import environ
from dotenv import find_dotenv, load_dotenv
import datetime as dt

load_dotenv(find_dotenv())


class Db:
    def __init__(self):
        # declear global vairable to be use.
        self.cnx = mysql.connector.connect(
            host=environ.get("HOST"),
            user=environ.get("DB_USER"),
            password=environ.get("DB_PASS"),
            database=environ.get("DB")
        )

        self.cursor = self.cnx.cursor(buffered=True)
        self.now = dt.datetime.today()

    def get_coffees(self):
        '''
        get all available coffee from coffee table,
        return every field from coffee table.
        '''
        sql_get_coffees = "SELECT * FROM coffee"
        self.cursor.execute(sql_get_coffees)
        self.cnx.commit()
        result = self.cursor.fetchall()

        return result

    def get_cof_resource(self, coffee_id):
        '''
        get material for each individual coffee, return a single row.
        '''
        sql_cof_mat = f"SELECT mat_cofbean, mat_water, mat_sugar, coffee.coffee_price \
            FROM material \
                INNER JOIN coffee ON material.mat_id = coffee.mat_id \
                    WHERE coffee.coffee_id = {coffee_id}"
        self.cursor.execute(sql_cof_mat)
        self.cnx.commit()
        cof_mat = self.cursor.fetchone()

        return cof_mat

    def get_resource(self):
        '''
        get available resource from resource table, return (cof_bean, water, sugar)
        '''
        sql_available_resource = f"SELECT cof_bean, water, sugar FROM resource"
        self.cursor.execute(sql_available_resource)
        self.cnx.commit()
        available_resource = self.cursor.fetchone()

        return available_resource

    def check_mat(self, coffee_id):
        '''
        compare coffee material with resource table, return True for sufficient and False for insufficient 
        '''

        cof_mat = self.get_cof_resource(coffee_id)
        available_resource = self.get_resource()

        if available_resource >= cof_mat:
            return True
        else:
            return False

    def make_coffee(self, coffee_id):
        '''
        this function handle deduct material from stock table
        '''
        cof_mat = self.get_cof_resource(coffee_id)
        available_resource = self.get_resource()

        result = [available_resource[x] - cof_mat[x]
                  for x in range(len(available_resource))]

        self.update_resource(result)

    def update_resource(self, resource):
        '''
        this function handling material deduction from resource table.
        '''
        sql_update = f"UPDATE resource SET cof_bean={resource[0]},water={resource[1]}, sugar={resource[2]} WHERE res_id=1"
        self.cursor.execute(sql_update)
        self.cnx.commit()
