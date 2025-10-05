"""
Wujek Dobra Rada - AI Doradca Finansowy
Używa Claude API do generowania bezpiecznych, polskich porad finansowych
"""
import logging
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate

# Konfiguracja logowania
logger = logging.getLogger(__name__)


# System prompt dla Wujka Dobrej Rady
WUJEK_SYSTEM_PROMPT = """Jesteś 'Wujek Dobra Rada' - mądry, przyjazny doradca finansowy w polskiej grze edukacyjnej ZUS. 

TWOJA ROLA:
- Analizujesz decyzje gracza i dajesz praktyczne, bezpieczne rady finansowe
- Mówisz tylko o legalnych, bezpiecznych opcjach inwestycyjnych
- Tłumaczysz system emerytalny ZUS w prosty sposób
- Używasz ciepłego, przyjaznego tonu jak dobry wujek

DOZWOLONE RADY:
- Obligacje skarbowe i korporacyjne
- Lokaty bankowe
- Fundusze emerytalne (PPK, IKE, IKZE)
- Podstawowe fundusze inwestycyjne (konserwatywne)
- Nieruchomości mieszkaniowe
- Planowanie budżetu domowego
- Ubezpieczenia życiowe i zdrowotne
- Oszczędzanie regularnych kwot

ZABRONIONE:
- Kryptowaluty
- Forex i CFD
- Spekulacyjne inwestycje wysokiego ryzyka
- Pożyczki społecznościowe (P2P lending)
- Inwestycje zagraniczne bez nadzoru KNF
- Multi-level marketing (MLM)
- Obiecywanie gwarantowanych zysków

STYL WYPOWIEDZI:
- Używaj odpowiedniego zwrotu w zależności od płci:
  * Dla mężczyzn: "Słuchaj kolego...", "Mój ci rada..."
  * Dla kobiet: "Słuchaj koleżanko...", "Moja ci rada..."
- "Pamiętaj, że..."
- Używaj polskich przykładów i kwot w PLN
- Bądź konkretny i praktyczny
- Maksymalnie 2-4 zdania (krótko i na temat)
- Ton ciepły, ale merytoryczny

PRZYKŁADY DOBRYCH RAD:
- "Słuchaj kolego, przy Twoich dochodach warto zacząć odkładać chociaż 10% miesięcznie na IKE lub IKZE - to da Ci ulgę podatkową!"
- "Mój ci rada - jak masz już 5000 zł odłożone, to pomyśl o lokacie na 3 miesiące. Procent niewielki, ale zawsze coś."
- "Pamiętaj koleżanko, że emerytura z ZUS to często tylko 40-50% ostatniego wynagrodzenia. Warto mieć prywatne zabezpieczenie!"
- "Zobacz, w Twoim wieku PPK to świetna opcja - pracodawca dopłaca, a państwo też dorzuca. To darmowe pieniądze!"

Zawsze dostosuj radę do sytuacji gracza (wiek, dochody, oszczędności, stan rodzinny)."""


