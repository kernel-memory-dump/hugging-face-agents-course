# Hugging Face Agents Course Notes and Projects

This repository contains my work and notes while following the Hugging Face Agents course. Each chapter has its own directory with specific projects and notes.

## Course Structure

| Chapter | Topic | Description |
|---------|-------|-------------|
| 0 | Onboarding | Set up with the tools and platforms that will be used. |
| 1 | Agent Fundamentals | Tools, Thoughts, Actions, Observations, and their formats. LLMs, messages, special tokens and chat templates. Simple use case using python functions as tools. |
| 2 | Frameworks | Understanding fundamentals implementation in popular libraries: smolagents, LangGraph, LLamaIndex |
| 3 | Use Cases | Building real life use cases |
| 4 | Final Assignment | Building an agent for a selected benchmark and proving understanding of Agents on the student leaderboard |

## Repository Structure

```
.
├── chapter_0/            # Onboarding
├── chapter_1/            # Agent Fundamentals
├── chapter_2/            # Frameworks
├── chapter_3/            # Use Cases
├── chapter_4/            # Final Assignment
├── notes/                # General course notes
└── requirements.txt      # Global dependencies
```

## Setup Instructions

1. Clone this repository
2. Create a virtual environment for each chapter:
   ```bash
   cd chapter_X
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   .\venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

## Notes

Each chapter directory contains:
- A README.md with chapter-specific notes
- Project code and resources
- Chapter-specific virtual environment
- Chapter-specific requirements.txt if needed

The `notes/` directory contains general course notes and insights that span multiple chapters. 