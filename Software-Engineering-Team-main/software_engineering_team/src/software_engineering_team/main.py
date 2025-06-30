from crew import SoftwareEngineeringTeam

from dotenv import load_dotenv

import os

import traceback

from utils.write_output import save_crew_output_to_disk

# Set LiteLLM config path
os.environ["LITELLM_CONFIG_PATH"] = ".litellm/config.yaml"

load_dotenv()

def run(user_requirements: str):
    """
    Run the crew and save the output.
    """
    print("🔐 Loaded GROQ key:", os.getenv("GROQ_API_KEY"))

    print("🔐 Loaded GEMINI key:", os.getenv("GEMINI_API_KEY"))

    # Ensure API keys are loaded
    if not os.getenv("GROQ_API_KEY"):

        raise Exception("GROQ_API_KEY environment variable is not set.")
    
    if not os.getenv("GEMINI_API_KEY"):

        raise Exception("GEMINI_API_KEY environment variable is not set.")

    inputs = {'user_requirements': user_requirements}

    try:

        print("🛠️ Creating SoftwareEngineeringTeam...")
        
        team = SoftwareEngineeringTeam()

        print("🤖 Getting crew...")

        crew = team.crew()

        print("🚀 Starting crew execution...")

        result = crew.kickoff(inputs=inputs)

        print("✅ Crew execution completed. Saving output...")

        zip_path = save_crew_output_to_disk(result)

        print(f"📁 Output saved to: {zip_path}")

        # 🔍 Debugging the result object
        print("[DEBUG] result type:", type(result))

        print("[DEBUG] result str:", str(result)[:300])  # First 300 chars

        if hasattr(result, "raw_output"):

            print("[DEBUG] result.raw_output exists")

            if isinstance(result.raw_output, dict):

                print("[DEBUG] raw_output is a dict with files:")

                for k, v in result.raw_output.items():

                    print(f" - {k}: {v[:80].strip()}...") 
                     # Print sample
            else:

                print("[DEBUG] raw_output is NOT a dict:", type(result.raw_output))
        else:

            print("[DEBUG] result has NO raw_output attribute")

        return str(result), zip_path

    except Exception as e:

        print("❌ Error during crew execution:")

        print(traceback.format_exc())

        raise Exception(f"An error occurred while running the crew: {e}")




