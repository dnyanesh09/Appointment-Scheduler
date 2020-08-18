from flask import Flask, request, jsonify
import json
from flask_cors import cross_origin
from exchangelib import fields,properties,DELEGATE,protocol,services, Account, Credentials, CalendarItem, EWSDateTime, EWSTimeZone, Attendee, Mailbox,EWSTimeZone, EWSDateTime, EWSDate
from exchangelib.items import MeetingRequest, MeetingCancellation, SEND_TO_ALL_AND_SAVE_COPY
# from exchangelib.util import to_xml
from exchangelib.version import Version


from credentials import password,userid
# import exchangelib.services
app = Flask(__name__)

usrData = {}
account = ""

@app.route("/chat" , methods = ['POST'])
@cross_origin(origin='*')
def chat():
    req = request.json
    # message = req['msg']
    userdata = {
    "stage" : req['stage'],
    "uname" : req['uname'],
    "email" : req['email'],
    "phone" : req['phone'],
    "year"  : req["year"],
    "month" : req["month"],
    "date"  : req["date"],
    "hours" : req["hours"],
    "mins"  : req["mins"]
    }
    print("Complete Request : ", req)
    response = {}
    # if (stage == 1):
    #     opstr = "How May i help you ? "+"Book An Appointment "
    #     response['respMsg'] = opstr
    # # response['respMsg'] = "Welcome to Appointment Scheduler"
    sendInvite(userdata)
    response = json.dumps(response)
    return response

    print("Hello World")

def sendInvite(userdata):
    tz = EWSTimeZone.localzone()
    cal = CalendarItem(
        folder=account.calendar,
        start=tz.localize(EWSDateTime(userdata['year'], userdata['month'], userdata['date'], userdata['hours'], userdata['mins'])),
        end=tz.localize(EWSDateTime(userdata['year'], userdata['month'], userdata['date'], userdata['hours']+1, userdata['mins'])),
        subject='Appointment Scheduled With '+userdata['uname'],
        body='Appointment for enquiry with '+ userdata['uname'] + " Contact Number for user is : "+ userdata['phone'],
        location='Online meeting room',
        required_attendees=[Attendee(
            mailbox=Mailbox(email_address='dnyaneshnawale9@outlook.com'),
            response_type='Accept'
        ),
            Attendee(
                mailbox=Mailbox(email_address=userdata['email']),
                response_type='Accept'
            ),
            Attendee(
                mailbox=Mailbox(email_address="dnyaneshnawale9@gmail.com"),
                response_type='Accept'
            )
        ]

    )

    print(cal.save(send_meeting_invitations=SEND_TO_ALL_AND_SAVE_COPY))

    # print(my_account)
def generate_Acc():
    tz = EWSTimeZone.localzone()
    credentials = Credentials(username= userid, password= password)
    my_account = Account(primary_smtp_address=userid, credentials=credentials, autodiscover=True,
                         access_type=DELEGATE)

    global account
    account = my_account
    # services.GetUserAvailability

    # for calendar_item in my_account.calendar.filter(start__lt=tz.localize(EWSDateTime(2020, 7, 10+1 )),end__gt=tz.localize(EWSDateTime(2020, 8, 3))):
    #     print(calendar_item)


    # items = my_account.calendar.filter(
    #     start__lt=tz.localize(EWSDateTime(2020, 7, 10 )),
    #     end__gt=tz.localize(EWSDateTime(2020, 12, 31)),
    #     # categories__contains=['foo', 'bar'],
    # )
    # for item in items:
    #     print(item.start, item.end, item.subject, item.body, item.location)


def get_other_info ():
    tz = EWSTimeZone.localzone()
    end = tz.localize(EWSDateTime(2020,8,30))
    start = tz.localize(EWSDateTime.now())
    # Create a list of (account, attendee_type, exclude_conflicts) tuples
    # services.get_user_availability()
    accounts = [("dnyaneshnawale9@outlook.com", 'Required',False )]

    # ("dnyaneshnawale9@outlook.com", 'Required', False)
    # properties.FreeBusyView.__dict__
    freeBusyView = list(account.protocol.get_free_busy_info(accounts=accounts, start=start, end=end))
    # fields.EWSElementListField.value_cls
    # print("freeBusyView : ", get_user_availability.GetUserAvailability.get_payload(freeBusyView))
    print(" FreeBusyView : ",freeBusyView )
    print("Type of freeBusyView : ", type(freeBusyView[0]))


    for i in freeBusyView:
        # print(properties.FreeBusyView().)
        # print(type(i))
        print("Calener Eveents : ",i)
        print("Calender events 2 : ",i.calendar_events)
        kk=i.calendar_events
        if kk != None:
            for k in kk:
                print("Calender Details : ")
                print("ELEMENT_NAME : ",k.ELEMENT_NAME)
                print(" busy_type : ",k.busy_type)
                print("details : ", k.details)
                print("subject : ", k.details.subject)
                print("end : ",k.end)
                print("start : ", k.start)
        else:
            print("Calender Details : No appointment found")

    #     tt= i.get_field_by_fieldname("calendar_events")
    #     print("tt : ",tt.__dict__)
    #     # properties.EWSElementListField.field_uri_postfix
    #     print("tt DATA : ",tt.field_uri_postfix)
    #     print("type of tt : ", type(tt))
    #     properties.CalendarEvent.get_field_by_fieldname("start")
    #     print("Start : ",tt.value_cls.get_field_by_fieldname("start"))
    #     # tt2 = tt.properties.CalendarEvent()
    #     print(" Cal 2 : ", type(tt),"  ", tt.value_cls)
    #     print("Calender Event Fields : ",properties.CalendarEvent.FIELDS)
        # for j in list(i.get_field_by_fieldname('calendar_events')):
        #     print(j)
        # print(i.to_xml(version = 1.0))
    # print(freeBusyView ," ... ", type(freeBusyView))
    # sss =
    # print(account.protocol.get_free_busy_info.FIELDS)
    # for i in freeBusyView:
    #     print(i)
if __name__ == "__main__":
    generate_Acc()
    get_other_info()
    # app.run(host='localhost',port=7002,debug=True)
