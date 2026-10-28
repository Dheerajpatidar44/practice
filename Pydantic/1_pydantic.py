def insert_patient_data(name: str, age: int):

    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError('Incorrect age')
        else:
            print(name)
            print(age)
            print('inserted to database ')
    else: 
        raise TypeError('Incorrect data types')

def update_patient_data(name: str, age: int):

    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('updated to database ')
    else: 
        raise TypeError('Incorrect data types')

insert_patient_data('dheeraj', 30)

# ye problem aati he pyhton me type validation ke liye 
# isko solve karne ke liye hum pydantic ka use krte he 


