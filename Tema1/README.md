# Tema1

## **Descrierea aplicatiei**
###### Aplicatia de tip **client-server**, simuleaza comunicare intre trei procese/noduri, ideea principala fiind: **Nodurile A si B** nu pot comunica impreuna decat prin intermediul **nodului KM** care comunica cu cele doua noduri prin mesaje criptate.
&nbsp;
## **Modalitatea de functionare**
###### **Nodul Key Manager (KM)**:  este nodul server ar aplicatiei si acesta asigura comunicarea intre cele doua noduri de tip client, acesta fiind singurul care cunoaste toate cheile de criptare.
###### **Nodul A**: nod client , ce alege modul de criptare a mesajelor in interiorul aplicatiei si transmite un mesaj spre **nodul B**.
###### **Nodul B**: nod client, ce primeste mesajul criptat de la **nodul A**  si il afiseaza.

![image](https://user-images.githubusercontent.com/61733856/99820187-18050d00-2b59-11eb-81f6-d5a565e2b8d3.png)

## **Modalitatea de rezolvare**
### Implementarea criptarii/decriptarii
###### Pentru implementarea criptarilor am urmat diagramele de mai jos, primul pas fiind mereu caz special atat in criptare cat si in decriptare deoarece foloseste IV-ul si nu un bloc de Cyphertext.
