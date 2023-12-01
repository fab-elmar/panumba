import os

import openai


def format_response(response):
    # Extract the integer and context from the response
    # 
    return formatted_response

def main():
    openai.api_key = os.environ.get('OPENAI_API_KEY')  # By account erstellung bekommt man 5 Dollar guthaben und kann einen Api key erstellen 

    while True:
        user_question = input("Enter your question (or 'q' to quit): ")

        if user_question.lower() == 'q':
            conn.close()
            break
        

   
        #structured_prompt = f"Please provide a concise answer to the following question. Start your response with a number that is directly related to or logically derived from the question. Follow the number with a brief explanation, no more than 75 words, on why this number was chosen or its relevance.\n\nQuestion: {user_question}\nAnswer:\nNumber: "
        structured_prompt = f" instructions: Provide an answer in two parts to the following question. Firstly, start your response with 'Number:', followed by an integer that is somehow logically associated with the question. This value must be of type integer, not a string. Then, after the integer, on a new line, start with 'ExNonation:', providing a brief explanation (No more than 75 Words!)of why you choose this number used to derive the number.  In the case of abstract questions, such as 'What color is the sky?', derive a number using a logical method of your choice based and explain this method in the context. Here is the question: {user_question}"
        
        # Send the combined prompt to the OpenAI API 
        response = openai.Completion.create(
            engine="curie",  # davinci, curie, babbage, ada, or any other engine, davinci is the most powerful
            prompt=structured_prompt,
            max_tokens=150  # Tokens are roughly equal to words, adjust as needed
        )


  
        print(response)
        
        

if __name__ == "__main__":
    main()
    
    
    