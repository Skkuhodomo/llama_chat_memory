# Chat with memorable LLAMA (Local)
##### Memory-capable Ollama available for use  locally and on the web! 
## Sequence
<center>

![class-diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/Skkuhodomo/llama_chat_memory/main/diagram/sequence.puml) 
</center>

## Update Plan (with user authentication)
![class-diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/Skkuhodomo/llama_chat_memory/main/diagram/context.puml) 


## To Get Started 
### Install Ollama 
Download ollama (7b-chat)
https://ollama.com 

#### Start Ollama Server 
```
ollama serve 
```

#### Check Download
```
ollama run llama2:7b-chat
```

####  Download Source Code

```
git clone https://github.com/Skkuhodomo/llama_chat_memory
```
#### Install Libraries
```
pip install -t requirements.txt
```
#### Run 

```
streamlit run app.py
```

## Example 
<img src = "example.png"/>



