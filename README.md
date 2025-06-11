# DouYuSearcher MCP Server

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

一个轻量级的 MCP 服务器，支持通过斗鱼房间ID或关键词搜索获取斗鱼直播房间信息。

## 功能特性

- **房间信息查询**：通过 `get_room(room_id)` 工具，输入斗鱼房间ID，获取详细房间信息（包括头像、分区、主播、状态、热度等）。
- **关键词搜索房间**：通过 `search_rooms(keyword)` 工具，输入关键词，搜索相关斗鱼房间。
- **Markdown 表格输出**：所有信息均以美观的 Markdown 表格形式返回，支持图片展示。
![image](https://github.com/user-attachments/assets/f95d1a69-00b1-41ae-bf7d-f0012eb30fd4)

## 安装方法

### 前置条件
- Python 3.10+
- `pip`

### 安装步骤
1. 克隆本仓库：
   ```bash
   git clone https://github.com/LokerL/douyu-mcp-py.git
   cd douyu-mcp-py
   ```
2. 安装依赖：
   ```bash
   uv install
   ```

## 使用方法

### 运行和测试
- Windows下直接运行：
  ```bash
  ./inspector.cmd
  ```

### 工具说明

#### 工具：`get_room(room_id)`
根据斗鱼房间ID获取房间详细信息。
- **参数**：`room_id`（整数，斗鱼房间ID）
- **返回**：Markdown 表格，包含头像、房间ID、分区名、房间名、主播名、房间状态、热度、房间封面图、房间链接。
- **示例输出**：
  ```
  | 名称          | 信息             |
  |----------------|-------------------|
  | 头像           | ![Avatar](https://example.com/avatar.jpg) |
  | 房间ID         | 12345   |
  | 分区名         | 英雄联盟 |
  | 房间名         | 斗鱼最强 |
  | 主播名         | 张三 |
  | 房间状态       | 直播中 |
  | 热度           | 123456 |
  | 房间封面图     | ![Room Thumb](https://example.com/thumb.jpg) |
  | 房间链接       | [Link](https://www.douyu.com/71415) |
  ```

#### 工具：`search_rooms(keyword)`
通过关键词搜索斗鱼房间，返回第一个相关房间信息。
- **参数**：`keyword`（字符串，搜索关键词）
- **返回**：Markdown 表格，包含分区名、是否直播、关键词、主播昵称、房间ID。
- **示例输出**：
  ```
  | 名称          | 信息             |
  |----------------|-------------------|
  | 分区名         | 英雄联盟 |
  | 是否直播       | 直播中 |
  | 关键词         | 英雄联盟 |
  | 主播昵称       | 张三 |
  | 房间 ID       | 123456 |
  ```

## 许可证

MIT License. 详见 [LICENSE](LICENSE)。
