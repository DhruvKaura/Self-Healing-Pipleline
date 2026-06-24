import json

from ollama import chat


class HealingService:

    @staticmethod
    def generate_mapping(expected_columns, actual_columns):

        prompt = f"""
You are an expert data engineer.

Expected Columns:
{expected_columns}

Actual Columns:
{actual_columns}

Map EVERY actual column to the most appropriate expected column.

Return ONLY valid JSON.

Example:

{{
  "user_id": "id",
  "cost": "price",
  "date_of_purchase": "transaction_date"
}}

Do not explain.
Do not use markdown.
Return JSON only.
"""
        response = chat(model="phi3", messages=[{"role": "user", "content": prompt}])

        content = response["message"]["content"]

        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        mapping = json.loads(content)

        return mapping
