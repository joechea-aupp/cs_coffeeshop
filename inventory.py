from db import Db


class Inventory(Db):
    def refill(self, item, to_refill):
        '''
        refill resource by item category.
        '''
        resource = self.get_resource()
        resource_list = {
            "cof_bean": resource[0],
            "water": resource[1],
            "sugar": resource[2]
        }

        if not item in resource_list:
            return "item not found!"

        resource_list[item] += to_refill

        sql = f"UPDATE resource SET {item}={resource_list[item]} WHERE res_id=1"
        self.cursor.execute(sql)
        self.cnx.commit()
