from Methods import Methods
from Email import Email
import runpy
import sched, time

s = sched.scheduler(time.time, time.sleep)

# contractorEmailList = Methods().contractorList()
# runpy.run_path(path_name='main.py')
# print(len(contractorEmailList))

count = 0

def do_something(sc): 
    try:
        runpy.run_path(path_name='main.py')
        global count
        print(count)
        count+=1
        print('Working')

        if count == 5:
            print('Days verification finished')
            Email.email_when_complete('')
            count = 0
    except BaseException:
        print("Error found: Please check API")
        Email.email_when_error('')

    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()

