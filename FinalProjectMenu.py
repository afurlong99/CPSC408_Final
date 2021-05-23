import sqlite3
import pandas as pd
from pandas import DataFrame
import matplotlib as mpl
from datetime import datetime
mpl.use('tkagg')
import matplotlib.pyplot as plt
mpl.use('module://backend_interagg')
import FinalProject


conn = sqlite3.connect('Housing.db')
c = conn.cursor()

print("Loading...")
FinalProject.insertData()

c.execute("DROP INDEX IF EXISTS index_name;")
c.execute("CREATE INDEX index_name ON House(OwnerId);")

c.execute("DROP VIEW IF EXISTS Graph1;")
c.execute("DROP VIEW IF EXISTS Graph2;")

c.execute("CREATE VIEW Graph1 AS SELECT Value, SIZE FROM House;")
c.execute("CREATE VIEW Graph2 AS Select avg(Value), numBed from House Group By numBed")

def UserInterface():
    while True:
        print(">>>>>>>>>>>>> WELCOME TO FINDESTATE <<<<<<<<<<<<< \n")
        print("Please choose form our menu options: ")
        print("1. Manage By ID ")
        print("2. Personalized Features")
        print("3. Exit" )
        menu = input(" Choose Option: ")
        if menu == "1":
            UserInterface1()
        elif menu == '2':
            UserInterface2()
        elif menu == "3":
            print("Exit Program")
            conn.commit()
            break
        else:
            print("Incorrect Input")
            UserInterface()
            break
def UserInterface1():
    print("What would you like to do?\n")
    print("1.Search OwnerID")
    print("2.Update OwnerID")
    print("3.Add OwnerID")
    print("4.Delete OwnerID")
    print("5.View Table")
    print("6.Go Back")
    menu2 = input(" Choose Option: ")
    if menu2 == "1":
        SearchID()
    if menu2 == "2":
        updateInfo()
    if menu2 == "3":
        AddID()
    if menu2 == "4":
        deleteOwnerID()
    if menu2 == "5":
        df = DataFrame(c.execute('Select * from House').fetchall())
        df.columns = ['OwnerID', 'Value', 'Size', 'Pool', 'Garage', 'NumBathroom',
        'NumBedroom', 'IsDeleted']
        print(df)
        UserInterface1()
    if menu2 == "6":
        UserInterface()
        quit()
def UserInterface2():
    print("\nFindaState Features:\n")
    print("1.Personalized filtration. ")
    print("2.Graphical Representation.")
    print("3.Demographic Insights.")
    print("5.Go Back")
    menu2 = input("\nChoose Option: ")
    if menu2 == '1':
        filter()
    if menu2 == "2":
        plot()
    if menu2 == "3":
        demographics()
    if menu2 == "5":
        UserInterface()
        quit()
