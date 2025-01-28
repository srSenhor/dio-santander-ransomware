import sys
import os
import pyaes

def encrypt(file_content: str, key: str):
    aes = pyaes.AESModeOfOperationCTR(key=key)
    return aes.encrypt(file_content)

def decrypt(file_content: str, key: str):
    aes = pyaes.AESModeOfOperationCTR(key=key)
    return aes.decrypt(file_content)

def save_file(file_path: str, file_content: str, mode: int):
    os.remove(file_path)

    new_file = open(file_path, 'wb')
    new_file.write(file_content)
    new_file.close()


def get_file_content(file_path: str) -> str:
    archive = open(file=file_path, mode='rb')
    archive_content = archive.read()
    archive.close()
    return archive_content

def main():
    if (len(sys.argv) < 4):
        print('need more arguments')
        sys.exit(1)

    file_path = sys.argv[1]
    file_content = get_file_content(file_path = file_path)

    mode = int(sys.argv[2])
    key = sys.argv[3]
    key = key.encode('utf-8')
    file_content = encrypt(file_content=file_content, key=key) if mode == 0 else decrypt(file_content=file_content, key=key)
    save_file(file_path=file_path, file_content=file_content, mode=mode)

    

if __name__ == '__main__':
    main()

#    abcdefghijk12345