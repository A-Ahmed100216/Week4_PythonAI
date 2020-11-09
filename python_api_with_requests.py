# importing requests t make an api call to the web

import requests
from emoji import emojize


live_response=requests.get("https://www.bbc.co.uk/")
print(live_response.status_code)
# Returns an integer response code.
# code 200 to show this website is live.
# We can use an if statement to return a print statement.
if live_response.status_code==200:
    print("This website is live. Status code: " + str(live_response.status_code) + emojize((" :thumbs_up:")))

else:
    print("Ooops something went wrong, please try later")