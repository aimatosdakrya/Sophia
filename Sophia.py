import requests
import folium
import os

def get_location(ip):
    """GET LOCATION FROM IP ADDRESS"""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()  # RAISE HTTPERROR FOR BAD RESPONSES
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {"status": "fail"}

def show_map(lat, lon):
    """SHOW MAP IN DEFAULT BROWSER"""
    # CREATE A FOLIUM MAP AND SAVE IT AS AN HTML FILE
    map_location = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup='Location').add_to(map_location)
    map_path = 'map.html'
    map_location.save(map_path)

    # OPEN THE MAP HTML FILE IN THE DEFAULT BROWSER
    if os.name == 'nt':  # FOR WINDOWS
        os.system(f'start {map_path}')
    elif os.name == 'posix':  # FOR macOS and LINUX
        os.system(f'open {map_path}')  # macOS
        # os.system(f'xdg-open {map_path}')  # LINUX

def search_ip(ip):
    """HANDLE IP SEARCH"""
    if not ip:
        print("Please enter an IP address.")
        return

    data = get_location(ip)
    if data['status'] == 'fail':
        print("Invalid IP address or request failed.")
    else:
        lat = data['lat']
        lon = data['lon']
        show_map(lat, lon)
        # PRINT LOCATION DATA
        print(f"IP Address: {data.get('query', 'N/A')}")
        print(f"Reverse: {data.get('as', 'N/A')}")
        print(f"Proxy?: {data.get('proxy', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")

# MAIN EXECUTION
if __name__ == "__main__":
    ip = input(str("Enter the IP address: "))
    search_ip(ip)

# IP CATEGORY :)
ipCategory = len(ip)
if ipCategory >= 37:
    print(f'IP type: IPV6')
elif ipCategory < 37:
    print(f'IP type: IPV4')