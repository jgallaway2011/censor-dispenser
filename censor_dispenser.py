# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#List of text that should be censored
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

#List of negative words
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#Lists of Punctuation
punctuation_after = [" ", ",", "!", "?", ".", "%", "/", ")"]
punctuation_before = ["("]

#Functions

#Takes text input that will be censored only for letters. Spaces and punctuation will remain as is. 
# The censored text is returned.
def censor_format(text_to_censor):
    censored_text = ""
    for i in range(len(text_to_censor)):
        if text_to_censor[i] in punctuation_after or text_to_censor[i] in punctuation_before:
            censored_text += text_to_censor[i]
        else:
            censored_text += "*"
    return censored_text

#Takes in email text and will censor for text provided by the user upon calling the function.
def censor_text(email, text_to_censor):
    censored_text = censor_format(text_to_censor)
    return email.replace(text_to_censor, censored_text)

#Takes in email text and will censor for a list of words.  The function is built to handle capitalization and uses surrounding
#punctuation/spaces to ensure that a censored word is not removed from a larger word.
def censor_text_with_list(email, list_of_text_to_censor):
    list_of_text_to_censor_edited = []
    for text in list_of_text_to_censor:
        text_titled = text.title()
        for punctuation in punctuation_after:
            text_with_punctuation = text + punctuation
            text_titled_with_punctuation = text_titled + punctuation
            list_of_text_to_censor_edited.append(text_with_punctuation)
            list_of_text_to_censor_edited.append(text_titled_with_punctuation)
        for punctuation in punctuation_before:
            text_with_punctuation = punctuation + text
            text_titled_with_punctuation = punctuation + text_titled
            list_of_text_to_censor_edited.append(text_with_punctuation)
            list_of_text_to_censor_edited.append(text_titled_with_punctuation)
    for text in list_of_text_to_censor_edited:
        censored_text = censor_format(text)
        email = email.replace(text, censored_text)
    return email

#Function Calls

#Test for censor_text function
#print(censor_text(email_one, "learning algorithms"))

#Test for censor_text_with_list function
print(censor_text_with_list(email_two, proprietary_terms))