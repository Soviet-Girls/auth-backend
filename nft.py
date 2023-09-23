from web3 import Web3
import abi

rpc_url = 'https://polygon.rpc.thirdweb.com'
chain_id = 137

w3 = Web3(Web3.HTTPProvider(rpc_url))

nft_address = '0x15F4272460062b835Ba0abBf7A5E407F3EF425d3'
nft_contract = w3.eth.contract(nft_address, abi=abi.thirdweb)

def check_owner(address):
    balance = nft_contract.functions.balanceOf(address).call()
    if balance > 0:
        return True
    return False

def generate_json(image_url: str, author: str) -> dict:
    return {   
        "description": "https://vk.ru/minting_bot",      
        "image": image_url,  
        "name": "VK Minting Bot NFT",   
        "attributes": [
            { "trait_type": "Author", "value": author }
        ]
    }