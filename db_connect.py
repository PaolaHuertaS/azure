import os
import psycopg2

password = os.getenv("DB_PASSWORD")

cnx = psycopg2.connect(
    user="fsvbkhvxta@webproveedores-server",
    password="r0Yt$gVLsCi7$zCK",
    host="webproveedores-server.postgres.database.azure.com",
    port=5432,
    database="webproveedores-database",
    sslmode="require"
)

