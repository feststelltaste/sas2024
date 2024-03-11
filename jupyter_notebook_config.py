# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'neo4j': {
        'command': None,  # Da Neo4j bereits läuft, kein Startbefehl nötig
        'port': 7474,  # Port, auf dem Neo4j lauscht
        'absolute_url': False,  # Relative URLs innerhalb von Jupyter verwenden
        'timeout': 60,  # Timeout für Verbindungsaufbau, kann angepasst werden
        'launcher_entry': {  # Eintrag im Jupyter Launcher
            'enabled': True,
            'title': 'Neo4j Browser'
        }
    }
}
