__author__ = 'epq_008'
import urllib2

# Reads the content of a web page at a specified URL
# Returns a list containing the lines of the fetched web page
def grabWebPage(url):
    urlHandler = urllib2.urlopen(url)
    lines = urlHandler.readlines()
    urlHandler.close()
    return lines

# Returns the substring contained between a left and a right delimiter
def substringBetween(string, leftDelimiter, rightDelimiter):
    index1 = string.find(leftDelimiter) + len(leftDelimiter)
    index2 = string.find(rightDelimiter)
    return string[index1:index2]

# Extracts information from a single line of text
# Parameters:
#   htmlLines is a list of lines
#   lineIdentifier is a string contained only in the line that has the information we seek
#   leftDelimiter, rightDelimiter are strings that surround the information we want to extract
# Returns a string
def wrapInfoInDocument(htmlLines, lineIdentifier, leftDelimiter, rightDelimiter):
    for line in htmlLines:
        if lineIdentifier in line:
            info = substringBetween(line, leftDelimiter, rightDelimiter)
            return info

# Wraps the current time in Pittsburgh from http://tycho.usno.navy.mil/cgi-bin/timer.pl
# Returns a string
def wrapTime():
    webLines = grabWebPage('http://tycho.usno.navy.mil/cgi-bin/timer.pl')
    time = wrapInfoInDocument(webLines, 'Eastern Time', ', ', ' EDT')
    return time

# Wraps the price of gold from http://www.ticker.com
# Returns a string
def wrapGoldPrice():
    webLines = grabWebPage('http://www.ticker.com')
    gold = wrapInfoInDocument(webLines, '<div class="cell">Gold', '<span  style="padding-left:30px;">', '</span>')
    return gold

# Generates an HTML document including the current time in Pittsburgh,
# and the current price of gold.
# Returns a string
def generateTimeGoldPage():
    time = wrapTime()
    goldPrice = wrapGoldPrice()
    title = 'Time and Gold in Pittsburgh'
    content = '<h1>Hi everyone!</h1>\n'
    content += '<p>It is now ' + time + ' in Pittsburgh, '
    content += 'and the price of gold is ' + goldPrice + '.</p>\n'
    page = generateHTMLPage(title, content)
    return page

# Generates a standard HTML page with a given title and body
# Returns a string
def generateHTMLPage(title, content):
    page = '<html>\n'
    page += '<head>\n'
    page += '<title>' + title + '</title>\n'
    page += '</head>\n'
    page += '<body>\n' + content + '</body>\n'
    page += '</html>\n'
    return page

# Saves a string into a file. (See fileIO.py for details)
# Returns None
def saveText(text, fileName):
    fileHandler = open(fileName, "wt") # wt stands for write text
    fileHandler.write(text) # write the text
    fileHandler.close() # close the file

# Test the preceding code by creating and displaying
# a web page with the current time in Pittsburgh and
# the current price of gold
page = generateTimeGoldPage()
print page
saveText(page, "test.html")
import webbrowser
webbrowser.open("test.html")