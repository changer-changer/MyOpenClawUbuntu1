#!/usr/bin/env python3
"""
Mode-SI 封面生成器 v2.0 - 优化版（单图，等待多图skill更新）
优化点: 更大的标题、更强的视觉冲击、信息密度提升
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_si_cover_v2():
    # 画布尺寸 3:4
    WIDTH, HEIGHT = 1080, 1440
    
    # 颜色定义 - 档案感配色（优化对比度）
    BG_DARK = (15, 15, 20)         # 更深的背景
    TEXT_WHITE = (255, 255, 255)   # 纯白文字
    ACCENT_GREEN = (80, 220, 150)  # 更亮的绿色
    ACCENT_RED = (255, 100, 100)   # 更亮的红色
    ACCENT_ORANGE = (255, 160, 80) # 橙色强调
    GRAY_SUB = (140, 140, 150)     # 灰色次要文字
    
    # 创建画布
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # 尝试加载字体
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", 84)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", 42)
        body_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", 32)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Light.ttc", 26)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = body_font = small_font = title_font
    
    # ===== 顶部品牌标识 =====
    draw.text((60, 50), "SI", font=small_font, fill=GRAY_SUB)
    draw.text((110, 50), "超级个体进化室", font=small_font, fill=GRAY_SUB)
    
    # ===== 大年份标记（视觉锤） =====
    draw.text((60, 120), "2017", font=subtitle_font, fill=ACCENT_GREEN)
    draw.line([(60, 175), (180, 175)], fill=ACCENT_GREEN, width=3)
    draw.text((200, 135), "→ 2025", font=body_font, fill=GRAY_SUB)
    
    # ===== 主标题（更大字号） =====
    title_lines = ["王兴8年前的", "内部演讲，", "预判了互联网的", "全部未来"]
    y_pos = 220
    for line in title_lines:
        draw.text((60, y_pos), line, font=title_font, fill=TEXT_WHITE)
        y_pos += 100
    
    # ===== 分隔线 =====
    draw.line([(60, 640), (1020, 640)], fill=(50, 50, 60), width=2)
    
    # ===== 核心要点（更大的展示） =====
    key_points = [
        ("①", "互联网进入下半场", "增量→存量"),
        ("②", "从C端转向B端", "消费→产业"),
        ("③", "精细化运营是核心", "规模→效率"),
    ]
    
    y_pos = 680
    for num, title, desc in key_points:
        # 序号圆圈
        draw.ellipse([(60, y_pos), (110, y_pos+50)], fill=ACCENT_RED, outline=ACCENT_RED)
        draw.text((75, y_pos+8), num, font=body_font, fill=TEXT_WHITE)
        
        # 标题
        draw.text((130, y_pos+5), title, font=subtitle_font, fill=TEXT_WHITE)
        
        # 描述
        draw.text((130, y_pos+55), desc, font=body_font, fill=GRAY_SUB)
        
        y_pos += 120
    
    # ===== 验证框 =====
    verify_y = 1100
    draw.rectangle([(60, verify_y), (1020, verify_y+100)], fill=(30, 35, 40), outline=ACCENT_GREEN, width=2)
    draw.text((80, verify_y+20), "✓ 2017年没人信  →  2025年全应验", font=body_font, fill=ACCENT_GREEN)
    draw.text((80, verify_y+60), "真正的认知领先，是能看到8年后的局面", font=small_font, fill=GRAY_SUB)
    
    # ===== 底部引流 =====
    draw.line([(60, 1260), (1020, 1260)], fill=(50, 50, 60), width=1)
    draw.text((60, 1290), "评论区扣1领取王兴2017年演讲全文", font=subtitle_font, fill=ACCENT_ORANGE)
    
    # ===== 底部品牌 =====
    draw.text((60, 1380), "SI 超级个体进化室 | 每周更新个人成长的思考", font=small_font, fill=(80, 80, 90))
    
    # 保存
    output_path = "/home/cuizhixing/.openclaw/workspace/xhs-memory/mode-si/assets/cover_si_vol02.png"
    img.save(output_path, "PNG", quality=95)
    print(f"✅ Mode-SI Vol.02 封面已生成: {output_path}")
    return output_path

if __name__ == "__main__":
    create_si_cover_v2()
