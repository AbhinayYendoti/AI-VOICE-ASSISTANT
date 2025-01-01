import asyncio
import logging
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
import os

# Set up logging to capture full traceback
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by Abhinay Yendoti using LiveKit. Your interface with users will be voice."
            "You should use short and concise responses, and avoid using unpronounceable punctuation."
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.SST(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=initial_ctx
    )
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hello, how may I help you!", allow_interruptions=True)

if __name__ == "__main__":
    try:
        WorkerOptions.port = 8090  # Change port to avoid conflict
        WorkerOptions.token = os.getenv("LIVEKIT_TOKEN")
        cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
    except Exception as e:
        logging.error("Worker initialization failed", exc_info=True)
