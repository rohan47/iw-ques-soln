#!/usr/bin/python3
import inotify.adapters
import subprocess
import asyncio
import websockets

def get_ofset(f, lineno):
    line_offset = []
    offset = 0
    for line in f:
        line_offset.append(offset)
        offset += len(line)
    return line_offset[lineno]

async def file_operation(websocket, path):
    #test = await websocket.recv()
    with open("demo.log") as f:
        f.seek(0)
        lineno = int(subprocess.getoutput('wc -l demo.log | cut -d" " -f1 ')) - 10
        if lineno > 0:
            f.seek( get_ofset(f, lineno))
        else:
            f.seek(0)
        #print(f.read())
        for line in f.readlines():
            await websocket.send(line)
        i = inotify.adapters.Inotify()
        i.add_watch("demo.log")
        for event in i.event_gen(yield_nones=False):
            (_, type_name, path, filename) = event
            if type_name == ['IN_MODIFY']:
                #print(f.read())
                await websocket.send(f.read())

start_server = websockets.serve(file_operation, 'localhost', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
