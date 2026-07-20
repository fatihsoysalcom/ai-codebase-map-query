import json

# --- Simulated Codebase Summaries ---
# In a real scenario, an AI would process actual code files once
# to extract these high-level summaries (e.g., function names, class names, docstrings).
SIMULATED_CODEBASE_SUMMARIES = {
    "src/auth/user_manager.py": {
        "description": "Handles user authentication, registration, and session management.",
        "functions": ["register_user", "login_user", "logout_user", "get_current_user"],
        "classes": ["UserManager"]
    },
    "src/data/processor.py": {
        "description": "Utility functions for data validation and transformation.",
        "functions": ["validate_input", "transform_data", "clean_string"],
        "classes": ["DataProcessor"]
    },
    "src/api/routes.py": {
        "description": "Defines API endpoints for user and data operations.",
        "functions": ["get_user_profile_route", "post_data_route"],
        "classes": []
    },
    "config/settings.py": {
        "description": "Application configuration settings.",
        "functions": [],
        "classes": []
    }
}

def generate_project_map(codebase_summaries):
    """
    Generates a structured 'map' of the project from high-level summaries.
    This map is what an AI would use to quickly understand the codebase structure
    without needing to re-read every line of code repeatedly.
    """
    project_map = {}
    for path, summary in codebase_summaries.items():
        project_map[path] = {
            "overview": summary["description"],
            "entry_points": summary["functions"] + summary["classes"]
        }
    return project_map

def ai_query_with_map(project_map, query):
    """
    Simulates an AI using the project map to answer a query.
    It demonstrates how the AI can quickly identify relevant files/components
    without needing to re-read the full content of every file.
    """
    print(f"AI received query: '{query}'")
    print("--- AI Consulting Project Map ---")

    relevant_components = []
    query_keywords = query.lower().split()

    for path, info in project_map.items():
        # AI checks if query keywords are in the file overview or entry points in the map
        if any(keyword in info["overview"].lower() for keyword in query_keywords) or \
           any(any(keyword in ep.lower() for keyword in query_keywords) for ep in info["entry_points"]):
            relevant_components.append(path)
            print(f"  Map suggests '{path}' is relevant (Overview: '{info['overview']}')")

    if relevant_components:
        print("\n--- AI Identified Relevant Components (based on map) ---")
        for component in relevant_components:
            print(f"- {component}")
        print("\nAI would now focus on these specific files for deeper analysis,")
        # This is the core concept: avoiding full codebase re-scan
        print("instead of scanning the entire codebase again for every query.")
    else:
        print("\nNo directly relevant components found in the map for this query.")
        print("AI might need to broaden its search or ask for clarification.")

# --- Main execution ---
if __name__ == "__main__":
    print("Step 1: AI processes codebase once to generate a project map.")
    project_map = generate_project_map(SIMULATED_CODEBASE_SUMMARIES)
    print("\nGenerated Project Map (simplified view):")
    print(json.dumps(project_map, indent=2)) # Using json for pretty print of the map

    print("\n" + "="*80 + "\n")

    print("Step 2: AI answers queries using the pre-generated map.")

    # Example Query 1: Find user authentication logic
    ai_query_with_map(project_map, "How do I handle user login?")
    print("\n" + "-"*40 + "\n")

    # Example Query 2: Find data validation utilities
    ai_query_with_map(project_map, "Where are the data validation functions?")
    print("\n" + "-"*40 + "\n")

    # Example Query 3: Find API routes
    ai_query_with_map(project_map, "Show me the API endpoints.")
    print("\n" + "-"*40 + "\n")

    # Example Query 4: Query for something not directly in the map
    ai_query_with_map(project_map, "What's the database schema?")
    print("\n" + "-"*40 + "\n")
