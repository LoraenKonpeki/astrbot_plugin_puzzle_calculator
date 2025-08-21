from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register(
    "puzzle_calculator",
    "Loraen_Konpeki",
    "在AstrBot上完成简单的古典密码解密和加密功能",
    "1.1",
)
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
为了输入速度，建议直接将所有两个一组的旗语拼起来输入。例如 "/fl 62797281"。（当然也可以用空格分隔，如 "/fl 62 79 72 81"）
不用担心输入顺序，28和82表示同一个旗语。

如果你没有数字小键盘，可以使用键盘左半部分的 QWEDCXZA 八个方向作为输入。例如 "/fl dxQexqWZ"（不区分大小写）

如果使用手机九键键盘方向，请使用：/flk /flagk /semaphorek
        """
        yield event.plain_result(help_message)

    @filter.command("flag", alias={"fl", "semaphore", "flagk", "flk", "semaphorek"})
    async def flag_decode(self, event: AstrMessageEvent):
        """电脑键盘旗语解码"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)
        message_str = message_str.strip().split()
        flags = []  # 用于存储旗语
        flags_strs = message_str[1:]  # 获取除指令外的所有内容
        for flags_str in flags_strs:
            flags += [flags_str[i : i + 2] for i in range(0, len(flags_str), 2)]
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
                "ZX": "A",
                "XA": "B",
                "XQ": "C",
                "XW": "D",
                "XE": "E",
                "XD": "F",
                "XC": "G",
                "ZA": "H",
                "QZ": "I",
                "DW": "J",
                "WZ": "K",
                "EZ": "L",
                "ZD": "M",
                "CZ": "N",
                "QA": "O",
                "WA": "P",
                "EA": "Q",
                "DA": "R",
                "CA": "S",
                "QW": "T",
                "QE": "U",
                "WC": "V",
                "ED": "W",
                "EC": "X",
                "CW": "Y",
                "DC": "Z",
            }
            if "k" in message_str[0].lower():  # 检测是否使用手机键盘旗语
                dic_flag = {
                    "78": "A",
                    "84": "B",
                    "81": "C",
                    "82": "D",
                    "83": "E",
                    "86": "F",
                    "89": "G",
                    "74": "H",
                    "17": "I",
                    "62": "J",
                    "27": "K",
                    "37": "L",
                    "76": "M",
                    "97": "N",
                    "14": "O",
                    "24": "P",
                    "34": "Q",
                    "64": "R",
                    "94": "S",
                    "12": "T",
                    "13": "U",
                    "29": "V",
                    "36": "W",
                    "39": "X",
                    "92": "Y",
                    "69": "Z",
                    "ZX": "A",
                    "XA": "B",
                    "XQ": "C",
                    "XW": "D",
                    "XE": "E",
                    "XD": "F",
                    "XC": "G",
                    "ZA": "H",
                    "QZ": "I",
                    "DW": "J",
                    "WZ": "K",
                    "EZ": "L",
                    "ZD": "M",
                    "CZ": "N",
                    "QA": "O",
                    "WA": "P",
                    "EA": "Q",
                    "DA": "R",
                    "CA": "S",
                    "QW": "T",
                    "QE": "U",
                    "WC": "V",
                    "ED": "W",
                    "EC": "X",
                    "CW": "Y",
                    "DC": "Z",
                }

            result = ""
            for flag in flags:
                flag = flag.upper()  # 转换为大写以匹配字典
                if flag in dic_flag:
                    result += dic_flag[flag]
                elif (flag[1] + flag[0]) in dic_flag:
                    result += dic_flag[flag[1] + flag[0]]
                else:
                    result += "?"
            yield event.plain_result(f"解码结果: \n{result.lower()}")

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

