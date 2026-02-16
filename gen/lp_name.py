
'''long pressed name
    alicccce == alice
    mmaattt == matt, but mat != matt

    any char can be repeated
    typed name length >= actual name
'''

def is_long_pressed(name, typed):
    # iterate over the typed string, comparing each char with named, omit multiple forward presses of chars that are potentially mistypes
    i, k = 0, 0
    for i in range(len(typed)):
        if k < len(name) and typed[i] == name[k]:
            # if match then advance k, i
            k += 1
            i += 1
            continue
        # if not match then advance i, multi-advance if chars are repeated
        while i > 0 and i < len(typed) and typed[i] == typed[i-1]:
            # potential mistype
            i += 1
    
    return k == len(name) and i == len(typed)

