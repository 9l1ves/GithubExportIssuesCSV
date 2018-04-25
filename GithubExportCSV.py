import csv
import requests
import argparse
import os
import backoff
from requests import RequestException, HTTPError, ConnectionError, ConnectTimeout, Timeout, ReadTimeout, TooManyRedirects


def write_issues(r,csvout):
    #output a list of issues to csv
    if not r.status_code == 200:
        raise Exception(r.status_code)
    for issue in r.json():
        labels = issue['labels']
        newlabel = ""
        if isinstance(labels,list):
            for label in labels:
                newlabel = newlabel + label['name'] + " "
        elif isinstance(labels,dict):
            newlabel = labels['name']

        assignees = issue['assignee']
        assigned = ""
        if isinstance(assignees,list):
            for assignee in assignees:
                assigned = assigned + assignee['login']
        elif isinstance(assignees,dict):
            assigned = assignees['login']
        title = issue['title']
        title = title.replace("\"","\"\"")
        title = "\"" + title + "\""
        csvout.writerow([issue['number'], title , newlabel, issue['created_at'], issue['updated_at'],issue['state'],assigned])

@backoff.on_exception(backoff.constant, (RequestException),interval=10, max_tries=20)
def intial_login(auth,url,path):
    """ Performs the intial login to github issues repo to pull the issues

    :param auth: authentication to use for the github repo
    :param url: url of the repo issues to utilise
    :param path: path for the csv file
    :return: request object
    :return: csv file object
    """
    try:
        r = requests.get(url, auth=auth)
        csvfile = path
        os.makedirs(os.path.dirname(csvfile), exist_ok=True)
        csvout = csv.writer(open(csvfile, 'w'), delimiter=',', lineterminator='\n')
        csvout.writerow(('id', 'Title', 'Labels', 'Created At', 'Updated At', 'Status', 'Assigned'))
        write_issues(r,csvout)
        return r, csvout
    except (RequestException, HTTPError, ConnectionError, ConnectTimeout, Timeout, ReadTimeout, TooManyRedirects) as e:
        print("A Connection Error Occured Retrying")
        raise RequestException

@backoff.on_exception(backoff.constant, (RequestException),interval=10, max_tries=20)
def remaining_pages(auth,r,csvout,pages):
    """ Pulls issue data from the remaining pages

    :param auth: authentication to use for the github repo
    :param r: request object
    :param csvout: csv file object
    :param pages: a dict that contains the next page to proceed to
    :return: current page a dict object with the current page dict object
    """
    try:
        r = requests.get(pages['next'], auth=auth)
        write_issues(r,csvout)
        currentpage = dict([(rel[6:-1], url[url.index('<')+1:-1]) for url, rel in
                    [link.split(';') for link in
                        r.headers['link'].split(',')]])
        return currentpage
    except (RequestException, HTTPError, ConnectionError, ConnectTimeout, Timeout, ReadTimeout, TooManyRedirects) as e:
        print("A Connection Error Occured Retrying")
        raise RequestException

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--username', '-u', dest='githubusername', required=True,
                       help='Github Username')
    parser.add_argument('--password', '-p', dest='githubpassword', required=True,
                       help='Github Personal Access Token. Can be created here: https://github.com/settings/tokens')
    parser.add_argument('--repo', '-r', dest='repo', required=True,
                       help='The Repository to connect to in the format username/repo (e.g. 9l1ves/GithubExportIssuesCSV)')
    parser.add_argument('--filepath', '-f', dest='path', required=False, default="C:\\temp\\githubdump.csv",
                       help='The path where you want the CSV file stored')
    args = parser.parse_known_args()
   
    github_user = args[0].githubusername
    github_password = args[0].githubpassword
    repo = args[0].repo
    repo_url = 'https://api.github.com/repos/%s/issues?state=all' % repo
    auth = (github_user, github_password)
    path = args[0].path
    r, csvout = intial_login(auth,repo_url,path)
   
    # Check header if there is additional pages to retrieve
    if 'link' in r.headers:
        pages = dict(
            [(rel[6:-1], url[url.index('<')+1:-1]) for url, rel in
                [link.split(';') for link in
                    r.headers['link'].split(',')]])
        last = False
        while 'last' in pages and 'next' in pages:
                pages = remaining_pages(auth,r,csvout,pages)
                if last:
                    break
                if pages['next'] == pages['last']:
                   last = True
        
    print("Done Retrieving Github issues")
