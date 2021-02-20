class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


title_aux = input()
painter_aux = input()
year_aux = input()

art = Painting(title_aux, painter_aux, year_aux)

print("\"" + art.title + "\" by " + art.painter + " (" + art.year + ") hangs in the " + Painting.museum + ".")
