def upper_lower_case(string):
    uppercase_count = 0
    lowercase_count = 0

    for character in string:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1
    
    return (f"Ther's {uppercase_count} upper cases and {lowercase_count} lower cases")

print(upper_lower_case("I love Nation Sushi"))  