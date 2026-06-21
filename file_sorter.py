import shutil
from pathlib import Path

TARGET_DIR = Path.home() / "Downloads"
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Media": [".mp4", ".mp3", ".mov", ".mkv", ".wav"],
    "3D": [".stl", ".obj"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"]
}

def organize_folder(target_path):
    if not target_path.exists():
        print(f"Error: The directory {target_path} does not exist.")
        return

    print(f"Scanning and organizing: {target_path.resolve()}\n")


    # .iterdir() loops through everything inside the folder
    for item in target_path.iterdir():
        
        # Skip folders; we only want to sort actual files
        if item.is_dir():
            continue
            
        
        file_extension = item.suffix.lower()
        
       
        if file_extension in [".tmp", ".log"]:
            print("Temp file found. Do you want to delete them y/n: ")
            delete = input()
            if delete == 'y':
                print(f"🗑️ Deleting temporary file: {item.name}")
                item.unlink()  
                continue

        destination_folder_name = "Others" 
        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                destination_folder_name = folder_name
                break
        
        
        destination_dir = target_path / destination_folder_name
        
        destination_dir.mkdir(parents=True, exist_ok=True)
        
        final_destination = destination_dir / item.name
        
        print(f"📁 Moving {item.name} -> {destination_folder_name}/")
        shutil.move(str(item), str(final_destination))

    print("\nSorting complete!")

# Run the script
if __name__ == "__main__":
    organize_folder(TARGET_DIR)