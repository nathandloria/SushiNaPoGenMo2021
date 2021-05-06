import gen 

def parse_input_file(path:str):
    with open(path) as file:
        input_string = file.read()
        # get rid of newline "\n"
        input_list = input_string.split("\n")
    
    return input_list

def append_poems_to_file(path:str, search_terms: list):
    with open(path, "a+") as file:
        for term in search_terms:
            print(f"generating poem about {term}")
            poem = gen.generate_poem(term)
            file.write("\n------------------------")
            file.write(f"\n+---+ Your poem from the news surrounding {term} +---+")
            file.write(poem)
            file.write("\n------------------------\n")

if __name__ == "__main__":
    INPUT_FILE_NAME = "search-input.txt"
    OUTPUT_FILE_NAME = "poems.txt"
    append_poems_to_file(OUTPUT_FILE_NAME, parse_input_file(INPUT_FILE_NAME)) 
    
       