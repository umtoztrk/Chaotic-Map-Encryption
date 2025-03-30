#include "LorenzEncrypt.h"
#include <fstream>
#include <vector>
#include <cmath>
#include <stdexcept>

void lorenzEncrypt(const std::string &inputPath, const std::string &outputPath) {
    std::ifstream inputFile(inputPath, std::ios::binary);
    std::ofstream outputFile(outputPath, std::ios::binary);

    if (!inputFile || !outputFile) {
        throw std::runtime_error("Dosya açılamadı!");
    }

    // Giriş dosyasını oku
    std::vector<unsigned char> data((std::istreambuf_iterator<char>(inputFile)),
                                    std::istreambuf_iterator<char>());

    // Lorenz attractor başlangıç değerleri
    double x = 0.1, y = 0.1, z = 0.1;

    for (size_t i = 0; i < data.size(); i++) {
        // Lorenz attractor'un bir adımını hesapla
        double dx = sigma * (y - x) * dt;
        double dy = (x * (rho - z) - y) * dt;
        double dz = (x * y - beta * z) * dt;
        x += dx;
        y += dy;
        z += dz;

        // Şifreleme (veriyi x, y, z'nin kombinasyonuyla karıştır)
        data[i] ^= static_cast<unsigned char>(fabs(x * 255)) ^
                   static_cast<unsigned char>(fabs(y * 255)) ^
                   static_cast<unsigned char>(fabs(z * 255));
    }

    outputFile.write(reinterpret_cast<const char *>(data.data()), data.size());
    inputFile.close();
    outputFile.close();
}

void lorenzDecrypt(const std::string &inputPath, const std::string &outputPath) {
    std::ifstream inputFile(inputPath, std::ios::binary);
    std::ofstream outputFile(outputPath, std::ios::binary);

    if (!inputFile || !outputFile) {
        throw std::runtime_error("Dosya açılamadı!");
    }

    // Giriş dosyasını oku
    std::vector<unsigned char> data((std::istreambuf_iterator<char>(inputFile)),
                                    std::istreambuf_iterator<char>());

    // Lorenz attractor başlangıç değerleri
    double x = 0.1, y = 0.1, z = 0.1;

    for (size_t i = 0; i < data.size(); i++) {
        // Lorenz attractor'un bir adımını hesapla
        double dx = sigma * (y - x) * dt;
        double dy = (x * (rho - z) - y) * dt;
        double dz = (x * y - beta * z) * dt;
        x += dx;
        y += dy;
        z += dz;

        // Şifre çözme (aynı algoritma kullanılır)
        data[i] ^= static_cast<unsigned char>(fabs(x * 255)) ^
                   static_cast<unsigned char>(fabs(y * 255)) ^
                   static_cast<unsigned char>(fabs(z * 255));
    }

    outputFile.write(reinterpret_cast<const char *>(data.data()), data.size());
    inputFile.close();
    outputFile.close();
}


