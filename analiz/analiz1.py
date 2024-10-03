import os

def find_files(extension, directory):
    files_found = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                files_found.append(os.path.join(root, file))
    return files_found

# zararlı davranıs
def perform_malicious_action(files):
    for file in files:
        print(f"Deleting file: {file}")
        # burda dosya silme işlemi yerine sadece ekrana yazdırıyoruz.
        # gerçek zararlı yazılım burada dosyaları silebilir ya da değiştirebilir

def main():
    target_extension = '.txt' # dosya uzantısı
    directory_to_search = '/' # aranacak dizin

    # zararlı yazılım dosyaları bulur
    files = find_files(target_extension, directory_to_search)
    print(f"Found {len(files)} files with {target_extension} extension.")

    perform_malicious_action(files)

if __name__ == "__main__":
    main()
