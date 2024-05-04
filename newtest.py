import shopify
from values import*


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
Inventory_Level=shopify.Location.inventory_levels(Locations[0])
AllInventory=get_all_resources(Inventory_Level)
print(AllInventory)


