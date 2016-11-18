from bs4 import BeautifulSoup

url = r"5_date_query_submit.html"
soup = BeautifulSoup(open(url).read(),"lxml")

table = soup.find('table', {'class': 'Grid'})
rows = table.findAll('tr')
cnt = 0
relative_link = []

for tr in rows:
	print "You're in the for loop"
	cols = tr.findAll('td')
	if len(cols)>0:
		print "You're in the if statement"
		cnt=cnt+1
		links = cols[0].findAll['a']('href')
		relative_link.append(links)
print cnt		
for link in relative_link:
#			absolute_link = 'http://judis.nic.in/supremecourt/' + link
	print "You're in the link loop"
	print link
	
#		anchor_tags.append(anchors)

judgements_links = []
for table_row in soup.select(".Table1 tr"):
	print "hello 2"
	table_cells = table_row.findAll('td')

	if len(table_cells) > 0:
		print "Hello"
		relative_link = table_cells[0].find('a')['href']
		absolute_link = 'http://judis.nic.in/supremecourt/' + relative_link
		judgements_links.append(absolute_link)