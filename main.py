
from stemmer_pt_br import stemmer_pt_br

def main():
    words = ["meninas", "bibliotecária", "dentista"]

    for word in words:
        stemmer_pt_br_result = stemmer_pt_br(word)
        print(f"Original: {word}", f"Stemmer: {stemmer_pt_br_result}")
        

if __name__ == "__main__":
    main()