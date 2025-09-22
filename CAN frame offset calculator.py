def devide(x):
    y = x - 3.487617
    return y

if __name__ == "__main__":
    i = 1;
    for i in range(0,99):
        numInput = input("请输入帧发送时间：");
        timeOutput = devide(float(numInput));
        print("帧offset为：" + str(timeOutput));
   