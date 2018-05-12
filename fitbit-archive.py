#!/usr/bin/env python

def run_main(fname='server.yaml', **kwargs):
    import yaml
    import fitbit

    #_get fitbit authentication info
    login = yaml.load(open(fname, 'r'))
    ClientID = login.pop('ClientID', None)
    ClientSecret = login.pop('ClientSecret', None)
    auth = fitbit.Fitbit(ClientID, ClientSecret, **login)
    #_timeout info and what not should be gathered later

    print dir(auth)
    auth.get_heartrate_intradate(date='2018-03-20') 
    
if __name__ == '__main__':
    run_main()
