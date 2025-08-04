from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("puzzle_calculator", "Loraen_Konpeki", "在AstrBot上完成简单的古典密码解密和加密功能", "1.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @filter.command("flaghelp", alias={"flhelp", "semaphorehelp"})
    async def flag_help(self, event: AstrMessageEvent):
        """旗语解码帮助"""
        message_chain = event.get_messages()
        logger.info(message_chain)
        help_message = """
        旗语解码帮助:

        /fl（或 /flag 或 /semaphore）+旗语
        数字对应方向参考电脑数字小键盘。（例如：2↓ 4← 8↑ 9↗）
        为了输入速度，直接将所有两个一组的旗语拼起来输入。例如 "/fl 62797281"。
        不用担心输入顺序，28和82表示同一个旗语。

        如果你没有数字小键盘，可以使用键盘左半部分的 QWEDCXZA 八个方向作为输入。例如 "/fl dxQexqWZ"（不区分大小写）

        如果使用手机九键键盘方向，请使用：/flk /flagk /semaphorek
        """
        yield event.plain_result(help_message)

    @filter.command("flag", alias={"fl", "semaphore", "flagk", "flk", "semaphorek"})
    async def flag_decode(self, event: AstrMessageEvent, flags_str: str):
        """电脑键盘旗语解码"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)
        message_str = message_str.strip().split()

        flags = [flags_str[i:i+2] for i in range(0, len(flags_str), 2)]
        if flags == []:
            yield event.plain_result("请输入待解码旗语！")
        elif not all(len(flag) == 2 for flag in flags):
            print(f"flags: {flags}")
            yield event.plain_result(f"旗语必须是长度为2的字符串！\n你的输入：{flags}")
        else:
            dic_flag = {
                "12": "A", "24": "B", "27": "C", "28": "D", "29": "E",
                "26": "F", "23": "G", "14": "H", "71": "I", "68": "J",
                "81": "K", "91": "L", "16": "M", "31": "N", "74": "O",
                "84": "P", "94": "Q", "64": "R", "34": "S", "78": "T",
                "79": "U", "83": "V", "96": "W", "93": "X", "38": "Y",
                "63": "Z",
                "ZX": "A", "XA": "B", "XQ": "C", "XW": "D", "XE": "E",
                "XD": "F", "XC": "G", "ZA": "H", "QZ": "I", "DW": "J",
                "WZ": "K", "EZ": "L", "ZD": "M", "CZ": "N", "QA": "O",
                "WA": "P", "EA": "Q", "DA": "R", "CA": "S", "QW": "T",
                "QE": "U", "WC": "V", "ED": "W", "EC": "X", "CW": "Y",
                "DC": "Z"
            }
            if 'k' in message_str[0].lower():  # 检测是否使用手机键盘旗语
                dic_flag = {
                    '78': 'A', '84': 'B', '81': 'C', '82': 'D', '83': 'E',
                    '86': 'F', '89': 'G', '74': 'H', '17': 'I', '62': 'J',
                    '27': 'K', '37': 'L', '76': 'M', '97': 'N', '14': 'O',
                    '24': 'P', '34': 'Q', '64': 'R', '94': 'S', '12': 'T',
                    '13': 'U', '29': 'V', '36': 'W', '39': 'X', '92': 'Y',
                    '69': 'Z',
                    "ZX": "A", "XA": "B", "XQ": "C", "XW": "D", "XE": "E",
                    "XD": "F", "XC": "G", "ZA": "H", "QZ": "I", "DW": "J",
                    "WZ": "K", "EZ": "L", "ZD": "M", "CZ": "N", "QA": "O",
                    "WA": "P", "EA": "Q", "DA": "R", "CA": "S", "QW": "T",
                    "QE": "U", "WC": "V", "ED": "W", "EC": "X", "CW": "Y",
                    "DC": "Z"
                }

            result = ""
            for flag in flags:
                flag = flag.upper()  # 转换为大写以匹配字典
                if flag in dic_flag:
                    result += dic_flag[flag]
                elif (flag[1]+flag[0]) in dic_flag:
                    result += dic_flag[flag[1]+flag[0]]
                else:
                    result += "?"
            yield event.plain_result(f"解码结果: \n{result.lower()}")

    # @filter.command("flk", alias={"flagk", "semaphorek"})
    # async def flagk_decode(self, event: AstrMessageEvent, flags_str: str):
    #     """手机键盘旗语解码"""
    #     message_str = event.message_str
    #     message_str = event.message_str  # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages()
    #     logger.info(message_chain)

    #     flags = [flags_str[i:i+2] for i in range(0, len(flags_str), 2)]
    #     if flags == []:
    #         yield event.plain_result("请输入待解码旗语！")
    #     elif not all(len(flag) == 2 for flag in flags):
    #         print(f"flags: {flags}")
    #         yield event.plain_result(f"旗语必须是长度为2的字符串！\n你的输入：{flags}")
    #     else:
    #         dic_flag = {
    #             '78': 'A', '84': 'B', '87': 'C', '88': 'D', '89': 'E',
    #             '86': 'F', '83': 'G', '74': 'H', '77': 'I', '68': 'J',
    #             '87': 'K', '97': 'L', '76': 'M', '91': 'N', '84': 'O',
    #             '94': 'P', '94': 'Q', '64': 'R', '94': 'S', '78': 'T',
    #             '79': 'U', '93': 'V', '96': 'W', '93': 'X', '98': 'Y',
    #             '69': 'Z',
    #             "ZX": "A", "XA": "B", "XQ": "C", "XW": "D", "XE": "E",
    #             "XD": "F", "XC": "G", "ZA": "H", "QZ": "I", "DW": "J",
    #             "WZ": "K", "EZ": "L", "ZD": "M", "CZ": "N", "QA": "O",
    #             "WA": "P", "EA": "Q", "DA": "R", "CA": "S", "QW": "T",
    #             "QE": "U", "WC": "V", "ED": "W", "EC": "X", "CW": "Y",
    #             "DC": "Z"
    #         }
    #         result = ""
    #         for flag in flags:
    #             flag = flag.upper()  # 转换为大写以匹配字典
    #             if flag in dic_flag:
    #                 result += dic_flag[flag]
    #             elif (flag[1]+flag[0]) in dic_flag:
    #                 result += dic_flag[flag[1]+flag[0]]
    #             else:
    #                 result += "?"
    #         yield event.plain_result(f"解码结果: \n{result.lower()}")

    @filter.command("blindhelp", alias={"blhelp"})
    async def blind_help(self, event: AstrMessageEvent):
        """旗语解码帮助"""
        message_chain = event.get_messages()
        logger.info(message_chain)
        help_message = """
        盲文解码帮助:

        可用指令：/bl /blind
        数字对应六个点参考电脑数字小键盘左半部分六个数字。（每排两个点分别为 78 45 12）
        盲文之间用空格分隔，例如 "/bl 478 712 78 71"。
        不用担心输入顺序。

        如果你没有数字小键盘，可以使用键盘左半部分的 QW AS ZX 六个键作为输入。例如 "/bl aqw qzx QW Qz"

        如果使用手机九键键盘，仍然用左半部分，请使用：/flk /flagk /semaphorek
        """
        yield event.plain_result(help_message)

    @filter.command("blind", alias={"bl", "blindk", "blk"})
    async def blind_decode(self, event: AstrMessageEvent):
        """电脑键盘盲文解码"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)

        blinds = message_str.strip().split()[1:]
        if blinds == []:
            yield event.plain_result("请输入待解码盲文！")
        else:
            dic_blind = {
                "7": "A", "47": "B", "78": "C", "578": "D", "57": "E",
                "478": "F", "4578": "G", "457": "H", "48": "I", "458": "J",
                "17": "K", "147": "L", "178": "M", "1578": "N", "157": "O",
                "1478": "P", "14578": "Q", "1457": "R", "148": "S", "1458": "T",
                "127": "U", "1247": "V", "2458": "W", "1278": "X", "12578": "Y",
                "1257": "Z", "245": ".", "4": ",", "45": ":",
                "14": ";", "158": "@", "1258": "#", "145": "+", "12": "-",
                "18": "/", "15": "*", "1245": "=", '124': '?',
                'Q': 'A', 'AQ': 'B', 'QW': 'C', 'QSW': 'D', 'QS': 'E',
                'AQW': 'F', 'AQSW': 'G', 'AQS': 'H', 'AW': 'I', 'ASW': 'J',
                'QZ': 'K', 'AQZ': 'L', 'QWZ': 'M', 'QSWZ': 'N', 'QSZ': 'O',
                'AQWZ': 'P', 'AQSWZ': 'Q', 'AQSZ': 'R', 'AWZ': 'S', 'ASWZ': 'T',
                'QXZ': 'U', 'AQXZ': 'V', 'ASWX': 'W', 'QWXZ': 'X', 'QSWXZ': 'Y',
                'QSXZ': 'Z', 'ASX': '.', 'A': ',', 'AS': ':',
                'AZ': ';', 'SWZ': '@', 'SWXZ': '#', 'ASZ': '+', 'XZ': '-',
                'WZ': '/', 'SZ': '*', 'ASXZ': '=', 'AXZ': '?'
            }
            if 'k' in message_str[0].lower():  # 检测是否使用手机键盘盲文
                dic_blind = {
                    '1': 'A', '14': 'B', '12': 'C', '125': 'D', '15': 'E',
                    '124': 'F', '1245': 'G', '145': 'H', '24': 'I', '245': 'J',
                    '17': 'K', '147': 'L', '127': 'M', '1257': 'N', '157': 'O',
                    '1247': 'P', '12457': 'Q', '1457': 'R', '247': 'S', '2457': 'T',
                    '178': 'U', '1478': 'V', '2458': 'W', '1278': 'X', '12578': 'Y',
                    '1578': 'Z', '458': '.', '4': ',', '45': ':',
                    '47': ';', '257': '@', '2578': '#', '457': '+', '78': '-',
                    '27': '/', '57': '*', '4578': '=', '478': '?',
                    'Q': 'A', 'AQ': 'B', 'QW': 'C', 'QSW': 'D', 'QS': 'E',
                    'AQW': 'F', 'AQSW': 'G', 'AQS': 'H', 'AW': 'I', 'ASW': 'J',
                    'QZ': 'K', 'AQZ': 'L', 'QWZ': 'M', 'QSWZ': 'N', 'QSZ': 'O',
                    'AQWZ': 'P', 'AQSWZ': 'Q', 'AQSZ': 'R', 'AWZ': 'S', 'ASWZ': 'T',
                    'QXZ': 'U', 'AQXZ': 'V', 'ASWX': 'W', 'QWXZ': 'X', 'QSWXZ': 'Y',
                    'QSXZ': 'Z', 'ASX': '.', 'A': ',', 'AS': ':',
                    'AZ': ';', 'SWZ': '@', 'SWXZ': '#', 'ASZ': '+', 'XZ': '-',
                    'WZ': '/', 'SZ': '*', 'ASXZ': '=', 'AXZ': '?'
                }

            result = ""
            for blind in blinds:
                blind = ''.join(sorted(blind.strip())).upper()
                if blind in dic_blind:
                    result += dic_blind[blind]
                else:
                    result += "?"
            yield event.plain_result(f"解码结果: \n{result.lower()}")

    # @filter.command("blindk", alias={"blk"})
    # async def blindk_decode(self, event: AstrMessageEvent):
    #     """手机键盘盲文解码"""
    #     message_str = event.message_str  # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages()
    #     logger.info(message_chain)

    #     blinds = message_str.strip().split()[1:]
    #     if blinds == []:
    #         yield event.plain_result("请输入待解码盲文！")
    #     else:
    #         dic_blind = {
    #             '1': 'A', '14': 'B', '12': 'C', '125': 'D', '15': 'E',
    #             '124': 'F', '1245': 'G', '145': 'H', '24': 'I', '245': 'J',
    #             '17': 'K', '147': 'L', '127': 'M', '1257': 'N', '157': 'O',
    #             '1247': 'P', '12457': 'Q', '1457': 'R', '247': 'S', '2457': 'T',
    #             '178': 'U', '1478': 'V', '2458': 'W', '1278': 'X', '12578': 'Y',
    #             '1578': 'Z', '458': '.', '4': ',', '45': ':',
    #             '47': ';', '257': '@', '2578': '#', '457': '+', '78': '-',
    #             '27': '/', '57': '*', '4578': '=', '478': '?',
    #             'Q': 'A', 'AQ': 'B', 'QW': 'C', 'QSW': 'D', 'QS': 'E',
    #             'AQW': 'F', 'AQSW': 'G', 'AQS': 'H', 'AW': 'I', 'ASW': 'J',
    #             'QZ': 'K', 'AQZ': 'L', 'QWZ': 'M', 'QSWZ': 'N', 'QSZ': 'O',
    #             'AQWZ': 'P', 'AQSWZ': 'Q', 'AQSZ': 'R', 'AWZ': 'S', 'ASWZ': 'T',
    #             'QXZ': 'U', 'AQXZ': 'V', 'ASWX': 'W', 'QWXZ': 'X', 'QSWXZ': 'Y',
    #             'QSXZ': 'Z', 'ASX': '.', 'A': ',', 'AS': ':',
    #             'AZ': ';', 'SWZ': '@', 'SWXZ': '#', 'ASZ': '+', 'XZ': '-',
    #             'WZ': '/', 'SZ': '*', 'ASXZ': '=', 'AXZ': '?'
    #         }
    #         result = ""
    #         for blind in blinds:
    #             blind = ''.join(sorted(blind.strip())).upper()
    #             if blind in dic_blind:
    #                 result += dic_blind[blind]
    #             else:
    #                 result += "?"
    #         yield event.plain_result(f"解码结果: \n{result.lower()}")

        async def terminate(self):
            """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
