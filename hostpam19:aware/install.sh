#! /bin/bash
# Install hostpam
useradd anna
useradd gustavo
echo "anna" | passwd --stdin anna
echo "gustavo" | passwd --stdin gustavo
cp /opt/docker/login.defs /etc/login.defs
cp /opt/docker/chfn /etc/pam.d/chfn
cp /opt/docker/pam_python.so /usr/lib64/security/.
