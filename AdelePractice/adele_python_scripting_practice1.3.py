# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Return the number of times that the string "code" appears anywhere
#    in the given string, except we'll accept any letter for the 'd', 
#    so "cope" and "cooe" count.              
#
# Examples:
#
#    CountCode('aaacodebbb') → 1
#    CountCode('codexxcode') → 2

import re

def CountCode(string):
    """ 
    Return the number of times that the string "code" appears anywhere
    in the given string, except we'll accept any letter for the 'd', 
    so "cope" and "cooe" count.
    """
    count = 0
    
    print(string)

    for i in range(len(string)):        
        substring = string[i:i+4]  # extract a substring of length 4
        if re.search('co.e', substring):  # Using regex to match 'code', 'cope', 'cooe', etc.
            count += 1

    return count

# Pre defined test conditions
try:
    assert CountCode("aaacodebbb") == 1, "aaacodebbb"
    assert CountCode("codexxcode") == 2, "codexxcode"
    assert CountCode("cozexxcope") == 2, "cozexxcope"
    assert CountCode("") == 0, ""
    assert CountCode("acobeaconeacozea") == 3, "acobeaconeacozea"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
strings = [
"deeeeceacobccoe", "acoaodaacobecea", "acaeoaocddddaba", "cecaeoeccaaadcb",
"ooocoddbebboccd", "occcdbeoedccode", "eecddaoccoeacac", "accaoeececeobcc",
"eeodecdaceobced", "oaceobeeeoadebc", "aeeaocobeeoooeo", "oeeedocodedcabo",
"bcccobeacdceooa", "eeedddbobcoceeo", "oebcaeoboaacaoe", "aeebcceobocddce",
"oodacobecdbeebe", "accoccocccebodc", "boecacoobeceoeo", "eaobacdcoecdcco",
"ceaoaoebcoebaeo", "aceoaadeaooboce", "oabcoeeedceoocd", "beocecbeodacbod",
"eoeedccecddebcd", "ebecooeccdddadd", "dceodoooeeaoeeb", "cobebaeocacocce",
"cboecbeobaceeod", "bcceccoodbocoee", "oodoodacceecboc", "dooedceodcccocb",
"bdaadcobcebobea", "cabdeeoceedceeb", "ooboooaeoaoccco", "oecbooabccbaoco",
"eoeoeodaadeacoc", "oceocccbbccceoa", "obcooccboedoeca", "obcacbeccaoddde",
"ccecodbcccdeoco", "dabdebabaecooed", "oaoeoaaeceoeocc", "eddccccocoooced",
"aacbdoaacoceaoc", "ocoooeocoocooce", "ocabooadaaccecc", "aebcccecdaobedc",
"cdbeeeadabbcdeo", "ccccecoeooaooco", "caeeadceecaooce", "oceeccaadcoocod",
"ccoooeebccobeod", "eecdoecadccoaaa", "cbbcacodbccacoc", "eaeaoceecocdobo",
"cdeoecdcbabooba", "caeoccoeeecbecc", "eoabaddcoebaeea", "dceoccbcaceeacc",
"eeooodccedcdbcc", "eaaeoddoacdbaba", "eeoboeecoooceao", "cbcoeeeecceeede",
"cboeaoeoocdccbc", "deeaeoeedboacoe", "odoaboedcocoboe", "aoacccocccdbdad",
"aooeeooccbacoee", "obaabboccoaoeac", "aoccboccbocooea", "bcdeceaebccacod",
"ocoadoaobbdeece", "oaceceobeabccdc", "eceacceaeaobbec", "cbbdcooabaebbeo",
"odcbebeoccoebco", "acoocdcceeceooc", "boccabcdbcooede", "eeoecoeoodcoecb",
"dooodacdbodacaa", "ooceebeceeaecba", "dedeodebecoceeb", "eedcooboeoaoacc",
"oeccbocaacccoea", "ceaeaeooecobdbe", "ooodaaocabeceoo", "dbacboaebcddaco",
"adebedcaeocobco", "oceocebcedcooed", "cobbaeddocoedoc", "eebccccabdccccc",
"oecaccoacoocddd", "bocdedoeoaecoac", "eaoeocbccececac", "edebceceecbocad",
"dcaccocobdeceee", "ebcbooocoeoooco", "ecdoooaooacbado", "oeodcebcdceocee"
]
for string in strings:
    total += CountCode(string)
print(total)