## (一) 安裝 Docker

- 如果學員的作業系統是使用Windows 或 Mac 系列，而非Ubuntu 或 RedHat (CentOS) 等Linux-Like 作業系統，請先於系統上安裝Docker:

### Windows 7 & 8 作業系統的使用者:
- 安裝 Docker-toolbox:
- https://download.docker.com/win/stable/DockerToolbox.exe

### Windows 10 作業系統的使用者
- 安裝 Docker For Windows
- https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe

### Mac 作業系統的使用者
- 安裝 Docker For Mac
- https://download.docker.com/mac/stable/Docker.dmg

## (二) 啟用Docker 映像檔 jupyter/pyspark-notebook

1. 啟用Docker-Daemon (通常為雙擊Docker 圖樣或直接啟用該App)

2. 下載jupyter/pyspark-notebook
- docker pull jupyter/pyspark-notebook

3.  執行  jupyter/pyspark-notebook
- docker run -d -p 8888:8888 --name spark jupyter/pyspark-notebook

4. 檢視Notebook 連結
- docker exec -i spark jupyter notebook list
