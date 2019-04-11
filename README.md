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
3. Copy deploy.py and docker-compose.yml into ops-excercise directory:
```bash
cp ./skibidi/deploy.py ops-excercise/
cp ./skibidi/docker-compose.yml ops-excercise/
```
4. Step into ops-excercise directory:
```bash
cd ops-excercise
```
5. Run deploy.py:
```bash
python3 deploy.py
```
