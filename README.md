# ReadMe - Setting up Kaggle Environment

This ReadMe provides instructions for setting a ETL Pipeline.

## Prerequisites

Before you begin, make sure you have the following:

- Kaggle account: You must have a Kaggle account. If you don't have one, you can create it at [Kaggle.com](https://www.kaggle.com/).
- Install Docker on your system by following the instructions provided on the [Docker website](https://www.docker.com/get-started).

## Instructions

### 1. Create a `.kaggle` Directory

1. Create a directory named `.kaggle` in your user directory (usually `/home/yourusername/` on Linux, `C:\Users\yourusername\` on Windows).

   ```shell
   mkdir ~/.kaggle # Linux/Mac
   ```

   or

   ```shell
   mkdir C:\Users\yourusername\.kaggle # Windows
   ```

### 2. Place your Kaggle API Key

1. Log in to your Kaggle account.

2. Go to your Kaggle account settings by clicking on your profile picture and selecting "Account."

3. Scroll down to the "API" section and click on "Create New API Token." This will download a file called `kaggle.json`.

4. Move the `kaggle.json` file you downloaded in the previous step to the `.kaggle` directory you created in step 1.

   ```shell
   mv path/to/downloaded/kaggle.json ~/.kaggle/kaggle.json # Linux/Mac
   ```

   or

   ```shell
   move path\to\downloaded\kaggle.json C:\Users\yourusername\.kaggle\kaggle.json # Windows
   ```

   Make sure to replace `path/to/downloaded/kaggle.json` with the actual path to the downloaded file.

5. Protect your `kaggle.json` file:

   On Linux/Mac, you can restrict access to your API key using the following command:

   ```shell
   chmod 600 ~/.kaggle/kaggle.json
   ```

### 3. Add your Internet IP address

1. Determine your current public Internet IP address by using ifconfig command.

2. Create a file named `ip_address.txt` in the directory where you want to run your scripts. This file should contain your public IP address.

   ```shell
   echo "YOUR_PUBLIC_IP_ADDRESS" > path/to/ip_address.txt
   ```

   Replace `YOUR_PUBLIC_IP_ADDRESS` with the actual IP address you obtained in step 1.


### 4. Create a Virtual Environment

1. Create a Python virtual environment to manage your project dependencies. This step helps you isolate your project's dependencies from your system-wide Python installation.

   ```shell
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   source venv/bin/activate # On Linux/Mac
   .\venv\Scripts\Activate # On Windows
   ```

### 5. Install Project Dependencies

1. Make sure you are in your virtual environment (you should see the environment name in your terminal prompt).

2. Navigate to the directory where you have your project files, including the `requirements.txt` file.

3. Install the project dependencies using `pip`.

   ```shell
   pip install -r requirements.txt
   ```

### 6. Execute the `run_all.sh` script

1. Execute command to enable script execution:

   ```shell
   chmod +x run_all.sh
   ```

2. Run the script:
   ```shell
   ./run_all.sh # Linux/Mac (if you have made the script executable)
   ```

   or

   ```shell
   run_all.sh # Windows (if you have Cygwin or a similar Unix-like environment)
   ```

The `run_all.sh` script will use your Kaggle API key to download a dataset, then create a PostgreSQL container for the database where the raw data will be transferred to. It will also spin up Metabase so you can interact with your data visually!
