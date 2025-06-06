import asyncio
from ping3 import ping
from rich.console import Console
from rich.table import Table

console = Console()

async def ping_host(host):
    try:
        response = await asyncio.to_thread(ping, host, timeout=2)
        if response is None:
            return host, "Timeout", "❌", None
        else:
            return host, f"{round(response * 1000, 2)} ms", "✅", response
    except Exception as e:
        return host, str(e), "❌", None

async def main():
    with open("domains.txt", "r") as f:
        hosts = [line.strip() for line in f.readlines() if line.strip()]

    tasks = [ping_host(host) for host in hosts]
    results = await asyncio.gather(*tasks)

    table = Table(title="🌐 Network Latency Visualizer", show_lines=True)
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Latency", justify="right")
    table.add_column("Status", justify="center")
    
    for host, latency, status, value in results:
        color = "green" if value and value < 0.1 else "yellow" if value and value < 0.3 else "red"
        table.add_row(host, f"[{color}]{latency}[/{color}]", status)

    console.print(table)

if __name__ == "__main__":
    asyncio.run(main())
