# main.py
from mylib.lib import hash_sha256, hash_md5


def main():
    # Example use cases
    data = "Hello from Python!"
    sha256_result = hash_sha256(data)
    md5_result = hash_md5(data)

    print(f"SHA-256: {sha256_result}")
    print(f"MD5: {md5_result}")


if __name__ == "__main__":
    main()
