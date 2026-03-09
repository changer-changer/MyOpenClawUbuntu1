#!/usr/bin/env python3
"""
Mode-SI 封面合成器 - 将即梦图片拼到封面中
保持标题大字模式 + 图片元素融合
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_composite_cover():
    # 画布尺寸 3:4
    WIDTH, HEIGHT = 1080, 1440
    
    # 颜色定义
    BG_DARK = (15, 15, 20)
    TEXT_WHITE = (255, 255, 255)
    ACCENT_GREEN = (80, 220, 150)
    ACCENT_ORANGE = (255, 160, 80)
    GRAY_SUB = (140, 140, 150)
    
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # 加载字体
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", 40)
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", 28)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Light.ttc", 24)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = body_font = small_font = title_font
    
    # 尝试加载即梦生成的图片作为背景元素
    jimeng_path = "/home/cuizhixing/.openclaw/workspace/xhs-memory/mode-si/assets/jimeng/0_detail_jimeng-2026-03-07-7476-2004年，一位年轻的亚洲男性身着毕业礼服站在大学校门口，面前有两条路：一条通向....png"
    
    if os.path.exists(jimeng_path):
        # 加载即梦图片并调整大小作为背景元素
        jimeng_img = Image.open(jimeng_path)
        # 缩放并裁剪为适合的大小（右侧或下方展示）
        jimeng_img = jimeng_img.resize((600, 800), Image.Resampling.LANCZOS)
        # 创建半透明遮罩
        jimeng_img = jimeng_img.convert("RGBA")
        # 粘贴到右下角
        img.paste(jimeng_img, (480, 640), jimeng_img)
    
    # 顶部品牌标识
    draw.text((60, 50), "SI", font=small_font, fill=GRAY_SUB)
    draw.text((110, 50), "超级个体进化室", font=small_font, fill=GRAY_SUB)
    
    # 年份标记
    draw.text((60, 120), "2004 → 2024", font=subtitle_font, fill=ACCENT_GREEN)
    draw.line([(60, 175), (280, 175)], fill=ACCENT_GREEN, width=3)
    
    # 主标题（大字）
    draw.text((60, 220), "黄峥毕业时", font=title_font, fill=TEXT_WHITE)
    draw.text((60, 320), "的3个选择", font=title_font, fill=TEXT_WHITE)
    
    # 副标题
    draw.text((60, 440), "决定了拼多多今天的样子", font=subtitle_font, fill=ACCENT_ORANGE)
    
    # 分隔线
    draw.line([(60, 520), (600, 520)], fill=(50, 50, 60), width=2)
    
    # 核心要点（左侧文字区）
    points = [
        ("①", "去微软还是创业？"),
        ("②", "卖公司还是继续？"),
        ("③", "做游戏还是电商？"),
    ]
    
    y_pos = 560
    for num, text in points:
        draw.ellipse([(60, y_pos), (110, y_pos+50)], fill=ACCENT_ORANGE)
        draw.text((75, y_pos+8), num, font=body_font, fill=TEXT_WHITE)
        draw.text((130, y_pos+12), text, font=subtitle_font, fill=TEXT_WHITE)
        y_pos += 70
    
    # 底部引流
    draw.line([(60, 1280), (1020, 1280)], fill=(50, 50, 60), width=1)
    draw.text((60, 1310), "评论区扣1领取黄峥完整编年史", font=subtitle_font, fill=ACCENT_GREEN)
    
    # 保存
    output_path = "/home/cuizhixing/.openclaw/workspace/xhs-memory/mode-si/assets/cover_composite_vol03.png"
    img.save(output_path, "PNG", quality=95)
    print(f"✅ 合成封面已生成: {output_path}")
    return output_path

if __name__ == "__main__":
    create_composite_cover()
