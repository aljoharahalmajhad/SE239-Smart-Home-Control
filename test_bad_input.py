import socket, time

def connect():
    s = socket.create_connection(("127.0.0.1", 5091))
    return s, s.makefile("r", encoding="utf-8", errors="replace")

def send(s, f, msg):
    s.sendall((msg + "\n").encode())
    return f.readline().strip()

# 1. Three clients log in at once (Week 8)
clients = []
for name in ["alice", "bob", "carol"]:
    s, f = connect()
    f.readline()
    print(name, "->", send(s, f, f"LOGIN {name}"))
    clients.append((s, f))

print("PING ->", send(*clients[0], "PING"))
print("LIST ->", send(*clients[0], "LIST"))

# 2. Bad input tests
s, f = connect(); f.readline()
print("Duplicate user ->", send(s, f, "LOGIN alice"))
print("Command before login ->", send(s, f, "HELLO"))
print("Empty command ->", send(s, f, ""))

# 3. Invalid bytes (this is the one that crashes the thread)
s, f = connect(); f.readline()
s.sendall(b"\xff\xfe\n")
time.sleep(0.5)

# 4. Is the server still alive?
s2, f2 = connect(); f2.readline()
print("Server alive ->", send(s2, f2, "LOGIN dave"))
print("LIST ->", send(s2, f2, "LIST"))
