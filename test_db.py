import unittest
from unittest.mock import patch, MagicMock
from  db import Db

class TestDb(unittest.TestCase):
    @patch('db.mysql.connector')
    def setUp(self, mock_sql):
        self.mock_cursor = MagicMock()
        mock_sql.connect().cursor.return_value = self.mock_cursor
        self.db = Db()

    def test_get_coffees(self):
        self.db.get_coffees()
        self.mock_cursor.execute.assert_called_once_with("SELECT * FROM coffee")
        self.mock_cursor.fetchall.assert_called_once()

    def test_get_cof_resource(self):
        self.db.get_cof_resource(1)
        self.mock_cursor.execute.assert_called_once()
        self.mock_cursor.fetchone.assert_called_once()

    def test_get_resource(self):
        self.db.get_resource()
        self.mock_cursor.execute.assert_called_once_with("SELECT cof_bean, water, sugar FROM resource")
        self.mock_cursor.fetchone.assert_called_once()

    def test_check_mat(self):
        self.db.get_cof_resource = MagicMock(return_value=[10, 10, 10])
        self.db.get_resource = MagicMock(return_value=[20, 20, 20])
        self.assertTrue(self.db.check_mat(1))

    def test_make_coffee(self):
        self.db.get_cof_resource = MagicMock(return_value=[10, 10, 10])
        self.db.get_resource = MagicMock(return_value=[20, 20, 20])
        self.db.update_resource = MagicMock()
        self.db.make_coffee(1)
        self.db.update_resource.assert_called_once_with([10, 10, 10])

if __name__ == '__main__':
    unittest.main()