
# Análisis de IP con APIVoid 🌐

Este script en Python utiliza la API de [APIVoid](https://www.apivoid.com/) para analizar direcciones IP y proporcionar información detallada, como:
- Deteción en listas negras.
- Proveedor de servicios (ISP) y rango de red (CIDR).
- Ubicación geográfica.
- DNS inverso y uso como proxy, VPN o en la red Tor.
- Historial de actividad maliciosa.

## ⚙️ Requisitos

- **Python 3.7 o superior**: Asegúrate de tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/).
- **Librerías necesarias**:
  - `requests`
  - `rich`

Puedes instalarlas ejecutando el siguiente comando:
```bash
pip install requests rich
```

- **API Key de APIVoid**:  
  Es obligatorio tener una API Key válida de APIVoid para usar este script. Si no tienes una, puedes registrarte y obtenerla en [APIVoid](https://www.apivoid.com/).

## 🚀 Uso del script

1. Clona este repositorio o descarga el archivo `IP_D.py`:
```bash
git clone https://github.com/CodingJAndres/APIVoid.git
```

2. Abre el archivo `IP_D.py` y reemplaza la variable `API_KEY` con tu propia API Key:
```python
API_KEY = "TU_API_KEY_AQUÍ"
```

3. Ejecuta el script en tu terminal:
```bash
python3 IP_D.py
```

4. Introduce la dirección IP que deseas analizar y revisa los resultados detallados.

## 📋 Ejemplo de salida

```plaintext
╭─────────────────────────────── Iniciando análisis ───────────────────────────────╮
│                           Analizando la IP: 185.199.111.153...                   │
╰──────────────────────────────────────────────────────────────────────────────────╯

╭────────────────────────── Información General ──────────────────────────╮
│ Proveedor de servicios (ISP): GitHub, Inc.                             │
│ Sistema Autónomo (ASN): AS36459                                        │
│ Ubicación: América del Norte, Estados Unidos, California, San Francisco │
│ Rango de red (CIDR): 185.199.108.0/22                                  │
│ DNS inverso: pages.github.io                                           │
╰────────────────────────────────────────────────────────────────────────╯

╭───────────────────────────── Listas Negras ─────────────────────────────╮
│ La IP está en las siguientes listas negras:                            │
│ - Spamhaus: Detectada (https://www.spamhaus.org)                       │
│ - SORBS: Detectada (https://www.sorbs.net)                             │
╰────────────────────────────────────────────────────────────────────────╯

╭─────────────────── Historial de actividad maliciosa ────────────────────╮
│ Puntuación de actividad maliciosa: 15                                  │
╰────────────────────────────────────────────────────────────────────────╯
```

## ❗ Notas importantes

- **Uso responsable**: Este script es únicamente para propósitos educativos y de investigación. No está diseñado para actividades maliciosas.
- **Límites de la API**: Verifica los límites de tu plan de APIVoid para evitar exceder el número permitido de solicitudes.

## 🛠️ Personalización

Si deseas agregar más funcionalidades o modificar el diseño de los resultados, siéntete libre de hacerlo. Si necesitas ayuda, ¡puedes contactarme!

## 📜 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

---

### 🌟 Contribuye

Si tienes ideas o mejoras, ¡los pull requests son bienvenidos! 😄
