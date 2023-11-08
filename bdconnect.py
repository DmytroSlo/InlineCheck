import datetime

import mysql.connector as mc

def get_data():
    db = mc.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="inlinelogs"
    )

    cursor = db.cursor()

    query = """
        SELECT name, MAX(time) as last_time
        FROM logs
        WHERE name IN ('INLINE 1', 'INLINE 2', 'INLINE 3')
        GROUP BY name
    """
    cursor.execute(query)

    results = cursor.fetchall()

    time_value1, time_value2, time_value3 = None, None, None

    for result in results:
        name = result[0]
        if name == "INLINE 1":
            time_value1 = result[1]
        elif name == "INLINE 2":
            time_value2 = result[1]
        elif name == "INLINE 3":
            time_value3 = result[1]

    cursor.close()
    db.close()

    return time_value1, time_value2, time_value3

def tenminutago():
    time_value1, time_value2, time_value3 = get_data()

    time_result1, time_result2, time_result3 = False, False, False

    current_time = datetime.datetime.now()

    if time_value1:
        time_difference = current_time - time_value1
        time_result1 = time_difference.total_seconds() < 600

    if time_value2:
        time_difference = current_time - time_value2
        time_result2 = time_difference.total_seconds() < 600

    if time_value3:
        time_difference = current_time - time_value3
        time_result3 = time_difference.total_seconds() < 600

    return time_result1, time_result2, time_result3

def result_time():
    time_result1, time_result2, time_result3 = tenminutago()

    time_boolen1, time_boolen2, time_boolen3 = False, False, False

    if time_result1:
        print("Mniej niż 10")
        time_boolen1 = False
    else:
        time_boolen1 = True

    if time_result2:
        print("Mniej niż 10")
        time_boolen2 = False
    else:
        time_boolen2 = True

    if time_result3:
        print("Mniej niż 10")
        time_boolen3 = False
    else:
        time_boolen3 = True

    return time_boolen1, time_boolen2, time_boolen3