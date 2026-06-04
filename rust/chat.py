import asyncio
from utils.responses import get_info_data
import rustplus

async def watch_team_chat(socket):
    last_message_time = None

    while True:
        try:
            messages = await socket.get_team_chat()
            if messages:
                latest = messages[-1]

                if last_message_time == latest.time:
                    await asyncio.sleep(2)
                    continue

                last_message_time = latest.time

                if latest.message.lower().strip() == "!pop":
                    server_info, _ = await get_info_data(socket)
                    await socket.send_team_message(f"{server_info.players}/{server_info.max_players}")
                if latest.message.lower().strip() == "!events":
                    markers = await socket.get_markers()
                    events = [m for m in markers if m.type.name in [
                        "CargoShip", "CH47", "PatrolHelicopter", "Explosion", "LockedCrate"
                    ]]
                    if events:
                        for event in events:
                            await socket.send_team_message(f" {event.type.name} at {int(event.x)}, {int(event.y)}")
                    else:
                        await socket.send_team_message("No active events right now")
        except Exception as e:
            print(f"Chat error: {e}")

        await asyncio.sleep(2)