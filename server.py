import pymssql as mc
import datetime

import pytz

from msgbox import bd_error


def get_data():
    try:
        db = mc.connect("kit-grd-sql01", "FLx_read", "Kitron2017+", "FactoryLogixPLp")

        cursor = db.cursor()

        query1 = """
            SELECT TOP (1)
            prt.Operator,
            prt.TimeCompleted_BaseDateTimeUTC as 'LastTime'
            FROM [FactoryLogixPLp].[dbo].[ItemInventories] ii
            LEFT JOIN ProductRouteTransactions prt ON prt.ItemInventoryID = ii.id
            RIGHT JOIN FactoryResourceBases frb ON frb.id = prt.WorkstationID
            WHERE frb.name = 'Test 01' 
            AND prt.TimeStarted_BaseDateTimeUTC >= ' '
            AND prt.Operator IN ('HUSQV_INLINE1  (xLink)')
            ORDER BY prt.TimeStarted_BaseDateTimeUTC DESC
        """
        cursor.execute(query1)

        results = cursor.fetchall()

        query2 = """
            SELECT TOP (1)
            prt.Operator,
            prt.TimeCompleted_BaseDateTimeUTC as 'LastTime'
            FROM [FactoryLogixPLp].[dbo].[ItemInventories] ii
            LEFT JOIN ProductRouteTransactions prt ON prt.ItemInventoryID = ii.id
            RIGHT JOIN FactoryResourceBases frb ON frb.id = prt.WorkstationID
            WHERE frb.name = 'Test 01' 
            AND prt.TimeStarted_BaseDateTimeUTC >= ' '
            AND prt.Operator IN ('HUSQV_INLINE2  (xLink)')
            ORDER BY prt.TimeStarted_BaseDateTimeUTC DESC
        """
        cursor.execute(query2)

        results2 = cursor.fetchall()

        query3 = """
            SELECT TOP (1)
            prt.Operator,
            prt.TimeCompleted_BaseDateTimeUTC as 'LastTime'
            FROM [FactoryLogixPLp].[dbo].[ItemInventories] ii
            LEFT JOIN ProductRouteTransactions prt ON prt.ItemInventoryID = ii.id
            RIGHT JOIN FactoryResourceBases frb ON frb.id = prt.WorkstationID
            WHERE frb.name = 'Test 01' 
            AND prt.TimeStarted_BaseDateTimeUTC >= ' '
            AND prt.Operator IN ('HUSQV_INLINE3  (xLink)')
            ORDER BY prt.TimeStarted_BaseDateTimeUTC DESC
        """
        cursor.execute(query3)

        results3 = cursor.fetchall()

        time_value1, time_value2, time_value3 = None, None, None

        for result in results:
            time_value1 = result[1]

        for result2 in results2:
            time_value2 = result2[1]

        for result3 in results3:
            time_value3 = result3[1]

        #Inline I Time
        time_utc = pytz.utc
        current_time = pytz.timezone('Europe/Warsaw')
        strefa_utc = time_utc.localize(time_value1)
        local_time1_utc = strefa_utc.astimezone(current_time)
        local_time1 = local_time1_utc

        #Inline II Time
        time_utc = pytz.utc
        current_time = pytz.timezone('Europe/Warsaw')
        strefa_utc = time_utc.localize(time_value2)
        local_time2_utc = strefa_utc.astimezone(current_time)
        local_time2 = local_time2_utc

        #Inline III Time
        time_utc = pytz.utc
        current_time = pytz.timezone('Europe/Warsaw')
        strefa_utc = time_utc.localize(time_value3)
        local_time3_utc = strefa_utc.astimezone(current_time)
        local_time3 = local_time3_utc

        cursor.close()
        db.close()

        return local_time1, local_time2, local_time3
    except mc.Error as e:
        bd_error()
        print(e)

p21 = True
p15 = False
p0 = False

def timeP21():
    global p21, p15, p0
    p21 = True
    p15 = False
    p0 = False

def timeP15():
    global p21, p15, p0
    p21 = False
    p15 = True
    p0 = False

def timeP0():
    global p21, p15, p0
    p21 = False
    p15 = False
    p0 = True

def tenminutago():
    local_time1, local_time2, local_time3 = get_data()

    time_result1, time_result2, time_result3 = False, False, False

    current_time = datetime.datetime.now(pytz.timezone('Europe/Warsaw'))

    if local_time1 is not None:
        time_difference = current_time - local_time1

        if p0 == True and p15 == False and p21 == False:
            time_result1 = time_difference.total_seconds() < 300
        elif p0 == False and p15 == True and p21 == False:
            time_result1 = time_difference.total_seconds() < 420
        elif p0 == False and p15 == False and p21 == True:
            time_result1 = time_difference.total_seconds() < 180
    else:
        time_result1 = True

    if local_time2 is not None:
        time_difference = current_time - local_time2
        if p0 == True and p15 == False and p21 == False:
            time_result2 = time_difference.total_seconds() < 300
        elif p0 == False and p15 == True and p21 == False:
            time_result2 = time_difference.total_seconds() < 420
        elif p0 == False and p15 == False and p21 == True:
            time_result2 = time_difference.total_seconds() < 180
    else:
        time_result2 = True

    if local_time3 is not None:
        time_difference = current_time - local_time3
        if p0 == True and p15 == False and p21 == False:
            time_result3 = time_difference.total_seconds() < 300
        elif p0 == False and p15 == True and p21 == False:
            time_result3 = time_difference.total_seconds() < 420
        elif p0 == False and p15 == False and p21 == True:
            time_result3 = time_difference.total_seconds() < 180
    else:
        time_result3 = True

    return time_result1, time_result2, time_result3