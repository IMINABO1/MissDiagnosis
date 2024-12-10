from bs4 import BeautifulSoup
import pprint

def parse_disease_outbreaks_as_dict(html_content):
    """
    Parses HTML content to extract disease outbreak details into a dictionary of dictionaries.
    Removes links and formats titles with "in" instead of "-".
    Ensures there are no commas in the output.
    
    Args:
        html_content (str): The HTML content as a string.

    Returns:
        dict: A dictionary of dictionaries, where each key is a unique identifier for the outbreak.
    """
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all outbreak items
    outbreak_items = soup.find_all("a", class_="sf-list-vertical__item")

    # Initialize a dictionary to store structured data
    outbreaks = {}

    # Extract data from each outbreak item
    for idx, item in enumerate(outbreak_items, start=1):
        # Create a unique identifier (e.g., "outbreak_1", "outbreak_2")
        outbreak_id = f"outbreak_{idx}"

        # Extract data into a dictionary
        outbreak = {}

        # Extract the date and title
        title_container = item.find("h4", class_="sf-list-vertical__title")
        if title_container:
            # Date is the second span in the title
            date_span = title_container.find_all("span")[1]
            outbreak["date"] = date_span.text.strip().replace("|", "").replace(",", "")

            # Title is in the last span
            title_span = title_container.find("span", class_="trimmed")
            if title_span:
                # Replace " - " with " in " and remove commas
                outbreak["title"] = title_span.text.strip().replace(" - ", " in ").replace(",", "")

        # Add the outbreak dictionary to the main dictionary
        outbreaks[outbreak_id] = outbreak

    return outbreaks

# Example usage
if __name__ == "__main__":
    # Read the HTML from a file (or provide directly as a string)
    with open("res.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Parse the outbreaks into a dictionary of dictionaries
    outbreaks = parse_disease_outbreaks_as_dict(html_content)

    # Pretty print the nested dictionary
    pprint.pprint(outbreaks, indent=4)
    print(len(outbreaks))
