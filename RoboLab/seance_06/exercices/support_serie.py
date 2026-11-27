import csv, math
from pathlib import Path
CHAMPS=('time_us','count','theta_rad','omega_rad_s','setpoint_rad','pwm','error_rad')
DONNEES=Path(__file__).resolve().parent.parent/'donnees'/'synthetiques'
def lire_csv(nom):
    with (DONNEES/nom).open(encoding='utf8',newline='') as f:
        return [{k:float(v) for k,v in r.items()} for r in csv.DictReader(f)]
def ouvrir_port(port):
    import serial
    return serial.Serial(port,115200,timeout=.1,write_timeout=.2)
def stop(port):
    port.write(b'STOP\n')
# Aucun démarrage moteur automatique : configuration et ACK sous contrôle enseignant.
