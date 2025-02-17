from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def function1():
    cpuusage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_used = round(memory.used / (1024 ** 3), 1)
    memory_total = round(memory.total / (1024 ** 3), 1)
    memory_percent = memory.percent
    disk = psutil.disk_usage("/")
    disk_used = round(disk.used / (1024 ** 3), 1)
    disk_total = round(disk.total / (1024 ** 3), 1)
    disk_percent = disk.percent
    network = psutil.net_io_counters()
    network_sent = round(network.bytes_sent / (1024 ** 3), 1)
    network_recv = round(network.bytes_recv / (1024 ** 3), 1)
    return render_template(
        "index.html",
        cpuusage=cpuusage,
        memory_used=memory_used,
        memory_total=memory_total,
        memory_percent=memory_percent,
        disk_used=disk_used,
        disk_total=disk_total,
        disk_percent=disk_percent,
        network_sent=network_sent,
        network_recv=network_recv
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=20007, debug=True)