Good commit history - could be *richer*.

See general comments for this assignment.

Avoid using globals whenever possible.

Try and avoid assigning True/False to booleans:
```
    if s[0]=="y" or s[0] == "Y":
        return True
    elif s[0]=="n" or s[0] == "N":
        return False
    else:
        while s[0]!="y" or s[0] != "Y" or s[0]!= "n" or s[0] != "N":
            print(prompt)
            s = input()
            if s[0] == "y" or s[0] == "Y":
                return  True
                break
            elif s[0] == "n" or s[0] == "N":
                return  False
                break

```

Grade: B/A
