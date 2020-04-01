def pronounce(name):
    """
    Generate the pronunciation code of the string
    
    """
    name = name.upper()
    result = ""
    if len(name) == 0 :
        return '0000'
    else:
        result += name[0]
        dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}
        for char in name[1:]:
            for key in dictionary.keys():
                if char in key:
                    code = dictionary[key]
                    if code != result[-1]:
                        result += code
        
        if len(result) == 2 and result[1] == '.':
            return result[0]+'999' 
        result = result.replace(".", "")
        result = result[:4].ljust(4, "0")

    return result