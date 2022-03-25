# Install Anaconda on a Z VM

- Follow the [Install instructions in Installing on Linux-s390x (IBM Z)](https://docs.anaconda.com/anaconda/install/linux-s390x/)
- Where it says [download the Anaconda installer](https://www.anaconda.com/download/#linux) for Linux-s390x use the curl command to download from command line

```
$ curl -O https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-s390x.sh
```

By default Anaconda will try to install in the following location: /home/ubuntu/anaconda3 That’s fine.

```
$ bash ./Anaconda3-2021.11-Linux-s390x.sh
```
