# skibidi

## About
Using skibidi you can deploy your service easily

## Prerequisites
* Python 3.*
* docker-compose

## Usage Instructions
1. Clone ops-exercise:
```bash
git clone git@github.com:bigpandaio/ops-exercise.git
```
2. Clone skibidi:
```bash
git clone https://github.com/noisleahcim/skibidi
```
3. Copy deploy.py and docker-compose.yml into ops-exercise directory:
```bash
cp ./skibidi/deploy.py ./ops-exercise/
cp ./skibidi/docker-compose.yml ./ops-exercise/
```
4. Step into ops-exercise directory:
```bash
cd ops-exercise
```
5. Run deploy.py:
```bash
python3 deploy.py
```
