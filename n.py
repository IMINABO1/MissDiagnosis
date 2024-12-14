from notion_client import Client

# Your authentication token
TOKEN = ""

# Your actual database ID
database_id = ""

# Initialize Notion client with your integration token
notion = Client(auth=TOKEN)

# Your outbreak data dictionary
outbreak_data = {
    'outbreak_1': {'date': '13 November 2024 ', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_10': {'date': '20 September 2024 ', 'title': 'Avian Influenza A(H9N2) in Ghana'},
    'outbreak_11': {'date': '4 September 2024 ', 'title': 'Influenza A(H1N1) variant virus in Viet Nam'},
    'outbreak_12': {'date': '2 September 2024 ', 'title': 'Avian Influenza A(H5N1) in Cambodia'},
    'outbreak_13': {'date': '30 August 2024 ', 'title': 'Mpox in Sweden'},
    'outbreak_14': {'date': '23 August 2024 ', 'title': 'Oropouche virus disease in Region of the Americas'},
    'outbreak_15': {'date': '23 August 2024 ', 'title': 'Acute encephalitis syndrome due to Chandipura virus in India'},
    'outbreak_16': {'date': '22 August 2024 ', 'title': 'Mpox – African Region'},
    'outbreak_17': {'date': '31 July 2024 ', 'title': 'Antimicrobial Resistance Hypervirulent Klebsiella pneumoniae in Global situation'},
    'outbreak_18': {'date': '22 July 2024 ', 'title': 'Dengue in Iran (Islamic Republic of)'},
    'outbreak_19': {'date': '9 July 2024 ', 'title': 'Mpox in South Africa'},
    'outbreak_2': {'date': '1 November 2024 ', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_20': {'date': '14 June 2024 ', 'title': 'Avian Influenza A(H5N2) in Mexico'},
    'outbreak_3': {'date': '31 October 2024 ', 'title': 'Malaria in Ethiopia'},
    'outbreak_4': {'date': '25 October 2024 ', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_5': {'date': '18 October 2024 ', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_6': {'date': '11 October 2024 ', 'title': 'Marburg virus disease in Rwanda'},
    'outbreak_7': {'date': '3 October 2024 ', 'title': 'West Nile virus in Barbados'},
    'outbreak_8': {'date': '2 October 2024 ', 'title': 'Middle East respiratory syndrome coronavirus in Kingdom of Saudi Arabia'},
    'outbreak_9': {'date': '30 September 2024 ', 'title': 'Marburg virus disease in Rwanda'}
}

# Iterate over each outbreak and create a Notion page for it
for outbreak_id, outbreak_info in outbreak_data.items():
    try:
        # Create a new page in Notion for each outbreak
        response = notion.pages.create(
            parent={"database_id": database_id},  # Using the correct database_id
            properties={
                "Place": {
                    "title": [  # Use the title property for the first column
                        {
                            "text": {
                                "content": outbreak_info['title']  # Use 'title' here
                            }
                        }
                    ]
                },
                "Disease": {
                    "multi_select": [
                        {"name": outbreak_info['title']}  # Using 'title' for Disease
                    ]
                }
            }
        )
        print(f"Page created for: {outbreak_info['title']}")
    except Exception as e:
        print(f"Error creating page for {outbreak_id}: {str(e)}")
