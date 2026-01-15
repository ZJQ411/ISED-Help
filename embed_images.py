#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 Markdown 文件中的图片引用转换为 Base64 编码的嵌入式图片
"""

import os
import base64
import re

def image_to_base64(image_path):
    """将图片文件转换为 Base64 编码"""
    try:
        with open(image_path, 'rb') as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
        return None

def get_image_mime_type(filename):
    """根据文件扩展名获取 MIME 类型"""
    ext = os.path.splitext(filename)[1].lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }
    return mime_types.get(ext, 'image/png')

def embed_images_in_markdown(md_file):
    """在 Markdown 文件中嵌入 Base64 编码的图片"""
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找所有图片引用 ![alt](filename.ext)
    image_pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        image_name = match.group(2)
        
        # 检查图片文件是否存在
        if not os.path.exists(image_name):
            print(f"Warning: Image not found: {image_name}")
            return match.group(0)  # 返回原始文本
        
        # 转换为 Base64
        base64_data = image_to_base64(image_name)
        if base64_data is None:
            return match.group(0)
        
        mime_type = get_image_mime_type(image_name)
        
        # 创建 Data URL
        data_url = f"data:{mime_type};base64,{base64_data}"
        
        print(f"Embedded: {image_name} ({len(base64_data)} bytes)")
        
        return f"![{alt_text}]({data_url})"
    
    # 替换所有图片引用
    new_content = re.sub(image_pattern, replace_image, content)
    
    # 保存新文件
    output_file = md_file.replace('.md', '_embedded.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\nSaved embedded version to: {output_file}")

if __name__ == '__main__':
    # 处理 Feishu Wiki 文件
    print("Processing ISED_Help_Feishu_Wiki.md...")
    embed_images_in_markdown('ISED_Help_Feishu_Wiki.md')
    
    print("\nProcessing Equipment_Tab_Chinese_Guide_with_Images.md...")
    embed_images_in_markdown('Equipment_Tab_Chinese_Guide_with_Images.md')
