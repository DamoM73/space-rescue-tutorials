from GameFrame import Level, Globals
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hud import Score, Lives, Rescued, Streak, PowerMeter

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("background.png")
        
        # add objects
        self.ship = Ship(self, 25, 50)
        self.add_room_object(self.ship)
        self.add_room_object(Zork(self,1120, 50))
        
        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)
        self.rescued = Rescued(self, 20, Globals.SCREEN_HEIGHT - 60)
        self.add_room_object(self.rescued)
        self.streak = Streak(self, Globals.SCREEN_WIDTH - 480, Globals.SCREEN_HEIGHT - 60)
        self.add_room_object(self.streak)
        self.power_meter = PowerMeter(self, Globals.SCREEN_WIDTH - 150, 55)
        self.add_room_object(self.power_meter)
        
        # load sound files
        self.shoot_laser = self.load_sound("Laser_shot.ogg")
        self.asteroid_shot = self.load_sound("Asteroid_shot.wav")
        self.astronaut_saved = self.load_sound("Astronaut_saved.ogg")
        self.asteroid_collision = self.load_sound("Ship_damage.ogg")
        self.astronaut_shot = self.load_sound("Astronaut_hit.ogg")
        self.goal_reached = self.load_sound("Bonus_score.mp3")
        self.life_gained = self.load_sound("Life_increase.ogg")
        self.shield_up = self.load_sound("Shields.ogg")
        self.max_shot = self.load_sound("Max_shot_increase.wav")
        self.power_used = self.load_sound("Skill_used.mp3")
