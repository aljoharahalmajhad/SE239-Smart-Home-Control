
import socket

HOST = "127.0.0.1"
PORT = 5091


def main():
    try:
        with socket.create_connection((HOST, PORT), timeout=10) as connection:
            connection.settimeout(None)
            reader = connection.makefile("r", encoding="utf-8")
            print(reader.readline().strip())
            username = input("Username: ").strip()
            connection.sendall(f"LOGIN {username}\n".encode())
            response = reader.readline().strip()
            print(response)
            if not response.startswith("OK "):
                return
            print("Commands: PING, LIST, QUIT")
            while True:
                command = input("> ").strip()
                if not command:
                    continue
                connection.sendall((command + "\n").encode())
                reply = reader.readline()
                if not reply:
                    print("Server disconnected.")
                    break
                print(reply.strip())
                if command.upper() == "QUIT":
                    break
    except (OSError, ConnectionError) as error:
        print(f"Could not communicate with server: {error}")
    except (KeyboardInterrupt, EOFError):
        print("\nClient closed.")


if __name__ == "__main__":
    main()
