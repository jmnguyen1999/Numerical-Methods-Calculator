class Interpolation:
    def __init__(self, xs, ys, cs, n, z):
        self.xs = xs
        self.ys = ys
        self.cs = cs
        self.n = n
        self.z = z

    def coeff(self):
        for i in range(0, (self.n)+1):
            self.cs.append(self.ys[i])
        for j in range(1, (self.n)+1):
            for k in range(self.n, j-1, -1):
                self.cs[k] = (self.cs[k] - self.cs[k - 1]) / (self.xs[k] - self.xs[k - j])

    def evalnewton(self):
        result = self.cs[self.n]
        for i in range((self.n)-1, -1, -1):
            result = result * (self.z - self.xs[i]) + self.cs[i]
        return result

    def execute(self):
        self.coeff()
        return self.evalnewton()

