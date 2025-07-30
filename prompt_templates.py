# prompt_templates.py

TRAVEL_ADVISORY_PROMPT = """
You are a helpful travel assistant. Generate {num_ideas} travel advisory and destination information pieces for passengers interested in the destination: **{niche}**.

Each advisory should be {include_outline} and written in a **{tone}** tone.

Include:
- Weather conditions and climate tips
- Cultural do's and don'ts
- Popular local attractions and landmarks
- Emergency contact advice or travel safety tips
- Any local health or travel restrictions

Make the content informative, easy to understand, and suitable for travelers.
"""
