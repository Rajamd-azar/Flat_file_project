import pandas as pd
from classes import constants
from classes.validating_detail import Validation



def get_dataframe():
    df = pd.read_csv(constants.PATH)
    print(df)

    return df

def get_employee_details(df):
    print(df)

def update_employee_details(df,name,department):
    df.loc[df.index[(df['name'] == name)],'department'] = department
    df.to_csv(constants.PATH,index=False)
    print("Updated successfully")

def insert_employee_details(df,name,department,b_month,rating):
    df = pd.DataFrame([[name,department,b_month,rating]],columns=['name','department','birthday month','rating'])
    df.to_csv(constants.PATH,mode='a',index=False,header=False)
    print("Inserted successfully")

def delete_employee_details(df,name):
    df.drop(df.index[(df['name'] == name)],axis=0,inplace=True)
    df.to_csv(constants.PATH,index=False)
    print("Deleted successfully")

if __name__ == "__main__":

    try:
        print("Flat File database")

        while True:
            df = pd.read_csv(constants.PATH, error_bad_lines=False)

            print("1.Get Employee details\n2.update employee details\n3.Insert employee details\n4.delete employee details\n5.Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                get_employee_details(df)

            elif choice ==2:
                name= input("Enter employee name: ")
                department = input("Enter which department want to change: ")
                update_employee_details(df,name,department)

            elif choice ==3:
                name = input("Enter Employee name: ")
                department = input("Enter Department: ")
                b_month = Validation().validate_birthday_month(input("Enter birthday month: "))
                rating = Validation().validate_rating(input("Enter Rating: "))

                insert_employee_details(df,name,department,b_month,rating)

            elif choice == 4:
                name = input("Enter employee name: ")

                delete_employee_details(df,name)

            elif choice ==5:
                break
            else:
                print("Enter valid choice")
                continue


    except ValueError as e :
        print(e)
    except FileNotFoundError:
        df = pd.DataFrame([['','','','']],columns=['name','department','birthday month','rating'])
        df.to_csv(constants.PATH,index=False)
