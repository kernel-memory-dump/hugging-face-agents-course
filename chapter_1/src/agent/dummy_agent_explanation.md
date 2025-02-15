# Dummy Agent Explanation and Code Flow

## Overview

This document explains the dummy agent examples which simulate a basic agent behavior using two approaches:

- **Text Generation Approach (dummy_agent_text.py):** A complete prompt is constructed by combining a complex system prompt with a user query. This prompt is then processed using the text generation method.
- **Chat Approach (dummy_agent_chat.py):** A list of messages is constructed (with system and user roles) to simulate a conversation. This message list is processed using the chat completions method.

Both examples use a system prompt that instructs the model about tool usage (e.g., get_weather), and outline the chain-of-thought reasoning process. The response ultimately simulates the agent's reasoning process.

## Code Explanation

### Dummy Agent - Text Generation

- **Environment Loading:** The script loads environment variables using `python-dotenv`.
- **Token Check:** The Hugging Face token (HF_TOKEN) is retrieved from the .env file; if missing, an error is raised.
- **Client Initialization:** An `InferenceClient` is created using the token.
- **System Prompt Definition:** A detailed system prompt is defined that explains how to use tools such as `get_weather`.
- **Prompt Construction:** A prompt is constructed that includes the system prompt, special tokens (e.g., `<|begin_of_text|>`), and the user question.
- **Text Generation Call:** The `client.text_generation()` method is called with the constructed prompt and a maximum token limit.
- **Output:** The model's generated response is printed.

### Dummy Agent - Chat Method

- **Environment Setup:** The script loads environment variables and checks the token.
- **Client Initialization:** The same `InferenceClient` is used.
- **System Prompt Definition:** A detailed system prompt is set up with instructions on tool usage.
- **Message List Construction:** A list of messages is constructed, including a system message (with detailed instructions) and a user message asking "What's the weather in London ?".
- **Chat Completions Call:** The `client.chat.completions.create()` method is called with these messages.
- **Output:** The assistant's message from the response is printed.

## Mermaid Flow Chart

```mermaid
flowchart TD
    A[Start] --> B[Load Environment Variables]
    B --> C[Check HF_TOKEN]
    C -- Missing --> D[Raise Error]
    C -- Valid --> E[Initialize InferenceClient]
    E --> F[Define SYSTEM_PROMPT with tool instructions]
    F --> G[Construct Prompt (Text Variant) or Messages (Chat Variant)]
    G --> H[Call text_generation (for text) / chat.completions.create (for chat)]
    H --> I[Receive Output]
    I --> J[Print Output]
    J --> K[End]
```

## Output Explanation

For the **Text Generation** approach:
- The combined prompt including system instructions and the query is processed.
- The output is a generated text response that follows the system instructions on tool usage. The response may include a structured chain-of-thought and a final answer.

For the **Chat** approach:
- The conversation style (with system and user roles) is processed.
- The output is the assistant's message, which is a concise and targeted response following the provided instructions.

This dummy agent setup demonstrates how complex system prompts and role-based messages can be used to direct the behavior of language models in a tool-assisted agent scenario. 