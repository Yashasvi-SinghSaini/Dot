from math import floor
def shorten_doubt(text):
    newtext = text
    def str_add(old_str, to_add_text, index): #THIS FUNCTION INSERTS A SUBSTRING TO A EXISTING STRING
        newstr=old_str[0:index] + to_add_text + old_str[index:]
        return newstr
    
    lines=floor(len(text)/30)
    for i in range(lines):
        if len(newtext) >= 30:
            if '\n' not in newtext:
                where_to_add = newtext[0:30].rindex(' ')
                newtext = str_add(newtext, '\n', where_to_add)
            elif '\n' in newtext:
                where_to_add = newtext[0:newtext.rindex('\n')+40].rindex(' ') 
                newtext = str_add(newtext, '\n', where_to_add)
    return newtext