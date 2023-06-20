import sys;
'''
Sys library provides various functions and variables that are
used to manipulate different parts of the Python runtime environment.

'''
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    '''
    this will hold all info about exception like 
    in which file exception is occured, in which line exception is occuring etc.
    '''
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error meassage [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message
     
    
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

'''    
if __name__ == "__main__" :

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
'''