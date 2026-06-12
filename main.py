# main.py

from parser import BattleParser

def main():
    parser = BattleParser()

    with open("sample_battle.txt", "r", encoding="utf-8") as f:
        for line in f:
            parser.parse_line(line)

    print("\n=== FINAL BATTLE STATE ===\n")
    for name, data in parser.state.to_dict().items():
        print(name, data)

if __name__ == "__main__":
    main()