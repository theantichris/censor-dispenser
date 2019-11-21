email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_phrase(text, phrase):
    return text.replace(phrase, "RECACTED")

print(censor_phrase(email_one, proprietary_terms[4]))

def censor_phrases(text, phrases):
    for phrase in phrases:
        text = censor_phrase(text, phrase)
    return text

print(censor_phrases(email_two, proprietary_terms))