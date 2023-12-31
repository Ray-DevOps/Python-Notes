

# Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages 
# that can be used to extract data from HTML, which is useful for web scraping. 

# Web scraping is the process of extracting information from a website from the website's underlying HTML code. 
# Note: Legally, you can only scrap data that is publicly available and not copyrighted.
# Also, you can't scrape data that is behind authentication. This is because data behind authentication usually binds the users
# to policies and terms of service, whereas users cannot be bound to policies with data that is readily available without authentication.

# As a rule of thumb, if you come across a website that provides an API endpoint, it is always better to register and use the API
# than to scrape their data directly.
# Also, using Python loops to continuously scrape data can result in serious traffic on the website and affect human user experience

# When you visit any website, to see the kind of data that you are not allow to scrape, add "/robots.txt" to the root of the URL.
# For example https://www.linkedin.com/robots.txt will show you all the data categories that you can't scrape from linkedIn



#                                         ILLUSTRATION
#                               ---------------------------------

#  In this illustration, we use Beautiful Soup to extract data from the site website.html, which is located
#  [here] (https://github.com/Ray-DevOps/Python-Notes/blob/main/beautiful-soup/website.html)

from bs4 import BeautifulSoup                               # We start by importing the Beautiful Soup class from the Beautiful Soup 4 (bs4) module.                                       

with open('website.html', encoding="utf8") as file:
    file_content = file.read()

soup = BeautifulSoup(file_content, 'html.parser')          # In some cases, we may have to use the 'lxml' instead of 'html.parser' in which case we import lxml



print(soup.title)              ---------->           <title>Angela's Personal Site</title>                 # This prints the title of the html file
print(soup.title.string)       ---------->           Angela's Personal Site                                # This prints the string in the title of the html file
print(soup.title.name)         ---------->           title                                                 # This prints the name of the title which is "title"

print(soup)                    ---------->           # This will print out the entire HTML code
print(soup.prettify())         ---------->           # This will print out the entire HTML code with the proper indentation to make it easier to read

print(soup.p)                      ---------->           # This will print out the first paragraph in the HTML code
print(soup.find_all(name="p"))     ---------->           # This will print out all the paragraphs in the HTML code

print(soup.a)                      ---------->           # This will print out the first anchor tag in the HTML code
print(soup.find_all(name="a"))     ---------->           # This will print out all the anchor tags in the HTML code

print(soup.li)                     ---------->           # This will print out the first paragraph in the HTML code
print(soup.ol)                     ---------->           # This will print out the first ordered list in the HTML code
print(soup.ul)                     ---------->           # This will print out the first unordered list in the HTML code
print(soup.find_all(name="ul"))    ---------->           # This will print out all the unordered lists in the HTML code


# Suppose you wanted to print only the texts in the anchor tags, you would loop through all the anchor tags, and use the
# getText() method to print them out, as shown below.


all_anchor_tags = soup.find_all(name="a")

for tags in all_anchor_tags:
    print(tags.getText())      
    
        |
        ↓

   The App Brewery
   My Hobbies
   Contact Me



# Suppose you wanted to print only the links in the anchor tags, you would loop through all the anchor tags, and use the
# get() method to print the "href" as the links are the href values:


all_anchor_tags = soup.find_all(name="a")

for tags in all_anchor_tags:
    print(tags.get("href"))      
    
        |
        ↓

https://www.appbrewery.co/
https://angelabauer.github.io/cv/hobbies.html
https://angelabauer.github.io/cv/contact-me.html



# While the find_all() method prints every element that matches a criteria, the find() method can be used to find a particular
# element that matches a particular criteria (such as a heading with a specific name, or paragraph with specific ID)


heading = soup.find(name="h1", id="name")
print(heading)             ---------->        <h1 id="name">Angela Yu</h1>

section_heading = soup.find(name="h3", class_="heading")                                          # Eventhough the name of the actual attribute in the HTLM file is "class",
print(section_heading)     ---------->       <h3 class="heading">Books and Teaching</h3>       # we add _ so that it doesn't clash with the "class" keyword for creating classes in Python
print(section_heading.getText())        ---------->       Books and Teaching                       # To print only the text contained in the heading
print(section_heading.name)             ---------->       h3                                       # To get just the name of the tag
print(section_heading.get("class"))     ---------->       ['heading']                              # To get the value of the "class" attribute


# We can also use CSS selectors to get hold of elements in the HTML code. The select_one() method will return the first matching
# item, while select_all() will return all matching items.


company_url = soup.select_one(selector="p a")                                                    # To get the first "a tag" which sits inside a "p tag" (first anchor_tag inside a paragraph)
print(company_url)                    ---------->     <a href="https://www.appbrewery.co/">The App Brewery</a>



# To use the CSS selector to select an element by ID, we use the # sign

name = soup.select_one(selector="#name")
print(name)                          ---------->     <h1 id="name">Angela Yu</h1>                # This picks the first element with the ID "name"


# To use the CSS selector to select an element by class, we use .                         

headings = soup.select(".heading")                                                               # This selects all elements with class "heading"
print(headings)                      ---------->      [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]






