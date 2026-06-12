# parser.py

from state import BattleState

class BattleParser:
    def __init__(self):
        self.state = BattleState()

    def parse_line(self, line: str):
        line = line.strip()

        # MOVE
        if " used " in line:
            self._handle_move(line)

        # ITEM REVEAL (Life Orb / Focus Sash)
        if "Life Orb" in line:
            self._handle_item(line, "Life Orb")

        if "Focus Sash" in line:
            self._handle_item(line, "Focus Sash")

    def _handle_move(self, line):
        try:
            attacker, move_part = line.split(" used ")
            move = move_part.replace("!", "").strip()

            attacker = self._clean(attacker)

            p = self.state.get(attacker)
            p.moves.add(move)
        except:
            pass

    def _handle_item(self, line, item):
        name = self._extract_name(line)
        p = self.state.get(name)
        p.item = item

    def _clean(self, text):
        return (
            text.replace("The opposing ", "")
                .replace(" used", "")
                .strip()
        )

    def _extract_name(self, line):
        # simple MVP extractor (we will improve later)
        words = line.split()
        return self._clean(words[2]) if len(words) > 2 else "unknown"