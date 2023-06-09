#!/usr/bin/env python

import subprocess

# Disable root login
subprocess.call("sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config", shell=True)

# Set password policy
subprocess.call("apt-get install -y libpam-pwquality", shell=True)
subprocess.call("sed -i 's/# minlen = 9/minlen = 14/' /etc/security/pwquality.conf", shell=True)

# Update and upgrade packages
subprocess.call("apt-get update", shell=True)
subprocess.call("apt-get upgrade -y", shell=True)

# Configure firewall (assuming ufw is installed)
subprocess.call("ufw default deny incoming", shell=True)
subprocess.call("ufw default allow outgoing", shell=True)
subprocess.call("ufw allow ssh", shell=True)
subprocess.call("ufw enable", shell=True)

print("Security hardening completed.")
