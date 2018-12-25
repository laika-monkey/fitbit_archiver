#!/usr/bin/env python
# Convert old fitbit archive to csv or netcdf files for reading
# Convert daily exports to json files or fiddling
# Walter
################################################################################
################################################################################
#############################################################################_80

~~~ HALT UNTIL GRAPH TEST DONE.  DON'T BOTHER IF FAST ENOUGH ~~~
~~~ PUT ALL THIS SHIT INTO A DATABASE ON RDS DERP ~~~
def run_main(**kwargs):
    daily_convert('20181102')

def read_json(fname, **kwargs):
    ''' takes json data from text file and puts it into a list of dicts '''
    import json
    with open(fname, 'r') as f:
        return json.load(f)

def daily_convert(dtg, path='/mnt/media/data/waltersessions/user-site-export',
    **kwargs):
    ''' Read in files for given day from json and dump to some other format '''
    from glob import glob
    import os
    import re

    yyyy, mm, dd = dtg[:4], dtg[4:6], dtg[6:8]

    file_fmt = '-{}-{}-{}.json'.format(yyyy, mm, dd) 
    files = glob('{}/*{}'.format(path, file_fmt))
    regex = re.compile('/([\w\d_-]+){}'.format(file_fmt))

    for fname in files:
        check = regex.search(fname)
        field = check.group(1)
        data = read_json(fname)
        print '\n\n' 
        print field, fname

if __name__ == '__main__':
    run_main()
