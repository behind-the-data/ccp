####################################################################################################
# STRING MODULES: strip
# rstrip, lstrip, strip
# Why: Eliminate whitespace in strings when some sort of cross-check/mapping operation is required.
####################################################################################################




# Assign a string to a variable
favorite_language = 'python '

print(favorite_language) # Notice how the space was also in output?

# Let is strip it at the right side (i.e. RTRIM in SQL)
print(favorite_language.rstrip())

# Let us keep the string trimmed/stripped
favorite_language = favorite_language.rstrip()

print(favorite_language)
