def character_count(string, char):
    
    i = 0
    characters_found = 0
    
    while i < len(string):
        if string[i] == char:
            characters_found += 1
        i += 1
    
    return characters_found
    


char = "l" 
string = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"



print "Last character is:", string[len(string) - 1]
print "String lenght is:", len(string)

print "#Characters: ", character_count(string, char)

