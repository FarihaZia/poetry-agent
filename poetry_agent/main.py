from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, handoff
from dotenv import load_dotenv
import os

import requests

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# --- Analyst Agents ---
lyric_agent = Agent(
    name="Lyric Analyst",
    instructions="""
You analyze poems that show deep emotions like love, sadness, or loneliness. Also tell the analyst what specific emotions are present.
Give a detailed and easy-to-understand explanation of what the poem means emotionally.
"""
)

narrative_agent = Agent(
    name="Narrative Analyst",
    instructions="""
You analyze story-based poems with characters, plot, or events.
Explain the story, theme, and message in a simple way.
"""
)

dramatic_agent = Agent(
    name="Dramatic Analyst",
    instructions="""
You analyze poems that feel like a monologue or stage performance.
Explain what the speaker is expressing and how it's dramatic.
"""
)

# --- Triage Agent ---
triage_agent = Agent(
    name="Triage Agent",
    instructions="""
You are the Triage Agent. Read the poem and decide its type:
- LYRIC: If it talks about "I", "my", or emotions like sadness or love.
- NARRATIVE: If it tells a story or event.
- DRAMATIC: If it feels like a speech, monologue, or character act.

Then, hand off to the correct agent for full analysis (tashreeh).
""",
    handoffs=[lyric_agent, narrative_agent, dramatic_agent]
)

# --- User Poem Input ---
print("📜 Enter a 2-stanza poem (press Enter twice to finish):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

poem = "\n".join(lines).strip()

# Default poem if input is empty
if not poem:
    poem = """
Earlier you were quite arrogant  
then learnt the lesson by life  
and came into reality  
and knew your position in the world
"""

# --- Run the Triage Agent ---
response = Runner.run_sync(
    triage_agent,
    input=poem,
    run_config=config
)

# --- Final Output ---
print("\n📝 Final Tashreeh (Poetry Analysis):\n")
print(response.final_output)

