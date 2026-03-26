#Install library first (see requirements.txt)
from openai import OpenAI



def read_api_key(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

key = read_api_key("../files/openrouter.key")



#Init variables
prompt = "Is the concept Trapezoid, with parent Bone, equivalent to Trapezoid, with parent polygon? Reply only with Yes or No."
#prompt = "Is the concept Lymphokine equivalent to the concept Therapeutic Lymphokine? Reply only with Yes or No."
#prompt = "If something is a Therapeutic Lymphokine, is it also Lymphokine? Reply only with Yes or No."
#prompt = "If something is a Lymphokine, is it also a Therapeutic Lymphokine? Reply only with Yes or No."
web = "https://github.com/city-knowledge-graphs"
sitename = "City Knowledge Graphs"
llm = "qwen/qwen3-8b"


#Call the API
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key,
)
completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": web, # Optional. Site URL for rankings on openrouter.ai.
    "X-OpenRouter-Title": sitename, # Optional. Site title for rankings on openrouter.ai.
  },
  model=llm,
  messages=[
    {
      "role": "user",
      "content": prompt
    }
  ]
)

#Print results (it may take a few seconds)
print("LLM: " + llm)
print("Prompt: " + prompt)
print("Answer: " + str(completion.choices[0].message.content))

