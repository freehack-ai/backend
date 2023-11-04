from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType
import replicate
import json
import yaml
import os


with open("config.yaml") as f:
    config_data = yaml.load(f, Loader=yaml.FullLoader)
    open_ai_key = config_data["OPENAI_API_KEY"]
    os.environ["OPENAI_API_KEY"] = open_ai_key
    replicate_key = config_data["REPLICATE_API_TOKEN"]
    os.environ["REPLICATE_API_KEY"] = replicate_key


# extract the first job from the jobs.json file
with open("jobs.json") as f:
    jobs = json.load(f)

job = jobs[0]


def create_logo_design(job):
    blurb = job["blurb"]
    requirements = job["requirements"]
    prompt = f"Design a logo following these requirements: {blurb} {requirements}"
    output = replicate.run(
        "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
        input={"prompt": prompt},
    )
    return output


logo_design_tool = Tool.from_function(
    func=create_logo_design,
    name="LogoDesigner",
    description="Creates a logo from a description",
)


prompt_template = "Decide whether or not you have the ability to perform this task {task}. If you do have this ability, return True, otherwise return False."
prompt_template.format(task=job)
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))

assessor_tool = Tool.from_function(
    func=llm_chain.run,
    name="Assessor",
    description="Decides whether or not to perform a task.",
)
tools = [logo_design_tool, assessor_tool]

agent = initialize_agent(
    tools=tools, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, llm=llm, verbose=True
)

prompt = "For the following task, decide whether or not you have the ability to perform it. If you do have this ability, perform the task and create the logo, otherwise  skip and return nothing.\n \n Task: Design the logo presented in the input."

print(agent.run(prompt))
