import os
import time
import argparse
  
try:
  from http.server import HTTPServer, BaseHTTPRequestHandler
  
except ImportError: 
  input(
      f"Module http.server not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install sock.et.\npress enter to exit")
  exit()

print("Simp on Lemonade1S#5327 and CNJ#0516 or you’re Gay! >_<")
time.sleep(2)
os.system("clear")

print("""
                                                          H
 __       _____   ______________   ________   __________o===o__     ______    _____
|  |     |  ___| |   __    __   | |        | |    __    ||H|_   \  |       \ |  ___|
|  |___  |  ___| |  |  |  |  |  | |    —   | |   |  |   ||H|_ \  | |   —   | |  ___| 
|______| |_____| |_ |  |_ |  |_ | |________| |__ |  |__ ||H|   |_| |_______/ |_____|
                                                         |H|
                                                          V
      """)

parser = argparse.ArgumentParser(description = "Lemonade is a simple hacking console with cool features for begginer hackers! made by pastlecry#8645")

parser.add_argument('--PORT', '--P', type = int, help = 'Server Port', default = 9999)
parser.add_argument('--HOST', '--H', type = str, help = 'Server ip address', default = '')

arguments = parser.parse_args()


host = arguments.HOST
port = arguments.PORT

class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type","text/html")
    self.end_headers()
  
    self.wfile.write(bytes("<html><body><h1>SERVER IS RUNNING!<h1><body><html>", "utf-8"))
    print(f"ip: {self.client_address[0]}")

def main():
  server = HTTPServer((host, port), Server)
  print(f"Server is running...")
  print(f"port: {port}")
  server.serve_forever()
  server.server_close()
  print("Server stopped!")
 
if __name__ == "__main__":
 main()
