import os

import pathlib

import tempfile

import gradio as gr

from main import run

from pathlib import Path

import pdfplumber

from docx import Document

import time

import random

import shutil

import zipfile

import re

ALLOWED_EXTENSIONS = {".pdf" , ".docx", ".txt"}

MAX_ALLOWED_PAGES = 30

FUN_FACTS = [

    "💡 The first computer bug was a literal moth found in a computer.",

    "🚀 NASA's Curiosity rover is powered by a processor slower than a modern smartphone.",

    "🧠 The original name for Java was Oak.",

    "🐍 Python is named after Monty Python, not the snake.",

    "📄 The first software license was issued in 1969.",

    "👩‍💻 The first known programmer was Ada Lovelace—in the 1800s!",

    "🗂️ Git was created by Linus Torvalds—the creator of Linux.",

    "🔁 Recursion is when a function calls itself. See: Recursion.",

    "🧱 'Hello, World!' is the first program in nearly every programming language.",

    "⏳ Software engineers spend 80% of their time debugging. The other 20%? Writing bugs."

]

def display_random_fun_fact() -> str:

    return random.choice(FUN_FACTS)


def validate_file_extension(file_path: pathlib.Path) -> tuple[bool, str]:
    """
    Validates if a file has a proper extension and is supported.
    Returns (is_valid, error_message)
    """
    suffix = file_path.suffix.lower()
    
    # Check if file has no extension or just a dot
    if not suffix or suffix == ".":

        return False, f"File '{file_path.name}' has no valid extension. Please ensure your file has a .pdf, .docx, or .txt extension"
    
    # Check if extension is supported
    if suffix not in ALLOWED_EXTENSIONS:

        return False, f"Unsupported format: {suffix}. System only accepts .pdf, .docx, and .txt"
    
    return True, ""


def extract_text_from_document(file_path: pathlib.Path) -> str:

    # Validate file extension first
    is_valid, error_message = validate_file_extension(file_path)

    if not is_valid:

        raise ValueError(f"❌ {error_message}")
    
    suffix = file_path.suffix.lower()
    
    """Reading Text document file."""

    if suffix == ".txt":

        with open(file_path, "r", encoding = "utf-8", errors = "ignore") as text_document_file:

            document_text = text_document_file.read()

        return document_text
    
    """Reading PDF document file."""

    if suffix == ".pdf":

        with pdfplumber.open(file_path) as pdf_document_file:

            if len(pdf_document_file.pages) > MAX_ALLOWED_PAGES:

                raise ValueError(f"📄 Document exceeded allowed page limit, please upload up to {MAX_ALLOWED_PAGES} pages only.")
            
            pdf_document_text = "\n".join(page.extract_text() or " " for page in pdf_document_file.pages)

        return pdf_document_text    
    
    """Reading Word document file."""

    if suffix == ".docx":

        word_document_file = Document(file_path)

        word_document_text = "\n".join(page.text for page in word_document_file.paragraphs)

        if not word_document_text.strip():

            raise ValueError("🔍 Document is empty")
        
        #Page count estimate: 400 words -> 1 page 

        if (len(word_document_text.split()) / 400) > MAX_ALLOWED_PAGES:

            raise ValueError(f"Max Limit Allowed: {MAX_ALLOWED_PAGES} pages.")
        
        return word_document_text

def get_output_file_extension(language_used: str) -> str:

    extension_map = {

        "java" : "java",

        "python" : "py",

        "go" : "go",

        "javascript" : "js",

        "kotlin" : "kt",

        "c++" : "cpp",

        "typescript" : "ts",

        "rust" : "rs",

        "ruby" : "rb",

        "c#" : "csharp",

        "c" : "c"

    }

    language = language_used.strip().lower()

    output_file_extension = extension_map.get(language, "txt")
                                             
    if output_file_extension == "txt":
  
        print(f"Unknown language '{language}', defaulting to .txt")

    return output_file_extension


def download_project_bundle(project_summary: str, project_source_code: str, language_used: str) -> str:

    """Saves the project summary and backend source code to files, zips them, and returns the path to the zip file."""

    output_directory = pathlib.Path("Output_package")

    output_directory.mkdir(exist_ok= True)

    summary_file = output_directory/"summary.txt"

    summary_file.write_text(project_summary, encoding= "utf-8")

    output_file_extension = get_output_file_extension(language_used)

    output_code_file = output_directory/f"main.{output_file_extension}"

    output_code_file.write_text(project_source_code, encoding = "utf-8")

    zip_path = pathlib.Path("DevPilot's Project Output.zip")

    shutil.make_archive(base_name = zip_path.with_suffix(""), format = 'zip', root_dir = output_directory)

    return str(zip_path.resolve())


