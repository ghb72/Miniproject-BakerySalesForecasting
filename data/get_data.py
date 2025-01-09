import kagglehub

# Download latest version
path = kagglehub.dataset_download("matthieugimbert/french-bakery-daily-sales")

print("Path to dataset files:", path)