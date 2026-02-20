import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
REPORT_PATH = os.getenv("REPORT_PATH")

RECIPIENTS = [
    "leonardo.pimentel@londoncg.com",
    "fernando.sanchez@londoncg.com",
    "jaime.restrepo@londoncg.com",
    "ernesto.garcia@londoncg.com",
    "juancarlos.muro@londoncg.com",
]

SUBJECT = "\U0001f4ca Reporte LinkedIn LCG M\u00e9xico \u2014 Enero/Febrero 2026"

HTML_BODY = """\
<html>
<head>
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; color: #1a1a2e; background: #f4f6f9; margin: 0; padding: 0; }
  .container { max-width: 680px; margin: 0 auto; padding: 32px 24px; }
  .header { background: linear-gradient(135deg, #0a3161 0%, #0077b5 100%); color: white; padding: 28px 32px; border-radius: 12px 12px 0 0; }
  .header h1 { font-size: 20px; font-weight: 300; margin: 0; }
  .header p { font-size: 13px; opacity: 0.8; margin: 6px 0 0; }
  .content { background: white; padding: 28px 32px; border-radius: 0 0 12px 12px; }
  .kpi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 20px 0; }
  .kpi { background: #f8fbff; border-radius: 8px; padding: 16px; border-left: 3px solid #0077b5; }
  .kpi.green { border-left-color: #00875a; }
  .kpi.orange { border-left-color: #ff6b2b; }
  .kpi .value { font-size: 24px; font-weight: 700; color: #0a3161; }
  .kpi.green .value { color: #00875a; }
  .kpi.orange .value { color: #ff6b2b; }
  .kpi .label { font-size: 11px; color: #666; margin-top: 2px; }
  .section-title { font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #0077b5; text-transform: uppercase; margin: 24px 0 12px; }
  .insight { font-size: 13px; line-height: 1.6; color: #333; margin-bottom: 8px; padding-left: 14px; border-left: 3px solid #0077b5; }
  .insight.warn { border-left-color: #ff6b2b; }
  .footer { text-align: center; font-size: 11px; color: #999; margin-top: 24px; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>London Consulting Group M&eacute;xico</h1>
    <p>Reporte de Desempe&ntilde;o LinkedIn &mdash; 20 Enero &ndash; 18 Febrero 2026</p>
  </div>
  <div class="content">
    <p style="font-size:14px;color:#333;">Estimados Directores,</p>
    <p style="font-size:13px;color:#555;line-height:1.6;">
      Adjunto encontrar&aacute;n el reporte completo de desempe&ntilde;o de LinkedIn para el per&iacute;odo
      <strong>20 de enero &ndash; 18 de febrero 2026</strong>. A continuaci&oacute;n, un resumen ejecutivo de los KPIs m&aacute;s relevantes:
    </p>

    <div class="section-title">KPIs Principales</div>
    <div class="kpi-grid">
      <div class="kpi">
        <div class="value">63,375</div>
        <div class="label">Impresiones totales (90.3% v&iacute;a pauta)</div>
      </div>
      <div class="kpi green">
        <div class="value">6.71%</div>
        <div class="label">Tasa de interacci&oacute;n org&aacute;nica (benchmark: 2&ndash;3%)</div>
      </div>
      <div class="kpi">
        <div class="value">47</div>
        <div class="label">Nuevos seguidores (100% org&aacute;nicos)</div>
      </div>
      <div class="kpi orange">
        <div class="value">1,202</div>
        <div class="label">Seguidores totales</div>
      </div>
    </div>

    <div class="section-title">Hallazgos Clave</div>
    <div class="insight">
      <strong>LCG lidera en engagement:</strong> 313 interacciones totales, m&aacute;s que Accenture y Sintec combinados (182), con 20.9 interacciones por post.
    </div>
    <div class="insight">
      <strong>Contenido org&aacute;nico efectivo:</strong> ER org&aacute;nica del 6.71%, m&aacute;s del doble del benchmark B2B de LinkedIn.
    </div>
    <div class="insight warn">
      <strong>Dependencia de pauta:</strong> 90.3% de impresiones son pagadas. ER pagada (1.27%) es 5x menor que org&aacute;nica &mdash; oportunidad de optimizar segmentaci&oacute;n.
    </div>
    <div class="insight warn">
      <strong>Brecha de seguidores:</strong> LCG (1,202) vs. Sintec (17,825) vs. Accenture (116,037). Crecer la base es prioridad.
    </div>

    <div class="section-title">M&eacute;tricas de Interacci&oacute;n</div>
    <div class="kpi-grid">
      <div class="kpi">
        <div class="value">253</div>
        <div class="label">Reacciones</div>
      </div>
      <div class="kpi">
        <div class="value">433</div>
        <div class="label">Clics</div>
      </div>
      <div class="kpi">
        <div class="value">65</div>
        <div class="label">Veces compartido</div>
      </div>
      <div class="kpi">
        <div class="value">438</div>
        <div class="label">Visitas a la p&aacute;gina</div>
      </div>
    </div>

    <p style="font-size:13px;color:#555;line-height:1.6;margin-top:20px;">
      El reporte completo con gr&aacute;ficas de tendencias, an&aacute;lisis competitivo detallado y recomendaciones
      estrat&eacute;gicas se encuentra en el archivo adjunto.
    </p>

    <div class="footer">
      <p>London Consulting Group M&eacute;xico &mdash; Reporte LinkedIn &mdash; Confidencial</p>
      <p>Generado autom&aacute;ticamente el 20 de febrero de 2026</p>
    </div>
  </div>
</div>
</body>
</html>
"""


def send_report():
    msg = MIMEMultipart("mixed")
    msg["From"] = GMAIL_USER
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = SUBJECT

    html_part = MIMEText(HTML_BODY, "html")
    msg.attach(html_part)

    with open(REPORT_PATH, "rb") as f:
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(REPORT_PATH)}",
    )
    msg.attach(attachment)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, RECIPIENTS, msg.as_string())

    print(f"Reporte enviado exitosamente a {len(RECIPIENTS)} destinatarios.")


if __name__ == "__main__":
    send_report()
