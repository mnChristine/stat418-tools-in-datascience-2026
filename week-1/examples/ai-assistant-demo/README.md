# AI Assistant Demo - Using Claude Code (Cline) with OpenRouter

This example demonstrates how to effectively use Claude Code (Cline extension) with OpenRouter in your workflow.

## What You'll Learn

- How to ask effective questions
- Code generation with AI
- Code explanation and documentation
- Debugging with AI assistance
- Best practices for AI-assisted coding

## Prerequisites

- VSCode installed
- Cline extension installed
- OpenRouter API key configured (see STUDENT_SETUP.md)

## Example Tasks

### 1. Code Generation

**Prompt**: "Write a Python function that calculates the factorial of a number"

**What to expect**: Cline will generate a function with proper error handling.

**Try it**:
1. Create a new file: `factorial.py`
2. Open Cline panel (click robot icon in sidebar)
3. Type the prompt above
4. Review the generated code
5. Ask follow-up: "Add type hints and docstring"

### 2. Code Explanation

**Prompt**: "Explain what this code does line by line"

**Use case**: Understanding unfamiliar code

**Try it**:
1. Open `analyze_data.py` from the python-setup example
2. Select a block of code
3. In Cline chat: "Explain the selected code"
4. Or use Cmd/Ctrl+L to add code to context, then ask

### 3. Adding Documentation

**Prompt**: "Add a comprehensive docstring to this function"

**Try it**:
1. Write a simple function:
```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```
2. Select the function (Cmd/Ctrl+L to add to Cline)
3. Ask Cline to add documentation
4. Review and edit the generated docstring

### 4. Debugging Help

**Prompt**: "Why is this code giving me an error? [paste error message]"

**Try it**:
1. Create code with an intentional error:
```python
def divide(a, b):
    return a / b

result = divide(10, 0)
```
2. Run it and copy the error
3. Ask Cline: "I'm getting this error: [paste error]. How do I fix it?"

### 5. Code Refactoring

**Prompt**: "Refactor this code to be more efficient and readable"

**Try it**:
1. Write inefficient code:
```python
numbers = [1, 2, 3, 4, 5]
result = []
for i in range(len(numbers)):
    result.append(numbers[i] * 2)
```
2. Ask Cline to refactor it
3. Compare the suggestions

### 6. Test Generation

**Prompt**: "Write unit tests for this function"

**Try it**:
1. Write a function:
```python
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
```
2. Ask Cline to generate tests
3. Review the test cases

## Effective Prompting Tips

### Be Specific

**Bad**: "Write code"
**Good**: "Write a Python function that reads a CSV file and returns a pandas DataFrame"

### Provide Context

**Bad**: "Fix this"
**Good**: "This function should validate email addresses, but it's not catching invalid formats. Here's the code: [paste code]"

### Iterate

1. Start with a basic request
2. Review the output
3. Ask for improvements or modifications
4. Repeat until satisfied

### Ask for Explanations

- "Explain why you chose this approach"
- "What are the trade-offs of this solution?"
- "Are there alternative ways to do this?"

## Example Workflow

Let's build a simple data processor:

### Step 1: Initial Request

**Prompt**: "Create a Python script that reads a CSV file with columns 'name', 'age', 'score' and calculates the average score"

### Step 2: Add Error Handling

**Prompt**: "Add error handling for missing files and invalid data"

### Step 3: Add Features

**Prompt**: "Add a function to find the top 3 performers"

### Step 4: Add Documentation

**Prompt**: "Add docstrings and type hints to all functions"

### Step 5: Add Tests

**Prompt**: "Create unit tests for these functions"

## What AI Can Help With

**Good use cases**:
- Boilerplate code generation
- Writing documentation
- Explaining unfamiliar code
- Suggesting improvements
- Finding bugs
- Writing tests
- Converting between formats
- Learning new libraries

**Not recommended**:
- Copying code without understanding
- Skipping learning fundamentals
- Trusting output without review
- Complex architectural decisions
- Security-critical code without verification

## Best Practices

### 1. Always Review Generated Code

- Don't blindly accept AI suggestions
- Understand what the code does
- Test thoroughly
- Check for edge cases

### 2. Use AI as a Learning Tool

- Ask "why" questions
- Request explanations
- Compare different approaches
- Learn from the patterns

### 3. Maintain Code Quality

- Follow project style guidelines
- Add your own comments
- Refactor as needed
- Write your own tests

### 4. Be Aware of Limitations

- AI can make mistakes
- May suggest outdated approaches
- Doesn't understand your full context
- Can't replace critical thinking

## Cline-Specific Features

### Adding Files to Context

- Use Cmd/Ctrl+L to add current file
- Use @ symbol to reference files: `@filename.py`
- Add multiple files for better context

### Using Tools

Cline can:
- Read and write files
- Execute commands
- Search your codebase
- List directory contents

### Model Selection

In Cline settings, you can choose different models:
- **anthropic/claude-3.5-sonnet** (recommended, most capable)
- **google/gemini-2.0-flash-exp:free** (fast, completely free)
- **meta-llama/llama-3.2-3b-instruct:free** (smaller, free)

Free models are sufficient for most tasks in this course.

## Practice Exercises

### Exercise 1: Data Validator

Ask Cline to help you create a function that validates:
- Email addresses
- Phone numbers
- Dates in YYYY-MM-DD format

### Exercise 2: File Processor

Build a script that:
1. Reads multiple CSV files from a directory
2. Combines them into one DataFrame
3. Removes duplicates
4. Exports to a new CSV

Use Cline to help with each step.

### Exercise 3: Error Handler

Create a robust function with:
- Try-except blocks
- Logging
- Custom error messages
- Input validation

Ask Cline for best practices.

## Common Issues

**Problem**: Cline not responding
- Check internet connection
- Verify OpenRouter API key in settings
- Check Cline output panel for errors
- Restart VSCode

**Problem**: "API key invalid" error
- Verify you copied the full API key from OpenRouter
- Make sure you selected "OpenRouter" as the provider
- Try generating a new key at openrouter.ai

**Problem**: Responses are too generic
- Be more specific in your prompts
- Provide more context
- Show example input/output
- Iterate with follow-up questions

**Problem**: Code doesn't work as expected
- Review the code carefully
- Test with different inputs
- Ask Cline to explain the logic
- Debug step by step

**Problem**: Rate limits
- OpenRouter free tier has generous limits
- If you hit limits, wait a moment
- Consider using a free model (`:free` suffix)
- Check your OpenRouter dashboard

## OpenRouter Benefits

- **Multiple Models**: Access Claude, GPT, Gemini, and more
- **Free Tier**: Generous free credits for new users
- **Free Models**: Several models with `:free` suffix
- **No Vendor Lock-in**: Switch models easily
- **Cost Tracking**: Dashboard shows usage

## Next Steps

- Practice with the exercises above
- Use Cline in your homework assignments
- Experiment with different prompting styles
- Try different models to see what works best
- Share useful prompts with classmates
- Learn when to use AI vs. when to code from scratch

## Resources

- [Cline Documentation](https://github.com/cline/cline)
- [OpenRouter](https://openrouter.ai/)
- [OpenRouter Models](https://openrouter.ai/models)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)