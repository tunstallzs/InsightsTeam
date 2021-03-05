import requests
import json

# ---------------------------- Part I ----------------------------

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
# that add your name to our database (as well as some other data...). Neat isn't it?
print("post_response: ", post_response.status_code, post_response.json())

# You may have noticed that we pass in a filed called data. Why so? This is because we need to pass 
# some data for the API to work properly - specifcally, we need to know who is using this method. 
# An important note! Please make sure that your name is exactly the same in all cases - otherwise, 
# a different person will be attributed. 

# Finally, you may have also seen the TID and hash fields. What are these? Well, although this is 
# not the case for our simple API, most API's will require some sort of authentication key/passcode.
# After all, it would be a little bit of a security breach if any person were able to pull 
# the records of a company like Google. 
# Our TID and hash fields also accomplish a similar objective. In order to make sure that everyone 
# has actually gone through these tutorials, a specific TID and hash combination must be passed 
# to validate the API call. While the TID will be readily revealed, the hash code will require
# a little bit more work. We will not reveal the hashcode always - you may have to figure out the 
# hash by completeing a problem set. 

# Let's say that you try to "hack" the tutorial and disregard the idea that you need a hash. Let's
# try passing something random into the hash and see what it returns. 
bad_response = requests.post("https://9dontxvnf1.execute-api.us-east-2.amazonaws.com/alpha/record",
                data=json.dumps({"full_name" : name, "TID" : "00", "hash" : "random!"})
            )
print("bad_response: ", bad_response.json())

# Aha! It seems thw API is able to tell that your hash is incorrect and thus will not be accepted. 
# But let's explore a little bit more about the bad_response object - what is it and what can we do 
# with it?
print("type of bad_response: ", type(bad_response))

# It seems that it is Response object from the requests library. We won't go through the methods and 
# and the structure of this object - this is very well documented in the requests library - you
# should check this out if you plan on using this further. BUt one thing that we can do with it, 
# for easy parsing, is to the .json() method, which will give us access to the data that the API
# returned. Let's see what a successful repsonse looks like. 
print("post_resonse (a successful response): ", post_response.json())

# Note that most API requests will have a status code associated with them - these are the 404
# errors you might see pop up. Specifcally, these are known as HTTP codes/responses. 
# You can see waht the status of your API request by writing post_response.status_code
# Note that code 200 means that your API was successful. 
# Note, just because a post code of 200 is returned does not mean that what you wanted 
# to get out of it was successful - just that the syntax of your call was correct. 
# An example of this is in our bad_response - the status itself was 200 (meaning that you 
# made a call) but the data returned tells us that hash/anything else was not successful. 
# Let's see it here
print("bad_response.status_code: ", bad_response.status_code, "\n")


# ---------------------------- Part II ----------------------------


# Ok, now that we have talked at length about how we can send POST requests, let's talk about 
# GET requests - these are made simply to get data. Let's see the format of the call here. 
get_response = requests.get("https://9dontxvnf1.execute-api.us-east-2.amazonaws.com/alpha/record", 
                        data=json.dumps({"full_name": "Rashed Rifat"})
                        )
print("get_response.status_code: ", get_response.status_code, "\nget_response JSON: ", get_response.json())
 
# As you can see, we have been returned some data from our servers that give us some clue as to
# one's progress in the team. If we want to parse through it - well! This goes back to our 
# discussion on JSON objects. 
JSON_response = get_response.json()
print("message: ", JSON_response["message"])


# Note that this is of type string, so we need to load it to a JSON object.
# And then we need to use the subscript operator to open it up 
message = json.loads(JSON_response["message"])
print("tutorial01: ", message["tutorial01"])

# Okay, let's wrap up and execute the attendance.py file! 