def build_software(user_requirements: str):
    """Orchestrates the entire software building process, streams status updates,
    bundles the results, and provides download link + readable output"""
    
    yield "Requirements received.."
    time.sleep(5)

    yield f" 🧠 Did you know: {display_random_fun_fact()}"
    time.sleep(5)

    yield "Initiating build.."
    time.sleep(5)

    yield f"Building in progress....."
    time.sleep(5)

    yield f"📚 Did you know: {display_random_fun_fact()}"
    time.sleep(5)

    build_team = None

    try:
        build_team_result = run(user_requirements)
        
        # Handle the tuple returned by run function
        if isinstance(build_team_result, tuple):

            build_team, zip_path = build_team_result

        else:

            build_team = build_team_result

            zip_path = None
        
        yield "Build success"
        time.sleep(5)

        yield f"🧠 Did you know: {display_random_fun_fact()}"
        time.sleep(5)

        if "```" in build_team:

            separate_parts = build_team.split("```", 1)

            project_summary = separate_parts[0].strip()

            project_source_code = separate_parts[1].replace("python", " ").strip()

        else:

            project_summary = build_team.strip()

            project_source_code = "No source code generated"
        
        """Detect language from agent output"""

        language_match = re.search(r"(java|python|c\+\+|go|typescript|javascript|kotlin|ruby|c#|rust|c)", build_team.lower())

        language_used = language_match.group(1) if language_match else "txt"

        """Package output for download"""
        if zip_path is None:

            zip_file_path = download_project_bundle(project_summary, project_source_code, language_used)

        else:

            zip_file_path = zip_path

        yield "Output package now available for download"
        time.sleep(1.2)

        final_output_md = f"""### 📝 Project Summary:

{project_summary}

---

### 💾 [Click here to download your project bundle]({zip_file_path})

---

### 💡 Generated Source Code:

```{language_used}
{project_source_code}
```"""
        
        yield final_output_md, zip_file_path
    
    except Exception as e:

        error_msg = f"Build crashed, please try again after sometime : {e}"

        yield error_msg, None

        return

def initiate_software_build_process_text_input(user_requirement, viewmode):

    if not user_requirement.strip():

        yield "No requirement provided.", None

    else:

        for result in build_software(user_requirements=user_requirement):

            if isinstance(result, tuple):

                yield result

            else:

                yield result, None


def initiate_software_build_process_file_input(file):

    if file is None:

        yield " ❌ No file uploaded"

        return 
    
    # Create a temporary path that preserves the original filename
    original_filename = pathlib.Path(file.name) if hasattr(file, 'name') else pathlib.Path(file)

    temp_path = pathlib.Path(tempfile.mktemp(suffix=original_filename.suffix))
    
    try:
        # Copy the file to preserve the original
        shutil.copy2(file, temp_path)
        
        # Validate the file extension
        is_valid, error_message = validate_file_extension(temp_path)

        if not is_valid:

            yield f"❌ {error_message}"

            return
            
        user_requirement = extract_text_from_document(temp_path)
        
        for result in build_software(user_requirements=user_requirement):

            if isinstance(result, tuple):

                yield result[0]  # Only yield the markdown string for file input

            else:

                yield result
    
    except ValueError as VE:

        yield f"❌ File upload error: {VE}"

    except Exception as e:

        yield f"❌ Unexpected error processing file: {str(e)}"
    
    finally:

        if temp_path.exists():

            temp_path.unlink()


"""Defining the Gradio User interface Layout"""

with gr.Blocks(theme = gr.themes.Soft(primary_hue = "slate", secondary_hue = "purple"), title = "Faiaz's DevPilot: CodeCrew Foundry by CrewStormAI") as gradio_ui:

    gr.Markdown(
        
        """# 🚀 Faiaz's DevPilot: CodeCrew Foundry by CrewStorm AI
    ### Build with ProductForge Precision™️*
    > Describe it once. Let Faiaz's AI Engineers – your very own LaunchSmiths – forge, build and bring your ideas to life.
    
    ---
    """
    )

    view_mode = gr.Radio(["💻 Code Only", "📜 Code + Summary"], 
                         
                           value = "📜 Code + Summary",
                          
                           label = "Choose content type")

    with gr.Tab("💬 Type out your requirement"):

        user_input = gr.Textbox(lines =  8, label = "Briefly describe your requirement...")

        run_user_requirement_button = gr.Button("🚀 Run")

    with gr.Tab("Upload your requirements or SRS document"):

        gr.Markdown(
            
            """
        **📋 Supported File Formats:**
        - **PDF** (.pdf) - Up to 30 pages
        - **Word Document** (.docx) - Up to 30 pages (estimated)
        - **Text File** (.txt) - Plain text documents
        
        **⚠️ Important:** Make sure your file has a proper extension (.pdf, .docx, or .txt)
        """
        
        )
        
        user_input_file = gr.File(

            label="Upload Requirements Document", 

            file_types=[".pdf", ".docx", ".txt"],

            file_count="single"
        )

        run_user_document_button = gr.Button("🚀 Run with document")

    output_md = gr.Markdown(label = "📜 Team Output")

    zip_output = gr.File(label = "Download Project Bundle(.zip)")

    run_user_requirement_button.click(fn = initiate_software_build_process_text_input, inputs = [user_input, view_mode], outputs= [output_md, zip_output], queue= True, show_progress = True)

    run_user_document_button.click(fn = initiate_software_build_process_file_input, inputs = [user_input_file], outputs= [output_md], queue = True, show_progress = True)

