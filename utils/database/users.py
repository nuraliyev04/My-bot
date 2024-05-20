import psycopg2

def conn_db():
    conn = psycopg2.connect(
    host = 'localhost',
    database = 'aiogram3',
    user = 'postgres',
    password = '1',
    port = "5432"
    )
    conn.autocommit = True
    return conn

def close_db(conn):
    if conn:
        conn.close()

def create_user(fio, username, chat_id):
    conn = conn_db()



    with conn.cursor() as cursor:
        cursor.execute(f'''
        insert into users (fio, username, chat_id) values ('{fio}','{username}','{chat_id}');  
        ''')

    close_db(conn)

#homework

def update_user(phone, chat_id):
    conn = conn_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        update users set phone='{phone}' where chat_id='{chat_id}';
        """)

    close_db(conn)

def delete_user(chat_id):

    conn = conn_db()
    with conn.cursor() as cursor:
        cursor.execute(f"""
        delete from users where chat_id='{chat_id}';
        """)

    close_db(conn)

def get_user_by_id(chat_id):
    conn = conn_db()
    with conn.cursor() as cursor:
        cursor.execute(f"""
        select * from users where chat_id='{chat_id}';
            """)
        result = cursor.fetchall()

    close_db(conn)
    return result

def get_users():
    conn = conn_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        select * from users;
        """)
        result = cursor.fetchall()

        close_db(conn)
        return result

def get_my_user(chat_id):
    conn = conn_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        select * from users;
        """)
        result = cursor.fetchall()
    close_db(conn)
    return result


    # conn.commit()
    # cur.close()
    # conn.close()
    # markup = aiogram.types.InlineKeyboardMarkup()
    # markup.add(aiogram.types.InlineKeyboardButton("Userlar ro'yxati", callback_data='users'))
    # bot.send_message(message.chat.id, "Ro'yxatdan o'tildi!", reply_markup=markup)



