def greetings():
    
    print( """

    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """)

def read_template(filePath):
    with open(filePath) as target_file:
        file_contents = target_file.read()
        return file_contents


#def parse_template(result):








#def merge():
