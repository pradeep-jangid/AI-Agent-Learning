import asyncio
import time

async def call_llm(model: str, sleep_time:int) -> str:
    print(f"Calling {model}...")
    await asyncio.sleep(sleep_time)  # simulate sleep(seconds) API call
    print(f"Finished {model}")
    return f"Response from {model}"

async def sequential():
    print("\n--- Sequential ---")
    start = time.perf_counter()

    r1 = await call_llm("gpt-4o", 1)
    r2 = await call_llm("claude", 1)
    r3 = await call_llm("gemini", 1)

    end = time.perf_counter()
    print(f"Sequential took: {end - start:.2f}s")
    return r1, r2, r3

async def parallel():
    print("\n--- Parallel with gather ---")
    start = time.perf_counter()

    r1, r2, r3 = await asyncio.gather(
        call_llm("gpt-4o", 1),
        call_llm("claude", 1),
        call_llm("gemini", 1)
    )

    end = time.perf_counter()
    print(f"Parallel took: {end - start:.2f}s")
    return r1, r2, r3

async def main():
    await sequential()
    await parallel()

asyncio.run(main())