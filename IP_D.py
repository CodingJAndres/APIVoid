import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Inicializar consola para salida estilizada
console = Console()

# Tu API Key de APIVoid
API_KEY = "54fffa31c62d647b156f1d22d618cf147ae8b96f"

def analizar_ip(ip):
    url = f"https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key={API_KEY}&ip={ip}"
    
    console.print(Panel(f"[bold yellow]Analizando la IP: [white]{ip}[/white]...[/bold yellow]", title="[bold blue]Iniciando análisis[/bold blue]"))
    
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            
            if "error" in data and data["error"]:
                console.print(Panel(f"[bold red]Error en el análisis:[/bold red] {data['error']['message']}", title="[bold red]Error[/bold red]"))
            else:
                report = data["data"]["report"]
                blacklists = report["blacklists"]
                detections = blacklists.get("detections", 0)
                
                # Información general de la IP
                ip_info = report.get("information", {})
                asn = ip_info.get("asn", "N/A")
                isp = ip_info.get("isp", "N/A")
                continent = ip_info.get("continent_name", "N/A")
                country = ip_info.get("country_name", "N/A")
                region = ip_info.get("region_name", "N/A")
                city = ip_info.get("city_name", "N/A")
                cidr = ip_info.get("network", {}).get("cidr", "N/A")
                dns_reverse = ip_info.get("dns", {}).get("reverse", "No configurado")
                
                # Panel de información general
                info_general = f"""
[bold yellow]Proveedor de servicios (ISP):[/bold yellow] {isp}
[bold yellow]Sistema Autónomo (ASN):[/bold yellow] {asn}
[bold yellow]Ubicación:[/bold yellow] {continent}, {country}, {region}, {city}
[bold yellow]Rango de red (CIDR):[/bold yellow] {cidr}
[bold yellow]DNS inverso:[/bold yellow] {dns_reverse}
"""
                console.print(Panel(info_general, title="[bold blue]Información General[/bold blue]", style="cyan"))
                
                # Panel de listas negras
                if detections > 0:
                    lista_negra = "[bold red]La IP está en las siguientes listas negras:[/bold red]\n"
                    for provider, details in blacklists["engines"].items():
                        if details.get("detected"):
                            lista_negra += f"- {provider}: Detectada ([blue]{details.get('reference', 'Sin referencia')}[/blue])\n"
                    console.print(Panel(lista_negra, title="[bold red]Listas Negras[/bold red]", style="red"))
                else:
                    console.print(Panel("[bold green]La IP no está en listas negras conocidas.[/bold green]", title="[bold green]Listas Negras[/bold green]", style="green"))
                
                # Información adicional
                is_proxy = "Sí" if ip_info.get("is_proxy", False) else "No"
                is_vpn = "Sí" if ip_info.get("is_vpn", False) else "No"
                is_tor = "Sí" if ip_info.get("is_tor", False) else "No"
                last_malicious_activity = report.get("last_malicious_activity", "No reportada")
                
                info_adicional = f"""
[bold yellow]¿Es un proxy?[/bold yellow] {is_proxy}
[bold yellow]¿Es una VPN?[/bold yellow] {is_vpn}
[bold yellow]¿Pertenece a la red Tor?[/bold yellow] {is_tor}
[bold yellow]Última actividad maliciosa reportada:[/bold yellow] {last_malicious_activity}
"""
                console.print(Panel(info_adicional, title="[bold magenta]Información Adicional[/bold magenta]", style="magenta"))
                
                # Historial de actividad maliciosa
                malicious_score = report.get("score", {}).get("value", "N/A")
                malicious_score_panel = f"""
[bold yellow]Puntuación de actividad maliciosa:[/bold yellow] {malicious_score}
"""
                console.print(Panel(malicious_score_panel, title="[bold green]Historial de actividad maliciosa[/bold green]", style="green"))
        except Exception as e:
            console.print(Panel(f"[bold red]Error procesando la respuesta: {e}[/bold red]", title="[bold red]Error[/bold red]"))
    else:
        console.print(Panel(f"[bold red]Error en la solicitud: Código {response.status_code}[/bold red]", title="[bold red]Error[/bold red]"))

# Probar con una IP
ip_a_analizar = input("Introduce la IP para analizar: ")
analizar_ip(ip_a_analizar)
