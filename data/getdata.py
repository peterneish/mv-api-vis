import urllib, json
start = "http://collections.museumvictoria.com.au/api/search?collection=Dorothy+Howard+Collection&envelope=true"

# set a limit so that we don't create stupidly big files
pagelimit = 5

# store our raw data here
all_json = "alljson.json"

# get the first page
response = urllib.urlopen(start)
page1_raw = response.read()
page1_parsed = json.loads(page1_raw)

numpages = page1_parsed['headers']['totalPages']
if numpages > pagelimit:
    numpages = pagelimit

print numpages

all_data = page1_parsed['response']

for p in range(2,numpages+1):
    nextpage = start+"&page="+str(p)
    print "Fetching " + nextpage
    response = urllib.urlopen(nextpage)
    parsed = json.loads(response.read())
    all_data.append(parsed['response'])

# write to file
f_all = open(all_json, 'w')
json.dump(all_data, f_all)
f_all.close()






