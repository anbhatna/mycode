#!/usr/bin/python

import yaml

def main():
    hitchhikers=[{"name":"ZZZ","species":"betel"},{"name":"Arthur","species":"Human"}]

    print(hitchhikers)
    zfile = open("galaxyguide.yaml","w")
    yaml.dump(hitchhikers,zfile)
    zfile.close()

main()
