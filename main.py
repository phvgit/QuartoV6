from gui import GuiMainWin
from match import Match

if __name__ == "__main__":
    match = Match()
    app = GuiMainWin(match)
    app.mainloop()