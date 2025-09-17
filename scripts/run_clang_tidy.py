#!/usr/bin/env python3
import subprocess
import sys

def main():
    files = [f for f in sys.argv[1:] if f.endswith((".cpp", ".cc", ".h", ".hpp"))]
    if not files:
        return 0
    for f in files:
        print(f"Running clang-tidy on {f}")
        result = subprocess.run(
            ["clang-tidy", f, "--", "-std=c++17"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if result.returncode != 0:
            print(result.stdout)
            return result.returncode
    return 0

if __name__ == "__main__":
    sys.exit(main())
