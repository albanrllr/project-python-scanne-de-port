import subprocess
import socket
import ipaddress

choix = input("Voulez-vous entrer un nom de domaine ou une adresse IP ? : ")

if choix == "un nom de domaine":
    cible = input("Entrez le nom de domaine : ")
elif choix == "une adresse ip":
    cible = input("Entrez l'adresse IP : ")
else:
    print("Choix non reconnu.")
          
    exit() 



try:
    result_ping = subprocess.run(["ping", "-n", "1", cible], capture_output=True, text=True, check=True)
    print("Ping réussi :")
    print(result_ping.stdout)

except subprocess.CalledProcessError as e:
    print("Hôte injoinable. Vérifiez l'adresse IP ou le nom de domaine.")
    print(e.stderr)
    exit()

except Exception as erreur:
    print("Une autre erreur est survenue :", erreur)




try:
    port_debut = int(input("Entrez le port de début : "))
    port_fin = int(input("Entrez le port de fin : "))

    if port_debut < 1 or port_fin > 65535 or port_debut > port_fin:
        print("Plage de ports invalide.")
        exit()

except ValueError:
    print("Entrée invalide. Veuillez entrer des nombres.")
    exit()



print(f"\n--- DÉBUT DU SCAN DE {port_debut} À {port_fin} SUR {cible} ---\n")

for port in range(port_debut, port_fin + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        resultat = sock.connect_ex((cible, port))

        if resultat == 0:
            print(f"Port {port:<5} est OUVERT")
        else:
            print(f"Port {port:<5} est FERMÉ ou FILTRÉ")

    except socket.error as e:
        print(f"Erreur réseau sur le port {port} : {e}")

    finally:
        sock.close()



print("\nScan terminé.")




