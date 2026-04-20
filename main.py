from prompt_config import system_prompt, get_context_prompt
def get_perfect_prompt(user_input):
    retrieved_context = get_context_prompt(user_input)

    full_prompt = f"""
    {system_prompt}

    ### NGỮ CẢNH TRI THỨC TRUY XUẤT ĐƯỢC:
    {retrieved_context}

    ### CÂU CẦN DỊCH:
    "{user_input}"
    """
    return full_prompt

if __name__ == "__main__":
    question = input("Nhập câu cần dịch: ")
    print(get_perfect_prompt(question))