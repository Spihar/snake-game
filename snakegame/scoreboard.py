from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            temp = file.read()
            self.highscore = int(temp)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.writing()


    def update(self):
        self.score += 1
        self.clear()
        self.writing()

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
            temp = str(self.highscore)
            with open("data.txt", mode="w") as file:
                file.write(temp)

        self.score = 0


    '''def game_over(self):
        self.goto(0,0)
        self.write("game over",align="center",font=('Arial', 25, 'normal'))'''

    def writing(self):
        self.write(f"score = {self.score}  highscore: {self.highscore}", False, align="center")
