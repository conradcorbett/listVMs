#! /usr/bin/env python

import requests

def main():
	cluster_VIP = raw_input("Enter Cluster VIP: ")
	username = raw_input("Enter Username: ")
	password = raw_input("Enter password: ")

	requests.packages.urllib3.disable_warnings()
	base_url = "https://" + cluster_VIP + ":9440/PrismGateway/services/rest/v2.0/"
	print base_url
	s = requests.Session()
	s.auth = (username,password)
	s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
	
	data = s.get(base_url + 'vms', verify=False).json()

	for e in data["entities"]:
		print(e["name"])

if __name__ == "__main__":
    main()