class Settings():
    """一个存储游戏《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        #射击时间间隔，单位毫秒
        self.fire_time_interval = 200

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏节奏
        self.ship_speed_increment = 0.2
        self.bullet_speed_increment = 0.3
        self.alien_speed_increment = 0.1
        self.speedup_scale = 1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.75
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor= 0.5

        # 计分
        self.alien_points = 50

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor+= self.ship_speed_increment * self.speedup_scale
        self.bullet_speed_factor += self.bullet_speed_increment * self.speedup_scale
        self.alien_speed_factor += self.alien_speed_increment * self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)