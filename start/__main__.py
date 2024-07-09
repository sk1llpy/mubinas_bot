import sys
from utils import polling
from data import config

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m start <mode>")
        print("Modes: polling")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == "polling":
        polling.main()

    else:
        print(f"Unknown mode: {mode}")
        print("Usage: python -m start <mode>")
        print("Modes: polling")
        sys.exit(1)


if __name__ == "__main__":
    main()
