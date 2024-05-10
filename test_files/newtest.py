import shopify
from ids_passwords_strings.values import*
import time


def get_all_resources(resource_type, **kwargs):
    resource_count = resource_type.count(**kwargs)
    resources = []
    if resource_count > 0:
        page=resource_type.find(**kwargs)
        resources.extend(page)
        while page.has_next_page():
            page = page.next_page()
            resources.extend(page)
    return resources





session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)
shop = shopify.Shop.current()

Locations = shopify.Location.find()
inventory = []
for location in Locations:
    print("next location")
    Inventory_Level=shopify.Location.inventory_levels(location)
    inventory.extend(Inventory_Level)
    while Inventory_Level.has_next_page():
        time.sleep(0.5)
        print("next Page")
        Inventory_Level = Inventory_Level.next_page()
        inventory.extend(Inventory_Level)

print(inventory)


