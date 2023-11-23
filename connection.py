from PySide6 import QtSql, QtWidgets


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('clients_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'Невозможно открыть базу данных',
                                           'Нажмите, чтобы закрыть', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec('CREATE TABLE IF NOT EXISTS clients (ID integer primary key AUTOINCREMENT, Name VARCHAR(40), '
                   'Comment VARCHAR(100), Inviter VARCHAR(40))')
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_client_query(self, name, comment, inviter):
        sql_query = "INSERT INTO clients (Name, Comment, Inviter) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, comment, inviter])

    def update_client_query(self, name, comment, inviter, id):
        sql_query = "UPDATE clients SET Name=?, Comment=?, Inviter=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [name, comment, inviter, id])

    def delete_client_query(self, id):
        sql_query = "DELETE FROM clients WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_data(self, cursor):
        cursor.execute("SELECT * FROM clients_db.db")
        data = cursor.fetchall()
        return data
