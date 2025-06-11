import requests
from mcp.server.fastmcp import FastMCP, Context

# Initialize the MCP server
mcp = FastMCP("DouYuSearcher", dependencies=["requests"])

# API endpoint for DouYu room information
ROOM_API= "http://open.douyucdn.cn/api/RoomApi/room/"

# API endpoint for DouYu search
SEARCH_API= "https://www.douyu.com/japi/search/api/getSearchRec"


@mcp.tool()
def get_room(room_id: int) -> str:
    """
    通过斗鱼房间的ID获取斗鱼房间信息。
    Get room information from DouYu by room ID.

    Args:
        room_id (int): 斗鱼房间ID。整数类型的ID被接受。
        room_id (int): The ID of the DouYu room. A numeric  ID is accepted. Like 71415.

    Returns:
        一个markdown表格，包含房间信息。
        a Markdown table containing room information.
        - 头像 URL 使用 image标签展示
        - 房间ID
        - 分区名
        - 房间名
        - 主播名
        - 房间状态（直播中 or 未开播）
        - 热度
        - 房间封面图 URL 图片 使用 image标签展示
    """
    room_id = str(room_id)
    url = f"{ROOM_API}{room_id}"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()["data"]
            # Remove unnecessary fields "gift"
            data["room_status"] = "直播中" if data["room_status"] == "1" else "未开播"
            del data["gift"]
            table = [
                "| 名称          | 信息             |",
                "|----------------|-------------------|",
                f"| 头像           | ![Avatar]({data['avatar']}) |",
                f"| 房间ID         | {data['room_id']}   |",
                f"| 分区名         | {data['cate_name']} |",
                f"| 房间名         | {data['room_name']} |",
                f"| 主播名         | {data['owner_name']} |",
                f"| 房间状态       | {data['room_status']} |",
                f"| 热度           | {data['hn']}         |",
                f"| 房间封面图     | ![Room Thumb]({data['room_thumb']}) |",
                f"| 房间链接       | [Link](https://www.douyu.com/{data['room_id']}) |"
            ]

            markdown_table = "\n".join(table)
            return markdown_table
        else:
            return "获取房间信息失败，API错误。"
    except requests.RequestException as e:
        return f"请求失败: {str(e)}"
    except Exception as e:
        # Handle unexpected errors and return an error message
        return f"发生意外错误: {str(e)}"

@mcp.tool()
def search_rooms(keyword: str) -> str:
    """
    通过关键字搜索斗鱼房间。
    Search for DouYu rooms by keyword.

    Args:
        keyword (str): 查询关键词。
        keyword (str): The search keyword.

    Returns:
        一个markdown表格，包含房间信息。
        a Markdown table containing room information.
        - 分区名
        - 是否直播（'直播中' or '未开播'）
        - 关键词
        - 主播昵称
        - 房间 ID
    """
    keyword = keyword.strip()
    if not keyword:
        return "请输入有效的关键词。"

    try:
        response = requests.get(SEARCH_API, params={"kw": keyword})
        if response.status_code == 200:
            data = response.json().get("data", [])
            if not data:
                return "没有找到相关房间。"
            first_room = data["roomResult"][0]
            table = [
                "| 名称          | 信息             |",
                "|----------------|-------------------|",
                f"| 分区名         | {first_room.get('cateName', '')} |",
                f"| 是否直播       | {'直播中' if first_room.get('isLive', 0) == 1 else '未开播'} |",
                f"| 关键词         | {first_room.get('kw', '')} |",
                f"| 主播昵称       | {first_room.get('nickName', '')} |",
                f"| 房间 ID       | {first_room.get('rid', 0)} |",
            ]

            return "\n".join(table)
        else:
            return "搜索失败，API错误。"
    except requests.RequestException as e:
        return f"请求失败: {str(e)}"
    except Exception as e:
        # Handle unexpected errors and return an error message
        return f"发生意外错误: {str(e)}"

# Start the server
if __name__ == "__main__":
    mcp.run()

