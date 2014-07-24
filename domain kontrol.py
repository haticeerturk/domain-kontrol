import urllib2 , re

site = raw_input("Aranacak siteyi girin: ")

url = "http://www.whois.com.tr/?q=" + site +""

ara = urllib2.urlopen(url)

oku = ara.read()

aranan = re.search("status wrong",oku)

if aranan :
        print "Kullanimda"

else :
        print "Musait"
