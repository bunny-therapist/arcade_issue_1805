import arcade
import pathlib

MAP_FILE = pathlib.Path(__file__).parent / "map.tmx"


class IssueDemonstrationWindow(arcade.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map = arcade.load_tilemap(MAP_FILE)
        self.sprite_list = self.map.sprite_lists["objects"]
        self.set_viewport(
            left=0,
            right=self.map.width,
            bottom=0,
            top=self.map.height,
        )

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()


window = IssueDemonstrationWindow()
arcade.run()
