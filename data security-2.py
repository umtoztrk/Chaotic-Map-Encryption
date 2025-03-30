import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
from skimage.feature import canny

# 1D Logistic Map
def logistic_map_encrypt_decrypt(image_array, key, iterations=100):
    np.random.seed(key)
    x = np.random.rand()
    for _ in range(iterations):
        x = 3.99 * x * (1 - x)
    chaotic_sequence = np.array([3.99 * x * (1 - x) for x in np.random.rand(image_array.size)])
    chaotic_sequence = chaotic_sequence.reshape(image_array.shape)
    chaotic_sequence = (chaotic_sequence * 255).astype(np.uint8)
    encrypted = np.bitwise_xor(image_array, chaotic_sequence)
    return encrypted

# 2D Henon Map
def henon_map_encrypt_decrypt(image_array, key, iterations=100):
    np.random.seed(key)
    
    
    x = (key % 1000) / 1000.0  
    y = (key % 500) / 500.0     
    
    a, b = 1.4, 0.3  # Henon map parameters.
    chaotic_sequence = np.zeros_like(image_array, dtype=np.float32)
    
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            x_new = 1 - a * x**2 + y
            y = b * x
            x = x_new
            chaotic_sequence[i, j] = x % 1  # We use the modular arithmetic to prevent overflow.
            
    chaotic_sequence = (chaotic_sequence * 255).astype(np.uint8)
    encrypted = np.bitwise_xor(image_array, chaotic_sequence)
    return encrypted


# 3D Lorenz Attractor
def lorenz_map_encrypt_decrypt(image_array, key, iterations=100):
    np.random.seed(key)
    
    
    x = (key % 1000) / 1000.0  
    y = (key % 500) / 500.0     
    z = (key % 250) / 250.0     
    
    sigma, rho, beta = 10, 28, 8 / 3  # Lorenz map parameters.
    dt = 0.001  
    chaotic_sequence = np.zeros_like(image_array, dtype=np.float32)
    
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            dx = sigma * (y - x) * dt
            dy = (x * (rho - z) - y) * dt
            dz = (x * y - beta * z) * dt
            x += dx
            y += dy
            z += dz
            chaotic_sequence[i, j] = x % 1  
    
    chaotic_sequence = (chaotic_sequence * 255).astype(np.uint8)
    encrypted = np.bitwise_xor(image_array, chaotic_sequence)
    return encrypted


# 4D Chen Map
def chen_map_encrypt_decrypt(image_array, key, iterations=100):
    np.random.seed(key)
    
    
    x = (key % 1000) / 1000.0  
    y = (key % 500) / 500.0     
    z = (key % 250) / 250.0     
    w = (key % 100) / 100.0     
    
    a, b, c, d = 35, 3, 12, 5   
    dt = 0.001  
    chaotic_sequence = np.zeros_like(image_array, dtype=np.float32)
    
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            dx = a * (y - x) + w * dt
            dy = (c - a) * x - x * z + c * y
            dz = x * y - b * z
            dw = -d * w + x * z
            x += dx * dt
            y += dy * dt
            z += dz * dt
            w += dw * dt
            chaotic_sequence[i, j] = x % 1  
    
    chaotic_sequence = (chaotic_sequence * 255).astype(np.uint8)
    encrypted = np.bitwise_xor(image_array, chaotic_sequence)
    return encrypted


# Encryption Quality Metrics
def calculate_entropy(image_array):
    histogram, _ = np.histogram(image_array, bins=256, range=(0, 256))
    probabilities = histogram / image_array.size
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
    return entropy

def calculate_correlation(image_array):
    flat_array = image_array.flatten()
    shifted_array = np.roll(flat_array, 1)
    correlation = np.corrcoef(flat_array, shifted_array)[0, 1]
    return correlation

def calculate_psnr_ssim(original_image, encrypted_image):
    psnr_value = psnr(original_image, encrypted_image, data_range=255)
    ssim_value, _ = ssim(original_image, encrypted_image, full=True)
    return psnr_value, ssim_value

# Key Sensitivity
def key_sensitivity_test(image_array, method, key1, key2):
    encrypted_key1 = method(image_array, key1)
    encrypted_key2 = method(image_array, key2)
    difference = np.sum(encrypted_key1 != encrypted_key2) / image_array.size * 100
    return difference


def calculate_npcr_uaci(original, modified):
    npcr = np.sum(original != modified) / original.size * 100
    uaci = np.mean(np.abs(original - modified) / 255) * 100
    return npcr, uaci


