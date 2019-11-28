# EXAMEN HOSTPAM19  
## @isx4377298  


+ Imatge docker anomenada isx43577298/hostpam19:aware al dockerhub  
+ La imatge disposarà d'un dir /opt/docker  
+ En aquest directory existira un programa python anomenat pamaware.py que en executar-se verifica que qui l'executa sigui un usuari unix vàlid  
+ Implementació d'un modul pam propi anomenat pammates.py que fa una pregunta matematica que cal resoldre per poder superar l'autenticacio
+ La imatge contindrà 2 users unix valids: anna i gustavo (que tenen com a password el mateix nom d'usuari)  
+ Quan els usuaris es volen canviar el chfn se'ls aplica un fitxer de regles PAM que utilitza el modul pammates.py

### Ordres per posar en funcionament el docker

docker run --rm -h pam --name pam -it isx43577298/hostpam19:aware /bin/bash  

bash install.sh  

tar xvzf pam-python-1.0.6.tar.gz  
dnf -y install sphinx python3-sphinx gcc  
dnf -y install pam-devel  
dnf -y install redhat-rpm-config  
dnf -y install python-devel  

editar línia 201 de: /usr/include/features.h:  
canviar 700 per 600 en la línia# define _XOPEN_SOURCE 700


__Ordres per a conseguir pampython.so__  
make  
make install  
make build  
python setup.py build  
cp /pam-python-1.0.6/src/build/lib.linux-x86_64-2.7/pam-python.so .  






