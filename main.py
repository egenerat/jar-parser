from os import listdir
from os.path import isfile, join
import subprocess


def is_jar(path):
    return path.split('.')[-1].lower() == 'jar'


def get_jar_list(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and is_jar(f)]
    return onlyfiles


def execute_command(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    tmp = proc.stdout.read()
    return tmp


def find_file_in_jar(jar, searched_file):
    output = execute_command("""jar -tvf {} | awk '{{ print $8; }}' | grep {}""".format(jar, searched_file))
    if output:
        return format_string(output)
    return None


def format_string(input_string):
    return input_string.decode("utf-8").strip('\n')
