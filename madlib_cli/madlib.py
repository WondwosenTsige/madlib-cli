import re
def greetings():
    
    print( """

    **************************************
        Welcome to the madlib game!
    
    
     Instructions to play this game   
    **************************************
    """)

def read_template(filePath):
    #Open and read a file
    with open(filePath, "r") as target_file:
        file_contents = target_file.read()
        return file_contents


def parse_template(string):
    #Find the string part and return tuple
    #Replace the string and return string
    stripped_words = tuple(re.findall(r"({\w*})", string))
    string = re.sub(r"\{.*?\}", "{}", string)
    print(string, stripped_words)
    return (string, stripped_words)


def merge(string, new):
    return string.format(*new)


