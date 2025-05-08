from appdirs import AppDirs

import time
import asyncio

print(AppDirs('trader').user_config_dir)
print(AppDirs('trader').user_log_dir)

async def task1():
    print("task1")
    time.sleep(10)
    print("task1 over")

async def task2():
    print("task2")
    time.sleep(10)
    print("task2 over")


asyncio.run(task1())
asyncio.run(task2())