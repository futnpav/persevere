import requests
from bs4 import BeautifulSoup

def print_secret_message(url):
    # 1. Fetch the data from the URL
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the document.")
        return

    # 2. Parse the HTML table
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')

    data = []
    # Skip the header row (index 0)
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            try:
                # The format is typically: x, char, y
                # We strip extra whitespace or hidden characters
                x = int(cols[0].get_text().strip())
                char = cols[1].get_text().strip()
                y = int(cols[2].get_text().strip())
                data.append((x, y, char))
            except ValueError:
                # Skip rows that don't have valid integers (like extra headers)
                continue

    if not data:
        print("No data found.")
        return

    # 3. Determine grid dimensions
    max_x = max(item[0] for item in data)
    max_y = max(item[1] for item in data)

    # 4. Create the grid (initialized with spaces)
    # Grid is a list of lists: grid[y][x]
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # 5. Fill the grid with characters
    for x, y, char in data:
        grid[y][x] = char

    # 6. Print the grid
    # We print from max_y down to 0 because y=0 is usually the bottom 
    # and the top of the letters should be at the highest y-coordinate.
    for r in range(max_y, -1, -1):
        print("".join(grid[r]))

# Example usage:
# url = "YOUR_GOOGLE_DOC_URL_HERE"
# print_secret_message(url)

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
url2 = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_secret_message(url2)
