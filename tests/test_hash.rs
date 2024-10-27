use my_rust_project::{hash_sha256, hash_md5};

#[test]
fn test_sha256() {
    let data = "test".as_bytes();  // Convert &str to &[u8]
    let expected = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08";
    assert_eq!(hash_sha256(data), expected);
}

#[test]
fn test_md5() {
    let data = "test".as_bytes();  // Convert &str to &[u8]
    let expected = "098f6bcd4621d373cade4e832627b4f6";
    assert_eq!(hash_md5(data), expected);
}
