import subprocess

def run(cmd):
    print(f"$ {cmd}")
    subprocess.run(cmd, shell=True, check=False)

if __name__ == "__main__":
    run("pytest -q")
