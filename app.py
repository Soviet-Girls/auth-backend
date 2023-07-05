import os
import vk_api
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

import nft
import vk_auth

load_dotenv()

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)


vk_session = vk_api.VkApi(token=os.getenv("VK_TOKEN"))
vk = vk_session.get_api()

@app.route("/login", methods=["GET"])
def login():
    expire = request.args.get("expire")
    mid = request.args.get("mid")
    secret = request.args.get("secret")
    sid = request.args.get("sid")
    sig = request.args.get("sig")
    wallet = request.args.get("wallet")

    if not nft.check_owner(wallet):
        return make_response("No NFT on wallet", 403)
    
    if not vk_auth.check(expire, mid, secret, sid, sig):
        return make_response("VK Auth failed", 403)
    
    vk.storage.set(key="wallet", value=wallet, user_id=mid)

    link = vk.messages.getInviteLink(peer_id=os.getenv("PEER_ID"), reset=1)
    short_link = vk.utils.getShortLink(url=link["link"])['short_url']

    return jsonify({"link": short_link}), 200
