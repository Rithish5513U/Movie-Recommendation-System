import sys

def error_message(error, error_detail):
    _,_,info = error_detail.exc_info()
    file_name = info.tb_frame.f_code.co_filename
    error_msg = f"Error occured in Python Script name [{file_name}] line number [{info.tb_lineno}] error message [{str(error)}]"
    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, error_detail):
        super().__init__(error_msg)
        self.error_msg = error_message(error_msg, error_detail=error_detail)

    def __str__(self):
        return self.error_msg

