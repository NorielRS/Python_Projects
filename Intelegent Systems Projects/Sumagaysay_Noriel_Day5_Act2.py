# REVERSE A STRING

def reverse_string(og_string):
    x = ''
    # for i in og_string:
    #     x = i + x

    for i in reversed(range(len(og_string))):
        x = x + og_string[i]
    
    print(f'INPUT: {og_string}')
    print(f'OUTPUT: {x.upper()} ({len(x)} characters)')


reverse_string('hello')