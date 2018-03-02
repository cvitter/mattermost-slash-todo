from flask import Flask
from flask import request
import json
import requests

__doc__ = """\
todo.py

"""

"""
Read the specified list from disk and return it as a
JSON object to the calling method
"""
def getList(channel):
    return json.load( open( channel + '.json' ) )

"""
formatListOutput - output the list of todo items in Mattermost markdown
"""
def formatListOutput(listJson):
    markdown = "TODO List for " + listJson["todo"]["owner_name"] + ":\n"
    markdown += "| ID | Done | Description | Due |\n"
    markdown += "|:-----|:-----:|:-----|-----:|\n"
    for listItem in listJson["todo"]["items"]:
        done = " "
        if listItem["done"]: done = "X"
        markdown += "| " + listItem["id"] + " | " + done + " | " + listItem["description"] + " | " + listItem["due"] + " |\n"
    return markdown

"""
------------------------------------------------------------------------------------------
Flask application below
"""

app = Flask(__name__)
 
@app.route( "/todo", methods = [ 'POST' ] )
def todo():
    
    response_type = "ephemeral" #or in_channel
    
    """
    Capture form fields from Mattermost post
    """
    channel_name = "" # Channel name
    channel_id = "" # ID of the channel to verify that we are calling the right channel todo
    user_id = "" # The Mattermost user that executed the slash command
    user_name = "" #
    
    if len(request.form) > 0:
        # Channel slash command called from
        channel_id = request.form["channel_id"]
        channel_name = request.form["channel_name"]
        # The user that called the slash command
        user_id = request.form["user_id"]
        user_name = request.form["user_name"]
        # "text" = body of slash command
        paramstring = request.form["text"]
        
    """
    
    """
    listrequested = "" # The list (channel or user) that was requested
    action = "" # add, edit, done, notdone, remove (list is default action and doesn't need to be specified)
    itemid = ""
    itemdetails = []
    
    """
    Parse the "text" field for channel, command and todo item details
    """
    listrequested = user_id
    paramarray = []
    if len(paramstring) > 0 & paramstring.find(" ") != -1:
        
        paramarray = paramstring.split(" ")
        
        if paramarray[0] == "channel": listrequested = channel_id
        if len(paramarray) > 1: action = paramarray[1]
        if len(paramarray) > 2  & paramarray[2].find("|") != -1:
            itemdetails = paramarray[2].split("|")
            itemid = itemdetails[0]
        else:
            itemid = paramarray[2]
    
    # Retrieve the list requested as json
    listJson = getList(listrequested)
    
    if action == "add":
        output = ""
        
    elif action == "edit":
        output = ""
        
    elif action == "done":
        output = ""
    
    elif action == "notdone":
        output = ""
    
    elif action == "remove":
        output = ""

    elif action == "help":
        output = open('help.txt').read()
                
    else:
        # Get the list requested and generate output as markdown
        output = formatListOutput(listJson)
        if action == "showall": response_type = "in_channel"

    
    
    """
    Create data json object to return to Mattermost with
        response_type = in_channel (everyone sees) or ephemeral (only sender sees)
        text = the message to send
    """
    data = {
        "response_type": response_type,
        "text": output,
    }
    
    """
    Create the response object to send to Mattermost with the
    data object written as json, 200 status, and proper mimetype
    """
    response = app.response_class(
        response = json.dumps(data),
        status = 200,
        mimetype = 'application/json'
    )
    return response

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5003, debug = False)

"""
Curl Test Posts:
curl -X POST -F "channel_id=a" -F "channel_name=a" -F "user_id=a-todo" -F "user_name=1" -F text="" http://127.0.0.1:5003/todo

curl -X POST -F "channel_id=a-todo" -F "channel_name=a" -F "user_id=a-todo" -F "user_name=1" -F text="channel showall" http://127.0.0.1:5003/todo
"""