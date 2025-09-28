def calculate_remainder(decimal_num):
    return decimal_num % 16

if __name__ == "__main__":
    while True:
        try:
            input_str = input("请输入十进制数：")
            decimal_num = int(input_str)
            remainder = calculate_remainder(decimal_num)
            if remainder == 15:
                print(f"checksum计算正确,余数为{remainder}\n")
            else:
                print(f"checksum计算错误,余数为{remainder}（不为15）")
                break  
        except ValueError:
            print("输入错误，请输入有效的十进制整数\n")
        except Exception as e:
            print(f"发生未知错误：{e}，程序将退出")
            break
