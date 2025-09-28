BASE_VALUE = 3.487617

def calculate_offset(send_time):
    """计算帧offset值（发送时间减去基准值）"""
    return send_time - BASE_VALUE

if __name__ == "__main__":
    print("请输入帧发送时间，程序将计算对应的offset")
    print("输入 'q' 或 '退出' 可结束程序\n")

    while True:
        try:
            input_str = input("请输入帧发送时间：")
          
            if input_str.lower() in ['q', '退出']:
                print("程序已退出")
                break
            
            send_time = float(input_str)
            offset = calculate_offset(send_time)
            print(f"帧offset为：{offset:.6f}\n")
            
        except ValueError:
            print("输入无效，请输入数字类型的值（输入'q'可退出）\n")
        except Exception as e:
            print(f"发生错误：{e}，程序将退出")
            break
