from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain_ollama.llms import OllamaLLM

def generate(caption):
    llm = OllamaLLM(model='llama3.1', temperature=1)

    caption_template = PromptTemplate(
        input_variables = ['caption'],
        template = "I want to post on instagram and for that I need a caption of 250-300 characters. It could also involve emojis. The theme of the caption should be about {caption}."
    )


    chain = LLMChain(llm=llm, prompt=caption_template)

    response = chain.invoke({"caption": caption})
    return response