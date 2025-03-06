from robot import Robot
import pytest

class TestRobot:

    #övning 4:
    def setup_method(self):
        self.robot = Robot("Ai-Sauda", 50)


    def test_start(self):
        self.robot.start()
        assert self.robot.started is True
        assert self.robot.battery == 50

    

    def test_change(self):
       # self.robot = Robot("Ai-Sauda", 46)
        self.robot.charge()
        assert self.robot.battery == 100


    def test_move(self):
        #self.robot = Robot("Ai-Sauda", 50)
        self.robot.move(4) # 4 i detta fall meter som den går
        assert self.robot.battery == 10 # 10 i detta fall är batteriet som är kvar efter den har gått
    
    #övning 5:   
    def test_introduce(self):
        assert self.robot.introduce() == f"Hello, I am {self.robot.name}."


    #övning 7:
    def test_negative_moving(self):
        robot = Robot("Ai-Sauda", 100) #kolla om den behövs?
        with pytest.raises(ValueError):
            self.robot.moving(-5)
    
    #övning 9:
    def test_multiple_robots(self):
        robots = [Robot("Robot1", 100), Robot("Robot2", 100), Robot("Robot3", 100)]
        for robot in robots:
            assert robot.battery == 100
