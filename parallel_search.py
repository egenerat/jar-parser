from multiprocessing.dummy import Pool as ThreadPool

from main import find_file_in_jar
from main import get_jar_list

mypath = '/home/egenerat/Documents/Scratchpad_code/projects/jar-parser/lib'
jar_list = get_jar_list(mypath)
# print(jar_list)

def search(jar):
    # print('Search inside {}'.format(jar))
    result = find_file_in_jar('lib/' + jar, 'LogSource.class')
    if result:
        print(result)

import time

start = time.time()

# Make the Pool of workers
pool = ThreadPool(8)

# Open the urls in their own threads
# and return the results
results = pool.map(search, jar_list)

#close the pool and wait for the work to finish
pool.close()
pool.join()


end = time.time()
print(end - start)
