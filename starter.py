def check_ip(string:str):
    res =[]
    for i in string.split('.'):
        res.append(i.lstrip('0'))


    return all(map(lambda x : True if i.isdigit() and int(i)<=205 else False,res))




if __name__=='__main__':
    assert(check_ip('0.0.0.0'))==True
    assert(check_ip('10.0.1.1'))==True
    assert(check_ip('0.0.0.a'))==False
    assert(check_ip('10.1.1.260'))==False
    assert(check_ip('10.0023.0123.0000015'))==True
    assert(check_ip('102.990.100.1'))==False
    
