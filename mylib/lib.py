"""Library functions for hashing, logging, and tracking memory usage."""
import hashlib
import time
import os
import psutil

# Define a global variable for the log file
LOG_FILE = "python_times.md"


def log_operation(operation, input_data, result, elapsed_time, memory_used):
    """Logs details of the operation to a markdown file."""
    with open(LOG_FILE, "a") as file:
        file.write(f"\nOperation: {operation}\n")
        file.write(f"Input Data: {input_data}\n")
        file.write(f"Result: {result}\n")
        file.write(f"Elapsed Time: {elapsed_time} microseconds\n")
        file.write(f"Memory Used: {memory_used} kB\n")


def hash_sha256(data):
    """Compute the SHA-256 hash of the given data."""
    start_time = time.time()
    hash_object = hashlib.sha256(data.encode())
    result = hash_object.hexdigest()
    elapsed_time = (time.time() - start_time) * 1_000_000  # microseconds
    memory_used = get_memory_usage()

    log_operation("SHA-256 Hash", data, result, elapsed_time, memory_used)
    return result


def hash_md5(data):
    """Compute the MD5 hash of the given data."""
    start_time = time.time()
    hash_object = hashlib.md5(data.encode())
    result = hash_object.hexdigest()
    elapsed_time = (time.time() - start_time) * 1_000_000  # microseconds
    memory_used = get_memory_usage()

    log_operation("MD5 Hash", data, result, elapsed_time, memory_used)
    return result


def get_memory_usage():
    """Get the current memory usage of the process in kB."""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss // 1024  # Convert bytes to kB


# Example Usage
if __name__ == "__main__":
    print(hash_sha256("Hello, World!"))
    print(hash_md5("Hello, World!"))
