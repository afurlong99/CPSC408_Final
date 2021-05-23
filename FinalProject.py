import sqlite3
import pandas as pd
from pandas import DataFrame
from faker import Faker
import random
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
mpl.use('module://backend_interagg')

conn = sqlite3.connect('Housing.db')

c = conn.cursor()
fake = Faker('en_US')


def insertData():
    #House
    House = pd.DataFrame()
    OwnerID = []
    Value = []
    numBed = []
    numBath = []
    Size = []
    Pool = []
    Garage = []

    #Inserting fake information
    for i in range(1000):
        OwnerID.append(i)
        i+=1
        Value.append(fake.random_int(min=100, max=9999)*100)
        numBed.append(fake.random_int(min=1, max=9))
        numBath.append(fake.random_int(min=1, max=9))
        Size.append(fake.random_int(min=2000, max=5000))
        Pool.append(fake.pybool())
        Garage.append(fake.pybool())

    # Turning into column
    House["OwnerID"] = OwnerID
    House["Value"] = Value
    House["numBed"] = numBed
    House["numBath"] = numBath
    House["Size"] = Size
    House["Pool"] = Pool
    House["Garage"] = Garage

    for i, row in House.iterrows():

        c.execute('SELECT COUNT(*) from House')
        data = pd.DataFrame(c.fetchall())
        answer = data[0][0]
        if answer != len(House):
            print("Record inserted")
            sql = "INSERT INTO House VALUES (?,?,?,?,?,?,?, null)"
            c.execute(sql, tuple(row))
            conn.commit()
        else:
            break

    #Address
    Address = pd.DataFrame()
    OwnerID = []
    StreetNumber = []
    StreetName = []
    City = []
    State = []
    Zipcode = []

    #Inserting fake information
    for i in range(1000):
        OwnerID.append(i)
        i+=1
        StreetNumber.append(fake.building_number())
        StreetName.append(fake.street_name())
        City.append(fake.city())
        State.append(fake.state())
        Zipcode.append(fake.postcode())

    # Turning into column
    Address["OwnerID"] = OwnerID
    Address["StreetNumber"] = StreetNumber
    Address["StreetName"] = StreetName
    Address["City"] = City
    Address["State"] = State
    Address["Zipcode"] = Zipcode

    for i, row in Address.iterrows():

        c.execute('SELECT COUNT(*) from Address')
        data = pd.DataFrame(c.fetchall())
        answer = data[0][0]
        if answer <= len(Address):
            print("Record inserted")
            sql = "INSERT INTO Address VALUES (?,?,?,?,?,?, null)"
            c.execute(sql, tuple(row))
            conn.commit()
        else:
            break

    #Mortgage
    Mortgage=pd.DataFrame()
    OwnerID = []
    DownPayment = []
    InterestRate = []
    Years = []

    for i in range(1000):
        OwnerID.append(i)
        i+=1
        DownPayment.append(fake.random_int(min=100,max=5000)*100)
        InterestRate.append(fake.random_int(min=1.0, max=30.0))
        Years.append(fake.random_int(min=1, max=30))

    Mortgage["OwnerID"] = OwnerID
    Mortgage["DownPayment"] = DownPayment
    Mortgage["InterestRate"] = InterestRate
    Mortgage["Years"] = Years

    for i, row in Mortgage.iterrows():

        c.execute('SELECT COUNT(*) from Mortgage')
        data = pd.DataFrame(c.fetchall())
        answer = data[0][0]
        if answer != len(Mortgage):
            print("Record inserted")
            sql = "INSERT INTO Mortgage VALUES (?,?,?,?,null)"
            c.execute(sql, tuple(row))
            conn.commit()
        else:
            break

    #Neighborhood
    Neighborhood = pd.DataFrame()
    OwnerID = []
    Groceries = []
    Church = []
    EduLower = []
    EduHigher = []
    Retail = []
    Entertainment = []

    for i in range(1000):
        OwnerID.append(i)
        i+=1
        Groceries.append(float(fake.pydecimal(left_digits=1,right_digits=1,min_value=0,max_value=9)))
        Church.append(float(fake.pydecimal(left_digits=1,right_digits=1,min_value=0,max_value=9)))
        EduLower.append(float(fake.pydecimal(left_digits=1,right_digits=1,min_value=0,max_value=9)))
        EduHigher.append(float(fake.pydecimal(left_digits=1,right_digits=1,min_value=0,max_value=9)))
        Retail.append(float(fake.pydecimal(left_digits=1,right_digits=1,min_value=0,max_value=9)))
        Entertainment.append(float(fake.pydecimal(left_digits=1,right_digits=1,min_value=0,max_value=9)))

    Neighborhood["OwnerID"] = OwnerID
    Neighborhood["Groceries"] = Groceries
    Neighborhood["Church"] = Church
    Neighborhood["EduLower"] = EduLower
    Neighborhood["EduHigher"] = EduHigher
    Neighborhood["Retail"] = Retail
    Neighborhood["Entertainment"] = Entertainment

    for i, row in Neighborhood.iterrows():

        c.execute('SELECT COUNT(*) from Neighborhood')
        data = pd.DataFrame(c.fetchall())
        answer = data[0][0]
        if answer != len(Neighborhood):
            print("Record inserted")
            sql = "INSERT INTO Neighborhood VALUES (?,?,?,?,?,?,?,null)"
            c.execute(sql, tuple(row))
            conn.commit()
        else:
            break

    #Owner
    Owner = pd.DataFrame()
    DOB = []
    Sex = []
    my_gender_list = ['Male','Female']
    Occupation = []
    IncomeYear =[]
    MaritalStatus = []
    Children = []


    for i in range(1000):
        DOB.append(fake.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=80))
        Sex.append(fake.word(ext_word_list=my_gender_list))
        Occupation.append(fake.job())
        IncomeYear.append(round(random.randint(40000,120000)/1000)*1000)
        MaritalStatus.append(fake.pybool())
        Children.append(fake.random_int(min=0, max=5, step=1))


    Owner["OwnerID"] = OwnerID
    Owner["DOB"] = DOB
    Owner["Sex"] = Sex
    Owner["Occupation"] = Occupation
    Owner["IncomeYear"] = IncomeYear
    Owner["MaritalStatus"] = MaritalStatus
    Owner["Children"] = Children

    for i, row in Owner.iterrows():
        c.execute("SELECT COUNT(*) FROM Owner;")
        data = pd.DataFrame(c.fetchall())
        answer = data[0][0]
        if answer != len(Owner):
            print("Record inserted")
            sql = "INSERT INTO Owner VALUES (?,?,?,?,?,?,?, null)"
            c.execute(sql, tuple(row))
            conn.commit()
        else:
            break



    #Utilities
    Utilities = pd.DataFrame()
    Internet = []
    Water = []
    Electricity = []
    Gas =[]
    Waste = []


    for i in range(1000):
        Internet.append(fake.random_int(min=500, max=720, step=1))
        Water.append(fake.random_int(min=250, max=400, step=5))
        Electricity.append(fake.random_int(min=1000, max=1500, step=1))
        Gas.append(fake.random_int(min=500, max=700, step=1))
        Waste.append(fake.random_int(min=300, max=500, step=1))

    Utilities["OwnerID"] = OwnerID
    Utilities["Internet"] = Internet
    Utilities["Water"] = Water
    Utilities["Electricity"] = Electricity
    Utilities["Gas"] = Gas
    Utilities["Waste"] = Waste

    for i, row in Utilities.iterrows():
        c.execute("SELECT COUNT(*) FROM Utilities;")
        data = pd.DataFrame(c.fetchall())
        answer = data[0][0]
        if answer != len(Owner):
            print("Record inserted")
            sql = "INSERT INTO Utilities VALUES (?,?,?,?,?,?, null);"
            c.execute(sql, tuple(row))
            conn.commit()
        else:
            break
    print("Data insertion complete. ")