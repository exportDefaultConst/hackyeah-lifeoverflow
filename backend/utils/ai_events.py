"""
AI Event Generator using Anthropic Claude
"""
import os
import json
from anthropic import Anthropic
from config import Config

class AIEventGenerator:
    def __init__(self):
        self.client = Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        
    def generate_event(self, session, employment_context="", choice_history_context="", completed_events_context=""):
        """Generate a life event using Claude AI"""
        
        # Build context about the character
        character_info = f"""
Postać:
- Wiek: {session.age} lat
- Płeć: {'mężczyzna' if session.sex == 'male' else 'kobieta'}
- Zarobki miesięczne: {session.income} PLN
- Oszczędności: {session.savings} PLN
- Miesięczne koszty: {session.monthly_costs} PLN
- {employment_context}
"""

        if choice_history_context:
            character_info += f"\nHistoria ostatnich wyborów:\n{choice_history_context}"
            
        if completed_events_context:
            character_info += f"\n\nUkończone wydarzenia:\n{completed_events_context}"

        prompt = f"""Jesteś generatorem wydarzeń życiowych dla polskiej gry symulacyjnej o zarządzaniu finansami i ZUS.

{character_info}

Wygeneruj jedno realistyczne wydarzenie życiowe w formacie JSON. Wydarzenie powinno:
- Być odpowiednie dla wieku i sytuacji postaci
- Mieć 2-3 opcje wyboru z różnymi konsekwencjami finansowymi
- NIE powtarzać wydarzeń z listy ukończonych wydarzeń
- Być napisane po polsku
- Zawierać realistyczne kwoty w PLN
- Uwzględniać polski system ZUS i emerytalny

WAŻNE - Rodzaje zatrudnienia i składki ZUS:
- "type_employment": "UoP" - Umowa o pracę (pełne składki ZUS 19.52%, najlepsza emerytura)
- "type_employment": "zlecenie" - Umowa zlecenie (50% składek ZUS, niższa emerytura)
- "type_employment": "B2B" - Działalność gospodarcza (minimalne składki ZUS, musisz sam dbać o emeryturę)

Jeśli wydarzenie daje pracę, ZAWSZE ustaw "type_employment" na jedną z powyższych wartości!

Format JSON:
{{
    "event_key": "unique_event_name",
    "name": "Tytuł wydarzenia",
    "description": "Opis sytuacji (2-3 zdania)",
    "choices": [
        {{
            "text": "Opcja 1",
            "effects": {{
                "savings": 0,
                "income": 0,
                "type_employment": "UoP",  // OBOWIĄZKOWE gdy has_job=True
                "has_job": false,
                "monthly_costs": 0,
                "health": 0,
                "stress": 0,
                "zus_contributions": 0
            }},
            "consequence": "Co się stanie po tym wyborze"
        }}
    ]
}}

Zwróć TYLKO poprawny JSON, bez dodatkowych komentarzy."""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract JSON from response
            response_text = message.content[0].text.strip()
            
            # Remove markdown code blocks if present
            if response_text.startswith("`"):
                response_text = response_text.split("`")[1]
                if response_text.startswith("json"):
                    response_text = response_text[4:]
                response_text = response_text.strip()
            
            event_data = json.loads(response_text)
            
            # Ensure skip_years is 1 by default for AI events
            if 'skip_years' not in event_data:
                event_data['skip_years'] = 1
                
            return event_data
            
        except Exception as e:
            print(f"Error generating AI event: {str(e)}")
            # Return a fallback event
            return {
                "event_key": "ai_generation_error",
                "name": "Spokojny rok",
                "description": "Mijający rok przebiega bez większych niespodzianek. To dobry czas na refleksję i planowanie przyszłości.",
                "skip_years": 1,
                "choices": [
                    {
                        "text": "Kontynuuj",
                        "effects": {
                            "savings": 0,
                            "income": 0,
                            "monthly_costs": 0,
                            "health": 0,
                            "stress": -5
                        },
                        "consequence": "Życie toczy się dalej."
                    }
                ]
            }
