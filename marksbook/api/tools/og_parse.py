import urllib.request
from bs4 import BeautifulSoup


def get_page(url):
    """Scrapes a URL and returns the HTML source.
    Args:
        url (string): Fully qualified URL of a page.
    Returns:
        soup (string): HTML source of scraped page.
    """
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response,
                         'html.parser',
                         from_encoding=response.info().get_param('charset'))

    return soup


def get_og_title(soup):
    """Return the Open Graph title
    Args:
        soup: HTML from Beautiful Soup.
    Returns:
        value: Parsed content.
    """
    if soup.findAll("meta", property="og:title"):
        return soup.find("meta", property="og:title")["content"]
    else:
        return soup.title.string.strip()


def get_og_description(soup):
    """Return the Open Graph description
    Args:
        soup: HTML from Beautiful Soup.
    Returns:
        value: Parsed content.
    """
    if soup.findAll("meta", property="og:description"):
        return soup.find("meta", property="og:description")["content"]
    elif soup.findAll("meta", {"name": "description"}):
        return soup.find("meta", {"name": "description"})["content"]
    else:
        return 'No description'


def get_og_link_type(soup):
    if soup.findAll("meta", property="og:type"):
        print('type')
        return soup.find("meta", property="og:type")["content"]
    else:
        return 'website'


def get_og_image(soup):
    if soup.findAll("meta", property="og:image"):
        print('image')
        return soup.find("meta", property="og:image")["content"]
    else:
        return None

# soup2 = get_page("http://atrifonov.pythonanywhere.com/0/")
# print(get_no_og_title(soup2))


def get_og_info(link):
    """ Get nessesary og info from page by url link """
    soup = get_page(link)
    try:
        og_info = {
            'og_title': get_og_title(soup),
            'og_description': get_og_description(soup),
            'og_link_type': get_og_link_type(soup),
            'og_image': get_og_image(soup)
        }
        # print(og_info)
        return og_info
    except Exception as err:
        print(err)
        print('Smth go wrong while parsing!')
