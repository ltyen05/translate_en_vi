import sys
import os
import torch

# Tự động thêm thư mục gốc của dự án vào PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

from scripts.rag_core.llm_engine_manual import LocalFileModelConnector

def test_loading():
    print("=== KIỂM TRA NẠP MÔ HÌNH (MLX) ===")
    # Đường dẫn tương đối từ gốc dự án
    model_path = os.path.join(project_root, "outputs", "completed_model_mlx")
    
    if not os.path.exists(model_path):
        print(f"❌ Lỗi: Không tìm thấy thư mục model tại {model_path}")
        return

    try:
        # Khởi tạo engine
        engine = LocalFileModelConnector(model_path=model_path)
        
        if engine.model:
            print("✅ Thành công: Mô hình đã được nạp qua MLX.")
            test_prompt = "Translate to Vietnamese: Hello, how are you?"
            print(f"\nThử nghiệm generate ngắn: '{test_prompt}'")
            res = engine.generate(test_prompt)
            print(f"Kết quả: {res}")
        else:
            print("❌ Thất bại: engine.model is None.")
            
    except Exception as e:
        print(f"❌ Lỗi nghiêm trọng: {e}")

if __name__ == "__main__":
    test_loading()
