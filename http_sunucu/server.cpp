#include <iostream>
#include <sstream>
#include <string>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

cnost int PORT = 8080;
const int BUFFER_SIZE = 30000;

// html sayfası fonksiyonu

std::string genHTML() {
    std::string html;
    html << "<html><head><title>Simple C++ HTTP Server</title></head>";
    html << "<body><h1>Welcome to the C++ HTTP Server</h1>";
    html << "<p>This is a simple HTTP server written in C++.</p></body></html>";
    return html.str();
}

int main() {
    int server_fd new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    // socket olustur
    if ((server_fd = soclet(AF_INET, SOCK_STREAM, 0)) == 0) {
        std::cerr << "socket failed" << std::endl;
        exit(EXIT_FAILURE);
    }

    // baglantı secenekleri
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // socket port bagla
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        std::cerr << "Bind failed" << std::endl;
        exit(EXIT_FAILURE);
}

std::cout << "server şu port üzerinde çalışıyor" << PORT << std::endl;

while (true) {
    // gelen baglantı kabülü
    if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0) {
            std::cerr << "Accept failed" << std::endl;
            exit(EXIT_FAILURE);
}

 char buffer[BUFFER_SIZE] = {0};
        read(new_socket, buffer, BUFFER_SIZE);

        std::string request(buffer);
        std::cout << "alınan istek:\n" << request << std::endl;

        // http yanıtı
        std::string httpResponse;
        if (request.find("GET") == 0) {
            std::string html = generateHtml();
            httpResponse = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + std::to_string(html.size()) + "\r\n\r\n" + html;
        } else if (request.find("POST") == 0) {
            // POST verilerini işleyebiliriz (basit bir örnek)
            std::string body = "<html><body><h1>POST Request Received</h1></body></html>";
            httpResponse = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + std::to_string(body.size()) + "\r\n\r\n" + body;
        } else {
            httpResponse = "HTTP/1.1 405 Method Not Allowed\r\n\r\n";
        }

        // yanıtı istemciye gönder
        send(new_socket, httpResponse.c_str(), httpResponse.size(), 0);
        close(new_socket);
    }

    return 0;
}
