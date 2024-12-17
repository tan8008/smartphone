#!/usr/bin/env python
# import sys
# import warnings

# from my_smartphone.crew import MySmartphone

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs'
#     }
#     MySmartphone().crew().kickoff(inputs=inputs)


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         MySmartphone().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         MySmartphone().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         MySmartphone().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

import sys
import warnings
from smartphone_comparison.crew import SmartphoneComparison

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

#Original code required 3 text inputs; new code allows for multiple inputs in one text input.
# def get_smartphone_inputs():
#     """Get smartphone inputs from user"""
#     smartphones = []
#     print("Enter three smartphones to compare (e.g., 'iPhone 15 Pro Max'):")
#     for i in range(3):
#         smartphone = input(f"Smartphone {i+1}: ")
#         smartphones.append(smartphone)
#     return smartphones

def run():
    """Run the crew."""
    #this new code will allow for multiple inputs in one text input
    #smartphones = get_smartphone_inputs()
    inputs = {
        'smartphones': "iPhone 16, Samsung, LG",
        'features': "battery life, price"
    }
    SmartphoneComparison().crew().kickoff(inputs=inputs)

def train():
    #this new code will allow for multiple inputs in one text input
    """Train the crew for a given number of iterations."""
    inputs = {
        'smartphones': "iPhone 16, Samsung, LG"
    }

    try:
        SmartphoneComparison().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """Replay the crew execution from a specific task."""
    try:
        SmartphoneComparison().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """Test the crew execution and returns the results."""
    smartphones = get_smartphone_inputs()
    inputs = {
        'smartphones': smartphones
    }
    try:
        SmartphoneComparison().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
