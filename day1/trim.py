def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    if s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s
