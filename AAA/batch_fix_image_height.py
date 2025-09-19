import os
import re
import glob

def fix_image_height_clamp():
    """批量修复HTML文件中图片高度clamp样式"""
    html_files = glob.glob(os.path.join('d:\\hca\\web-art\\AAA', '*.html'))
    
    # 定义替换规则
    replace_rules = [
        # 替换 h-[clamp(2rem,6vw,3rem)] 为 h-12 (48px)
        (r'h-\[clamp\(2rem,6vw,3rem\)\]', 'h-12'),
        # 替换 h-[clamp(2rem,5vw,3rem)] 为 h-10 (40px)
        (r'h-\[clamp\(2rem,5vw,3rem\)\]', 'h-10')
    ]
    
    modified_files = []
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 应用所有替换规则
            for pattern, replacement in replace_rules:
                content = re.sub(pattern, replacement, content)
            
            # 如果内容有变化，则写入文件
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_files.append(os.path.basename(file_path))
                print(f"已修改: {os.path.basename(file_path)}")
                
        except Exception as e:
            print(f"处理文件 {os.path.basename(file_path)} 时出错: {e}")
    
    print(f"\n总共修改了 {len(modified_files)} 个文件:")
    for file in modified_files:
        print(f"  - {file}")

if __name__ == "__main__":
    fix_image_height_clamp()