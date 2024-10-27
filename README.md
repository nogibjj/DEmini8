[![Rust CI/CD Pipeline](https://github.com/nogibjj/DEmini8/actions/workflows/rustfmt.yml/badge.svg)](https://github.com/nogibjj/DEmini8/actions/workflows/rustfmt.yml)

[![Python CI/CD Pipeline](https://github.com/nogibjj/DEmini8/actions/workflows/pythonCI.yml/badge.svg)](https://github.com/nogibjj/DEmini8/actions/workflows/pythonCI.yml)

# DEmini8: Python and Rust 

This project showcases the performance differences between **Python** and **Rust** for hashing algorithms (SHA-256 and MD5). It includes benchmarking logic, memory usage tracking, and automation using GitHub Actions.

## Project Structure
   ```
DEmini8/
│
├── .github/
│   └── workflows/
│       ├── pythonCI.yml
│       └── rustfmt.yml
│
├── src/
│   ├── main.rs
│   └── lib.rs
├── tests/
│   └── test_hash.rs
├── main.py
├── test_main.py
├── benchmark.py
├── Cargo.toml
└── requirements.txt
   ```
## Installation

### Python Setup
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Rust Setup
1. Install Rust by following the instructions at [Rust Installation](https://www.rust-lang.org/tools/install).
2. Verify the installation:
   ```bash
   rustc --version
   cargo --version
   ```

## Usage

### Run Python Benchmark
To run the Python benchmark, execute:
```bash
python3 benchmark.py
```

### Run Rust Benchmark
To run the Rust benchmark, build the project in release mode:
```bash
cargo build --release
./target/release/my_rust_project
```
<img width="845" alt="image" src="https://github.com/user-attachments/assets/babc0565-a0a6-4ea0-a27b-9881ea78844f">


## GitHub Actions

This project includes two GitHub workflows:
- **Python CI:** Lint, format, test, and run benchmarks for the Python code.
- **Rust CI:** Format, lint, test, build, and benchmark the Rust code.

## Example Output

Below is an example of the benchmark output:

```
Benchmark Results:
Metric               Python          Rust           
--------------------------------------------------
SHA-256 Time (s)     0.003777        0.044086       
SHA-256 Memory (MB)  29.72           25552.00       
MD5 Time (s)         0.014292        0.014210       
MD5 Memory (MB)      29.72           27344.00    
```

## References

* [rust-cli-template](https://github.com/kbknapp/rust-cli-template)










