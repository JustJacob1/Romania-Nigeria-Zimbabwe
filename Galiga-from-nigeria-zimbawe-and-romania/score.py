class Score:
    def __init__(self):
        pass

    def read_file(self):
        file = "Galiga-from-nigeria-zimbawe-and-romania\highscore.txt"
        open_file = open(file)
        print(open_file.read())
        open_file.close()

    def write_file(self, score):
        file =  open("Galiga-from-nigeria-zimbawe-and-romania\highscore.txt", "w")
        file.write(score)
        file.close()

    def high_score(self, points, high_score):
        if points > high_score:
            self.write_file(points)
        