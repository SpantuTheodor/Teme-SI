# Tema1

## **Descrierea aplicatiei**
###### Aplicatia de tip **client-server**, simuleaza comunicare intre trei procese/noduri, ideea principala fiind: **Nodurile A si B** nu pot comunica impreuna decat prin intermediul **nodului KM** care comunica cu cele doua noduri prin mesaje criptate.
&nbsp;
## **Modalitatea de functionare**
###### **Nodul Key Manager (KM)**:  este nodul server ar aplicatiei si acesta asigura comunicarea intre cele doua noduri de tip client, acesta fiind singurul care cunoaste toate cheile de criptare.
###### **Nodul A**: nod client , ce alege modul de criptare a mesajelor in interiorul aplicatiei si transmite un mesaj spre **nodul B**.
###### **Nodul B**: nod client, ce primeste mesajul criptat de la **nodul A**  si il afiseaza.

<p align="center">
  <img align="center" src="https://github.com/SpantuTheodor/Teme-SI/blob/master/Tema1/README/Diagram.png" width="75%">
</p>
&nbsp;

## **Modalitatea de rezolvare**
#### Implementarea criptarii/decriptarii
###### Pentru implementarea criptarilor am urmat diagramele de mai jos, primul pas fiind mereu caz special atat in criptare cat si in decriptare deoarece foloseste IV-ul si nu un bloc de Cyphertext.
<p align="center">
  <img align="center" src="https://github.com/SpantuTheodor/Teme-SI/blob/master/Tema1/README/CBC_encryption.png" width="75%">
</p>

<p align="center">
  <img align="center" src="https://github.com/SpantuTheodor/Teme-SI/blob/master/Tema1/README/CBC_decryption.png" width="75%">
</p>

<p align="center">
  <img align="center" src="https://github.com/SpantuTheodor/Teme-SI/blob/master/Tema1/README/CFB_encryption.png" width="75%">
</p>

<p align="center">
  <img align="center" src="https://github.com/SpantuTheodor/Teme-SI/blob/master/Tema1/README/CFB_decryption.png" width="75%">
</p>
&nbsp;

###### Libraria AES din suita Crypto.Cipher si  libraria random au fost foarte de ajutor.
###### Prima pentru pasii “block cipher encryption/decryption” din diagramele de mai sus, iar a doua pentru a genera valori random pentru IV-uri.
&nbsp;
#### Implementarea TCP/IP
###### Pentru implementarea TCP/IP am folosit  libraria socket impreuna cu libraria pickle si chiar libraria time pentru comunicarea intre procese.
###### Socket-ul a asigurat comunicarea propriu zisa intre procese, pickle asigura transmiterea anumitor tipuri de date, spre exemplu liste, iar time am folosit pentru comunicarea continua intre doua procese, deoarece din cauza lipsei caracterului blocant a functiilor send si recv, in momentul trimiterii continue de date (spre exemplu in interiorul unei bucle while) am fi pierdut anumite date.
&nbsp;
## Linkuri utile
###### https://pymotw.com/2/socket/tcp.html
###### https://pycryptodome.readthedocs.io/en/latest/src/installation.html
###### https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
###### https://wiki.python.org/moin/UsingPickle
###### https://docs.python.org/3/library/time.html
