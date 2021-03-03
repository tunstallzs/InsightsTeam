import requests
import json

# By now, we have already reviewed what an API is - let's now talk about using them. 
# As dicussed earlier, we use endpoints, or certain URLs, and we can send special 
# requests to them, allow them to return to us some form of data (in JSON format). 
# While API's can return to us some form of data, they can also be used to trigger 
# all sorts of logic and code via the endpoints. This concerns with how an API is built - 
# certain requests to certain endpoints can trigger all sorts of logic within the code of the API
# This may be a bit complex to grasp, so let's first take a look at how to send our first 
# post request, which also has certain ramifications for this tutorial! 

name = "Rashed Rifat"
post_response = requests.post("https://9dontxvnf1.execute-api.us-east-2.amazonaws.com/alpha/record",
                data=json.dumps({"full_name" : name, "TID" : "00", "hash" : "HelloWorld!"})
            )

# Above, we see the strucre of how an API request can be coded. We have the URL that we wish to
# send the response to and the data that we send along with it. This data is crucail for the endpoint 
# to perform certain tasks. Without it, it may not work properly. You can find thw requried data ususally 
# within the API documentation. 
# A certain question you might have is what does this request do? Why am I sending it my name, TID and a hash?
# This is because this is how the Insights Team will be taking attendance! 
# When the above code is executed, the name you provide will be added to our servers and you will
# be marked as having completed this tutorial! We will be using this to track your progress and make 
# sure that everyone is on the right track. This is also an example of how API's can be used 
# to execute code logic - when you send an API request to above endpoint, a script executes (serverside)
# that add your name to our database. Neat isn't it?
print(post_response.status_code, post_response.json())


exit()
get_response = requests.get("https://9dontxvnf1.execute-api.us-east-2.amazonaws.com/alpha/record", 
                        data=json.dumps({"full_name": "Rashed Rifat"})
                        )
print(get_response.status_code, get_response.json())