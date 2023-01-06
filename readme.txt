This is a bot store that has 3 sections with products and showing contacts.
0.The bot is launched using the Pocking protocol - a long survey, for the bot to work continuously, transfer it to Webhuuk.
The bot was created in PYTHON (version 3), using the AIOGRAM library.
1.In the handlers section, in the client file, in the contact display function, you should add your contacts, for your users.
2.In the handlers section, in the admin file, in the registration of handlers, you should add your command to assign
administrator privileges to the user (instead of "****")the algorithm will be described below.
3.In the bot_run file.bat, in (set TOKEN=...) you should insert your token received from @BotFather, without quotes and apostrophes.
4.In the handlers section, in the client file, in the start function, after the phrase "write to him", you should insert a link to the bot.


ALGORITHM FOR ASSIGNING ADMINISTRATOR STATUS:
1. Add the bot to the group (which you create yourself).
2. If you are the only admin, then proceed to the next step ...
Add users (whom you are going to make an administrator),
give them the admin status in the group.
3. Next, the "administrator" must enter the command with "/" which you assign to the handler in the "admin" file.
4.Upon completion of the work on adding /removing products, you should send the "/start" command to the group
to switch to the "user" mode and view the products.

