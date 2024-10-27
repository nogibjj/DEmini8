import hashlib
import time
import psutil
import os
import subprocess

def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def hash_md5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()

def memory_usage():
    """Get current memory usage in MB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

def benchmark_python():
    """Benchmark Python SHA-256 and MD5."""
    data = b'a' * 10**7  # 10 MB of data

    # SHA-256 benchmark
    start_time = time.time()
    hash_sha256(data)
    sha256_time = time.time() - start_time
    sha256_memory = memory_usage()

    # MD5 benchmark
    start_time = time.time()
    hash_md5(data)
    md5_time = time.time() - start_time
    md5_memory = memory_usage()

    return sha256_time, sha256_memory, md5_time, md5_memory

def extract_float_from_output(line):
    """Extract the numeric value from the Rust output."""
    return float(line.split(": ")[1].strip().split()[0])

def benchmark_rust():
    """Run the Rust binary and parse its output."""
    result = subprocess.run(
        ["cargo", "run", "--release"], capture_output=True, text=True
    )

    output = result.stdout.splitlines()

    sha256_time = extract_float_from_output(output[0])
    sha256_memory = extract_float_from_output(output[1])
    md5_time = extract_float_from_output(output[2])
    md5_memory = extract_float_from_output(output[3])

    return sha256_time, sha256_memory, md5_time, md5_memory

def print_results(python_results, rust_results):
    """Print Python and Rust benchmark results in a table format."""
    print(f"{'Metric':<20} {'Python':<15} {'Rust':<15}")
    print("-" * 50)
    print(f"{'SHA-256 Time (s)':<20} {python_results[0]:<15.6f} {rust_results[0]:<15.6f}")
    print(f"{'SHA-256 Memory (MB)':<20} {python_results[1]:<15.2f} {rust_results[1]:<15.2f}")
    print(f"{'MD5 Time (s)':<20} {python_results[2]:<15.6f} {rust_results[2]:<15.6f}")
    print(f"{'MD5 Memory (MB)':<20} {python_results[3]:<15.2f} {rust_results[3]:<15.2f}")

if __name__ == "__main__":
    print("Running Python benchmarks...")
    python_results = benchmark_python()

    print("Running Rust benchmarks...")
    rust_results = benchmark_rust()

    print("\nBenchmark Results:")
    print_results(python_results, rust_results)
