import time
from kyber import Kyber768  # Örneğin varsayılan wrapper

keypair = Kyber768.generate_keypair()

start = time.time()
ciphertext = Kyber768.encrypt(keypair.public_key, b"test message")
end = time.time()

print(f"Şifreleme Süresi: {(end - start) * 1000:.3f} ms")
