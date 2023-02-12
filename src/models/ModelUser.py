from database.db import get_connection
from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute( """SELECT id, username, password, token, expiration FROM users 
                    WHERE username = '{}'""".format(user.username))
                
                row = cursor.fetchone()

            connection.close()

            if row != None:
                user = User(row[0], row[1], row[2], row[3], row[4])

                return user

            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_token(self, id, token):
        try:
            connection = get_connection()

            print(id, token)


            with connection.cursor() as cursor:
                sql_update_query = """UPDATE users SET token = %s WHERE id = %s"""
                record_to_update = (token, id)
                cursor.execute(sql_update_query, record_to_update)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)