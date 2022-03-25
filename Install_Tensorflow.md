# Install Tensorflow

## Retrieve TensorFlow image to run in your VM
[IBM Z and LinuxONE Container Registry](https://ibm.github.io/ibm-z-oss-hub/main/main.html) explains how TensorFlow image for s390X is stored in the IBM Cloud Container Registry (ICR).  
- ICR requires an IBM Cloud ID along with your API key for authentication.
- Log into IBM Cloud [cloud.ibm.com](http://cloud.ibm.com/) with your IBM ID. If you don't have an ID already, please create one.
- Get or Create an API Key on IBM Cloud using the Manage pulldown on top to navigate to the Access (IAM) interface. 
- From there, choose API keys on the left navigation, and then Create an IBM Cloud API key. You should see a window for naming and describing your access key.
- Once created, you can download the JSON file that looks something like this: 
```
{
    "name": "Sample IAMAPIKEY",
    "description": "A sample IBM Cloud API key",
    "createdAt": "2021-02-08T20:01+0000",
    "apikey": "B08t7_qWo60P123456789IXybgvgGqAty8ULka8ZnMAT"
}
```
    
- The apikey above is the key string needed for authenticating to ICR.  Save this file to a safe place and give it a useful name. Should you ever lose it, use the API keys interface to delete it and define a new one to remain secure. This key alone is what identifies you to ICR.
- Pull the tensorflow Image From the ibmz Namespace at IBM Cloud Container Registry (icr.io) 
- Install docker in your VM
```
$ sudo apt install docker.io
```
- Add the user you’re running the command as to the docker group.  
```
$ sudo usermod -a -G docker $USER
```
- After running the command, you need to terminate your SSH session and re-connect – or the group change does not take effect.
```
$ exit
$ ssh ubuntu@XX.YY.ZZ.WW
```
     
     
- Log into the ICR global region at icr.io, with the userid iamapikey. When ICR sees this specific userid, it will expect to receive an apikey for your IBM cloud apikey at the password prompt. If you have multiple keys generated for your userid, any of them should work.
```
$ docker login -u iamapikey icr.io
Password: <Paste the text of your apikey here>
Login Succeeded
```
    
- After logging in to ICR, pull the image using the fully qualified path to the tensorflow image using the pull string provided in the details page for the tensorflow image. While it is possible to pull an image by name and version (tag), the site recommends using the full sha256 hash for the image digest to be sure you get exactly the image you request.
```
$ docker pull icr.io/ibmz/tensorflow@sha256:f7358d3e6fa9f73d91cc497ef0674af9da4efa73cbde5bb8522660a1aed3833c
```
