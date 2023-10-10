import kaggle

dataset = "nelgiriyewithana/world-stock-prices-daily-updating"
download_path = "./raw_data"
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)
