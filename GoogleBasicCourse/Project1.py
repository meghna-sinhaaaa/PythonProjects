"""
Problem Statement : Process a list of event objects using their attributes to generate a report that lists all users currently logged in to the machines.
Event class with attribues : date user machine type (all strings) we only care about login and logout
"""

def get_event_date(event):
    return event.date
    
def current_users(events):
    events.sort(key = get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.Type == "login":
            machines[event.machine].add(event.user)
        elif event.Type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine,users in machines.items():
        if len(users) >0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine,user_list))

class Event:
    def __init__(self,event_date,event_type,machine_name,user):
        self.date = event_date
        self.Type = event_type
        self.machine = machine_name
        self.user = user
        
events = [
    Event('2020-01-21 12:45:56' , 'login' , 'ms.local' , 'jordan'),
    Event('2020-01-22 15:53:42' , 'logout' , 'ws.local' , 'jordan'),
    Event('2020-01-21 18:53:21' , 'login' , 'ws.local' , 'lane'),
    Event('2020-01-22 10:25:34' , 'logout' , 'ms.local' , 'jordan'),
    Event('2020-01-21 08:20:01' , 'login' , 'ws.local' , 'jordan'),
    Event('2020-01-23 11:24:35' , 'login' , 'mail.local' , 'chris')
]

users = current_users(events)
print(users)
generate_report(users)