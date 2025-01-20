import os
import glob
from PIL import Image
import concurrent.futures
import time

def convert_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'WEBP', lossless=True, quality=100, method=6)

def process_image(file_path):
    try:
        # 生成新的文件路径
        webp_path = os.path.splitext(file_path)[0] + '.webp'
        
        # 转换为WEBP
        convert_to_webp(file_path, webp_path)
        
        # 删除原始PNG文件
        os.remove(file_path)
        
        # 重命名WEBP文件为原始PNG文件名
        os.rename(webp_path, file_path)
        
        return f"成功处理: {file_path}"
    except Exception as e:
        return f"处理文件 {file_path} 时出错: {str(e)}"

def process_images(folder_path):
    png_files = glob.glob(os.path.join(folder_path, '**', '*.png'), recursive=True)
    total_files = len(png_files)

    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        future_to_file = {executor.submit(process_image, file_path): file_path for file_path in png_files}
        
        for index, future in enumerate(concurrent.futures.as_completed(future_to_file), 1):
            file_path = future_to_file[future]
            try:
                result = future.result()
                print(f"处理进度: {index}/{total_files} - {result}")
            except Exception as e:
                print(f"处理文件 {file_path} 时发生异常: {str(e)}")

    print("所有文件处理完成!")

# 使用示例
folder_to_process = '../build'  # 请替换为您要处理的文件夹路径
process_images(folder_to_process)
