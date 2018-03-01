# Mattermost Todo Slash Command

This repository contains a Python/Flask application used to power a Mattermost (https://about.mattermost.com/) slash command used to track todo lists.

**Note**: This code doesn't actually work yet so do not use it!

## Fanciful Specification:

The following is the plan for building the slash command in terms of features:

* `/todo` or `/todo channel` - will return a list of todo items assigned to the channel it
 was called from (replace channel with user name in the second example view the todo 
 list for a specific channel).


* `/todo add channel id|description|duedate|private` - will add a todo item to the channel 
(replace channel with user name to add it the user's todo list) with an id, 
description, due date, and private flag | separated. (**Note**: The private 
flag means that only the user assigned a todo item can see it. Channel items 
are visible to anyone in the channel.)

* `/todo edit channel id|description|duedate|private` - edits a todo item.

* `/todo done channel id` - marks a todo item as done (only the person assigned an item 
can mark it as done).

* `/todo notdone channel id` - marks a todo item as not done (only the person assigned an item 
can mark it as not done).

* `/todo remove channel id` - deletes an item from the list completely  (only the person 
assigned an item can delete it). 

 


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