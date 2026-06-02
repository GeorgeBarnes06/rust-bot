import json
from rustplus import RustSocket, ServerDetails

async def create_socket():
    with open("config.json") as f:
        config = json.load(f)

    r = config["rust"]
    details = ServerDetails(r["ip"], r["port"], r["steam_id"], r["player_token"])
    socket = RustSocket(details)
    await socket.connect()
    print("Rust connected!")
    return socket