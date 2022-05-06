from flask import Flask

app= Flask(__name__)


# In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:

# /welcome
# Returns “welcome”
# 
# /welcome/home
# Returns “welcome home”
# 
# /welcome/back
# Return “welcome back”
# Once you’ve finished this, run the tests for it:



@app.route('/welcome')
def say_welcome():
    return "welcome"


@app.route('/welcome/home')
def welcomeHome():
    # html = """
    # <html>
    #     <body>
    #         <h1> Welcome home! </h1>
    #         <p>welcome home</p>
    #     </body>
    # </html> 
    # """
    return "welcome home"  


@app.route('/welcome/back')
def welcomeBack():
    # html = """
    # <html>
    #     <body>
    #         <h1> Welcome back! </h1>
    #         <p>welcome back</p>
    #     </body>
    # </html> 
    # """
    return "welcome back"



