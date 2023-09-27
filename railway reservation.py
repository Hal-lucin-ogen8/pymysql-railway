import pymysql as ch  # To connect to MySql

conn = ch.connect(host='localhost', user="root", passwd='123456', database='railway',
                  autocommit=True)  # my password is 123456

'''if conn.is_connected()==1:
    print("Database connection successful.")
else:
    print("Database connection unsuccessful.")'''

cur = conn.cursor()
i = 0


def railsmenu():
    print("\n-------------------------")
    print(" Railway Reservation ")
    print("-------------------------")
    print("1.Train Detail")
    print("2.Reservation of Ticket")
    print("3.Cancellation of Ticket")
    print("4.Display ticket")
    print("5.For adding in train detail")
    print("6.For obtaining coach info of a train")
    print("7.Quit")

    n = int(input("\nEnter your choice : "))
    if (n == 1):
        train_detail()
    elif (n == 2):
        reservation()
    elif (n == 3):
        cancel()
    elif (n == 4):
        displayPNR()
    elif (n == 5):
        train()
    elif (n == 6):
        coach_info()
    elif (n == 7):
        return None
    else:
        print(" wrong choice ")
        railsmenu()


def train_detail():
    # function to show train details

    l = []
    a = str(input("Enter your starting point : "))
    b = str(input("Enter your destination : "))
    l.append(a)
    l.append(b)
    sql = "select * from train_detail where starting_point=%s and destination=%s"
    cur.execute(sql, l)
    f = cur.fetchall()
    l = len(f)
    print('\n*** TRAIN DETAILS ***')
    print(
        "------------------------------------------------------------------------------------------------------------------")
    print('Train no.'.ljust(10), 'cost'.ljust(10), 'via'.ljust(10), 'time'.ljust(10), 'days'.ljust(15),
          'Coach1'.ljust(8), 'Coach2'.ljust(8), 'Coach3'.ljust(8), 'Coach4'.ljust(8), 'Coach5'.ljust(8),
          'Coach6'.ljust(8))
    for j in range(0, l):
        print(str(f[j][0]).ljust(10), str(f[j][1]).ljust(10), f[j][4].ljust(10), f[j][5].ljust(10), f[j][6].ljust(15),
              str(f[j][7]).ljust(8), str(f[j][8]).ljust(8), str(f[j][9]).ljust(8), str(f[j][10]).ljust(8),
              str(f[j][11]).ljust(8), str(f[j][12]).ljust(8))
    print(
        "------------------------------------------------------------------------------------------------------------------")
    railsmenu()


def reservation():
    # function for reservation of ticket

    print("\nEnter YOUR INFORMATION AS FOLLOWS : \n")
    l = []
    l1 = []
    global i
    i += 1
    l.append(i)
    a = str(input("Enter passenger's name : "))
    l.append(a)

    b = str(input("Enter passenger age : "))
    l.append(b)
    c = str(input("Enter passenger gender M/F/O : "))
    l.append(c)
    d = int(input("Enter train_no : "))

    l.append(d)
    l1.append(d)
    e = "select starting_point,destination from train_detail where train_no=%s"
    cur.execute(e, l1)
    f = cur.fetchall()
    w = f[0]
    x = w[0]
    t = w[1]
    print(x, ' ----> ', t)
    l.append(x)
    l.append(t)
    coach = str(input('Enter coach number : '))
    coach = 'coach' + coach
    l.append(coach)
    g = "insert into user_information(unique_id,uname,age,gender,train_no,starting_point,destination,coach) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(g, l)
    Z = "select cost from train_detail where train_no=%s"
    cur.execute(Z, l1)
    n = cur.fetchall()
    print("\n-------------------------")
    print("you have to pay : ", n[0][0])
    print('Your unique ID is ', i)
    cur.execute('update train_detail set {} = {} -1 where train_no={}'.format(coach, coach, d))
    print('Your ticket has been booked.')
    print("-------------------------\n")
    railsmenu()