def add_noise(image_array, noise_type="salt_pepper", amount=0.02):
    noisy_image = image_array.copy()
    if noise_type == "salt_pepper":
        num_salt = np.ceil(amount * image_array.size * 0.5)
        num_pepper = np.ceil(amount * image_array.size * 0.5)

        # Salt
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image_array.shape]
        noisy_image[coords[0], coords[1]] = 255

        # Pepper
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image_array.shape]
        noisy_image[coords[0], coords[1]] = 0

    return noisy_image


def calculate_edr(original, encrypted):
    original_edges = canny(original)
    encrypted_edges = canny(encrypted)
    edr = np.sum(original_edges != encrypted_edges) / original_edges.size * 100
    return edr

def save_encrypted_image(encrypted_image, method_name):
    encrypted_image_pil = Image.fromarray(encrypted_image)
    encrypted_image_pil.save(f"C:/Users/umuto/Desktop/{method_name}_encrypted.jpeg")


import time
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def main():
    # Load the image
    image = Image.open("İnput İmage Address").convert("L")  # Enter image adress.s
    image_array = np.array(image)

    # Key
    key1 = 42
    key2 = 43  # Slightly different key for sensitivity analysis

    # Encryption and Decryption Times
    results = []

    methods = [
        logistic_map_encrypt_decrypt,
        henon_map_encrypt_decrypt,
        lorenz_map_encrypt_decrypt,
        chen_map_encrypt_decrypt
    ]
    method_names = ["Logistic Map", "Henon Map", "Lorenz Map", "Chen Map"]

    # Encrypt, Decrypt, and Calculate Metrics for Each Method
    for method_name, method in zip(method_names, methods):
        # Encryption
        start_time = time.time()
        encrypted_image = method(image_array, key1)
        # Decryption
        decryption_start_time = time.time()
        decrypted_image = method(encrypted_image, key1)
        end_time = time.time()

        # Metrics Calculations
        encryption_time = decryption_start_time - start_time
        decryption_time = end_time - decryption_start_time
        total_time = end_time - start_time

        entropy = calculate_entropy(encrypted_image)
        correlation = calculate_correlation(encrypted_image)
        psnr_value, ssim_value = calculate_psnr_ssim(image_array, encrypted_image)
        npcr, uaci = calculate_npcr_uaci(image_array, encrypted_image)
        key_sensitivity = key_sensitivity_test(image_array, method, key1, key2)

        # Add noise to the encrypted image
        noisy_image = add_noise(encrypted_image, noise_type="salt_pepper")
        psnr_noisy, ssim_noisy = calculate_psnr_ssim(encrypted_image, noisy_image)
        edr = calculate_edr(image_array, encrypted_image)

        # Save the encrypted images
        save_encrypted_image(encrypted_image, method_name)

        # Store results
        results.append({
            "Method": method_name,
            "Encryption Time (s)": encryption_time,
            "Decryption Time (s)": decryption_time,
            "Total Time (s)": total_time,
            "Entropy": entropy,
            "Correlation": correlation,
            "PSNR": psnr_value,
            "SSIM": ssim_value,
            "NPCR (%)": npcr,
            "UACI (%)": uaci,
            "Key Sensitivity (%)": key_sensitivity,
            "PSNR (Noisy)": psnr_noisy,
            "SSIM (Noisy)": ssim_noisy,
            "EDR (%)": edr
        })

    # Print Results
    for result in results:
        print(f"Method: {result['Method']}")
        for key, value in result.items():
            if key != "Method":
                print(f"  {key}: {value:.4f}")
        print()

    # Visualization
    fig, axs = plt.subplots(1, 5, figsize=(25, 5))
    axs[0].imshow(image_array, cmap="gray")
    axs[0].set_title("Original Image")

    for i, method_name in enumerate(method_names, 1):
        # Display the encrypted images
        axs[i].imshow(Image.open(f"C:/Users/umuto/Desktop/{method_name}_encrypted.jpeg"), cmap="gray")
        axs[i].set_title(f"{method_name} Encrypted")
    
    plt.show()

def save_encrypted_image(encrypted_image, method_name):
    encrypted_image_pil = Image.fromarray(encrypted_image)
    encrypted_image_pil.save(f"C:/Users/umuto/Desktop/{method_name}_encrypted.jpeg")

if __name__ == "__main__":
    main()
