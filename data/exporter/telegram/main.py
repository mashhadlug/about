#!/usr/bin/env python3
from telethon import TelegramClient
import asyncio, json, os, sys


async def main():
    HASH_ID = os.getenv('HASH_ID')
    HASH_API = os.getenv('HASH_API')
    CHAT_ID = os.getenv('CHAT_ID')

    if not HASH_ID or not HASH_API or not CHAT_ID:
        print("set HASH_ID, HASH_API and CHAT_ID")
        exit(-1)

    client = TelegramClient('mashhadlug', HASH_ID, HASH_API)

    await client.start()
    async for msg in client.iter_messages(CHAT_ID, reverse=True):
        if msg.message:
            print(json.dumps({
                "id": msg.id, "date": str(msg.date), "message": msg.message
            }, ensure_ascii=False))

asyncio.run(main())
