#!/usr/bin/python

import yaml

def main():
    #create a blob of data to work with
    hitchhikers=[{"name":"ZZZ","species":"betel"},{"name":"Arthur","species":"Human"}]

    #display our python data
    print(hitchhikers)
    
    #create the yaml string
    yamlstring = yaml.dump(hitchhikers)
    
    #Display a single string of yaml
    print(yamlstring)

main()
