def validate_ip(ipa):
    podzial= ipa.split('.')
    if len.podzial == 4: True
    for k in podzial[k] :
        if k.isdigit(): True
        
    for i in podzial[i] :
        if 0<i<255: True
    return     
        
        
print(validate_ip(244.234.001))\