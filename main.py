from os import listdir
from os.path import isfile, join
import subprocess


def get_jar_list(path):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # TODO filter only jar
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

mypath = '/home/egenerat/Documents/Scratchpad_code/projects/jar-parser/lib'
for i in get_jar_list(mypath):
    print('Search inside {}'.format(i))
    result = find_file_in_jar('lib/'+i, 'ViewHandler.class')
    if result:
        print(result)


# jsf-api.jar
# for /R %G in (*.jar) do @jar -tvf "%G" | find "Hello.class" > NUL && echo %G