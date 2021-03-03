# Here, we see a new keyword "import"
# The import keyword allows us to load a library into our working envrionment
# A library is simply a set of fucntions and classes that someone wrote that is 
# useful for certain operations. We will be using the reqyests and json library in this 
# tutorial. We can access the functions of a library by write <name_of_library>.<function_name>
import requests
import json

# A JSON Object 
# Simply put, a JSON object can be thought of as a dictonary of dictionaries. 
# Each value within a JSON object can be treated as a key, with a corresponding 
# value pair. Note that this value pair may be either a primtiive data type 
# or an object, such as another dictonary. 
# Let's quickly make a JSON from a string to see how it can be done. 
json_string = """{"a": "aa", "c": {"cc": "cccc", "dd": "dddd"}, "b": ["bb1", "bb2"]} """
demoJSON = json.loads(json_string)
print("demoJSON: ", demoJSON)

# While cool, it doesn't really have much functionality. Let's make a more complex JSON 
# object but this time, let's load it from a JSON file. Any idea how we can?
# What we do is we "open" the JSON file and then load it by using the JSON library. 
# It is always good practice to close your files after they have been opened. 
jsonFile = open("demo.json", 'r')
complexJSON = json.load(jsonFile)
print("ComplexJSON: ", complexJSON)
print("ComplexJSON Type: ", type(complexJSON))
jsonFile.close()


# Wait, if we are working with JSON obejcts, why does it say dict?
# This is because JSON obejcts are treated as dictonaries in Pythoon to make 
# our lives slightly easier/harder, depending on how you look at it. 
# Regardless, lets take a look at how we can go about accessing some variables within 
# the file. 
id = complexJSON["ID"]
print("ID: ", id)


# A JSON structure works similar to a dictonary so we can use 
# our normal subscript operator, [], to access the value pairs by 
# using the corresponding key. Let's expand on this a little bit furteher and find 
# the sequence value. 
# What complexJSON["type"] does is give us access to the type dictonary.
# As this is still a dictonary we can use the [] operator to gain access to its values 
sequence = complexJSON["type"]["sequence"]
print("sequence: ", sequence)

# We quickly went past some JSON methods so lets explore them a little bit more here. 
# What does json.loads (pronounched load-s) do?
# Well, it does as it states - it creates a JSON object (really a dictonary!)
# based on a JSON string. Can you guess what the s stands for?
# This is useful whenever we get back some sort of JSON object from an API - 
# sometimes, the retuned data is in a string format and can be converted into 
# a JSON object through this method. Let's explore this a little bit furtehr! 
loadJSON = json.loads("""{"Hello": "World", 
                        "Example": {
                            "Demo": "01", "Day": "Friday"}, 
                            "Librarires": ["JSON", "Requests"]
                            } """)
print("Loading a JSON string: ", loadJSON)


# What about JSON to load? Well, take a look at this folder - notice a demo.json 
# file? This is a JSON object and can be read as such. To load it into Python 
# we have to first open the file and then read it. To open it, we need to use 
# the open keyword, which allows for a file to be read by Python. 
# We can then pass this back into JSON.load() which will read it and return a neww
# JSON object. Take a look at this example in lines 23-27.
# Being able to read a file can be akin to a channel being opened - we must close 
# it when we are done. To do this, simply write fileName.close()


# That should be enough for a quick overview of what JSON is and how to use it. 
# Now, lets move onto API's, one of the reasons that we reviewed this in the first place. 