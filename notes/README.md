# Agents Course Notes

This document contains adapted and consolidated notes from the Hugging Face Agents course. It covers introductory concepts, model architectures, tool integration, and the cyclical nature of agent decision-making.

----

## Introduction

The [Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) explores how an Agent is a system that uses an AI Model (typically an LLM) as its core reasoning engine to:

- **Understand natural language:** Interpret and respond to human instructions in a meaningful way.
- **Reason and plan:** Analyze information, make decisions, and devise strategies to solve problems.
- **Interact with its environment:** Gather information, take actions, and observe the outcomes.

----

## Transformer Models Overview

### Encoders
- **Definition:** An encoder-based Transformer takes input text and converts it into dense representations (embeddings).
- **Example:** BERT from Google.
- **Use Cases:** Text classification, semantic search, Named Entity Recognition.
- **Typical Size:** Millions of parameters.

### Decoders
- **Definition:** A decoder-based Transformer generates new tokens one at a time to complete a sequence.
- **Example:** Llama from Meta.
- **Use Cases:** Text generation, chatbots, code generation.
- **Typical Size:** Billions of parameters.

### Seq2Seq (Encoder–Decoder)
- **Definition:** Combines an encoder to process input into context and a decoder to generate the output sequence.
- **Examples:** T5, BART.
- **Use Cases:** Translation, summarization, paraphrasing.
- **Typical Size:** Generally in the millions of parameters.

Tokenization converts text into tokens (often sub-word units), with models typically using a vocabulary of around 32,000 tokens.

----

## Agent Architectures and Prompts

LLMs work by predicting the next token based on a sequence of previous tokens. The input sequence is referred to as a _prompt_. Effective prompt design guides the model to produce desired outputs. Templates like ChatML structure conversations with clear role assignments (system, user, assistant), ensuring that instructions and tool descriptions are properly communicated.

----

## Tools and Their Integration

Tools extend an agent's capabilities. They include:

- A **textual description** of what the tool does.
- A **callable function** that performs the action.
- **Arguments** with defined names and types.
- An **output type**.

### Example: Tool Class

```python
class Tool:
    """A class representing a reusable piece of code (Tool)."""
    def __init__(self, name: str, description: str, func: callable, arguments: list, outputs: str):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        args_str = ", ".join([f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments])
        return f"Tool Name: {self.name}, Description: {self.description}, Arguments: {args_str}, Outputs: {self.outputs}"

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
```

A tool can be instantiated as:

```python
calculator_tool = Tool(
    "calculator",                   # name
    "Multiply two integers.",       # description
    calculator,                     # function to call
    [("a", "int"), ("b", "int")],   # inputs
    "int"                           # output type
)
```

Integrating tools allows agents to perform dynamic actions like calculations or data retrieval, transcending the model's static knowledge.

----

## Agent Decision Cycle

The agent operates in a cycle that typically includes:

1. **Thought:** The agent reasons about the task using available information, including the prompt and tool descriptions.
2. **Action:** It calls a tool to perform a specific operation.
3. **Observation:** It observes the output or result from the tool call and integrates this feedback back into its reasoning.

This cyclical process, often referred to as the **ReAct Cycle**, enables agents to iteratively refine their output and adapt based on real-time feedback.

----

## Additional Resources

- [Decoding Visualizer](https://agents-course-decoding-visualizer.hf.space)
- [Beam Search Visualizer](https://agents-course-beam-search-visualizer.hf.space)
- Hugging Face Agents course materials and documentation.

----

## Existing Structure and Guidelines

Refer to the rest of the `notes/` directory for:

- **General Concepts:** Core terminology and foundational ideas.
- **Best Practices:** Documented patterns and anti-patterns.
- **Troubleshooting:** Common issues and corresponding solutions.
- **Resources:** Useful links and references.
