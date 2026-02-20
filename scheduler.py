import schedule
import time
import subprocess
import sys


def run_report():
    print("Ejecutando envio de reporte...")
    subprocess.run([sys.executable, "send_report.py"], check=True)
    print("Envio completado.")


schedule.every().monday.at("07:00").do(run_report)

print("Scheduler activo. Enviara el reporte cada lunes a las 07:00 AM.")
print("Presiona Ctrl+C para detener.")

while True:
    schedule.run_pending()
    time.sleep(30)
