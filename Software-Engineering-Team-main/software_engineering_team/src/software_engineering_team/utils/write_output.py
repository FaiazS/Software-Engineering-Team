import os

import zipfile

from datetime import datetime

from pathlib import Path

def save_crew_output_to_disk(crew_output, output_dir=None):

    """
    Saves the crew's output to disk in a timestamped folder inside the output directory.
    Also zips the folder and returns the path to the zip.
    
    """
    if output_dir is None:

        project_root = Path(__file__).resolve().parent.parent

        output_dir = project_root/"output"

    output_dir.mkdir(parents= True, exist_ok = True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    run_dir = output_dir/ f"run_{timestamp}"

    run_dir.mkdir(parents = True, exist_ok = True)

    # Save the text output from Crew
    summary_path =  run_dir/ "summary.md"

    with open(summary_path, "w", encoding="utf-8") as f:

        f.write(str(crew_output))

    # If there's generated source code, store it too
    if hasattr(crew_output, "raw_output") and isinstance(crew_output.raw_output, dict):

        for filename, code in crew_output.raw_output.items():

            code_path = run_dir/ filename

            code_path.parent.mkdir(parents = True, exist_ok = True)

            with open(code_path, "w", encoding="utf-8") as f:

                f.write(code)

    # Zip the directory
    zip_path = output_dir/ f"run_{timestamp}.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

        for root, _, files in os.walk(run_dir):

            for file in files:

                abs_path = os.path.join(root, file)

                rel_path = os.path.relpath(abs_path, run_dir)

                zipf.write(abs_path, rel_path)

    print(f"[🧭] Final save location: {os.path.abspath(run_dir)}")
            
    return str(zip_path)

if __name__ == "__main__":
    class DummyOutput:
        def __str__(self):
            return "🔧 Test summary from Faiaz's Crew"

        raw_output = {
            "app/main.py": "# Test Python code\nprint('Het')",
            "README.md": "# This is a README"
        }

    save_crew_output_to_disk(DummyOutput())
