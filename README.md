# Mattermost Todo Slash Command

This repository contains a Python/Flask application used to power a Mattermost (https://about.mattermost.com/) slash command used to track todo lists.

**Note**: This code doesn't actually work yet so do not use it!

## Fanciful Specification:

The following is the plan for building the slash command in terms of features:

* `/todo help` - returns markdown formatted help for this slash command. 

* `/todo` or `/todo channel` - will return a list of todo items assigned to the current user
who executed the request. Adding the channel parameter will cause the command to return
the list of of todo items for the current channel.

* `/todo channel showall` - will return a list of todo items for the current channel that is visible
to all users.

* `/todo channel add id|description|duedate` - will add a todo item to the channel 
(replace **channel** with **user** to add it the user's todo list) with an id, 
description, and due date fields separated by "|".

* `/todo channel edit id|description|duedate` - edits a todo item (by channel or user list).

* `/todo channel done id` - marks a todo item as done (by channel or user list).

* `/todo channel notdone id` - marks a todo item as not done (by channel or user list).

* `/todo channel remove id` - deletes an item from the list completely (by channel or user list).

 


# Make this Project Better (Questions, Feedback, Pull Requests Etc.)

**Help!** If you like this project and want to make it even more awesome please contribute your ideas,
code, etc.

If you have any questions, feedback, suggestions, etc. please submit them via issues here: https://github.com/cvitter/mattermost-slash-todo/issues

If you find errors please feel to submit pull requests. Any help in improving this resource is appreciated!

# License
The content in this repository is Open Source material released under the MIT License. Please see the [LICENSE](LICENSE) file for full license details.

# Disclaimer

The code in this repository is not sponsored or supported by Mattermost, Inc.

# Authors
* Author: [Craig Vitter](https://github.com/cvitter)

# Contributors 
Please submit Issues and/or Pull Requests.