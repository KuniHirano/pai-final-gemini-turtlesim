import os
import subprocess
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

with open("prompt_en.txt", "r", encoding="utf-8") as f:
    pre_prompt = f.read()

def get_chat_response(prompt):
    res = client.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages=[{"role": "user", "content": prompt}],
    )
    return res.choices[0].message.content.strip()

def generate_python_script(code):
    # Remove ``` fences if the model added them
    if code.startswith("```"):
        code = code.split("\n", 1)[1].rsplit("```", 1)[0]
    with open("generated_script.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("=== Generated code ===\n" + code)

def run_python_script():
    try:
        result = subprocess.run(["python3", "generated_script.py"],
                                capture_output=True, text=True, timeout=60)
        print("=== stdout ===\n" + result.stdout)
        print("=== stderr ===\n" + result.stderr)
    except subprocess.TimeoutExpired:
        print("Timed out (60s). The generated script did not finish.")

if __name__ == "__main__":
    prompt = pre_prompt + input("Enter instruction: ")
    res = get_chat_response(prompt)
    generate_python_script(res)
    run_python_script()
