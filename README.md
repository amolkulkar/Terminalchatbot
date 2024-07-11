# Chatbot Project

This project contains a simple chatbot that responds to user inputs based on a given dataset. The chatbot is implemented in Python and runs in the terminal.

## Project Files

- `chatbot.py`: The main script to run the chatbot.
- `chatbot Data.csv`: The dataset containing input-output pairs.

## Prerequisites

- Python 3.x
- pandas library

## Installation

1. **Download the Project Files**

    Download or clone the repository containing the CSV files.

2. **Install Python**

    Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Install Required Libraries**

    Open a terminal or command prompt and run:
    ```bash
    pip install pandas
    ```

## Usage

1. **Place Files in the Same Directory**

    Ensure `chatbot.py` and `chatbot Data.csv` are in the same directory.

2. **Run the Chatbot Script**

    Open a terminal or command prompt, navigate to the directory, and run:
    ```bash
    python chatbot.py
    ```

3. **Interact with the Chatbot**

    The chatbot will start and prompt you for input. Type your messages and press Enter to get a response. Type `exit` to end the conversation.

## Dataset Format

The dataset (`chatbot Data.csv`) should have columns starting with `Input` and `Output`. The chatbot will match user inputs with the corresponding outputs.

## Example Interaction

Chatbot: Hello! Type 'exit' to end the conversation.
You: 1960
Chatbot: Response for input 1960
You: exit
Chatbot: Goodbye!

## Troubleshooting

- Ensure `chatbot Data.csv` is in the same directory as `chatbot.py`.
- Verify the dataset columns start with `Input` and `Output`.


