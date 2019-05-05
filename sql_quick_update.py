import sqlite3 as lite
from sqlite3 import Error
import sys


def create_connection(db_file):
    try:
        con = lite.connect(db_file)
        return con
    except Error as e:
        print(e)

    return None


def quick_update(con):

    cur = con.cursor()

    cur.execute(
# Combine all kentucky derby  and Star Wars day tweets into a supercategory
    # '''
    #     UPDATE table_name2
    #     SET column_2 = 'Kentucky Derby'
    #     WHERE column_2 = '#KentuckyDerby2019'
    #     OR column_2 = '#KyDerby'
    #     OR column_2 = '#KentuckyDerby145'
    #     OR column_2 = '#KentuckDerby';
    # '''
    #     UPDATE table_name2
    #     SET column_2 = '#MayThe4thBeWithYou'
    #     WHERE column_2 = '#StarWarsDay'
    #     OR column_2 = 'Star Wars'
    #     OR column_2 = 'May the 4th'
    '''
        UPDATE table_name2

                ''')

def main():
    database = 'C:/Users/warin/Desktop/APIs/Git Hub/twitterProject/my_db1.db'

    # create a database connection
    con = create_connection(database)
    with con:
        quick_update(con)
    con.commit()
if __name__ == '__main__':
    main()