如果使用手机九键键盘，仍然用左半部分，请使用：/blk /blindk
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
                "7": "A",
                "47": "B",
                "78": "C",
                "578": "D",
                "57": "E",
                "478": "F",
                "4578": "G",
                "457": "H",
                "48": "I",
                "458": "J",
                "17": "K",
                "147": "L",
                "178": "M",
                "1578": "N",
                "157": "O",
                "1478": "P",
                "14578": "Q",
                "1457": "R",
                "148": "S",
                "1458": "T",
                "127": "U",
                "1247": "V",
                "2458": "W",
                "1278": "X",
                "12578": "Y",
                "1257": "Z",
                "245": ".",
                "4": ",",
                "45": ":",
                "14": ";",
                "158": "@",
                "1258": "#",
                "145": "+",
                "12": "-",
                "18": "/",
                "15": "*",
                "1245": "=",
                "124": "?",
                "Q": "A",
                "AQ": "B",
                "QW": "C",
                "QSW": "D",
                "QS": "E",
                "AQW": "F",
                "AQSW": "G",
                "AQS": "H",
                "AW": "I",
                "ASW": "J",
                "QZ": "K",
                "AQZ": "L",
                "QWZ": "M",
                "QSWZ": "N",
                "QSZ": "O",
                "AQWZ": "P",
                "AQSWZ": "Q",
                "AQSZ": "R",
                "AWZ": "S",
                "ASWZ": "T",
                "QXZ": "U",
                "AQXZ": "V",
                "ASWX": "W",
                "QWXZ": "X",
                "QSWXZ": "Y",
                "QSXZ": "Z",
                "ASX": ".",
                "A": ",",
                "AS": ":",
                "AZ": ";",
                "SWZ": "@",
                "SWXZ": "#",
                "ASZ": "+",
                "XZ": "-",
                "WZ": "/",
                "SZ": "*",
                "ASXZ": "=",
                "AXZ": "?",
            }
            if "k" in message_str.split()[0].lower():  # 检测是否使用手机键盘盲文
                dic_blind = {
                    "1": "A",
                    "14": "B",
                    "12": "C",
                    "125": "D",
                    "15": "E",
                    "124": "F",
                    "1245": "G",
                    "145": "H",
                    "24": "I",
                    "245": "J",
                    "17": "K",
                    "147": "L",
                    "127": "M",
                    "1257": "N",
                    "157": "O",
                    "1247": "P",
                    "12457": "Q",
                    "1457": "R",
                    "247": "S",
                    "2457": "T",
                    "178": "U",
                    "1478": "V",
                    "2458": "W",
                    "1278": "X",
                    "12578": "Y",
                    "1578": "Z",
                    "458": ".",
                    "4": ",",
                    "45": ":",
                    "47": ";",
                    "257": "@",
                    "2578": "#",
                    "457": "+",
                    "78": "-",
                    "27": "/",
                    "57": "*",
                    "4578": "=",
                    "478": "?",
                    "Q": "A",
                    "AQ": "B",
                    "QW": "C",
                    "QSW": "D",
                    "QS": "E",
                    "AQW": "F",
                    "AQSW": "G",
                    "AQS": "H",
                    "AW": "I",
                    "ASW": "J",
                    "QZ": "K",
                    "AQZ": "L",
                    "QWZ": "M",
                    "QSWZ": "N",
                    "QSZ": "O",
                    "AQWZ": "P",
                    "AQSWZ": "Q",
                    "AQSZ": "R",
                    "AWZ": "S",
                    "ASWZ": "T",
                    "QXZ": "U",
                    "AQXZ": "V",
                    "ASWX": "W",
                    "QWXZ": "X",
                    "QSWXZ": "Y",
                    "QSXZ": "Z",
                    "ASX": ".",
                    "A": ",",
                    "AS": ":",
                    "AZ": ";",
                    "SWZ": "@",
                    "SWXZ": "#",
                    "ASZ": "+",
                    "XZ": "-",
                    "WZ": "/",
                    "SZ": "*",
                    "ASXZ": "=",
                    "AXZ": "?",
                }

            result = ""
            for blind in blinds:
                blind = "".join(sorted(blind.strip())).upper()
                if blind in dic_blind:
                    result += dic_blind[blind]
                else:
                    result += "?"
            yield event.plain_result(f"解码结果: \n{result.lower()}")

    @filter.command("morsehelp", alias={"mshelp"})
    async def morse_help(self, event: AstrMessageEvent):
        """摩尔斯电码帮助"""
        help_text = """
摩尔斯电码帮助：
/morse <摩尔斯电码> 或 /ms <摩尔斯电码>，电码之间用空格分隔
示例：/ms .- -... -.-.
                
横线可以用以下字符：- _ — 一
点可以用以下字符：. 、 · *
例如：/morse *一 —、、、 _·_·
                     """
        yield event.plain_result(help_text)

    @filter.command("morse", alias={"ms"})
    async def morse_decode(self, event: AstrMessageEvent):
        """摩尔斯电码解码"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)
        morse_code = message_str.strip().split()[1:]
        if morse_code == []:
            yield event.plain_result("请输入待解码摩尔斯电码！")
        else:
            dic_morse = {
                ".-": "A",
                "-...": "B",
                "-.-.": "C",
                "-..": "D",
                ".": "E",
                "..-.": "F",
                "--.": "G",
                "....": "H",
                "..": "I",
                ".---": "J",
                "-.-": "K",
                ".-..": "L",
                "--": "M",
                "-.": "N",
                "---": "O",
                ".--.": "P",
                "--.-": "Q",
                ".-.": "R",
                "...": "S",
                "-": "T",
                "..-": "U",
                "...-": "V",
                ".--": "W",
                "-..-": "X",
                "-.--": "Y",
                "--..": "Z",
                "-----": "0",
                ".----": "1",
                "..---": "2",
                "...--": "3",
                "....-": "4",
                ".....": "5",
                "-....": "6",
                "--...": "7",
                "---..": "8",
                "----.": "9",
            }

            result = ""
            for code in morse_code:
                code = code.translate(str.maketrans("_—一、·*", "---..."))
                if code in dic_morse:
                    result += dic_morse[code]
                else:
                    result += "?"
            yield event.plain_result(f"解码结果: \n{result.lower()}")

    async def caesar(self, string: str, shift: int):
        """凯撒密码加密"""
        result = ""
        for char in string:
            if char.isalpha():
                shift_base = ord("A") if char.isupper() else ord("a")
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result

    async def atbash(self, string: str):
        """阿特巴什密码加密"""
        result = ""
        for char in string:
            if char.isalpha():
                shift_base = ord("A") if char.isupper() else ord("a")
                result += chr(25 - (ord(char) - shift_base) + shift_base)
            else:
                result += char
        return result

    async def qwe_encode(self, string: str):
        """QWE密码加密"""
        result = ""
        dic_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        dic_lower = "qwertyuiopasdfghjklzxcvbnm"
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result += dic_upper[ord(char) - ord("A")]
                else:
                    result += dic_lower[ord(char) - ord("a")]
            else:
                result += char
        return result

    async def qwe_decode(self, string: str):
        """QWE密码解密"""
        result = ""
        dic_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
        dic_lower = "qwertyuiopasdfghjklzxcvbnm"
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result += chr(dic_upper.index(char) + ord("A"))
                else:
                    result += chr(dic_lower.index(char) + ord("a"))
            else:
                result += char
        return result

    @filter.command("caesar", alias={"ks"})
    async def caesar_command(self, event: AstrMessageEvent):
        """凯撒密码命令"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)
        messages = message_str.split()
        if len(messages) < 3:
            yield event.plain_result("请输入待加密文本和位移量！")
        else:
            text = messages[1].strip()
            try:
                shift = int(messages[2].strip())
            except ValueError:
                yield event.plain_result("位移量必须是一个整数！")
                return

            result = await self.caesar(text, shift)
            yield event.plain_result(f"凯撒位移结果: \n{result}")

    @filter.command("bomb")
    async def bomb_command(self, event: AstrMessageEvent):
        """爆破，爽"""
        message_str = event.message_str  # 用户发的纯文本消息字符串
        message_chain = event.get_messages()
        logger.info(message_chain)
        messages = message_str.split()
        if len(messages) < 2:
            yield event.plain_result("请输入待爆破的文本！")
        else:
            text = " ".join(messages[1:])
            result = "爆破结果：\n"
            for i in range(1, 26):
                result += f"凯撒+{i}: {await self.caesar(text, i)}\n"
            result += f"Atbash: {await self.atbash(text)}\n"
            result += f"QWE加密: {await self.qwe_encode(text)}\n"
            result += f"QWE解密: {await self.qwe_decode(text)}\n"
            yield event.plain_result(result)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
