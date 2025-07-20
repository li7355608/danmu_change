# bili录播姬弹幕格式转换工具（danmu_change）

本项目提供一个简单的工具，用于将录播姬的 XML 格式的弹幕文件转换为 CSV 格式，便于后续的数据处理和分析。

## 功能特性

- 将 XML 文件中的 `<d>` 标签解析为 CSV 文件
- 支持提取以下字段：
  - `setting`（对应 XML 中的 `p` 属性）
  - `user`（对应 XML 中的 `user` 属性）
  - `content`（对应 `<d>` 标签的文本内容）

## 使用方法

### 运行环境

- Python 3.x

### 依赖库

无需额外安装，标准库支持：
- `xml.etree.ElementTree`
- `csv`
- `os`
- `sys`

### 执行转换

```bash
python ChangeXmlToCsv.py input.xml
```

- `input.xml` 是你的弹幕 XML 文件。
- 转换后的 CSV 文件将保存在同一目录下，文件名为你的文件名，如 `input.csv`。

### 示例

输入 XML 内容示例：
```xml
<root>
    <d p="1" user="叔叔">你所热爱的就是你的生活</d>
    <d p="2" user="蒙古上单">你*什么时候*啊</d>
</root>
```

输出 CSV 文件内容：
```
setting,user,content
1,叔叔,你所热爱的就是你的生活
2,蒙古上单,你*什么时候*啊
```

## 项目结构

```
danmu_change/
├── ChangeXmlToCsv.py    # 转换脚本
├── change.bat           # 批处理脚本
└── README.md            # 项目说明

```

## 更新日志
- 1.0：初始版本发布
- 1.1：添加批处理脚本，开箱即用
  
## 注意事项
本工具目前**仅支持**转换**标准弹幕**数据，**不支持**舰长记录、礼物记录、SC留言。  
如需支持更多字段或格式转换，可继续扩展此工具。欢迎提交 issue 或 PR！