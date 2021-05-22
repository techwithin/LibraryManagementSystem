import pandas as pd
from .models import *


def populating():
    data = pd.read_csv("./NoDuplicates.csv")
    # data = data.drop_duplicates(subset=['bookname'])
    # index = data.index
    # lines = len(index)
    # print(data)
    # print(lines)
    # print(data.loc['bookname'])

    j = 0
    while(1):
        book = Books(
        acc_no = data['acc_no'][j],
        book_name = data['bookname'][j],
        authorname = data['authorname'][j],
        authorsmark = data['authorsmark'][j],
        copy_no = data['copy_no'][j],
        user_id = data['user_id'][j],
        publisher_name = data['publisher_name'][j],
        # date_of_pub = data['date_of_pub'][j],
        # date_of_acc = data['date_of_acc'][j],
        source = data['source'][j],
        bill_no = data['bill_no'][j],
        # date_of_bill = data['date_of_bill'][j],
        price = data['M:M'][j],
        )
        book.save()
        j = j+1
        if(j == 24):
            break
        


        
        


