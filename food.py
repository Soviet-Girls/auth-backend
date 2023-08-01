import requests

def get_items_by_collection(collection: str = "POLYGON:0xc66e770d36f373f410f342a3e1d4b905535ce1b5"):
    response = requests.get(f"https://api.rarible.org/v0.1/items/byCollection?collection={collection}&size=10000")
    return response.json()
        
def get_ownership(item_id: str):
    response = requests.get(f"https://api.rarible.org/v0.1/ownerships/byItem?itemId={item_id}")
    return response.json()
        
def check_ownership(wallet: str):
    items = get_items_by_collection()
    for item in items['items']:
        owners = get_ownership(item['id'])
        for owner in owners['ownerships']:
            if owner['owner'].split(':')[1].lower() == wallet.lower():
                if item['id'] == "POLYGON:0xc66e770d36f373f410f342a3e1d4b905535ce1b5:85190226308317464199122676410227843607654320109346695769644739293606544670721":
                    return True
    return False