# 🔍 Port & Host Scanner en Python

Ce projet est un **scanner réseau en ligne de commande** écrit en **Python 3.13.3**.  
Il permet :

- de **tester la connectivité** d'une adresse IP ou d'un nom de domaine via `ping`
- de **scanner une plage de ports** pour détecter ceux qui sont ouverts ou filtrés

Tout cela en utilisant **exclusivement des bibliothèques standard de Python** (`subprocess`, `socket`, `ipaddress`).

---

## 🚀 Fonctionnalités

- Choix entre un **nom de domaine** ou une **adresse IP**
- Ping de la cible pour vérifier la disponibilité
- Scan de ports (TCP uniquement) sur une plage définie
- Affichage clair du statut de chaque port (ouvert / fermé / filtré)
- Gestion des erreurs : adresses invalides, plage de ports incohérente, etc.

---

## 🛠️ Prérequis

- **Python 3.13.3** (ou toute version compatible >= 3.6)
- Fonctionne sur **Windows** (utilise `ping -n 1`)
- Pas besoin de dépendances externes

---

## 🧪 Exemple d'utilisation

```bash
$ python scanner.py
Voulez-vous entrer un nom de domaine ou une adresse IP ? : une adresse ip
Entrez l'adresse IP : 192.168.1.1
Ping réussi :
[...]

Entrez le port de début : 20
Entrez le port de fin : 25

--- DÉBUT DU SCAN DE 20 À 25 SUR 192.168.1.1 ---

Port 20    est FERMÉ ou FILTRÉ
Port 21    est OUVERT
Port 22    est OUVERT
Port 23    est FERMÉ ou FILTRÉ
Port 24    est FERMÉ ou FILTRÉ
Port 25    est OUVERT

Scan terminé.
