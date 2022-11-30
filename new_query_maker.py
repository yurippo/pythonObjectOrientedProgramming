# Python
# using lambda() function combined
# with map() function
#email_list = ["
#ssl.rengaw@gmail.com,inayara.o@gmail.com,danilo.vieira92@gmail.com"]
#now gonna get email_list from the input ;)

input_string = input("Enter your list of emails separated by comma:")

email_list = input_string.split(",")
# here we want to strip  all the emails
#  change them to lower case and return a clean list
email_stripped_list = tuple(map(str.strip, email_list))
final_email_list = tuple(map(lambda email: str.lower(email), email_stripped_list))
print(f"SELECT * FROM `AccessUserCompanyData` WHERE `email` IN {final_email_list} LIMIT 50")