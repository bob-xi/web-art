import os
import re

def batch_fix_fontsize():
    # 获取当前目录下所有HTML文件
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # 要查找和替换的模式
    pattern = r'text-\[clamp\(1\.5rem,4vw,2\.5rem\)\]'
    replacement = 'text-2xl'
    
    modified_files = []
    
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查文件是否包含需要替换的模式
            if re.search(pattern, content):
                # 执行替换
                new_content = re.sub(pattern, replacement, content)
                
                # 写回文件
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                modified_files.append(file)
                print(f"✓ 已修改: {file}")
            
        except Exception as e:
            print(f"✗ 处理文件 {file} 时出错: {e}")
    
    print(f"\n总共修改了 {len(modified_files)} 个文件:")
    for file in modified_files:
        print(f"  - {file}")

if __name__ == "__main__":
    batch_fix_fontsize()