import sys ## sys provide diff variablr nd func that are used to manipulate diff parts of python runtime enviornment
from src.logger import logging
## own raise custom exception
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() ##_,_,exc_tb this is the return type first two info are not imp and third is variable tht store details on which line error occured , wht occured
    file_name=exc_tb.tb_frame.f_code.co_filename ##  syntax to get file name
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    
## call this exception 
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


        