use my_rust_project::benchmark_hashing;

fn main() {
    let data = vec![b'a'; 10_000_000]; // 10 MB of data

    let (sha256_time, sha256_memory, md5_time, md5_memory) = benchmark_hashing(&data);

    println!("SHA-256 Time: {:.6} seconds", sha256_time);
    println!("SHA-256 Memory: {:.2} MB", sha256_memory);
    println!("MD5 Time: {:.6} seconds", md5_time);
    println!("MD5 Memory: {:.2} MB", md5_memory);
}
