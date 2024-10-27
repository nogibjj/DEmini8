[![Rustfmt](https://github.com/nogibjj/DEmini8/actions/workflows/rustfmt.yml/badge.svg)](https://github.com/nogibjj/DEmini8/actions/workflows/rustfmt.yml)

[![pythonCI](https://github.com/nogibjj/DEmini8/actions/workflows/pythonCI.yml/badge.svg)](https://github.com/nogibjj/DEmini8/actions/workflows/pythonCI.yml)

# DEmini8: Python and Rust 

This project showcases the performance differences between **Python** and **Rust** for hashing algorithms (SHA-256 and MD5). It includes benchmarking logic, memory usage tracking, and automation using GitHub Actions.

## Project Structure
DEmini8/
│
├── .github/
│   └── workflows/
│       ├── python.yml
│       └── rust.yml
│
├── src/
│   ├── main.rs
│   └── lib.rs
├── tests/
│   └── test_hash.rs
├── main.py
├── test_main.py
├── benchmark_and_plot.py
├── Cargo.toml
└── requirements.txt

## Installation

### Python Setup
1. Make sure you have **Python 3.8+** installed.
2. Install the dependencies:
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
python3 benchmark_and_plot.py
```

### Run Rust Benchmark
To run the Rust benchmark, build the project in release mode:
```bash
cargo build --release
./target/release/my_rust_project
```

## GitHub Actions

This project includes two GitHub workflows:
- **Python CI:** Lint, format, test, and run benchmarks for the Python code.
- **Rust CI:** Format, lint, test, build, and benchmark the Rust code.

## Example Output

Below is an example of the benchmark output:

```
SHA-256 Time: 0.012345 seconds
SHA-256 Memory: 2.50 MB
MD5 Time: 0.010123 seconds
MD5 Memory: 2.20 MB
```

## References

* [rust-cli-template](https://github.com/kbknapp/rust-cli-template)










