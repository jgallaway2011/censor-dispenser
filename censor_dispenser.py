# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#Terms that should be censored
proprietary_terms = [" she", " personality matrix ", " sense of self ", " self-preservation ", " learning algorithms ", " her ", " herself "]

#Functions
def censor_format(text_to_censor):
    censored_text = ""
    for i in range(len(text_to_censor)):
        if text_to_censor[i] == " ":
            censored_text += " "
        else:
            censored_text += "*"
    return censored_text

def censor_text(email, text_to_censor):
    censored_text = censor_format(text_to_censor)
    return email.replace(text_to_censor, censored_text)

def censor_text_with_list(email, list_of_text_to_censor):
    for text in list_of_text_to_censor:
        censored_text = censor_format(text)
        email = email.replace(text, censored_text)
    return email

#Function Calls
#print(censor_text(email_one, "learning algorithms"))
print(censor_text_with_list(email_two, proprietary_terms))