import requests

class RickAndMorty:
    BASE_URL = "https://rickandmortyapi.com/api/"

    def __init__(self):
        self.session = requests.Session()

    def get_character_by_id(self, id: int):
        response = self.session.get(self.BASE_URL + f'character/{id}')
        response.raise_for_status()  # if the request fails, this will raise a HTTPError
        return response.json()

def main():
    rick_and_morty = RickAndMorty()
    
    while True:
        try:
            character_id = int(input("\nEnter the ID of the character you want to get info about (0 to quit): "))
            if character_id == 0:
                break
            character = rick_and_morty.get_character_by_id(character_id)
            print(f"Name: {character['name']}")
            print(f"Status: {character['status']}")
            print(f"Species: {character['species']}")
            print(f"Gender: {character['gender']}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
