
from bottle import run, request, route
import sqlite3
import re


@route("/")
def index():
    return ("Welcome to the palindrome app")
    
@route("/palindrome/<input_s>", methods=["GET"])
def create_palindrome(input_s):
    conn = sqlite3.connect('palindrome.db')
    c = conn.cursor() 
    input_str = input_s.strip().lower()
    c.execute("CREATE TABLE IF NOT EXISTS palindrome (id INTEGER PRIMARY KEY, input_string char(50) NOT NULL, status bool NOT NULL)")

    if input_str == input_str[::-1]: 
        c.execute("SELECT * FROM palindrome WHERE input_string = ?",(input_str, ))
        results = c.fetchall()
        if not results:
            c.execute("INSERT INTO palindrome(input_string, status) VALUES(?,?)",(input_s, 1))
            input_str_id = c.lastrowid
            conn.commit()
            c.close()
            return {"msg" : f"The word {input_s } is a palindrome! It was inserted into the database, the ID is { input_str_id}", "status" : 1 }
        else:
            return { "msg" : f"The word {input_str } is already in the database!", "status" : 0 }
    else:
        return {"msg": f"The word {input_str }  is not a palindrome", "status" : 0 }
    
@route("/palindromes", method="POST")
def create_palindrome_from_file():
    upload = request.files.get('upload_file')
    print(upload)
    file_path = "./palindrome.txt"
    upload.save(file_path) 
    results = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_word = line.strip()
            lower_case_word = stripped_word.lower()
            formatted_word = re.sub(r"[^\w]","", lower_case_word ) # remove all punctuation and spaces
            if formatted_word == formatted_word[::-1]:
                formatted_res = f"{stripped_word}|true"
                
            else:
                formatted_res = f"{stripped_word}|false"
            results.append(formatted_res)
                
    return {"is_palindrome_results": results}     

@route("/palindromes/history", method="GET")
def get_palindromes():
    conn = sqlite3.connect('palindrome.db')
    c = conn.cursor() 
    c.execute("SELECT input_string FROM palindrome")
    results = c.fetchall()
    output = []
    for res in results:
        output.append(res[0])
    return { "palindromes": output}

if __name__ == "__main__":
    run(reloader=True, debug=True)