import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def get_data_from_local_html(html_name):
    """for debugging"""
    with open(html_name, "r", encoding="utf-8") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "lxml")
        json_str = soup.find("script", attrs={"class": "state-view"})
        data = json.loads(json_str.text)

    return data


def get_data_from_yandex_maps(url):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=ChromiumService(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")
    json_str = soup.find("script", attrs={"class": "state-view"})
    data = json.loads(json_str.text)

    return data


def format_coordinates_from_list_to_xml(track_points_list):
    track_segments_list = []

    for point in track_points_list:
        lat = point[1]
        lon = point[0]
        ele = ""
        time = ""

        track_segment = f"""\n      <trkpt lat="{lat}" lon="{lon}">
        <ele>{ele}</ele>
        <time>{time}</time>
      </trkpt>"""

        track_segments_list.append(track_segment)

    return "".join(track_segments_list)


def generate_route_name(data):
    route_points_name = data.get("stack")[0].get("routePoints")
    route_name = []

    for route_point in route_points_name:
        route_name.append(route_point.get("searchResult").get("address"))

    return " - ".join(route_name)


def generate_gpx(route_name, route_coordinates):
    gpx_string = f"""<?xml version='1.0' encoding='UTF-8'?>
    <gpx version="1.1" creator="https://t.me/kintolayli" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
      <metadata>
        <name>{route_name}</name>
        <author>
          <link href="https://t.me/kintolayli">
            <text>kintolayli</text>
            <type>text/html</type>
          </link>
        </author>
      </metadata>
      <trk>
        <name>{route_name}</name>
        <trkseg>{route_coordinates}
        </trkseg>
      </trk>
    </gpx>"""

    return gpx_string


def convert_to_gpx(url):
    data = get_data_from_yandex_maps(url)
    route_name = generate_route_name(data)
    routes = data.get("stack")[0].get("routerResponse").get("routes")

    gpx_routes = []

    for route in routes:
        route_coordinates = route.get("coordinates")
        filename = route.get("uuid")
        route_distance = route.get("distance").get("text")
        route_coordinates_xml = format_coordinates_from_list_to_xml(
            route_coordinates
        )

        gpx = generate_gpx(route_name, route_coordinates_xml)

        gpx_routes.append([gpx, filename, route_distance])

    return gpx_routes


def create_gpx_filename(route):
    filename = route[1]
    route_distance = route[2]

    return f"{filename}_{route_distance}.gpx"


def save_gpx_file_to_disk(route):
    gpx_file = route[0]
    full_filename = create_gpx_filename(route)
    with open(full_filename, "w", encoding="utf-8") as f:
        f.write(gpx_file)


def main(url):
    template = "https://yandex.ru/maps/"
    if url.startswith(template):
        routes = convert_to_gpx(url)

        for route in routes:
            save_gpx_file_to_disk(route)

        return "Success"
    else:
        return f"Input url does not match the template - {template}..."


if __name__ == "__main__":
    input_url = input("Input URL: ")
    response = main(input_url)
    print(response)
