#!/usr/bin/env python3
"""
Mode-SI 封面生成器 - 档案感/知识密度风格
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_si_cover():
    # 画布尺寸 3:4
    WIDTH, HEIGHT = 1080, 1440
    
    # 颜色定义 - 档案感配色
    BG_DARK = (18, 18, 22)        # 深灰黑背景
    TEXT_WHITE = (245, 245, 245)   # 米白文字
    ACCENT_GREEN = (100, 200, 150) # 绿色日期标记
    ACCENT_RED = (220, 100, 100)   # 红色重点
    ACCENT_ORANGE = (230, 150, 80) # 橙色强调
    GRAY_SUB = (120, 120, 130)     # 灰色次要文字
    
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # 尝试加载字体
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", 72)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", 36)
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Light.ttc", 28)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Thin.ttc", 24)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = body_font = small_font = title_font
    
    # ===== 顶部品牌标识 =====
    draw.text((60, 60), "SI", font=small_font, fill=GRAY_SUB)
    draw.text((100, 60), "超级个体进化室", font=small_font, fill=GRAY_SUB)
    
    # ===== 日期标记（绿色） =====
    draw.text((60, 140), "2005-2009", font=body_font, fill=ACCENT_GREEN)
    draw.line([(60, 185), (200, 185)], fill=ACCENT_GREEN, width=2)
    
    # ===== 主标题 =====
    title_lines = ["看张一鸣2005年的博客，", "他刚毕业就已经开悟"]
    y_pos = 240
    for line in title_lines:
        draw.text((60, y_pos), line, font=title_font, fill=TEXT_WHITE)
        y_pos += 90
    
    # ===== 分隔线 =====
    draw.line([(60, 450), (1020, 450)], fill=(60, 60, 70), width=1)
    
    # ===== 核心要点（红色标注） =====
    key_points = [
        ("① 延迟满足感", "不轻易满足，持续追求更好"),
        ("② 主动学习，不设边界", "持续编程到深夜，学分布式系统"),
        ("③ 对信息的敏感度", "信息流动比信息本身更重要"),
    ]
    
    y_pos = 500
    for title, desc in key_points:
        # 序号和标题 - 红色
        draw.text((60, y_pos), title, font=subtitle_font, fill=ACCENT_RED)
        y_pos += 50
        # 描述 - 灰色
        draw.text((60, y_pos), desc, font=body_font, fill=GRAY_SUB)
        y_pos += 80
    
    # ===== 金句框 =====
    quote_y = 850
    # 框背景
    draw.rectangle([(60, quote_y), (1020, quote_y + 140)], fill=(30, 30, 35), outline=(60, 60, 70), width=1)
    # 引用内容
    draw.text((80, quote_y + 20), '"如果一样东西你得到以后依然爱不释手，', font=body_font, fill=TEXT_WHITE)
    draw.text((80, quote_y + 60), '这才是你真正想要的。"', font=body_font, fill=TEXT_WHITE)
    draw.text((80, quote_y + 100), "—— 张一鸣，2006年", font=small_font, fill=ACCENT_ORANGE)
    
    # ===== 底部引流 =====
    draw.line([(60, 1200), (1020, 1200)], fill=(60, 60, 70), width=1)
    draw.text((60, 1230), "翻遍200+篇博客，发现字节崛起的全部密码", font=body_font, fill=GRAY_SUB)
    draw.text((60, 1280), "评论区扣1领取张一鸣博客合集", font=subtitle_font, fill=ACCENT_GREEN)
    
    # ===== 底部品牌 =====
    draw.text((60, 1380), "SI 超级个体进化室 | 每周更新个人成长的思考", font=small_font, fill=(80, 80, 90))
    
    # 保存
    output_path = "/home/cuizhixing/.openclaw/workspace/xhs-memory/mode-si/assets/cover_si_vol01.png"
    img.save(output_path, "PNG", quality=95)
    print(f"✅ Mode-SI 封面已生成: {output_path}")
    return output_path

if __name__ == "__main__":
    create_si_cover()
