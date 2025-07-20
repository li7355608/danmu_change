import sys
import xml.etree.ElementTree as ET
import csv
import os

def parse_xml(input_file):
    # 生成输出文件名
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.csv"

    # 解析 XML 文件
    tree = ET.parse(input_file)
    root = tree.getroot()

    # 打开 CSV 文件以写入解析后的数据
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['setting', 'user', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # 遍历 XML 中的每个 <d> 元素
        for elem in root.findall('d'):
            p = elem.get('p')
            user = elem.get('user')
            content = elem.text

            # 写入 CSV 文件
            writer.writerow({'setting': p, 'user': user, 'content': content})

    print(f"数据已成功解析并写入到 {output_file} 文件中。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python parse_xml.py <输入文件>")
    else:
        input_file = sys.argv[1]
        if not os.path.exists(input_file):
            print("文件不存在。")
        else:
            parse_xml(input_file)