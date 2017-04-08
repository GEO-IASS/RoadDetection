
# disjoint-set forests using union-by-rank


class UniSegment:

    def __init__(self, rank, size, id):
        self.rank = rank
        self.size = size
        self.id = id

    def get_size(self):
        return self.size


class Universe:

    def __init__(self, num_elements):
        self.segments = []
        self.num = num_elements
        for i in range(0, num_elements):
            self.segments.append(UniSegment(0, 1, i))

    def find(self, x):
        # finds which component the vertex belongs to
        y = x
        while y != self.segments[y].id:
            y = self.segments[y].id

        self.segments[x].id = y
        return y

    def join(self, x, y):
        # Join x,y based on rank
        if self.segments[x].rank > self.segments[y].rank:
            self.segments[y].id = x
            self.segments[x].size += self.segments[y].size
        else:
            self.segments[x].id = y
            self.segments[y].size += self.segments[x].size

            if self.segments[x].rank == self.segments[y].rank:
                self.segments[y].rank += 1

        self.num -= 1

    def get_size(self, x):
        e = self.segments[x]
        return e.get_size()

    def num_sets(self):
        return self.num
