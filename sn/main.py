#!/usr/bin/python3

input_file = ""
output_file = "sn/pass_dict.txt"

def delete(filePath):
    with open(filePath, "r") as f:
        data = f.read().split("\n")
    print(f"原始文件密码个数: {len(data)}, fileName: {filePath}")
    data = set(data)
    print(f"去重文件密码个数: {len(data)}")
    data = "\n".join(data)
    return data

if __name__ == "__main__":
    delete(filePath = input_file)

