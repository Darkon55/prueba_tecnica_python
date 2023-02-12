import requests

from database.db import get_connection 

from options.models import Endpoint


class EdnpointService:

    def __init__(self, table_name): 
        self.table_name = table_name

    def post_login(self, params):
        try:
            auth_data = {'usuario': params.username, 'contrasena': params.password}
            resp = requests.post(params.url, json=auth_data)

            return resp
        except Exception as ex:
            raise Exception(ex)
    
    def create_table(self):
        sql = (
            """
            CREATE TABLE IF NOT EXISTS public.users
                (
                    id CHARACTER(36) COLLATE pg_catalog."default" NOT NULL,
                    username CHARACTER VARYING(255) COLLATE pg_catalog."default" NOT NULL,
                    password character VARYING(255) COLLATE pg_catalog."default" NOT NULL,
                    token CHARACTER(36) COLLATE pg_catalog."default" NOT NULL,
                    expiration TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    CONSTRAINT users_pkey PRIMARY KEY (id)
                )

                TABLESPACE pg_default;

                ALTER TABLE IF EXISTS public.users
                    OWNER to postgres;
            """,
            """ 
                INSERT INTO public.users(
                    id, username, password, token, expiration)
                VALUES ('9b076635-ffad-431a-8c2c-b5f28e38df5f', 'Admin', '123', '59FF282D-8E98-445C-82F9-9D330E621790', '2040-04-30 11:40:40.190');
            """,
            """ 
                INSERT INTO public.users(
                    id, username, password, token, expiration)
                VALUES ('d3182061-564e-4adb-a778-3db244961479', 'Ecommerce', 'F4nt4s1!', '3E3F0F5E-D8D9-4369-B7C6-2ADD1CBF2E9E', '2022-07-08 00:00:00.005');
            """)
        conn = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            # create table one by one
            for command in sql:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()

            return ("Configuracion de Base de Datos Realizada")
        except (Exception) as ex:
            raise Exception(ex)
        finally:
            if conn is not None:
                conn.close()