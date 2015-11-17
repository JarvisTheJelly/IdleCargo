

class Resource(object):

    def __init__(self):
        self.abundance = 0;
        self.demand = 0;
        self.value = 0;
        self.icon = None

    def calculate_value(self):
        return float(self.demand) / self.abundance

    def draw_icon(self, surface, pos):
        surface.blit(self.icon, pos)


class Iron(Resource):

    def __init__(self):
        Resource.__init__(self)
