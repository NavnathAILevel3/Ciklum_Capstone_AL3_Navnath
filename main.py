import os
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Configuration - Level 3 Professional Setup
MODEL_NAME = "models/gemini-2.5-flash"
os.environ["GOOGLE_API_KEY"] = "AIzaSyAZUVC-oYwyG79H-UqJCd1G8cjRMORANp8"

def write_final_report_tool(content: str, filename: str) -> str:
    """
    TOOL-CALLING: This action persists the agent's reasoning to a file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"[ACTION] Success: Summary saved to {filename}"

def run_agentic_system():
    print(f"[*] Initializing Agentic System with {MODEL_NAME}...")
    try:
        # A. DATA PREPARATION (Retrieval)
        with open("achievements.txt", "r", encoding="utf-8") as file:
            context = file.read()

        # B. Initialize Gemini model
        llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0.7)

        # C. Generate initial project summary
        instruction = f"Based on these notes: {context}, write a professional GitHub project summary. End it with #Ciklum."
        response = llm.invoke(instruction)
        draft_summary = response.content
        print("\n--- AGENT GENERATED DRAFT SUMMARY --- \n")
        print(draft_summary)

        # D. Multi-iteration Self-Reflection loop with branding check
        refined_summary = draft_summary
        for i in range(2):  # run 2 reflection passes
            reflection_prompt = f"""
            Iteration {i+1} refinement:
            {refined_summary}

            Reflect critically, enforce 'Ciklum AI Academy 2026' branding,
            and provide a corrected version ready for publishing.
            """
            reflection_response = llm.invoke(reflection_prompt)
            refined_summary = reflection_response.content

        print("\n--- AGENT SELF-REFLECTION & FINAL REFINED SUMMARY --- \n")
        print(refined_summary)

        # E. LinkedIn Post generation based on refined summary
        linkedin_prompt = f"""
        Based on this refined summary:
        {refined_summary}

        Write a concise, engaging LinkedIn post highlighting the project achievements.
        Ensure it mentions 'Ciklum AI Academy 2026' and ends with #Ciklum.
        """
        linkedin_response = llm.invoke(linkedin_prompt)
        linkedin_post = linkedin_response.content
        print("\n--- AGENT GENERATED LINKEDIN POST --- \n")
        print(linkedin_post)

        # F. Persist results
        print(write_final_report_tool(refined_summary, "Agent_Final_Report.txt"))
        print(write_final_report_tool(linkedin_post, "Agent_LinkedIn_Post.txt"))

        # G. Consolidated Final Summary
        consolidated = (
                "--- Draft Summary ---\n" + draft_summary + "\n\n"
                                                            "--- Refined Summary ---\n" + refined_summary + "\n\n"
                                                                                                            "--- LinkedIn Post ---\n" + linkedin_post
        )
        print(write_final_report_tool(consolidated, "Final_Summary.txt"))

        # H. Evaluation Metrics
        print("\n--- AGENT EVALUATION ---\n")

        # Branding presence check
        if "Ciklum AI Academy 2026" in refined_summary and "Ciklum AI Academy 2026" in linkedin_post:
            print("[EVAL] Branding check passed ✅")
        else:
            print("[EVAL] Branding check failed ⚠️")

        # Word count check
        word_count = len(refined_summary.split())
        print(f"[EVAL] Refined summary length: {word_count} words")

        # Hashtag presence check
        if "#" in linkedin_post:
            print("[EVAL] LinkedIn post includes hashtags ✅")
        else:
            print("[EVAL] Missing hashtags ⚠️")

    except Exception as e:
        print("Error while running agentic system:", e)

# Entry point
if __name__ == "__main__":
    run_agentic_system()
