import sys
import signal


def run_cli():
    from ..rpc import HytaleRPC

    last_status = None

    def print_status(text):
        nonlocal last_status
        if text != last_status:
            last_status = text
            if "Connected" in text:
                print(f"  [+] Connected to Discord - Now showing your activity")
            elif "In Main Menu" in text:
                print(f"  [*] In Main Menu - Waiting in lobby")
            elif "Playing Singleplayer" in text:
                print(f"  [*] Entered World - Playing singleplayer")
            elif "Playing Multiplayer" in text:
                print(f"  [*] Joined Server - Playing multiplayer")
            elif "Loading" in text:
                print(f"  [*] Loading World - Entering game...")
            elif "Joining" in text:
                print(f"  [*] Joining Server - Connecting...")
            elif "Waiting" in text:
                print(f"  [.] Waiting - Launch Hytale to start")
            elif "Discord not running" in text:
                print(f"  [!] Discord not running")
            else:
                print(f"  [*] {text}")

    rpc = HytaleRPC(status_callback=print_status)

    def signal_handler(sig, frame):
        print("\n  [x] Shutting down...")
        rpc.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print("=" * 44)
    print("      Hytale Discord Rich Presence")
    print("=" * 44)
    print("\n  Press Ctrl+C to stop.\n")

    rpc.run()
