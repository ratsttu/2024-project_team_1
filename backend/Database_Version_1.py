import mysql.connector
import datetime
from PIL import Image
import io 

date=datetime.datetime.now()

def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def addData(date,Image1Path,Image2Path):
    connection = mysql.connector.connect(host='localhost',user='root',password='Mast3rP13c3!',database='rats_project1')
    cursor = connection.cursor()
    binary_data1 = convert_to_binary_data(Image1Path)
    binary_data2 = convert_to_binary_data(Image2Path)
    cursor.execute("INSERT INTO photos (dateCaptured,BeforePicture,AfterPicture) VALUES (%s,%s,%s)", (date,binary_data1,binary_data2))
    connection.commit()
    connection.close()

def getRow(index):
    connection = mysql.connector.connect(host='localhost',user='root',password='Mast3rP13c3!',database='rats_project1')
    cursor = connection.cursor()
    cursor.execute("Select * from photos")
    table=cursor.fetchall()
    connection.commit()
    connection.close()
    collectedRow=[]
    for i, row in enumerate (table):
        time_day=row[1]
        beforeImage= Image.open(io.BytesIO(row[2]))
        afterImage = Image.open(io.BytesIO(row[3]))
        if(i==(index-1)):
            collectedRow.append(time_day)
            collectedRow.append(beforeImage)
            collectedRow.append(afterImage)
    return collectedRow
def printRow(row):
    print(row[0])
    row[1].show()
    row[2].show()
def getTable():
    connection = mysql.connector.connect(host='localhost',user='root',password='Mast3rP13c3!',database='rats_project1')
    cursor = connection.cursor()
    cursor.execute("SELECT sum(char_length(indexed))FROM photos")
    maxRange=cursor.fetchone()[0]
    cursor.execute("select * from photos")
    table=cursor.fetchall()
    connection.commit()
    connection.close()
    table=[]
    for i in range(1,int(maxRange)+1):
        row=getRow(i)
        table.append(row)
    return table
def printTable(table):
    for i in range(len(table)):
        print(table[i][0])
        table[i][1].show()
        table[i][2].show()
printTable(getTable())
