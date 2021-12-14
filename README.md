# GULLAK ASSIGNMENT
REQUIREMENTS:
            pycharm.
SETUP INSTRUCTIONS:
            --> creaing a new project in PYCHARM provides an environment for the target application.
            --> This API requires packages namely flask and collections.so, that we have to install packages for this interpreter.
            --> Flask is a web framework.It provides you with tools, libraries and technologies that allow you to build a web application.
DESCRIPTION:
            -->It is a JSON API which takes a list of SMS as input and returns a spend summary in the response.
SAMPLE INPUT-1:
{
"sms":[{ "time" : "12-12-2021", "sender" : "AD-KOTAKB", "text" : "Rs.470.82
is debited from Kotak Bank a/c XXXX4685 to BBPSBP@ybl on 10-12-21. To
report fraud/raise dispute, click kotak.com/fraud. New balance: Rs.
19,050.35" }
,{ "time" : "12-12-2021", "sender" : "AX-KOTAKB", "text" : "Rs.103.00 is
debited from Kotak Bank a/c XXXX4685 to upiswiggy@icici on 12-12-21. To
report fraud/raise dispute, click kotak.com/fraud. New balance: Rs.
18,753.75" }
,{ "time" : "12-12-2021", "sender" : "AX-KOTAKB", "text" : "Rs.210.00 is
debited from Kotak Bank a/c XXXX4685 to upiswiggy@icici on 12-12-21. To
report fraud/raise dispute, click kotak.com/fraud. New balance: Rs.
18,543.75" }
]
}
SAMPLE OUTPUT-1:
{ "summary":
[ { "category" : "Bill Payment"
, "totalAmount" : "470.82"
, "smsArray" : [{ "time" : "12-12-2021", "sender" : "AD-KOTAKB", "text" :
"Rs.470.82 is debited from Kotak Bank a/c XXXX4685 to BBPSBP@ybl on
10-12-21. To report fraud/raise dispute, click kotak.com/fraud. New balance:
Rs. 19,050.35" }]
}
, { "category" : "Food"
, "totalAmount" : "313.00"
, "smsArray" : [{ "time" : "12-12-2021", "sender" : "AX-KOTAKB", "text" :
"Rs.103.00 is debited from Kotak Bank a/c XXXX4685 to upiswiggy@icici on
12-12-21. To report fraud/raise dispute, click kotak.com/fraud. New balance:
Rs. 18,753.75" }
, { "time" : "12-12-2021", "sender" : "AX-KOTAKB", "text" : "Rs.210.00 is
debited from Kotak Bank a/c XXXX4685 to upiswiggy@icici on 12-12-21. To
report fraud/raise dispute, click kotak.com/fraud. New balance: Rs.
18,543.75" }]
}
]
}
SAMPLE INPUT-2:
{
"sms":[{ "time" : "12-12-2021", "sender" : "AD-KOTAKB", "text" : "Rs.470.82
is debited from Kotak Bank a/c XXXX4685 to BBPSBP@ybl on 10-12-21. To
report fraud/raise dispute, click kotak.com/fraud. New balance: Rs.
19,050.35" }
]
}
SAMPLE-OUTPUT-2:
{
  "summary": [
    {
      "category": "Bill Payments",
      "totalAmount": "470.82",
      "smsArray": [
        {
          "sender": "AD-KOTAKB",
          "text": "Rs.470.82 is debited from kotak bank a/c XXXX4685 to BBPSBP@ybl on 10-12-21.To report fraud/raise dispute,click kotak.com/fraud.New Balance: Rs.19,050.35",
          "time": "12-12-2021"
        }
      ]
    }
  ]
}
