def full_emails(people):
    result = []
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result
    
    
print(full_emails([("alex@example.com","Alex dieog"),("shay@example.com", "Shay brad")]))