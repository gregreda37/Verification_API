import csv
import os


class Methods(object):
    def contractorList(self):
        contractorEmailList = []
        # file_name = os.listdir("/Users/gregoryreda/Desktop/Database/drbill_contracting_new_jersey_email.csv/")
        file_name = os.listdir("/Users/gregoryreda/Desktop/Database/")
        
        count = 0
        try:
            while count < 50:
                with open('/Users/gregoryreda/Desktop/Database/'+ file_name[count], 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)
    
                    for line in csv_reader:
                        contractorEmailList.append(line[0])
                    count += 1
            return contractorEmailList
            
        except BaseException:
            print('No more Files')
            
        

        
            
            



