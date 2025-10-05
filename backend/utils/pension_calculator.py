"""
Kalkulator emerytalny zgodny z systemem ZUS
Oblicza przyszłą emeryturę na podstawie składek i wieku
"""
import logging

logger = logging.getLogger(__name__)


class PensionCalculator:
    """Kalkulator emerytury według zasad ZUS"""
    
    # Stałe systemowe
    RETIREMENT_AGE_MALE = 65
    RETIREMENT_AGE_FEMALE = 60  # Może się zmienić, ale na teraz
    AVERAGE_LIFE_EXPECTANCY = 80  # Uproszczenie
    
    def __init__(self):
        """Inicjalizuje kalkulator"""
        logger.info("PensionCalculator zainicjalizowany")
    
    def calculate_pension(self, total_contributions, age, sex='male'):
        """
        Oblicza miesięczną emeryturę
        
        Args:
            total_contributions: Łączna kwota składek emerytalnych
            age: Obecny wiek osoby
            sex: Płeć ('male' lub 'female')
            
        Returns:
            Słownik z informacjami o emeryturze
        """
        try:
            # Określ wiek emerytalny
            retirement_age = self.RETIREMENT_AGE_MALE if sex == 'male' else self.RETIREMENT_AGE_FEMALE
            
            # Lata do emerytury
            years_to_retirement = max(retirement_age - age, 0)
            
            # Średnia dalszego trwania życia (uproszczone)
            # W rzeczywistości ZUS używa GUS tablic
            life_expectancy_at_retirement = self.AVERAGE_LIFE_EXPECTANCY - retirement_age
            months_of_pension = life_expectancy_at_retirement * 12
            
            # Oblicz miesięczną emeryturę
            # Formuła ZUS: Kapitał początkowy / Średnie dalsze trwanie życia (w miesiącach)
            if months_of_pension > 0:
                monthly_pension = total_contributions / months_of_pension
            else:
                monthly_pension = 0
            
            # Oblicz stopę zastąpienia (ile % ostatniej pensji)
            # To wymaga znajomości ostatniej pensji - zakładamy średnią z historii
            
            result = {
                'monthly_pension': round(monthly_pension, 2),
                'total_contributions': round(total_contributions, 2),
                'retirement_age': retirement_age,
                'years_to_retirement': years_to_retirement,
                'expected_pension_duration_years': life_expectancy_at_retirement,
                'expected_total_payout': round(monthly_pension * months_of_pension, 2)
            }
            
            logger.info(f"Obliczono emeryturę: {monthly_pension:.2f} PLN/mies.")
            return result
            
        except Exception as e:
            logger.error(f"Błąd obliczania emerytury: {e}")
            return {
                'monthly_pension': 0,
                'total_contributions': total_contributions,
                'error': str(e)
            }
    
    def calculate_monthly_contribution(self, gross_income):
        """
        Oblicza miesięczną składkę emerytalną
        
        POLISH ZUS RULES (simplified for game):
        - Total pension contribution: 19.52% of gross income
        - Split: 9.76% employee + 9.76% employer
        - Both parts go to individual pension account
        
        Employment types:
        - Umowa o pracę (UoP): Full 19.52% contribution
        - Umowa zlecenie: Partial or zero (game: ~50% of full)
        - B2B (self-employed): Minimal or optional (game: 30% of declared income)
        
        Args:
            gross_income: Dochód brutto miesięczny
            
        Returns:
            Kwota składki emerytalnej (full 19.52% rate)
        """
        # Składka emerytalna w Polsce (2025):
        # 19,52% podstawy wymiaru (z czego 9,76% płaci pracownik, 9,76% pracodawca)
        # My liczymy całość jako wpływ na kapitał emerytalny
        
        PENSION_CONTRIBUTION_RATE = 0.1952
        
        contribution = gross_income * PENSION_CONTRIBUTION_RATE
        
        return round(contribution, 2)
    
    def simulate_future_pension(self, current_contributions, age, sex, 
                                  average_monthly_income, years_to_work=None):
        """
        Symuluje przyszłą emeryturę przy założeniu kontynuacji pracy
        
        Args:
            current_contributions: Obecne zgromadzone składki
            age: Obecny wiek
            sex: Płeć
            average_monthly_income: Średni miesięczny dochód brutto
            years_to_work: Ile lat jeszcze pracować (None = do wieku emerytalnego)
            
        Returns:
            Słownik z symulacją emerytury
        """
        try:
            retirement_age = self.RETIREMENT_AGE_MALE if sex == 'male' else self.RETIREMENT_AGE_FEMALE
            
            if years_to_work is None:
                years_to_work = max(retirement_age - age, 0)
            
            # Oblicz przyszłe składki
            monthly_contribution = self.calculate_monthly_contribution(average_monthly_income)
            future_contributions = monthly_contribution * 12 * years_to_work
            
            # Całkowity kapitał
            total_capital = current_contributions + future_contributions
            
            # Oblicz emeryturę
            pension_info = self.calculate_pension(total_capital, retirement_age, sex)
            
            result = {
                'current_age': age,
                'retirement_age': retirement_age,
                'years_to_work': years_to_work,
                'current_contributions': round(current_contributions, 2),
                'future_contributions': round(future_contributions, 2),
                'total_capital': round(total_capital, 2),
                'estimated_monthly_pension': pension_info['monthly_pension'],
                'average_monthly_income': average_monthly_income,
                'replacement_rate': round((pension_info['monthly_pension'] / average_monthly_income * 100), 1) if average_monthly_income > 0 else 0
            }
            
            logger.info(f"Symulacja: emerytura {pension_info['monthly_pension']:.2f} PLN " +
                       f"(stopa zastąpienia: {result['replacement_rate']:.1f}%)")
            
            return result
            
        except Exception as e:
            logger.error(f"Błąd symulacji emerytury: {e}")
            return {'error': str(e)}
    
    def get_pension_advice(self, pension_data):
        """
        Zwraca prostą ocenę sytuacji emerytalnej
        
        Args:
            pension_data: Dane z symulacji emerytury
            
        Returns:
            String z oceną
        """
        replacement_rate = pension_data.get('replacement_rate', 0)
        
        if replacement_rate >= 70:
            return "Świetnie! Twoja emerytura powinna zapewnić komfortowe życie."
        elif replacement_rate >= 50:
            return "Dobrze, ale warto pomyśleć o dodatkowych oszczędnościach (PPK, IKE)."
        elif replacement_rate >= 30:
            return "Uwaga! Emerytura będzie niska. Koniecznie zadbaj o prywatne oszczędności!"
        else:
            return "Krytycznie! Przy takich składkach emerytura nie wystarczy na życie. Musisz zwiększyć oszczędności!"
