from flask import Flask, jsonify, request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Set up OpenAI API key
load_dotenv()
openai_api_key = os.environ.get('OPENAI_API_KEY')


@app.route('/chat', methods=['GET'])
def chat():
    user_input = "tell me about the history of friday the 13th"

    # Get response from OpenAI's GPT-3
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can choose other engines if preferred
        messages=[
            {"role": "system", "content": "You are the MBTI personality INTP."},
            {"role": "user", "content": "Hi, what are your hobbies?"}],
        max_tokens=200,  # Limit the response length
        temperature=.7  # 0 (more deterministic) - 2 (more random)
    )

    chatbot_response = completion.choices[0].message
    print(chatbot_response)
    return jsonify(message=chatbot_response)


if __name__ == '__main__':
    app.run(debug=True)