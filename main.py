from pathlib import Path

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register


@register(
    "help_image_reply",
    "your_name",
    "收到 /help 时回复自定义图片",
    "1.0.2",
    "https://github.com/LiYH2008/astrbot_piugin_help_image_reply"
)
class HelpImageReplyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.help_image_path = str(
            (Path(__file__).parent / "assets" / "help.png").resolve()
        )

    @filter.command("help")
    async def on_help(self, event: AstrMessageEvent):
        yield event.image_result(self.help_image_path)