def SearchID():
    while True:
        print("Search OwnerID:")
        print("1.Address Information")
        print("2.House Information")
        print("3.Mortgage Information")
        print("4.Neighborhood Information")
        print("5.Owner Information")
        print("6.Utilities Information")
        print("7.Back\n")
        menu = input("Choose Option: ")
        if menu == "7":
            UserInterface1()
            quit()
        if menu == "1":
            print("\nPlease Enter OwnerID")
            inputOwnerID = input("OwnerID: ")
            c.execute('SELECT * FROM Address WHERE OwnerID = ? ', (inputOwnerID,))
            output = c.fetchall()
            if output == []:
                print("Incorrect Input.")
                SearchID()
                break
            else:
                df = DataFrame(output, columns=['OwnerId', 'StreetNumber', 'StreetName', 'City', 'State', 'Zipcode', 'IsDeleted'])
                print(df)
                SearchID()
                break
        if menu == "2":
            print("\nPlease Enter OwnerID")
            inputOwnerID = input("OwnerID: ")
            c.execute('SELECT * FROM House WHERE OwnerID = ? ', (inputOwnerID,))
            output = c.fetchall()
            if output == []:
                print("Incorrect Input.")
                SearchID()
                break
            else:
                df = DataFrame(output, columns=['OwnerId', 'Value', 'numBed', 'numBath', 'Size', 'Pool','Garage', 'isDeleted'])
                print(df)
                SearchID()
                break
        if menu == "3":
            print("\nPlease Enter OwnerID")
            inputOwnerID = input("OwnerID: ")
            c.execute('SELECT * FROM Mortgage WHERE OwnerID = ? ', (inputOwnerID,))
            output = c.fetchall()
            if output == []:
                print("Incorrect Input.")
                SearchID()
                break
            else:
                df = DataFrame(output, columns=['OwnerId', 'DownPayment', 'InterestRate', 'Years', 'isDeleted'])
                print(df)
                SearchID()
                break
        if menu == "4":
            print("\nPlease Enter OwnerID")
            inputOwnerID = input("OwnerID: ")
            c.execute('SELECT * FROM Neighborhood WHERE OwnerID = ? ', (inputOwnerID,))
            output = c.fetchall()
            if output == []:
                print("Incorrect Input.")
                SearchID()
                break
            else:
                df = DataFrame(output, columns=['OwnerId', 'Groceries', 'Church', 'EduLower','EduHigher','Retail','Entertainment', 'isDeleted'])
                print(df)
                SearchID()
                break
        if menu == "5":
            print("\nPlease Enter OwnerID")
            inputOwnerID = input("OwnerID: ")
            c.execute('SELECT * FROM Owner WHERE OwnerID = ? ', (inputOwnerID,))
            output = c.fetchall()
            if output == []:
                print("Incorrect Input.")
                SearchID()
                break
            else:
                df = DataFrame(output, columns=['OwnerId', 'DOB', 'Sex', 'Occupation','IncomeYear','MaritalStatus','Children', 'isDeleted'])
                print(df)
                SearchID()
                break
        if menu == "6":
            print("\nPlease Enter OwnerID")
            inputOwnerID = input("OwnerID: ")
            c.execute('SELECT * FROM Utilities WHERE OwnerID = ? ', (inputOwnerID,))
            output = c.fetchall()
            if output == []:
                print("Incorrect Input.")
                SearchID()
                break
            else:
                df = DataFrame(output, columns=['OwnerId', 'Internet', 'Water', 'Electricity','Gas','Waste', 'isDeleted'])
                print(df)
                SearchID()
                break
        if menu == "7":
            UserInterface1()
            quit()
