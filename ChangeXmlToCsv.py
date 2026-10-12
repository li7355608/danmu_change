import argparse
import csv
import os
import sys
import xml.etree.ElementTree as ET

P_FIELDNAMES = ['time', 'mode', 'fontsize', 'color', 'send_ts', 'pool', 'uid', 'dbid']
CSV_FIELDNAMES = P_FIELDNAMES + ['user', 'content']


def parse_p(p_value):
    row = dict.fromkeys(P_FIELDNAMES, '')
    if p_value:
        for key, value in zip(P_FIELDNAMES, p_value.split(',')):
            row[key] = value
    return row


def convert_xml_to_csv(input_file, output_file):
    count = 0
    stack = []
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        for event, elem in ET.iterparse(input_file, events=('start', 'end')):
            if event == 'start':
                stack.append(elem)
                continue
            stack.pop()
            if len(stack) != 1 or elem.tag != 'd':
                continue
            row = parse_p(elem.get('p'))
            row['user'] = elem.get('user') or ''
            row['content'] = elem.text or ''
            writer.writerow(row)
            count += 1
            elem.clear()
            stack[0].remove(elem)
    return count


def build_output_path(input_file, output_override):
    if output_override:
        return output_override
    return os.path.splitext(input_file)[0] + '.csv'


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='将B站录播姬弹幕XML文件转换为CSV格式')
    parser.add_argument('files', nargs='+', help='待转换的弹幕XML文件路径（支持多个）')
    parser.add_argument('-o', '--output',
                        help='输出CSV文件路径（仅转换单个文件时有效）')
    args = parser.parse_args(argv)

    if args.output and len(args.files) > 1:
        parser.error('-o/--output 仅在转换单个文件时可用')

    failed = 0
    for input_file in args.files:
        if not os.path.exists(input_file):
            print(f'文件不存在: {input_file}', file=sys.stderr)
            failed += 1
            continue
        try:
            output_file = build_output_path(input_file, args.output)
            count = convert_xml_to_csv(input_file, output_file)
        except ET.ParseError as exc:
            print(f'XML解析失败 ({input_file}): {exc}', file=sys.stderr)
            failed += 1
            continue
        except OSError as exc:
            print(f'文件读写失败 ({input_file}): {exc}', file=sys.stderr)
            failed += 1
            continue
        print(f'{input_file}: 转换 {count} 条弹幕，已写入 {output_file}')

    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
