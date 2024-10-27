use md5::{Digest as Md5Digest, Md5};
use sha2::Sha256;
use std::time::Instant;
use sysinfo::{Pid, PidExt, ProcessExt, System, SystemExt};

pub fn hash_sha256(data: &[u8]) -> String {
    let mut hasher = Sha256::new();
    hasher.update(data);
    format!("{:x}", hasher.finalize())
}

pub fn hash_md5(data: &[u8]) -> String {
    let mut hasher = Md5::new();
    hasher.update(data);
    format!("{:x}", hasher.finalize())
}

pub fn memory_usage() -> f64 {
    let mut sys = System::new_all();
    sys.refresh_processes();
    let pid = Pid::from_u32(std::process::id());
    if let Some(process) = sys.process(pid) {
        process.memory() as f64 / 1024.0 // Convert KB to MB
    } else {
        0.0
    }
}

pub fn benchmark_hashing(data: &[u8]) -> (f64, f64, f64, f64) {
    // Benchmark SHA-256
    let start = Instant::now();
    let _ = hash_sha256(data);
    let sha256_time = start.elapsed().as_secs_f64();
    let sha256_memory = memory_usage();

    // Benchmark MD5
    let start = Instant::now();
    let _ = hash_md5(data);
    let md5_time = start.elapsed().as_secs_f64();
    let md5_memory = memory_usage();

    (sha256_time, sha256_memory, md5_time, md5_memory)
}