#Updates
def updateInfo():
    OwnerID = input("\nPlease enter the OwnerID of the house you would like to update:")
    input1 = input("\nWould you like to Update by House(Press h) or Owner (Press o) information( Press 3 to go back):")
    if input1.lower() == 'h':
        print("The following are available to update in the Home Table ")
        print("1. Value")
        print("2. Number of Bedrooms")
        print("3. Number of Bathroom")
        print("4. Pool Installation")
        print("5. Garage Installation")
        print("6. Back")
        input2 = input("Please select the number of the feature you would like to alter: ")
        if input2== '6':
            updateInfo()
        if input2 == '1':
            newValue1 = input("The new value of the home: ")
            c.execute('UPDATE House SET Value = ? WHERE OwnerID = ? ', (newValue1,OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()
        if input2 == '2':
            newValue2 = input("The new number of bedrooms in the home: ")
            c.execute('UPDATE House SET numBed = ? WHERE OwnerID = ? ', (newValue2, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()
        if input2 == '3':
            newValue3 = input("The new Number bathrooms in the home: ")
            c.execute('UPDATE House SET numBath = ? WHERE OwnerID = ? ', (newValue3, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()
        if input2 == '4':
            newValue4 = input("New pool Installation( Type 1 for yes 0 for no ):")
            c.execute('UPDATE House SET Pool = ? WHERE OwnerID = ? ', (newValue4, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()
        if input2 == '5':
            newValue5 = input("New Garage Installation( Type 1 for yes 0 for no ): ")
            c.execute('UPDATE House SET Garage = ? WHERE OwnerID = ? ', (newValue5, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()
        if input2 == '6':
            updateInfo()
            quit()
    elif input1.lower() == 'o':
        print("The following are available to update in the OwnerInfo Table ")
        print("1. Occupation")
        print("2. Income per year")
        print("3. Marital Status")
        print("4. Number of Children")
        print("5. Back")
        input2 = input("Choose a number for the feature you would like to alter: ")
        if input2 == '5':
            updateInfo()

        if input2 == '1':
            newValue1 = input("The new Occupation of the home: ")
            c.execute('UPDATE Owner SET Occupation = ? WHERE OwnerID = ? ', (newValue1, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()

        if input2 == '2':
            newValue2 = input("The new Income per year: ")
            c.execute('UPDATE Owner SET IncomeYear = ? WHERE OwnerID = ? ', (newValue2, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()

        if input2 == '3':
            newValue3 = input("New Marital Status( Type 1 for yes 0 for no ):")
            c.execute('UPDATE Owner SET MaritalStatus = ? WHERE OwnerID = ? ', (newValue3, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()

        if input2 == '4':
            newValue4 = input("The new number of children:")
            c.execute('UPDATE Owner SET Children = ? WHERE OwnerID = ? ', (newValue4, OwnerID))
            conn.commit()
            print("Updated Information Successfully")
            updateInfo()
        if input2 == '5':
            updateInfo()
            quit()

        else:
            UserInterface1()
            quit()

def AddID():
    while True:
        print("Add OwnerID:")
        print("1.Address Information")
        print("2.House Information")
        print("3.Mortgage Information")
        print("4.Neighborhood Information")
        print("5.Owner Information")
        print("6.Utilities Information")
        print("7.Go Back")
        menu = input(" Choose Option: ")
        if menu == "1":
            while True:
                try:
                    inputStreetNumber = int(input("StreetNumber: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number: ")
            while True:
                try:
                    inputStreetName = str(input("StreetName: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a String: ")
            while True:
                try:
                    inputCity = str(input("City: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a String: ")
            while True:
                try:
                    inputState = str(input("State: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a String: ")
            while True:
                try:
                    inputZipcode = int(input("ZipCode: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be 5 number Zipcode: ")
            nStudentID = c.execute('SELECT OwnerID from Address where OwnerID = (SELECT max(OwnerID) from Address) ').fetchall()
            df = pd.DataFrame(nStudentID)
            newId = df[0][0]
            newId = int(newId) + 1
            c.execute('INSERT INTO Address(OwnerID,StreetNumber,StreetName,City,State,Zipcode) VALUES (?,?,?,?,?,?)',
                (newId, inputStreetNumber,inputStreetName,inputCity,inputState,inputZipcode))
            conn.commit()
            print("\nOwnerID Address Information Added!\n")
        if menu == '2':
            while True:
                try:
                    inputValue = int(input("Value: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputnumBed = int(input("Number of Bedrooms: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputnumBath = int(input("Number of Bathrooms: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputSize = int(input("House Size in Sq Ft: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputPool = bool(input("Does the House have a pool?(0 = no, 1 = yes) : "))
                    if inputPool == '0':
                        print("No")
                    elif inputPool == '1':
                        print("Yes")
                    else:
                        print("Incorrect Form. Input must be 0 or 1 ")
                    break
                except ValueError:
                    print("Incorrect Form. Input must be 0 or 1 ")
            while True:
                try:
                    inputGarage = bool(input("Does the House have a Garage?(0 = no, 1 = yes) : "))
                    if inputGarage == '0' | inputGarage == '1':
                        continue
                    else:
                        print("Incorrect Form. Input must be 0 or 1 ")
                    break
                except ValueError:
                    print("Incorrect Form. Input must be 0 or 1 ")
            nStudentID = c.execute('SELECT OwnerID from House where OwnerID = (SELECT max(OwnerID) from House) ').fetchall()
            df = pd.DataFrame(nStudentID)
            newId = df[0][0]
            newId = int(newId) + 1
            c.execute('INSERT INTO House(OwnerID,Value,numBed,numBath,Size,Pool,Garage) VALUES (?,?,?,?,?,?,?)',
                (newId, inputValue,inputnumBed,inputnumBath,inputSize,inputPool,inputGarage))
            conn.commit()
            print("\nOwnerID House Information Added!\n")
        if menu == "3":
            while True:
                try:
                    inputDownPayment = int(input("DownPayment: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputInterestRate = int(input("Interest Rate: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputYears = int(input("Years: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            nStudentID = c.execute('SELECT OwnerID from Mortgage where OwnerID = (SELECT max(OwnerID) from Mortgage) ').fetchall()
            df = pd.DataFrame(nStudentID)
            newId = df[0][0]
            newId = int(newId) + 1
            c.execute('INSERT INTO Mortgage(OwnerID,DownPayment,InterestRate,Years) VALUES (?,?,?,?)',
                (newId, inputDownPayment,inputInterestRate,inputYears))
            conn.commit()
            print("\nOwnerID Mortgage Information Added!\n")
        if menu == "4":
            while True:
                try:
                    inputGroceries = float(input("Closest Supermarket in miles (decimal form): "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a float Number! ")
            while True:
                try:
                    inputChurch = float(input("Closest Church in miles (decimal form): "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a float Number! ")
            while True:
                try:
                    inputEduLower = float(input("Closest Lower School in miles (decimal form): "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a float Number! ")
            while True:
                try:
                    inputEduHigher = float(input("Closest High School in miles (decimal form): "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a float Number! ")
            while True:
                try:
                    inputRetail = float(input("Closest Retail Store in miles (decimal form): "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a float Number! ")
            while True:
                try:
                    inputEntertainment = float(input("Closest Entertainment Store in miles (decimal form): "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a float Number! ")
            nStudentID = c.execute('SELECT OwnerID from Neighborhood where OwnerID = (SELECT max(OwnerID) from Neighborhood) ').fetchall()
            df = pd.DataFrame(nStudentID)
            newId = df[0][0]
            newId = int(newId) + 1
            c.execute('INSERT INTO Neighborhood(OwnerID,Groceries,Church,EduLower,EduHigher,Retail,Entertainment) VALUES (?,?,?,?,?,?,?)',
                (newId, inputGroceries,inputChurch,inputEduLower,inputEduHigher,inputRetail,inputEntertainment))
            conn.commit()
            print("\nOwnerID Neighborhood Information Added!\n")
        if menu == "5":
            while True:
                try:
                    print("Please enter Date of Birth (MM-DD-YYYY Format)")
                    # inputMonth = int(input("Enter Month: "))
                    # inputDay = int(input("Enter Day: "))
                    # inputYear = int(input("Enter Year: "))
                    date_entry = input('Enter Date of Birth in YYYY-MM-DD format')
                    inputYear,inputMonth,inputDay = map(int, date_entry.split('-'))
                    inputDOB = datetime.date(inputMonth,inputDay,inputYear)
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputSex = str(input("Sex: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a String! ")
            while True:
                try:
                    inputOccupation = str(input("Occupation: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a String! ")
            while True:
                try:
                    inputIncomeYear = int(input("State: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputMaritalStatus = str(input("Marital Status: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must a String! ")
            while True:
                try:
                    inputChildren = str(input("Number of Children: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            nStudentID = c.execute('SELECT OwnerID from Owner where OwnerID = (SELECT max(OwnerID) from Owner) ').fetchall()
            df = pd.DataFrame(nStudentID)
            newId = df[0][0]
            newId = int(newId) + 1
            c.execute('INSERT INTO Owner(OwnerID,DOB,Sex,Occupation,IncomeYear,MaritalStatus,Children) VALUES (?,?,?,?,?,?,?)',
                (newId, inputDOB,inputSex,inputOccupation,inputIncomeYear,inputMaritalStatus,inputChildren))
            conn.commit()
            print("\nOwnerID Owner Information Added!\n")
        if menu == "6":
            while True:
                try:
                    inputInternet = int(input("Annual Internet Cost: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputWater = int(input("Annual Water Cost: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputElectricity = int(input("Annual Electric Cost: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputGas = int(input("Annual Gas Cost: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            while True:
                try:
                    inputWaste = int(input("Annual Waste Cost: "))
                    break
                except ValueError:
                    print("Incorrect Form. Must be a Number! ")
            nStudentID = c.execute('SELECT OwnerID from Utilities where OwnerID = (SELECT max(OwnerID) from Utilities) ').fetchall()
            df = pd.DataFrame(nStudentID)
            newId = df[0][0]
            newId = int(newId) + 1
            c.execute('INSERT INTO Utilities(OwnerID,Internet,Water,Electricity,Gas,Waste) VALUES (?,?,?,?,?,?)',
                (newId, inputInternet,inputWater,inputElectricity,inputGas,inputWaste))
            conn.commit()
            print("\nOwnerID Utilities Information Added!\n")
        if menu == "7":
                UserInterface1()
                quit()

def deleteOwnerID():
    print("\nPlease enter OwnerID of the house to delete."
        "\nPress B to go back ")
    nSID = input("input: ")

    check = c.execute('SELECT isDeleted FROM Address WHERE OwnerID = ?', (nSID,)).fetchall()

    if nSID == 'b':
        UserInterface1()
        quit()
    if check != []:
        print('\nThis house has already been deleted. \n')
        deleteOwnerID()
        quit()
    c.execute('SELECT * FROM Address WHERE OwnerID = ?', (nSID,))
    output = c.fetchall()
    #check if input valid
    if output == []:
        print("Invalid Input. Please Try Again.")
        deleteOwnerID()
    else:
        c.execute('UPDATE Address SET isDeleted = ? WHERE OwnerID = ?', (1,nSID))
        c.execute('UPDATE House SET isDeleted = ? WHERE OwnerID = ?', (1, nSID))
        c.execute('UPDATE Owner SET isDeleted = ? WHERE OwnerID = ?', (1, nSID))
        c.execute('UPDATE Utilities SET isDeleted = ? WHERE OwnerID = ?', (1, nSID))
        c.execute('UPDATE Mortgage SET isDeleted = ? WHERE OwnerID = ?', (1, nSID))
        c.execute('UPDATE Neighborhood SET isDeleted = ? WHERE OwnerID = ?', (1, nSID))
    conn.commit()
    print("Address Successfully Deleted")
    UserInterface1()


#UserInterface()

def plot():

    print("PLease enter the plot you would like to see: ")
    print("1. Value vs Size")
    print("2. Value vs Number of Bedrooms")
    print("3. Back")
    choice = input("Choice: ")

    if choice == '3':
        UserInterface2()
        quit()

    if choice == '1':
        df = DataFrame(c.execute('Select Value, Size from House').fetchall())
        df.columns = ['Value', 'Size']
        ax1 = df.plot(kind='scatter', x='Value', y='Size', color='blue', alpha=0.5, figsize=(10, 7))
        plt.show()
        plot()
    if choice =='2':
        df1 = DataFrame(c.execute('Select avg(Value), numBed from House Group By numBed').fetchall())
        df1.columns = ['AverageValue', 'NumberBedroom']
        # plt.bar(df1["NumberBedroom"].astype(str), df1["AverageValue"])
        df1["NumberBedroom"] =df1["NumberBedroom"].astype(str)
        ax2 = df1.plot(kind='bar', x = "NumberBedroom", y="AverageValue", color='blue', alpha=0.5, figsize=(10, 7))
        plt.show()
        plot()

# legend, title and labels.
def filter():
    print("\n1. Budget filter")
    print("2. Locational filter")
    print("3. Home Lay out filter")
    print("4. Compare Homes")
    print('5. Back')
    answer = input("\nPLease select which filter you'd like to apply: ")
    if answer =='5':
        UserInterface2()
        quit()
    if answer == '1':
        Min = input("Enter Minimum price: ")
        Max = input("Enter Maximum Price: ")
        df0 = DataFrame((c.execute('SELECT Address.OwnerID, Address.StreetNumber,Address.StreetName,Address.City,House.Value,House.Size,House.Pool,House.Garage,House.numBath,House.numBed FROM Address INNER JOIN House ON Address.OwnerID = House.OwnerID INNER JOIN Utilities ON House.OwnerID = Utilities.OwnerID WHERE Value BETWEEN ? and ?;',(Min,Max)).fetchall()))
        if df0.empty:
            print("Nothing could be found with these specifications. ")
            filter()
            quit()
        else:
            df0.columns = ['OwnerID', 'Street#', 'Street', 'City', 'Value', 'Size', 'Pool', 'Garage', 'NumBathroom', 'NumBedroom']
            print(df0)
            filter()
    if answer == '2':
        answer2 = input("Would you like to filter by city(Press C) or state(Press S): ")
        if answer2.lower() == 's':
            State = input("Please Enter the desired state you would like to filter by:")
            df = DataFrame(c.execute('SELECT Address.OwnerID, Address.StreetNumber,Address.StreetName,Address.City ,House.Value,House.Size,House.Pool,House.Garage,House.numBath,House.numBed FROM Address INNER JOIN House ON Address.OwnerID = House.OwnerID INNER JOIN Utilities ON House.OwnerID = Utilities.OwnerID WHERE Address.State == ?;',(State,)).fetchall())
            if df.empty:
                print("Nothing could be found with these specifications. ")
                filter()
                quit()
            else:
                df.columns = ['OwnerID', 'Street#', 'Street', 'City', 'Value', 'Size', 'Pool', 'Garage', 'NumBathroom','NumBedroom']
                print(df)
                filter()
        elif answer2.lower() == 'c':
            city = input("Please Enter the desired city you would like to filter by:")
            df1 = DataFrame(c.execute('SELECT Address.OwnerID, Address.StreetNumber,Address.StreetName,Address.State ,House.Value,House.Size,House.Pool,House.Garage,House.numBath,House.numBed FROM Address INNER JOIN House ON Address.OwnerID = House.OwnerID INNER JOIN Utilities ON House.OwnerID = Utilities.OwnerID WHERE Address.City == ?;',(city,)).fetchall())
            if df1.empty:
                print("Nothing could be found with these specifications. ")
                filter()
                quit()
            else:
                df1.columns = ['OwnerID', 'Street#', 'Street','State', 'Value', 'Size', 'Pool', 'Garage', 'NumBathroom','NumBedroom']
                print(df1)
                filter()
        else:
            print("Incorrect Input ")
            filter()
    if answer == '3':
        sqftmin = input("Please enter your minimum square footage: ")
        sqftmax = input("Please enter your maximum square footage: ")
        rooms = input("Please enter your desired number of rooms: ")
        bathrooms = input("Please enter your desired number of bathrooms: ")
        pool = input("Would you like a pool(Type 1 for yes and 0 for no):")
        garage = input("Would you like a garage(Type 1 for yes and 0 for no):")
        df2 = DataFrame(c.execute('SELECT Address.OwnerID, Address.StreetNumber,Address.StreetName, Address.City,House.Value,House.Size,House.Pool,House.Garage,House.numBath,House.numBed FROM Address INNER JOIN House ON Address.OwnerID = House.OwnerID INNER JOIN Utilities ON House.OwnerID = Utilities.OwnerID WHERE House.Size between ? and ? and House.numBed >= ? andHouse.numBath >= ? and House.Pool = ? and House.Garage = ?;', (sqftmin, sqftmax, rooms, bathrooms, pool, garage)).fetchall())
        if df2.empty:
            print("\nNothing could be found with these specifications. ")
            filter()
            quit()
        else:
            df2.columns = ['OwnerID', 'Street#', 'Street', 'City', 'Value', 'Size', 'Pool', 'Garage', 'NumBathroom',
            'NumBedroom']
            print(df2)
            filter()
            quit()
    if answer == '4':
        print(
            "\nThe compare home function allows you to find housing all of over the USA with around the same value as your current house. ")
        CityC = input("Please Enter your current city:")
        dfGG = DataFrame(c.execute(
            "Select Address.StreetNumber,Address.StreetName,Address.City,Address.State,Address.Zipcode,House.Value FROM House JOIN Address ON House.OwnerID = Address.OwnerID where Value <= (SELECT avg(House.Value) FROM House JOIN Address ON House.OwnerID = Address.OwnerID WHERE Address.City == ? )",
            (CityC,)).fetchall())
        dfGG.columns = ['StreetNumber', 'StreetName', 'City', 'State', 'ZipCode', 'Value']
        print(dfGG)
        filter()
        quit()


def demographics():
    print(" Please choose Financial Demographics by:")
    print("1. City ")
    print("2. State ")
    print('3. Back')
    answer = input("Please choose: ")
    if answer == '1':
        df = DataFrame(c.execute('SELECT avg(House.Value),avg(Owner.IncomeYear),count(Address.StreetName),Address.City FROM House INNER JOIN Address ON Address.OwnerID = House.OwnerID INNER JOIN Owner ON House.OwnerID = Owner.OwnerID GROUP BY Address.City;').fetchall())
        df.columns = ['Average House Value', 'Average Income', 'Amount of Properties', 'City']
        print(df)
        demographics()
        quit()
    if answer == '2':
        df1 = DataFrame(c.execute('SELECT avg(House.Value),avg(Owner.IncomeYear),count(Address.StreetName),Address.State FROM House INNER JOIN Address ON Address.OwnerID = House.OwnerID INNER JOIN Owner ON House.OwnerID = Owner.OwnerID GROUP BY Address.State;').fetchall())
        df1.columns = ['Average House Value', 'Average Income', 'Amount of Properties', 'State']
        print(df1)
        demographics()
        quit()
    if answer == '3':
        UserInterface2()
        quit()

UserInterface()