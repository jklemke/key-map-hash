import datetime
import uuid                                                                     
import hashlib                                                                  
import baseconv                                                                 
import random

oTime = datetime.datetime.now()
print(oTime.isoformat())

ALPHANUMERICS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'     
ALPHABETICS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'   
keylength = 24  
                                                                                
def newkey():
    converter = baseconv.BaseConverter(ALPHANUMERICS)                                
    uuid4_as_hex = str(uuid.uuid4()).replace('-','')                            
    uuid4_as_int = int(uuid4_as_hex, 16)                                        
    retval = random.choice(ALPHABETICS) + random.choice(ALPHANUMERICS) + converter.encode(uuid4_as_int)   
    # // occasionally, the base62 may be shorter, so pad if needed
    while (len(retval) < keylength):
        retval += random.choice(ALPHANUMERICS) 
    return retval
                                   
