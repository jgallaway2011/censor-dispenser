# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#Functions
def censor_text(email, text_to_censor):
    if text_to_censor in email:
        email_censored = email.replace(text_to_censor, "*" * len(text_to_censor))
    return email_censored

#Function Calls
print(censor_text(email_one, "learning algorithms"))