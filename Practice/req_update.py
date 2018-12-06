# Written by Justine Schabel

from jira import JIRA
import csv
from collections import OrderedDict 
import requests
requests.packages.urllib3.disable_warnings() 

withdrawn = []


# pull ccbs from jira
def get_issues(jira_obj, filter_str):
    issues = []
    add_issue = issues.append
    for issue in jira_obj.search_issues(filter_str, maxResults=1000):        
        constant_data = {
            "Key": str(issue),
            "Reported Status": str(issue.fields.status),
            "Reporter": str(issue.fields.reporter),
            "Created": str(issue.fields.created),
            "Description": str(issue.fields.description),
             "Customer": str(issue.fields.customfield_10031).partition(
                'value=\'')[2].partition(
                    '\'')[0] if issue.fields.customfield_10031 else 'None',
            "Resolved": str(issue.fields.resolutiondate),
            "Updated": str(issue.fields.updated),
            "Linked Issues":  str(issue.fields.issuelinks),
            "Title": str(issue.fields.summary)
        }
        add_issue(constant_data)
    return issues


# pass in windows credentials to sign in to jira, return a jira_obj 
def jira_signin(usr='intentionally blank', passwd='intentionally blank'):
    return JIRA({'server': 'intentionally blank', 'verify': False},
                basic_auth=(usr, passwd), max_retries=1) 


# read in all ccbs from DNG export csv
def read_in_artifacts(filename = 'export.csv'):
	ccbs = []
	with open(filename, encoding="utf8") as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=',')
		for row in csv_reader:
			if row['Scratch Pad'] != '':
				if row['Scratch Pad'] == 'Withdrawn':
					withdrawn.append(row)
				else:
					ccbs.append(row) 
	return ccbs
		

# iterate over dng ccbs, comp, update, but if dne add it 
def compare_Jira_DNG(dng, jira):
	dng_upload = []
	add_ccb = dng_upload.append
	found = False
	for nonordered_item in jira:
		for ordered_item in dng:
			name = ordered_item['Primary Text'].split('browse/')[1][:-1]
			if name == nonordered_item['Key']:
				if ordered_item['Scratch Pad'] == 'Withdrawn' or nonordered_item['Reported Status'] == 'Withdrawn':
					withdrawn.append(ordered_item['id'])
				else:
					found = True 
					updated_ccb = comp_ccb(ordered_item, nonordered_item)
					add_ccb(updated_ccb)
		if found == False and nonordered_item['Reported Status'] != 'Withdrawn' :
			formatted_ccb = formatted(nonordered_item)
			add_ccb(formatted_ccb)
		found = False 
	return dng_upload


# take a jira ccb and format if for a DNG csv upload 
def formatted(jira):
	link = 'LINK title=\"{key}\" uri=https://nsg-jira.intel.com/browse/{key}'.format(key = jira['Key'])
	dng_format = OrderedDict()
	dng_format['id'] = ''
	dng_format['Link:NSG: CRD to PRD (<)'] = ''	
	dng_format['Dependencies'] = ''	
	dng_format['Artifact Type'] = 'Customer Requirement'	
	dng_format['Name'] = jira['Title']
	dng_format['Target'] = ''	
	dng_format['Minimum'] = jira['Description']
	dng_format['Primary Text'] = '{'+link+'}'
	dng_format['Scratch Pad'] = jira['Reported Status']
	dng_format['Stakeholders'] = jira['Customer']
	dng_format['Status State'] = 'v1.0 - Baseline Change'	
	dng_format['Rationale Category'] = 'Customer ask - driven by industry'	
	dng_format['Comments Count'] = '0'	
	dng_format['Grade'] = ''	
	dng_format['Domain'] = ''	
	dng_format['Sub-Domain'] = ''	
	dng_format['Link:NSG: PRD to CRD (>)'] = ''
	return dng_format


# take an issue thats in dng and look for udpates
def comp_ccb(dng, jira):
	dng['Scratch Pad'] = jira['Reported Status']
	return dng


def write_to_csv(fully_updated_ccbs, filename = 'new_upload.csv'):
	with open("new_upload.csv", "w",newline='') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(fully_updated_ccbs[0].keys())
		for item in fully_updated_ccbs:
			writer.writerow(item.values())


if __name__ == "__main__":
	user = jira_signin()
	filter_str ='intentionally blank'
	ccb_jira = get_issues(user, filter_str)
	ccb_dng = read_in_artifacts()
	final = compare_Jira_DNG(ccb_dng, ccb_jira)
	write_to_csv(final)
	print(withdrawn)
