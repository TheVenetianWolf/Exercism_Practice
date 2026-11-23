def response(hey_bob):
    message = hey_bob.strip()
    
    if message.strip() == "":
        return "Fine. Be that way!"
    elif message.isupper() and message.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif message.isupper():
        return "Whoa, chill out!"
    elif message.endswith("?"):
        return "Sure."
    else:
        return "Whatever."