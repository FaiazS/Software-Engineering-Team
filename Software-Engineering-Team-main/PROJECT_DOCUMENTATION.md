# Faiaz's DevPilot: CodeCrew Foundry by CrewStorm AI

## 🚀 Project Overview

**Faiaz's DevPilot: CodeCrew Foundry** is an AI-powered software development platform that leverages the **crewAI** framework to create a collaborative team of AI agents capable of designing, building, and testing software applications from natural language requirements.

This system essentially acts as an **AI-powered software development team** that can take high-level requirements and transform them into fully functional applications with proper architecture, testing, and documentation.

## 🏗️ Core Architecture

The project implements a **multi-agent AI system** with four specialized AI agents working together in a sequential workflow:

### 🤖 The AI Team Members

#### 1. **Engineering Lead** (`groq/llama-3.1-70b-versatile`)
- **Role**: Oversees backend architecture and guides engineering vision
- **Responsibilities**:
  - Analyzes software requirements thoroughly
  - Breaks down requirements into well-defined functionalities
  - Designs modular and robust microservices-based architecture
  - Enforces separation of concerns and single responsibility principles
  - Creates scalable, maintainable system blueprints
- **Output**: Structured software design documents in markdown format

#### 2. **Backend Engineer** (`groq/deepseek-r1-distill-llama-70b`)
- **Role**: Implements software designs using efficient, modular, and scalable practices
- **Responsibilities**:
  - Builds robust backend services based on design documents
  - Writes clean, production-level code following SOLID principles
  - Implements appropriate software design patterns
  - Adds robust logging and error-handling strategies
  - Chooses appropriate frameworks and ORMs
- **Output**: Complete backend implementation with source code and setup instructions

#### 3. **Frontend Engineer** (`groq/llama-3.1-8b-instant`)
- **Role**: Implements user interfaces and interactions
- **Responsibilities**:
  - Builds intuitive, responsive, and interactive UIs
  - Follows component-based architecture principles
  - Applies SOLID principles for UI logic and state management
  - Ensures proper API integration with backend services
  - Maintains code readability and modularity
- **Output**: Complete frontend implementation with interactive components

#### 4. **Test Engineer** (`gemini-2.5-flash`)
- **Role**: Ensures software correctness, performance, and reliability
- **Responsibilities**:
  - Designs and implements automated test suites
  - Creates unit, integration, and system tests
  - Performs security validation and vulnerability scanning
  - Ensures comprehensive test coverage
  - Validates adherence to requirements
- **Output**: Complete test suite with testing framework and instructions

## 🔄 Workflow Process

The agents work in a **sequential process**:

```
User Requirements → Design → Backend → Frontend → Testing → Project Bundle
```

### Detailed Workflow:

1. **Requirements Analysis**: System processes user input (text or document)
2. **Software Design**: Engineering Lead creates architectural blueprint
3. **Backend Development**: Backend Engineer implements core services
4. **Frontend Development**: Frontend Engineer builds user interface
5. **Quality Assurance**: Test Engineer creates comprehensive test suite
6. **Project Delivery**: System bundles everything into downloadable format

## 🎯 Key Features

### 📝 **Smart Requirements Processing**
- **Multiple Input Formats**: Text input, PDF, DOCX, and TXT files
- **Document Validation**: File type checking and page limit enforcement (30 pages max)
- **Text Extraction**: Automated extraction from various document formats
- **Language Detection**: Automatic programming language identification

### 🏗️ **Modular Architecture Design**
- **Microservices Principles**: Enforces service separation and independence
- **SOLID Design Patterns**: Implements industry-standard design principles
- **Separation of Concerns**: Clear boundaries between different system components
- **Scalability Focus**: Architecture designed for easy scaling and maintenance

### 🛠️ **Multi-Technology Support**
- **Backend Technologies**: Python, Java, Go, Node.js, Spring Boot, FastAPI, Django, Flask
- **Frontend Technologies**: React, Angular, Vue, Gradio, Streamlit, Flutter
- **Testing Frameworks**: PyTest, JUnit, Jest, and other language-specific tools
- **Database Support**: Various ORMs and database technologies

### 📦 **Complete Project Delivery**
- **Production-Ready Code**: Industry-standard coding practices
- **Installation Instructions**: Step-by-step setup guidance
- **Configuration Management**: Environment variables and configuration files
- **Project Bundling**: ZIP file with all project components

## 🖥️ User Interface

The project provides a **Gradio web interface** with two primary input methods:

### 💬 **Text Input Tab**
- Large text area for typing software requirements
- Real-time processing and status updates
- Progress indicators during build process

### 📄 **File Upload Tab**
- **Supported Formats**: PDF, DOCX, TXT
- **File Validation**: Extension checking and page limit enforcement
- **Document Processing**: Automated text extraction and analysis

### 📊 **Output Display**
- **Real-time Updates**: Streaming status messages and progress
- **Fun Facts**: Educational programming trivia during processing
- **Markdown Rendering**: Formatted output with code highlighting
- **Download Links**: Direct access to project bundles

## 🛠️ Technical Stack

### **Core Framework**
- **crewAI**: Multi-agent orchestration and collaboration framework
- **Python 3.10-3.13**: Primary programming language

### **User Interface**
- **Gradio**: Web-based interface for user interaction
- **Custom Themes**: Soft theme with slate and purple color scheme

