# EXAMEN HOSTPAM19  
## @isx43577298  

docker hub: https://hub.docker.com/repository/docker/isx43577298/hostpam19


+ Imatge docker anomenada isx43577298/hostpam19:aware al dockerhub  
+ La imatge disposarà d'un dir /opt/docker  
+ En aquest directory existira un programa python anomenat pamaware.py que en executar-se verifica que qui l'executa sigui un usuari unix vàlid  
+ Implementació d'un modul pam propi anomenat pammates.py que fa una pregunta matematica que cal resoldre per poder superar l'autenticacio
+ La imatge contindrà 2 users unix valids: anna i gustavo (que tenen com a password el mateix nom d'usuari)  
+ Quan els usuaris es volen canviar el chfn se'ls aplica un fitxer de regles PAM que utilitza el modul pammates.py

### Ordres per posar en funcionament el docker

$ docker run --rm -h pam --name pam -it isx43577298/hostpam19:aware /bin/bash  
$ dnf -y install sphinx python3-sphinx gcc  
$ dnf -y install pam-devel  
$ dnf -y install redhat-rpm-config  
$ dnf -y install python-devel  

editar línia 201 de: /usr/include/features.h:  
canviar 700 per 600 en la línia # define _XOPEN_SOURCE 700

$ bash install.sh

__UN COP REALITZADES LES ANTERIORS ORDRES FUNCIONARA CORRECTAMENT EL DOCKER__

__ORDRES QUE HE FET PER CONSEGUIR PAMPYTHON.SO EN LOCAL__

make
make install
make build
python setup.py build
