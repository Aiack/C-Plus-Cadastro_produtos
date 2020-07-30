from src.config.Firebird import Firebird

class main():
    def __init__(self):
        self.db = Firebird()
        
        print('main :', self.db)

if __name__ == "__main__":
    main()
    from src import Table_teste