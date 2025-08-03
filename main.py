from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("puzzle_calculator", "Loraen_Konpeki", "在AstrBot上完成简单的古典密码解密和加密功能", "1.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @filter.command("flag", alias={"semaphore"})
    async def helloworld(self, event: AstrMessageEvent, flags_str: str):
        """旗语解码"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)

        flags = [flags_str[i:i+2] for i in range(0, len(flags_str), 2)]
        if flags == []:
            yield event.plain_result("请输入待解码旗语！")
        elif not all(len(flag) == 2 for flag in flags):
            print(f"flags: {flags}")
            yield event.plain_result(f"旗语必须是长度为2的字符串！\n你的输入：{flags}")
        else:
            dic_flag = {
                "12": "A",
                "24": "B",
                "27": "C",
                "28": "D",
                "29": "E",
                "26": "F",
                "23": "G",
                "14": "H",
                "71": "I",
                "68": "J",
                "81": "K",
                "91": "L",
                "16": "M",
                "31": "N",
                "74": "O",
                "84": "P",
                "94": "Q",
                "64": "R",
                "34": "S",
                "78": "T",
                "79": "U",
                "83": "V",
                "96": "W",
                "93": "X",
                "38": "Y",
                "63": "Z",
            }
            result = ""
            for flag in flags:
                if flag in dic_flag:
                    result += dic_flag[flag]
                elif (flag[1]+flag[0]) in dic_flag:
                    result += dic_flag[flag[1]+flag[0]]
                else:
                    result += "?"
            yield event.plain_result(f"解码结果: \n{result.lower()}")

        async def terminate(self):
            """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
