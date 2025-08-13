help_message = """
    旗语解码帮助:

    /fl（或 /flag 或 /semaphore）+旗语
    数字对应方向参考电脑数字小键盘。（例如：2↓ 4← 8↑ 9↗）
    为了输入速度，直接将所有两个一组的旗语拼起来输入。例如 "/fl 62797281"。
    不用担心输入顺序，28和82表示同一个旗语。

    如果你没有数字小键盘，可以使用键盘左半部分的 QWEDCXZA 八个方向作为输入。例如 "/fl dxQexqWZ"（不区分大小写）

    如果使用手机九键键盘方向，请使用：/flk /flagk /semaphorek
    """
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
dic_flag_k = {
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


def help():
    return help_message


def decode(message_str):
    messages = message_str.strip().split()

    if len(messages) < 2:
        return "请输入待解码旗语！"
    flags_str = messages[1]
    flags = [flags_str[i : i + 2] for i in range(0, len(flags_str), 2)]
    if not all(len(flag) == 2 for flag in flags):
        return "旗语必须是长度为2的字符串！\n你的输入：{flags}"
    else:
        if "k" in message_str[0].lower():  # 检测是否使用手机键盘旗语
            dic_flag = dic_flag_k
            result = ""
            for flag in flags:
                flag = flag.upper()  # 转换为大写以匹配字典
                if flag in dic_flag:
                    result += dic_flag[flag]
                elif (flag[1] + flag[0]) in dic_flag:
                    result += dic_flag[flag[1] + flag[0]]
                else:
                    result += "?"
            return result.lower()
