import openai


def  open_file(filepath):
     with open(filepath,'r', encoding='utf-8') as infile:
         return infile.read()
            



    
openai.api_key= open_file('apikey.txt')     

def gpt3_completion (prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=500,freq_pen=0, pres_pen=0, stop=['JAX:', 'USER:']):
    

     prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()

     response = openai.Completion.create(
            engine=engine, 
            prompt=prompt,
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen,
            stop=stop)
     text = response['choices'][0]['text'].strip()
     return text

 
if __name__ == '__main__' :
  conversation = list()
  print("I am your career counselor who will help you think through on the possible career path")
  while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('chat.txt').replace('<<BLOCK>>', text_block)
        
        prompt = prompt + '\nJAX:'
        response = gpt3_completion(prompt)
        print('JAX:', response)
        conversation.append('JAX: %s' % response)
     #    print('....',text_block,'.....')
      

     


