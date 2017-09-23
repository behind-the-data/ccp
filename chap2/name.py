name = "ada lovelace"
print(name.title()) # the title() method returns titlecased STRING.

# All below are optional

# Only Capital letters
print(name.upper())

# Only Lower letters
print(name.lower())

## Concatenation ##

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

## Pass a string variable within a string ##

print("Hello, " + full_name.title() + "!")

## Store the above in a varialbe, then print said variable ##

message = "Hello, " + full_name.title() + "!"
print(message)
