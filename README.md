
# 在AstrBot上完成简单的古典密码解密和加密功能

### 指令列表：

##### 1. 旗语：

- `/flhelp` `/flaghelp` `/semaphorehelp` 获取旗语解码使用说明
- `/fl` `/flag` `/semaphore` 旗语解码（电脑小键盘 或 26键左边9x9区域）
- `/flk` `/flagk` `/semaphorek` 旗语解码（手机九键 或 26键9x9区域）

> 数字对应八个方向电脑数字小键盘：
>
> <table>
> <tr><td>7</td><td>8</td><td>9</td></tr>
> <tr><td>4</td><td>5</td><td>6</td></tr>
> <tr><td>1</td><td>2</td><td>3</td></tr>
> </table>
> 手机键盘 1↔7、2↔8、3↔9互换
>
> 无数字小键盘使用26键键盘左侧的 `Q W E D C X Z A` 表示方向  
>
> <table>
> <tr><td>Q</td><td>W</td><td>E</td></tr>
> <tr><td>A</td><td>S</td><td>D</td></tr>
> <tr><td>Z</td><td>X</td><td>C</td></tr>
> </table>
>
> **输入方式：**
>
> - 将旗语方向连续输入（每组两个数字）
> - 无需顺序：28和82表示同一结果
> - 示例：`/fl 62797281` `/flag dxQexqWZ`
> - 手机九键需要在指令后面加个k

---

##### 2. 盲文：

- `/blindhelp` `/blhelp` 获取盲文解码使用说明
- `/blind` `/bl` 盲文解码（电脑小键盘模式）
- `/blindk` `/blk` 盲文解码（手机键盘模式）

> 每个盲文由1-6个点位组成，点位位置对应键盘布局：
>
> - 电脑数字小键盘：
> 
> <table>
> <tr><td>7</td><td>8</td></tr>
> <tr><td>4</td><td>5</td></tr>
> <tr><td>1</td><td>2</td></tr>
> </table> 
>
> - 手机键盘 1↔7、2↔8互换
>
> 无数字小键盘使用26键键盘左侧的 `Q W A S Z X` 表示  
>
> <table>
> <tr><td>Q</td><td>W</td></tr>
> <tr><td>A</td><td>S</td></tr>
> <tr><td>Z</td><td>X</td></tr>
> </table>
>
> **输入方式：**
>
> - 用空格分隔每个盲文
> - 无需顺序
> - 支持数字或字母输入
>
> 示例：`/blind 478 712 78 71` `/bl aqw qzx QW Qz`
