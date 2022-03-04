# QuizTelegramChatBot
Creating a Telegram Chat Bot for sending notifications to do weekly/monthly quizzes from Google Sheets
"Google Forms-> Google Sheets -> Python Code on Heroku Cloud -> Telegram"

Steps Taken:

Step 1: CREATING PRIVATE KEY ON GOOGLE DEVELOPERS CONSOLE
Special Thanks - https://www.youtube.com/watch?v=bu5wXjz2KvU
1. Go to Google Developers Console. Create New Project. Search and Enable Google Drive and Google Sheets API
2. Credentials-> Manage Service Accounts -> Create Service Account -> Copy email account created. -> Share email account in google spreadsheet.
3. Manage Key-> Add Key-> Create new JSON key.-> Save private key to Computer
[*****My Private Key is Missing in Heroku folder due security purposes]


STEP 2: CREATE GOOGLE FORMS, LINK RESPONSES TO GOOGLE SPREADSHEET WITH SERVICE ACCOUNT

STEP 3: DOWNLOAD "DEPLOY HEROKU" FOLDER IN THIS REPOSITORY. PLACE YOUR PRIVATE KEY JSON FILE IN THIS FOLDER.

STEP 4: CREATE TELEGRAM BOT WITH BOTFATHER. CREATE TELEGRAM CHANNEL/GROUP. GET BOT TOKEN AND CHANNEL/GROUP CHAT ID. PLACE IN MAIN.PY. 
Special Thanks - https://www.youtube.com/watch?v=ps1yeWwd6iA

STEP 5: SET UP YOUR EXCEL SPREADSHEET TO SEND DATA. SEE MY EXAMPLE: 
https://docs.google.com/spreadsheets/d/153t0PWeDCx7Xh1s1hMjR2uczQ0amfGSTKSLyhrVJ-20/edit?usp=sharing

STEP 6: DEPLOY "DEPLOY HEROKU" FOLDER TO HEROKU. https://devcenter.heroku.com/articles/git
------------------------------------------------
How different is this idea from past repositories?
- The python app makes use of 'Scheduler' Library. When deployed to Heroku as Worker and not Webapp, it puts python code to sleep until moment. Effective way to save on dynos. [This is compared to web polling method, that consumes large amounts of Dynos due constant active state of python code]

How does the excel sheet work?
- Only the cells in orange should be edited. The rest of the cells are formulated.
- Python code grabs values from cells in red. These values will be triggered by python code to send notification to Telegram.

quizOpenReminder sheet:
- This sheet makes use of time. When the quiz is open, it will filter out the open quiz from the rest. The python code will only send notification for the quiz that is opened to telegram.

code sheet:
- cells B9 to M60 is synced to quizOpenReminder sheet timing. It only accepts responses within the quiz opening and closing time. Responses out of the quiz opening and closing time will be recorded in respective weekly/monthly quiz sheets but the student will not be recorded as "Quiz Completed". Indirectly, this acts as the quiz timer!


