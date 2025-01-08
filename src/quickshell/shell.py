import asyncio
from typing import Tuple


async def run_shell(cmd, print_output: bool = False) -> Tuple[str, str]:
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = [], []

    async def stream_output(stream, array, print_output):
        while True:
            line = await stream.readline()
            if line:
                text = line.decode().rstrip("\n")
                array.append(text)
                if print_output:
                    print(text)
            else:
                break

    await asyncio.gather(
        stream_output(process.stdout, stdout, print_output),
        stream_output(process.stderr, stderr, print_output)
    )

    await process.wait()

    return "\n".join(stdout), "\n".join(stderr)