### **Document Processing**
- **pdfplumber**: PDF text extraction and processing
- **python-docx**: Microsoft Word document handling
- **pathlib**: Cross-platform file path operations

### **AI Models**
- **Groq API**: High-performance inference for multiple agents
- **Gemini API**: Google's AI model for test engineering
- **LiteLLM**: Unified interface for multiple AI providers

### **Development Tools**
- **UV**: Fast Python package manager and installer
- **Hatchling**: Modern Python project build system
- **Environment Management**: .env file for API key configuration

## 📁 Project Structure

```
Software-Engineering-Team-main/
├── README.md
├── software_engineering_team/
│   ├── knowledge/
│   │   └── user_preference.txt
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   └── src/
│       └── software_engineering_team/
│           ├── __init__.py
│           ├── app.py                 # Main application entry point
│           ├── config/
│           │   ├── agents.yaml        # AI agent configurations
│           │   └── tasks.yaml         # Task definitions
│           ├── crew.py                # Crew orchestration logic
│           ├── main.py                # Core execution logic
│           ├── tools/
│           │   ├── __init__.py
│           │   └── custom_tool.py
│           ├── user_interface.py      # Gradio UI implementation
│           └── utils/
│               └── write_output.py    # Output management utilities
```

## 🚀 Getting Started

### Prerequisites
- Python >=3.10, <3.14
- UV package manager
- API keys for Groq and Gemini services

### Installation
```bash
# Install UV if not already installed
pip install uv

# Navigate to project directory
cd software_engineering_team

# Install dependencies
crewai install
```

### Configuration
1. Create a `.env` file in the project root
2. Add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

### Running the Application
```bash
# From the project root
crewai run

# Or run the Gradio interface directly
python src/software_engineering_team/app.py
```

## 💡 Use Cases

This system is ideal for:

### 🎯 **Rapid Prototyping**
- Quickly convert ideas into working software
- Validate concepts before full development
- Create proof-of-concept applications

### 📋 **Requirements to Code**
- Transform requirement documents into executable applications
- Bridge the gap between business requirements and technical implementation
- Automate the initial development phase

### 🎓 **Educational Purposes**
- Learn software architecture patterns
- Understand microservices design principles
- Study best practices in software development

### 🚀 **MVP Development**
- Create minimum viable products for startups
- Validate business ideas with working software
- Accelerate time-to-market for new products

### 🤖 **Automated Development**
- Generate code from specifications
- Reduce manual coding effort
- Standardize development processes

## 🔧 Customization

### **Agent Configuration**
Modify `src/software_engineering_team/config/agents.yaml` to:
- Change agent roles and responsibilities
- Adjust AI model assignments
- Customize agent behavior and goals

### **Task Configuration**
Modify `src/software_engineering_team/config/tasks.yaml` to:
- Define new task workflows
- Adjust task dependencies
- Customize output formats

### **Crew Logic**
Modify `src/software_engineering_team/crew.py` to:
- Add custom tools and utilities
- Implement specialized logic
- Integrate with external services

### **User Interface**
Modify `src/software_engineering_team/user_interface.py` to:
- Customize the web interface
- Add new input methods
- Enhance user experience

## 📊 Output Examples

### **Software Design Document**
```markdown
# Software Architecture Design

## Microservices Overview
- **User Service**: Handles user authentication and management
- **Product Service**: Manages product catalog and inventory
- **Order Service**: Processes orders and payments
- **Notification Service**: Handles email and SMS notifications

## API Interactions
- RESTful APIs with JSON payloads
- Event-driven communication between services
- Database per service pattern
```

### **Generated Code Structure**
```
output/
├── backend_module/
│   ├── user_service/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── requirements.txt
│   ├── product_service/
│   └── order_service/
├── frontend_module/
│   ├── components/
│   ├── pages/
│   └── package.json
└── tests_module/
    ├── unit_tests/
    ├── integration_tests/
    └── test_config.py
```

## 🔒 Security Considerations

- **API Key Management**: Secure storage of AI service credentials
- **Input Validation**: File type and size restrictions
- **Code Execution**: Safe execution environment for generated code
- **Error Handling**: Graceful failure handling and user feedback

## 🚀 Future Enhancements

### **Planned Features**
- **Database Integration**: Direct database schema generation
- **Deployment Automation**: Cloud deployment integration
- **Version Control**: Git repository creation and management
- **CI/CD Pipeline**: Automated testing and deployment workflows

### **Advanced Capabilities**
- **Multi-language Support**: Support for additional programming languages
- **Framework Selection**: AI-driven technology stack recommendations
- **Performance Optimization**: Automated code optimization
- **Security Scanning**: Built-in security vulnerability detection

## 📞 Support and Resources

### **Documentation**
- [crewAI Documentation](https://docs.crewai.com)
- [Gradio Documentation](https://gradio.app/docs/)
- [Project GitHub Repository](https://github.com/joaomdmoura/crewai)

### **Community**
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [GitHub Discussions](https://github.com/joaomdmoura/crewai/discussions)
- [Documentation Chat](https://chatg.pt/DWjSBZn)

## 📄 License

This project is built on top of the crewAI framework and follows its licensing terms. Please refer to the crewAI repository for specific license information.

---

**Built with ❤️ using crewAI and modern AI technologies**

*Transform your ideas into reality with the power of AI-driven software development.*