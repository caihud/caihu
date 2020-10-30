from datetime import datetime

from twilio.rest import Client 
 
account_sid = 'AC517caa4acbc1d0a4e36efcaa5c7524ba' 
auth_token = '4811ee23e9cfc81d38f27df650426f6e' 
client = Client(account_sid, auth_token) 

from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Teste de automação via Twilio',      
                              to='whatsapp:+5511992051752' 
                          ) 
 
    print(message.sid)

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'cron', hour='0-12')

sched.start()