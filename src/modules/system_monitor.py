# system_monitor.py
import psutil
import logging

class SystemMonitor:
    def __init__(self):
        pass

    def check_cpu_usage(self):
        """Check and return the current CPU usage."""
        cpu_usage = psutil.cpu_percent(interval=1)
        logging.info(f"Current CPU usage: {cpu_usage}%")
        return cpu_usage

    def check_memory_usage(self):
        """Check and return the current memory usage."""
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        logging.info(f"Current memory usage: {memory_usage}%")
        return memory_usage

    def check_disk_usage(self):
        """Check and return the current disk usage."""
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        logging.info(f"Current disk usage: {disk_usage}%")
        return disk_usage

    def get_system_info(self):
        """Return basic system information."""
        cpu = self.check_cpu_usage()
        memory = self.check_memory_usage()
        disk = self.check_disk_usage()
        return f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%"
