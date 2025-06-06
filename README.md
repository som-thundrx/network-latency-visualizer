# 🌐 Network Latency Visualizer

A simple yet powerful CLI tool to visualize the latency of multiple hosts in real time. It uses asynchronous pinging and displays results in a beautiful, color-coded terminal table.

This tool is ideal for network diagnostics, connectivity checks, or monitoring the responsiveness of servers — built with a clean, modular Python design.

---

## 📌 Features

- 🔁 **Asynchronous pinging** of multiple domains/IPs
- 🌈 **Color-coded latency display** (Green, Yellow, Red)
- 🧪 **Timeout & unreachable host detection**
- 📄 Reads from `domains.txt` input file
- 🎨 Beautiful CLI output using `rich`

---

## 🛠️ Tech Stack

- Python 3.8+
- [`ping3`](https://pypi.org/project/ping3/) – for ICMP ping
- [`rich`](https://pypi.org/project/rich/) – for terminal tables
- `asyncio` – for concurrent execution

---