def cancel():
    # function for cancellation of ticket

    try:
        a = int(input("Enter Unique_id Provided : "))
        print()
        cur.execute('select train_no, coach from user_information where unique_id={}'.format(a))
        k = cur.fetchone()
        coach = k[1]
        train = k[0]
        cur.execute('select cost from train_detail where train_no={}'.format(train))
        m = cur.fetchone()
        print('Your refund amount is Rs. ', m[0] * 0.2)
        frog = int(input('Do you wish to confirm ticket cancellation? 1.Yes 2.No '))
        if frog == 1:
            cur.execute('update train_detail set {} = {} +1 where train_no={}'.format(coach, coach, train))
            b = "delete from user_information where unique_id={}".format(a)
            cur.execute(b)
            print("YOUR TICKET IS CANCELLED")
        elif frog == 2:
            print('Your ticket has NOT been cancelled.')
        else:
            print('Wrong input')


    except:
        print('Sorry that ticket does not exist. Please retry.')
    railsmenu()


def displayPNR():
    # function to display PNR status

    l = []
    a = int(input("Enter Unique_id Provided : "))
    l.append(a)
    sql = "select * from user_information where unique_id=%s"
    cur.execute(sql, l)
    x = cur.fetchone()
    if x:
        print(
            "\n------------------------------------------------------------------------------------------------------------------")
        print('unique_id'.ljust(10), 'name'.ljust(20), 'age'.ljust(10), 'gender'.ljust(8), 'train'.ljust(8),
              'start point'.ljust(15), 'destination'.ljust(15), 'coach'.ljust(8))
        print(str(x[0]).ljust(10), x[1].ljust(20), str(x[2]).ljust(10), x[3].ljust(8), str(x[4]).ljust(8),
              x[5].ljust(15),
              x[6].ljust(15), x[7].ljust(8))
        print(
            "------------------------------------------------------------------------------------------------------------------")

    else:
        print('\nSorry that ticket does not exist. Please retry.')

    railsmenu()


def train():
    # Function To Add Train Details

    print("Train Details")
    ch = 'y'
    while (ch == 'y'):
        l = []
        tnum = int(input("Enter Train_no : "))
        l.append(tnum)
        ac1 = float(input("Enter ticket cost : "))
        l.append(ac1)
        ac2 = str(input("Enter Starting point Of Train : "))
        l.append(ac2)
        ac3 = str(input("Enter train's destination : "))
        l.append(ac3)
        slp = str(input("Enter via : "))
        l.append(slp)
        e = str(input("Enter time of departure of train : "))
        l.append(e)
        f = str(input("Enter travel day : "))
        l.append(f)
        c1 = int(input('Enter number of available seats in coach 1 : '))
        l.append(c1)
        c2 = int(input('Enter number of available seats in coach 2 : '))
        l.append(c2)
        c3 = int(input('Enter number of available seats in coach 3 : '))
        l.append(c3)
        c4 = int(input('Enter number of available seats in coach 4 : '))
        l.append(c4)
        c5 = int(input('Enter number of available seats in coach 5 : '))
        l.append(c5)
        c6 = int(input('Enter number of available seats in coach 6 : '))
        l.append(c6)
        sql = "insert into train_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, l)

        print("insertion completed")
        print("Do you want to insert more train Detail?")
        ch = input("Enter y/n")
    print('\n' * 10)

    print("===================================================================")
    railsmenu()


def coach_info():
    # function to show coach information

    train = int(input('Enter train number : '))
    coach = int(input('Enter coach number : '))
    coach = 'coach' + str(coach)
    cur.execute('select {} from train_detail where train_no={}'.format(train, coach))
    k = cur.fetchone()
    print('Seats left in selected coach = ', k[0])
    cur.execute("select * from user_information where train_no={} and coach='{}'".format(train, coach))
    k = cur.fetchall()
    print('unique_id'.ljust(10), 'name'.ljust(20), 'age'.ljust(10), 'gender'.ljust(8), 'start point'.ljust(15),
          'destination'.ljust(15))
    for x in k:
        print(str(x[0]).ljust(10), x[1].ljust(20), str(x[2]).ljust(10), x[3].ljust(8), x[5].ljust(15), x[6].ljust(15))
    railsmenu()


a = railsmenu()
print('Thank you for using our services.')