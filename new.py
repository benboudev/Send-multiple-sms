import androidhelper   
droid=androidhelper.Android()
droid.smsSend('messageplusgroupnumber','#name REMINDER ')     
person = {
   'man ':'1234567890', 
   }
for key, value in person.items():
    droid.smsSend(value,"hi "+key+"  Your bed is waiting for you and your pillow is ready to get smashed, let's go asleep early and have a successful day tomorrow, good night. ")           
droid.smsSend('messageplusgroupnumber','#name username')

