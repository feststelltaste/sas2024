# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'neo4j': {
        'command' : None,
        'absolute_url' : True,
        'port': 7474,
        'timeout': 60,
        'launcher_entry': {
            'enabled': True,
            'title': 'Neo4j Session'
        }
    }
}
