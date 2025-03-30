**Analysis of Encryption Techniques for Secure IoT Health Data Transfer**

This project explores and compares four chaotic encryption methods for securing medical imaging data, specifically chest tomography images, in IoT healthcare systems. The implemented encryption techniques include:

-1D Logistic Map

-2D Henon Map

-3D Lorenz Attractor

-4D Chen Map

**Key Features**

-Evaluation Metrics: Entropy, correlation, PSNR, SSIM, NPCR, UACI, key sensitivity, and computational time were used to assess performance.

-Tools: Python (NumPy, OpenCV, Matplotlib) for algorithm implementation and OMNET++ for IoMT network simulation.

-Results: The Henon Map and Lorenz Attractor demonstrated the best balance between security and efficiency, while the Chen Map showed strong resistance to differential attacks.

**Repository Contents**

-Python scripts for encryption/decryption algorithms.

-OMNET++ simulation files for secure data transmission.

-Test images and results (metrics, encrypted/decrypted images).

**Future Work**

Optimizing computational overhead and integrating chaotic systems with traditional cryptographic methods for enhanced security.
