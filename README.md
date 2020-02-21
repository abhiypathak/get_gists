## Python Utility to get publicly available gists  

### Overview
This utility can be used for getting publicly available gists for a given user from github API. 
It offers the following features:

1. Get publicly available gists of a given user
2. Keep a track of the each request and only give you any newly available public gists of a user of queried before 
using ```since``` parameter as described in the Github's API docs

The output will show the URLs of the gists

### Requirements
1. Python version required ```3.7.4``` or higher
2. Python package ```requests```

### Example Usage
```
$ python3 get_gists.py -u xxx
Connection to https://api.github.com/users/xxx/gists successful!
Will now proceed to get public gists for xxx user...
Following public gists are available
https://api.github.com/gists/ec3b35b83d07ef1d37a4af819723842b
https://api.github.com/gists/4a460749f5f2d01019812d536ed42648
https://api.github.com/gists/07b6d7ea669dee4add03feb4fd756a0e
https://api.github.com/gists/5219363
https://api.github.com/gists/4659986
https://api.github.com/gists/3696816
https://api.github.com/gists/2943743
https://api.github.com/gists/2942855
https://api.github.com/gists/2316017
https://api.github.com/gists/1051938
https://api.github.com/gists/895787
https://api.github.com/gists/846581
https://api.github.com/gists/782256
https://api.github.com/gists/777454
https://api.github.com/gists/777424
https://api.github.com/gists/772368
https://api.github.com/gists/772135
https://api.github.com/gists/760560
https://api.github.com/gists/760512
https://api.github.com/gists/760476
https://api.github.com/gists/733793
https://api.github.com/gists/722270
https://api.github.com/gists/706255
https://api.github.com/gists/585272
https://api.github.com/gists/585271
https://api.github.com/gists/562766
https://api.github.com/gists/538566
https://api.github.com/gists/525907
https://api.github.com/gists/512325
https://api.github.com/gists/445970

$ python get_gists.py -u xxx        
Connection to https://api.github.com/users/xxx/gists?since=2020-02-21T12:13:45Z successful!
Will now proceed to get public gists for xxx user...
No new gists available since your last look up at 2020-02-21T12:13:45Z

```

### Notes

This utility will create a ```.<username>_get_gists``` file in the users home directory to track the requests made.
A new file is created for each unique users

### TO-DO

- [ ] Create a new flag that resets the history
- [ ] Create a new flag to get raw urls of the gist
- [ ] Create a new flag to implement pagination as described here(https://developer.github.com/v3/gists/)
