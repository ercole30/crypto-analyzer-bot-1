from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(data: dict) -> str:
    return f"""
Sei un analista crypto indipendente.
Analizza il progetto seguente in modo oggettivo e critico.

NOME: {data['name']}
DESCRIZIONE: {data['description']['en'][:1500]}
MARKET CAP: {data['market_data']['market_cap']['usd']}
SUPPLY TOTALE: {data['market_data']['total_supply']}
PREZZO: {data['market_data']['current_price']['usd']}

Fornisci:
1. Use case
2. Tokenomics
3. Credibilità team
4. Rischi
5. Red flags
6. Valutazione rischio (1–5)

⚠️ NON fornire consigli finanziari.
"""

def analyze_project(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
