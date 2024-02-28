import requests
import bs4

def fetch_wikipedia_page_details(url):
    exclude_sections = ['See also', 'References', 'External links', 'Further reading', 'Notes', 'Bibliography']
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the title of the Wikipedia page
    title = soup.find('h1', id='firstHeading').text if soup.find('h1', id='firstHeading') else 'No Title Found'
    
    # Initialize list for links
    all_links = []
    
    # Find links from the introductory section
    parser_output = soup.find('div', class_='mw-parser-output')
    if parser_output:
        intro_section = parser_output.find('p')
        if intro_section:
            all_links.extend(['https://en.wikipedia.org' + a['href'] for a in intro_section.find_all('a', href=True) if a['href'].startswith('/wiki/')])
    
    # Find subsections and their links, avoiding excluded sections
    subsections = soup.find_all('span', class_='mw-headline')
    for subsection in subsections:
        if subsection.text not in exclude_sections:
            parent_section = subsection.find_parent('h2' if subsection.name == 'span' else 'h3')
            if parent_section:
                links = ['https://en.wikipedia.org' + a['href'] for a in parent_section.find_all_next('a', href=True) if a['href'].startswith('/wiki/')]
                all_links.extend(links)
                next_header = parent_section.find_next_sibling(['h2', 'h3'])
                if next_header and next_header.find('span', class_='mw-headline'):
                    break
    
    # Deduplicate the links list
    all_links = list(set(all_links))

    # Construct the return dictionary
    page_data = {
        'title': title,
        'links': all_links,
        'url': url
    }

    return page_data