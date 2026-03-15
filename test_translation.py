from prompt_config import get_context_prompt
import google.generativeai as genai
import os
from prompt_config import system_prompt

genai.configure(api_key="AIzaSyDyNfgA0Iz3J41wSQuNI-M3Z4J50HglruY")
model = genai.GenerativeModel(model_name="gemini-2.5-flash", 
                              system_instruction=system_prompt)

def translate(text):
    print(f"\n--- DỊCH CÂU: '{text}' ---")
    context = get_context_prompt(text)
    print("\n[CONTEXT ĐƯỢC TẠO RA]:")
    print(context)
    
    prompt = f"{context}\n\n[CÂU CẦN DỊCH]\n{text}"
    response = model.generate_content(prompt)
    
    print("\n[KẾT QUẢ TỪ GEMINI]:")
    print(response.text)
    print("-" * 50)

if __name__ == "__main__":
    # Test 1: Câu có chứa thuật ngữ công nghệ Microsoft (ví dụ: "active directory lightweight directory services")
    translate("Deploying active directory lightweight directory services can be challenging.")
    
    # Test 2: Câu có chứa thuật ngữ cũ của chúng ta (ví dụ: "spring boot")
    translate("We are building our new backend using spring boot and dependency injection.")
    
    # Test 3: Câu có chứa thuật ngữ phổ biến từ Microsoft (ví dụ: "word processing" hoặc "business software")
    translate("This server is used for word processing and business software.")
