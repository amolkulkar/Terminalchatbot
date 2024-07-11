import pandas as pd

# Load the dataset from the uploaded file
file_path = 'chatbot Data.csv' 
df = pd.read_csv(file_path)

# Set pandas options to display all rows
pd.set_option('display.max_rows', None)

# Display the entire DataFrame to ensure it's read correctly
print(df)

# Get the list of input and output columns dynamically
input_columns = [col for col in df.columns if col.startswith('Input')]
output_columns = [col for col in df.columns if col.startswith('Output')]

# Convert the dataframe to a list of dictionaries, only including pairs with both input and output
dataset = []
for index, row in df.iterrows():
    for input_col, output_col in zip(input_columns, output_columns):
        if pd.notna(row[input_col]) and pd.notna(row[output_col]):
            dataset.append({'input': str(row[input_col]), 'output': str(row[output_col])})

# Function to get the response
def get_response(user_input):
    for pair in dataset:
        if pair['input'].lower() == user_input.lower():
            return pair['output']
    return "I'm sorry, I don't understand that."

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot()
