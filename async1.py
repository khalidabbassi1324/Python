import asyncio

# Asynchronous function to count from 1 to 5 with a delay of 1 second
async def count_1():
    for i in range(1, 6):
        print(f"Count 1: {i}")
        await asyncio.sleep(1)  # Simulate work with a 1 second delay

# Asynchronous function to count from 6 to 10 with a delay of 1 second
async def count_2():
    for i in range(6, 11):
        print(f"Count 2: {i}")
        await asyncio.sleep(1)  # Simulate work with a 1 second delay

# Main async function to run both counting tasks concurrently
async def main():
    # Run count_1 and count_2 concurrently using asyncio.gather
    await asyncio.gather(count_1(), count_2())

# Run the main function using asyncio.run
if __name__ == "__main__":
    asyncio.run(main())
