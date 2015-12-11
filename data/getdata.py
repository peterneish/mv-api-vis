import urllib, json

# set the starting url
start = "http://collections.museumvictoria.com.au/api/search?collection=Dorothy+Howard+Collection&envelope=true"
pagelimit = 2

# store our raw data here
all_json = "alljson.json"

# get the first page in order to find out how many pages in total
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


def remove_none(obj):
  if isinstance(obj, (list, tuple, set)):
      return type(obj)(remove_none(x) for x in obj if x is not None)
  elif isinstance(obj, dict):
      return type(obj)((remove_none(k), remove_none(v))
          for k, v in obj.items() if k is not None and v is not None)
  else:
      return obj
all_data = remove_none(all_data)
# write to file
f_all = open(all_json, 'w')
json.dump(all_data, f_all)
f_all.close()
