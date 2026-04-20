import sys
import os
import time

# Tự động thêm thư mục gốc của dự án vào PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

from prompt_config import get_context_prompt, format_qwen_prompt
from scripts.rag_core.llm_engine_manual import LocalFileModelConnector

def run_full_flow_demo():
    # 1. Cấu hình đường dẫn mô hình
    model_path = os.path.join(project_root, "outputs", "completed_model_mlx")
    log_file = os.path.join(project_root, "demo_flow_log.md")
    
    print(f"=== ĐANG CHẠY FULL FLOW DEMO (LOG: {log_file}) ===")
    
    # 2. Khởi tạo Engine
    engine = LocalFileModelConnector(model_path=model_path)
    
    # 3. Input người dùng (Dài và chuyên môn cao)
    user_input = (
        "The patient presented with persistent vertigo and hearing loss. "
        "Upon examination, a diagnosis of Meniere's disease was suspected, "
        "and an intratympanic steroid injection was recommended to alleviate the symptoms."
    )
    
    # 4. Bước RAG
    print("-> Bước 1: Đang truy xuất ngữ cảnh (RAG)...")
    context = get_context_prompt(user_input, domain="medical")
    
    # 5. Bước Prompt
    print("-> Bước 2: Đang đóng gói Prompt...")
    full_prompt = format_qwen_prompt(user_input, context)
    
    # 6. Bước LLM
    print("-> Bước 3: Đang gửi tới mô hình MLX (5GB)...")
    start_time = time.time()
    translation = engine.generate(full_prompt)
    end_time = time.time()
    
    # 7. Xuất ra file log
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("# 📋 NHẬT KÝ LUỒNG DỊCH THUẬT RAG (FULL FLOW)\n\n")
        f.write(f"**Thời gian thực hiện**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Thời gian xử lý AI**: {end_time - start_time:.2f} giây\n\n")
        f.write("## 1. 📥 ĐẦU VÀO (USER INPUT)\n")
        f.write(f"```text\n{user_input}\n```\n\n")
        f.write("## 2. 🔍 NGỮ CẢNH TRUY XUẤT (RAG CONTEXT)\n")
        f.write(f"```text\n{context}\n```\n\n")
        f.write("## 3. 🧠 PROMPT CUỐI CÙNG (FINAL PROMPT TO AI)\n")
        f.write(f"```text\n{full_prompt}\n```\n\n")
        f.write("## 4. 📤 KẾT QUẢ ĐẦU RA (AI TRANSLATION)\n")
        f.write(f"**Dịch sang tiếng Việt**:\n\n")
        f.write(f"> {translation}\n")

    print(f"\n✅ ĐÃ XONG! Mời anh mở file '{log_file}' để xem chi tiết.")

if __name__ == "__main__":
    run_full_flow_demo()
