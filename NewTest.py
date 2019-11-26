import firebase_admin
import csv
import sys
import smtplib
from Contractors import Contractors
from Methods import Methods
from firebase_admin import credentials, firestore
cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


class Main(object):
    uid_list = []

#List of approved emails
    contractorEmailList = Methods().contractorList()

#list of contractor unverified emails
    emailList = []

# print(contractorEmailList)
    def setDocId(self):
        docs = db.collection(u'contractorprofiles').where(u'verified', u'==', False).stream()

        for doc in docs:
            uid_list.append(doc.id)

    print(uid_list)

    list_count = 0

    def checkStatus(self):
        # global list_count
        try:
            while list_count <= len(uid_list):
                doc_ref = db.collection(u'contractorprofiles').document(uid_list[list_count])
                doc = doc_ref.get()
                contractors = Contractors.from_dict(doc.to_dict())
                emailList.append(contractors.email)
                list_count += 1

        except IndexError:
            print("End of List")

    
# print(emailList)

    notVerified = []
    verified = []

    email_count = 0

    def isVerified(self):
        # global email_count 
        try:
            while email_count <= len(uid_list):
                if emailList[email_count] in contractorEmailList:
                    print(emailList[email_count] + " is in list")
                    email_count += 1
                    verified.append(emailList[email_count])
                else:
                    print(emailList[email_count] + " contractor is not in list")
                    notVerified.append(emailList[email_count])
                    email_count += 1
                
        except IndexError:
            print("List has Ended: Contractors with valid emails have been updated")

    

    print(verified)
    print(notVerified)


    final_count = 0

    def final_step(self):
        # global final_count
        try:
            while final_count <= len(verified):
                docs = db.collection(u'contractorprofiles').where(u'projectEmail', u'==', verified[final_count]).stream()
                for doc in docs:
                    print("Status change to verified "+ verified[final_count])
                    city_ref = db.collection(u'contractorprofiles').document(doc.id)
                    city_ref.update({u'verified': True})
                    final_count += 1
        except IndexError:
            print("No more Verified profiles")

    

