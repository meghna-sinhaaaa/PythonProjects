import re
log = "July 31 07:51:48 mycomputer bad_process[2345]: ERROR Performing package upgrade"

def extract_pid(log_line):
    regex = r"\[(\d+)\]\: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])