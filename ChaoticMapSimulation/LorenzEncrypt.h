#ifndef LORENZ_ENCRYPT_H
#define LORENZ_ENCRYPT_H

#include <string>

// Lorenz attractor parametreleri
const double sigma = 10.0;
const double rho = 28.0;
const double beta = 8.0 / 3.0;
const double dt = 0.01;

// Lorenz attractor tabanlı şifreleme ve şifre çözme fonksiyonları
void lorenzEncrypt(const std::string &inputPath, const std::string &outputPath);
void lorenzDecrypt(const std::string &inputPath, const std::string &outputPath);

#endif // LORENZ_ENCRYPT_H
