from flask import Flask,request
from collections import OrderedDict

app = Flask(__name__)
@app.route('/simple', methods = ['POST'])
def get_current_user():
    data = request.get_json(force=True)
    x = data['sms']
    arr = []
    food, travel, shopping, bill_payments, fd_arr, tr_arr, sp_arr, bp_arr = 0, 0, 0, 0, [], [], [], []
    for i in x:
        l1 = i['text'].split(" ")
        for j in l1:
            if "@" in j:
                x1 = j.split("@")
                if "swiggy" in x1[0] or "zomato" in x1[0]:
                    fd_arr.append(i)
                    food = food + float(l1[0][3:])
                elif "BBPSBP" in j:
                    bp_arr.append(i)
                    bill_payments = bill_payments + float(l1[0][3:])
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
