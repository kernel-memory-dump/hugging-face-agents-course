# Example Special Tokens Explanation

This file explains the behavior observed when using special tokens in the prompt for the Llama-3.2-3B-Instruct model.

## Code Example

The code in `example_special_tokens.py` uses the following prompt:

```
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
The capital of France is<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

This prompt includes special tokens:
- `<|begin_of_text|>` indicates the start of the input text.
- `<|start_header_id|>` and `<|end_header_id|>` separate headers for user and assistant roles.
- `<|eot_id|>` signals the end of the user's text.

## Expected Behavior and Output

When running the example:

- The client sends the prompt to the model with these special tokens.
- The model recognizes the structure and produces an output that marks the transition from the user's message to the assistant's response.
- As a result, the generated text is more controlled and is expected to include the end-of-sequence (EOS) marker at the appropriate point.

In our run, the output was concise (e.g., it returned "...Paris!"), demonstrating that the model correctly used the input structure to generate a focused answer. This contrasts with the earlier example (without special tokens), which produced multiple capitals. 

Using special tokens can be useful to direct the model's behavior, ensuring it terminates the sequence as expected and adheres to the desired conversational format. 