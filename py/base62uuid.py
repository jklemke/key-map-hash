import uuid                                                                     
import hashlib                                                                  
import baseconv                                                                 
                                                                                
ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'     
                                                                                
def base62uuid():                                                               
    converter = baseconv.BaseConverter(ALPHABET)                                
    uuid4_as_hex = str(uuid.uuid4()).replace('-','')                            
    uuid4_as_int = int(uuid4_as_hex, 16)                                        
    return converter.encode(uuid4_as_int)                                       
                                                                                
if __name__ == '__main__':                                                      
    print base62uuid() 