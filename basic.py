import re
import sys
import pdfplumber


# matches with expr,
def matchSub(expr, text):
    matches = re.findall(expr, text)
    cleaned = re.sub(expr, "", text)
    # return the first match if it exists along with the cleaned text
    return matches[0] if len(matches) else "", cleaned


def get_gpa(text):
    expr = r"[1-4](?:\.[0-9]{1,2})\/4"
    return matchSub(expr, text)

def get_phone(text): 
    expr = r"(?:\(\d{3}\)\s?\d{3}-\d{4}|\(\d{3}\)-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})"
    return matchSub(expr, text)

def get_email(text):
    expr = r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9._%+\-]+[A-Za-z]{2,}"
    return matchSub(expr, text)

def get_dates(text): 
    expr = r"\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|(?:Janurary|Febraury|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})"
    return matchSub(expr, text)
def get_linkedin(text): 
    expr = r"linkedin\.com/in/[A-Za-z0-9_\-]+/?"
    return matchSub(expr, text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("give resume path")
        exit(1)
    name = sys.argv[1]
    with pdfplumber.open(name) as pdf:
        text = pdf.pages[0].extract_text()
        
        # html = displacy.render(analyzer.get_doc(text), style = "ent", jupyter = False)
        

        gpa, text = get_gpa(text)
        phone, text = get_phone(text)
        email, text = get_email(text)
        dates, text = get_dates(text)
        linkedin, text = get_linkedin(text)
        print("gpa", gpa)
        print("phone", phone)
        print("email", email)
        print("dates", dates)
        print("linkedin", linkedin)
        print(text)
