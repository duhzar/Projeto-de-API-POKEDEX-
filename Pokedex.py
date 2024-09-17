import requests
import webbrowser

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        species_url = data['species']['url'] 
        return {
            'name': data['name'],
            'id': data['id'],
            'height': data['height'],
            'weight': data['weight'],
            'types': [type_info['type']['name'] for type_info in data['types']],
            'abilities': [ability['ability']['name'] for ability in data['abilities']],
            'sprite': data['sprites']['front_default'],  
            'species_url': species_url 
        }
    else:
        return None

def get_pokemon_description(species_url):
    response = requests.get(species_url)
    
    if response.status_code == 200:
        data = response.json()
        for entry in data['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                return entry['flavor_text']
    return "Descrição não disponível."

def show_sprite_in_browser(sprite_url):
    if sprite_url:
        webbrowser.open(sprite_url)
    else:
        print("URL da sprite não disponível.")  

while True:
    print('-------------------------------------------------------------------------')
    print('Bem-Vindo a Pokedex 1.0 do Professor Eduardo')
    pokemon_name = input("Digite o nome do Pokémon (ou 'sair' para encerrar): ").strip().lower()
    
    if pokemon_name == "sair":
        print("Encerrando o programa...")
        break

    pokemon_data = get_pokemon_info(pokemon_name)

    if pokemon_data:
        print('-------------------------------------------------------------------------')
        print(f"ID: {pokemon_data['id']}")
        print(f"Nome: {pokemon_data['name']}")
        print(f"Altura: {pokemon_data['height']} dm")
        print(f"Peso: {pokemon_data['weight']} hg")
        print("Tipos:", ', '.join(pokemon_data['types']))
        print("Habilidades:", ', '.join(pokemon_data['abilities']))
        print('-------------------------------------------------------------------------')
        
        # Mostrar a descrição
        description = get_pokemon_description(pokemon_data['species_url'])
        print(f"Descrição: {description}")

        # Mostrar a sprite
        if pokemon_data['sprite']:
            print(f"Exibindo a sprite de {pokemon_data['name']} no navegador...")
        show_sprite_in_browser(pokemon_data['sprite'])
    else:
        print("Sprite não disponível.")
else:
        print("Pokémon não encontrado.")
