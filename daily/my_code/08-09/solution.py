

class Soluton(object):
    def __init__(self, matrix):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.matrix = matrix
        self.path_info = [[{} for i in range (self.row)] for j in range(self.col)]
        self.init_update()

    def init_update(self):
        self.path_info[0][0]['from'] = (0, 0)
        self.path_info[0][0]['len'] = self.matrix[0][0]
        for i in range(1, self.row):
            self.path_info[i][0]['from'] = (i-1, 0)
            self.path_info[i][0]['len'] = self.matrix[i][0] + self.path_info[i-1][0]['len']

        for j in range(1, self.col):
            self.path_info[0][j]['from'] = (0, j-1)
            self.path_info[0][j]['len'] = self.matrix[0][j] + self.path_info[0][j-1]['len']

    def calculate_full_path(self):
        for row in range(1, self.row):
            for col in range(1, self.col):
                if self.path_info[row-1][col]['len'] <= self.path_info[row][col-1]['len']:
                    from_row = row-1
                    from_col = col
                else:
                    from_row = row
                    from_col = col -1

                self.path_info[row][col]['from'] = (from_row, from_col)
                self.path_info[row][col]['len'] = self.path_info[from_row][from_col]['len'] + self.matrix[row][col]

    def get_shortest_path(self, row, col):
        path = [(row, col)]
        length = self.path_info[row][col]['len']

        while True:
            point = self.path_info[row][col]['from']
            path.append(point)

            if point == (0, 0):
                break
            else:
                row = point[0]
                col = point[1]

        path.reverse()

        return length, path

if __name__ == '__main__':
    matrix = [[1, 3, 1, 5],
              [1, 5, 1, 2],
              [0, 2, 1, 1],
              [3, 1, 6, 1]]

    s = Soluton(matrix)
    for i in range(len(matrix)):
        print(matrix[i])
    s.calculate_full_path()
    length, path = s.get_shortest_path(3, 2)

    print(length)
    print(path)
