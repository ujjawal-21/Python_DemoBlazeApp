import logging
import os 

class LogGen:
    @staticmethod 
    def getLogs():
        log_path = os.path.join('C:\\Users\\HP\\eclipse-workspace\\PythonAutomation', "Logs", "automation.log")
        #print("path:",log_path)
        print("getLogs method called")
        print(log_path)
        #print("path:",os.path.dirname(os.getcwd()))
        logging.basicConfig(filename=log_path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger