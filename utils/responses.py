async def get_info_data(socket):
    info = await socket.get_info()
    time = await socket.get_time()
    return info, time