import urllib.request
import tarfile
import subprocess
import requests
import time

def main():
    # Variable Definition
    url = "https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz"
    images_dest = "public/images"
    healthcheck_url = "http://localhost:3000/health"

    get_images(url, images_dest)
    build_and_deploy_app_and_db()

    if check_app_health(healthcheck_url):
        print("Healthy")
    else:
        revert_deployment()

def extract_file(src, dest):
    """ Extract file from src to dest """
    tar = tarfile.open(src, "r:gz")
    tar.extractall(path=dest)
    tar.close()

def download_images_file(url):
    """ Download images file from url """
    file_name = url.split('/')[-1]
    urllib.request.urlretrieve(url, file_name)
    return file_name

def get_images(url, dest):
    """ Download images file from url, and extract images to dest """
    images_file = download_images_file(url)
    extract_file(images_file, dest)

def build_and_deploy_app_and_db():
    """ Build and deploy app and db using docker-compose """
    subprocess.run(["docker-compose", "up", "-d", "--build"])

def check_app_health(url):
    """ Check app's health """
    for attempt in range(1,4):
        try:
            raw_response = requests.get(url=url)
            print("Check Successful - Attempt No. {0}".format(attempt))

            json_response = raw_response.json()
            general_check = json_response['isSuccessful']
            db_check = json_response['checkDatabase']['success']
            disk_check = json_response['checkDisk']['success']

            if general_check and db_check and disk_check:
                return True
            else:
                return False
        except:
            print("Check Failed - {0}".format(attempt))
            time.sleep(attempt)

            if attempt == 3:
                return False

def revert_deployment():
    """ Revert deployment using docker-compose command """
    subprocess.run(["docker-compose", "down"])


if __name__ == "__main__":
    main()
