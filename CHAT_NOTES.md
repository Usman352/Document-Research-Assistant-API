# Personal Document Research Assistant API - Key Notes

## Project Setup
- Use FastAPI for the backend, with organized structure: `main.py`, `utils/`, `models/`.
- Use `requirements.txt` for dependencies and `.env` for secrets (like your OpenAI API key).
- Use a virtual environment (`venv`) to isolate dependencies.

## OpenAI API Usage
- Use your own, private OpenAI API key. Never use public/shared keys for production.
- The main Python SDK interface is `client = OpenAI(api_key=...)`.
- To get a model response:
  ```python
  completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": "Your prompt here"}]
  )
  print(completion.choices[0].message.content)
  ```
- `messages` is a list of dicts with `role` (`system`, `user`, `assistant`, `tool`) and `content`.
- Use `system` to set assistant behavior, `user` for user input, `assistant` for previous model replies.

## Cost Management
- GPT-3.5 Turbo is the cheapest paid model; `gpt-4o-mini` and similar are free/very cheap with data sharing enabled.
- Free quota is available if you enable sharing with OpenAI (see dashboard for limits).
- Always set strict free tier limits if exposing your API to users to avoid unexpected costs.

## Privacy & Data Sharing
- Enabling data sharing with OpenAI gives you a large free quota, but your users' data will be used to improve models.
- For privacy-sensitive or production APIs, disable sharing and pay for usage.
- `store=True` in API calls allows OpenAI to store your data for their use, but you cannot access stored conversations via the API.
- If you want to keep logs, implement your own logging in your code.

## Model Selection
- Cheapest: `gpt-4o-mini`, `gpt-4.1-mini`, `gpt-3.5-turbo` (see OpenAI pricing page for updates).
- Use `gpt-3.5-turbo` for most tasks; use `gpt-4o` or `gpt-4` for higher quality (higher cost).

## Prompt Engineering Tips
- For summarization, use longer input for better results.
- Specify the format: e.g., "Summarize in one sentence" or "Give 3 bullet points".
- For short input, the model may just paraphrase instead of summarizing.
- Use the `stop` parameter to control where the model stops generating output (e.g., `stop=["\nUser:"]`).

## Key Code Patterns
- To summarize text:
  ```python
  {"role": "user", "content": f"Summarize this text: {your_text}"}
  ```
- To access just the model's reply:
  ```python
  print(completion.choices[0].message.content)
  ```
- To log input/output yourself:
  ```python
  with open("chat_log.txt", "a") as f:
      f.write(f"User: {user_input}\nAssistant: {model_output}\n\n")
  ```

## Troubleshooting
- If you get `ModuleNotFoundError: No module named 'openai'`, make sure your virtual environment is activated and `openai` is installed in it.
- If you get quota errors, check your OpenAI dashboard for free credits or add billing.
- PowerShell's `curl` is not the same as Unix `curl`; use Python SDK for API calls on Windows.

## Additional Key Learnings (Appended)

### OpenAI Message Roles
- `system`: Sets assistant behavior/context (e.g., "You are a helpful assistant.")
- `user`: Represents the end user's input.
- `assistant`: Represents the model's previous replies (for multi-turn context).
- `tool` (or `function`): Used for advanced function/tool calling (rarely needed for basic use).

### `store=True` in API Calls
- `store=True` allows OpenAI to store your conversation for their own analytics/model improvement.
- **You cannot access stored conversations via the API.** If you want to keep logs, implement your own logging in your code.

### Accessing and Logging Data
- To retain your own chat history, log both input and output in your code (e.g., write to a file or database).

### Advanced `client.chat.completions` Methods
- `.create(...)`: Main method to get a model response.
- `.stream(...)`: Get streaming responses for real-time output.
- `.retrieve(...)`: Fetch a completion by ID (if available).
- `.list(...)`, `.delete(...)`, `.update(...)`: Manage completions (rarely used in most workflows).
- `.with_raw_response`, `.with_streaming_response`: For advanced/raw HTTP response handling.

### `messages` Structure
- `messages` is a list of dicts, each with a `role` and `content`.
- Example:
  ```python
  messages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Summarize this text: ..."},
      {"role": "assistant", "content": "Summary here."}
  ]
  ```

### Summarization Behavior
- For very short input, the model may paraphrase instead of summarizing.
- For best results, use longer input and specify the summary format (e.g., "in one sentence" or "as bullet points").

### `stop` Parameter
- Use `stop=["\nUser:"]` or similar to control where the model stops generating output, especially in chat-like scenarios.

---
**Retain this file for quick reference as you build and deploy your API!** 