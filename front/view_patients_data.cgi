#!/usr/bin/python
import cgi
import cgitb
form = cgi.FieldStorage()
cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print '<head>'
print "hello"