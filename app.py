from flask import Flask,request
from collections import OrderedDict

app = Flask(__name__)
@app.route('/simple', methods = ['POST'])
def get_current_user():
    data = request.get_json(force=True)
    x = data['sms']
    arr = []
    food, travel, shopping, bill_payments, fd_arr, tr_arr, sp_arr, bp_arr = 0, 0, 0, 0, [], [], [], []
    food_brand, bill_payments_type, travel_type, shopping_type = ["upiswiggy", "upizomato"], ["BBPSBP"], [], []
    for i in x:
        l1 = i['text'].split(" ")
        for j in l1:
            if "@" in j:
                x1 = j.split("@")
                if x1[0] in food_brand:
                    fd_arr.append(i)
                    food = food + float(l1[0][3:])
                elif x1[0] in bill_payments_type:
                    bp_arr.append(i)
                    bill_payments = bill_payments + float(l1[0][3:])
                elif x1[0] in travel_type:
                    tr_arr.append(i)
                    travel = travel + float(l1[0][3:])
                elif x1[0] in shopping_type:
                    sp_arr.append(i)
                    shopping = shopping + float(l1[0][3:])
    if food > 0:
        di = [("category", "Food"), ("totalAmount", str(food)), ("smsArray", fd_arr)]
        dic = OrderedDict(di)
        arr.append(dic)
    if bill_payments > 0:
        di = [("category", "Bill Payments"), ("totalAmount", str(bill_payments)), ("smsArray", bp_arr)]
        dic = OrderedDict(di)
        arr.append(dic)
    if travel > 0:
        di = [("category", "Travel"), ("totalAmount", str(travel)), ("smsArray", tr_arr)]
        dic = OrderedDict(di)
        arr.append(dic)
    if shopping > 0:
        di = [("category", "Shopping"), ("totalAmount", str(shopping)), ("smsArray", sp_arr)]
        dic = OrderedDict(di)
        arr.append(dic)
    res_dic = {}
    res_dic["summary"] = arr
    return res_dic

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
