activar siempre el venv, por temas de seguridad propia de linux
source .venv/bin/activate



Subir a git

1. Limpiar el rastro de submódulos internos

# Elimina la carpeta .git interna de los subproyectos
rm -rf Repo/Automated_DDoS_Attack_Detection_in_Software_Defined_Network_SDN/.git
rm -rf Repo/SDN_Topologia/.git

2. Forzar a Git a olvidar el "estado" anterior
bash

"git rm -r --cached Repo/Automated_DDoS_Attack_Detection_in_Software_Defined_Network_SDN
git rm -r --cached Repo/SDN_Topologia"


3. Agregar y subir todo de nuevo
Ahora ya no tienen el archivo .git interno

"git add .
git commit -m "Mensaje"
git push origin main"
