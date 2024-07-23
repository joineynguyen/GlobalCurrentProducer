import opentracing

# Set your OpenAI API key
openai.api_ey = ''

def create_prompt(news_item):
    # Create a prompt for ChatGPT to generate a news anchor script
    return f"Create a world news anchor script for the following headline: '{news_item['title']}' with details from the URL: {news_item['url']}"

def generate_news_anchor_script(title, url):
        # Generate a prompt and get the response from ChatGPT
        prompt = create_prompt({'title': title, 'url': url})