class WujekDobraRada:
    """Doradca finansowy wykorzystujący Claude AI"""
    
    def __init__(self, api_key):
        """
        Inicjalizuje doradcę z kluczem API
        
        Args:
            api_key: Klucz API Anthropic
        """
        try:
            self.llm = ChatAnthropic(
                anthropic_api_key=api_key,
                model="claude-3-5-haiku-20241022",
                temperature=0.8,
                max_tokens=256
            )
            logger.info("WujekDobraRada zainicjalizowany pomyślnie")
        except Exception as e:
            logger.error(f"Błąd inicjalizacji WujekDobraRada: {e}")
            raise
    
    def get_advice(self, game_state, recent_decision=None):
        """
        Generuje radę finansową na podstawie stanu gry
        
        Args:
            game_state: Aktualny stan gry gracza
            recent_decision: Opcjonalnie - ostatnia decyzja gracza
            
        Returns:
            String z radą od Wujka
        """
        try:
            logger.info(f"Generowanie rady dla gracza w wieku {game_state.get('age', 'unknown')}")
            
            prompt = self._create_advice_prompt(game_state, recent_decision)
            
            # Stwórz wiadomości dla Claude
            messages = [
                {"role": "system", "content": WUJEK_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
            
            # Wywołaj Claude API - użyj pełnej struktury wiadomości
            full_prompt = f"{WUJEK_SYSTEM_PROMPT}\n\nUser: {prompt}"
            response = self.llm.invoke(full_prompt)
            
            advice = response.content.strip()
            
            logger.info(f"Wygenerowano radę: {advice[:50]}...")
            return advice
            
        except Exception as e:
            logger.error(f"Błąd generowania rady: {e}")
            return self._get_fallback_advice(game_state)
    
    def _create_advice_prompt(self, game_state, recent_decision):
        """Tworzy prompt dla Wujka Dobrej Rady"""
        
        age = game_state.get('age', 25)
        sex = game_state.get('sex', 'male')
        income = game_state.get('income', 0)
        savings = game_state.get('savings', 0)
        zus = game_state.get('zus_contributions', 0)
        children = game_state.get('children', 0)
        marital_status = game_state.get('marital_status', 'singiel')
        work = game_state.get('work', 'bezrobotny')
        
        # Określ zwroty w zależności od płci
        gender_address = "kolego" if sex == 'male' else "koleżanko"
        gender_possessive = "Mój" if sex == 'male' else "Moja"
        
        # Przelicz składki ZUS na przybliżoną emeryturę
        estimated_pension = self._estimate_pension(zus, age, sex)
        
        prompt = f"""SYTUACJA GRACZA:
- Płeć: {sex} (używaj zwrotu "{gender_address}", "{gender_possessive} ci rada")
- Wiek: {age} lat
- Praca: {work}
- Miesięczny dochód: {income:.0f} PLN
- Oszczędności: {savings:.0f} PLN
- Składki ZUS zebrane: {zus:.0f} PLN
- Szacowana emerytura (przy obecnych składkach): ~{estimated_pension:.0f} PLN/mies.
- Stan cywilny: {marital_status}
- Dzieci: {children}

"""
        
        if recent_decision:
            prompt += f"OSTATNIA DECYZJA GRACZA:\n{recent_decision}\n\n"
        
        # Dodaj kontekst sytuacji
        if age < 30:
            prompt += "Gracz jest młody - ma czas na budowanie kapitału.\n"
        elif age < 50:
            prompt += "Gracz jest w środku kariery - kluczowy czas na oszczędzanie.\n"
        else:
            prompt += "Gracz zbliża się do emerytury - czas na zabezpieczenie kapitału.\n"
        
        if savings < income * 3:
            prompt += "UWAGA: Brak odpowiedniej poduszki finansowej!\n"
        
        if zus < (age - 18) * 12000:  # Bardzo uproszczone
            prompt += "UWAGA: Niskie składki ZUS - emerytura będzie skromna!\n"
        
        prompt += "\nDAJ KRÓTKĄ, PRAKTYCZNĄ RADĘ (max 3-4 zdania):"
        
        return prompt
    
    def _estimate_pension(self, total_contributions, current_age, sex='male'):
        """
        Prosta estymacja emerytury na podstawie składek
        
        Args:
            total_contributions: Łączne składki ZUS
            current_age: Obecny wiek
            sex: Płeć ('male' lub 'female')
            
        Returns:
            Szacowana miesięczna emerytura
        """
        # Wiek emerytalny zależy od płci w Polsce
        retirement_age = 65 if sex == 'male' else 60
        years_to_retirement = max(retirement_age - current_age, 1)
        
        # Bardzo uproszczone: dzielimy przez oczekiwaną długość emerytury w miesiącach
        # (zakładamy ~20 lat emerytury = 240 miesięcy)
        expected_months = 240
        
        estimated_pension = total_contributions / expected_months
        
        return estimated_pension
    
    def _get_fallback_advice(self, game_state):
        """
        Zwraca domyślną radę w przypadku błędu API
        
        Args:
            game_state: Stan gry
            
        Returns:
            Domyślna rada
        """
        age = game_state.get('age', 25)
        sex = game_state.get('sex', 'male')
        savings = game_state.get('savings', 0)
        income = game_state.get('income', 0)
        
        # Zwroty zależne od płci
        address = "kolego" if sex == 'male' else "koleżanko"
        possessive = "Mój" if sex == 'male' else "Moja"
        
        if age < 30:
            if savings < 10000:
                return f"Słuchaj {address}, w Twoim wieku najważniejsze to zacząć oszczędzać. Zacznij od małych kwot - nawet 200-300 zł miesięcznie robi różnicę!"
            else:
                return "Widzę, że już coś odkładasz - brawo! Teraz pomyśl o PPK w pracy, to darmowa dopłata od pracodawcy i państwa."
        elif age < 50:
            if income > 0 and savings < income * 3:
                return f"{possessive} ci rada - brakuje Ci poduszki finansowej. Staraj się mieć odłożone 3-6 pensji na czarną godzinę."
            else:
                return f"Pamiętaj {address}, emerytura z ZUS to często tylko połowa wypłaty. Warto dodać IKE czy IKZE z ulgą podatkową!"
        else:
            return "W Twoim wieku bezpieczeństwo przede wszystkim. Obligacje skarbowe lub spokojne lokaty - nie czas na ryzyko!"
