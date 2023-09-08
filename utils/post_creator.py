import requests
import json

def scanner(response_text):
  response_text = response_text.strip(" ").split('data: ')
  full_text = ""
  for single in response_text[1:-1]:
    single = json.loads(f"{single}") 
    if(single['choices'][0]['finish_reason']!='stop'):
      full_text += single['choices'][0]['delta']['content']
  return full_text


def gpt_gen(original_content):
  proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

  instructions = "I want you to act like human content / news writer. And our motive is readability, the readable Content, the more chance to get ranked. so please rewrite this article's paragraphs into an seo optimised and unique news article like human written news. and, totally plagiarism free. And most important that is, Make sure the topic is clear immediately or in starting, use passive voice in only 10% of contents. Most important, Make sure to shorten the sentences maximum sentence length will be 18 words, not more than. Use more and more Transition words like, so, and, but, etc. And make sure to use shorter and more familiar words to improve readability, this is too important part in SEO, so that can be easy to understand news content and more ease to read to my readers or audiance. Now rewrite this: "

  url = "https://api.openai.com/v1/chat/completions"
  headers = {"Content-type":"application/json" , "Authorization":"Bearer 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"}
  payload = {
      "model":"gpt-3.5-turbo",
      "messages":[{"role":"user","content":f"{instructions + original_content}"}],
  	"stream":True
    }

  res = requests.post(url,headers=headers,data=json.dumps(payload))

  final = scanner(res.text)

  return final

