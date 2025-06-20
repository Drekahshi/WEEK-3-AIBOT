#!/usr/bin/env python3
"""
DeFi Genie MVP - Your friendly DeFi companion! 🧞‍♂️
A terminal-based bot that helps users explore DeFi opportunities.
"""

import time
import sys
from typing import Dict, List, Tuple

class DeFiGenie:
    def __init__(self):
        self.user_risk_appetite = None
        self.static_data = self._load_static_data()
        
    def _load_static_data(self) -> Dict:
        """Load static APY and DeFi data for simulations"""
        return {
            'staking_pools': {
                'ETH 2.0': {'apy': 4.5, 'risk': 'low', 'min_amount': 32},
                'Cardano (ADA)': {'apy': 5.2, 'risk': 'low', 'min_amount': 10},
                'Solana (SOL)': {'apy': 6.8, 'risk': 'medium', 'min_amount': 1},
                'Polkadot (DOT)': {'apy': 12.5, 'risk': 'medium', 'min_amount': 1},
                'Cosmos (ATOM)': {'apy': 14.2, 'risk': 'medium', 'min_amount': 1}
            },
            'yield_farms': {
                'Uniswap V3 ETH/USDC': {'apy': 25.3, 'risk': 'high', 'tvl': '2.1B'},
                'PancakeSwap BNB/BUSD': {'apy': 18.7, 'risk': 'medium', 'tvl': '850M'},
                'Curve 3Pool': {'apy': 8.9, 'risk': 'low', 'tvl': '1.2B'},
                'Compound USDC': {'apy': 3.2, 'risk': 'low', 'tvl': '3.8B'},
                'Aave ETH': {'apy': 2.1, 'risk': 'low', 'tvl': '5.2B'}
            },
            'insurance_pools': {
                'Nexus Mutual': {'coverage_ratio': 0.95, 'premium': 2.6, 'risk': 'low'},
                'Cover Protocol': {'coverage_ratio': 0.90, 'premium': 3.2, 'risk': 'medium'},
                'Unslashed Finance': {'coverage_ratio': 0.85, 'premium': 4.1, 'risk': 'high'}
            }
        }
        
    def typewriter_print(self, text: str, delay: float = 0.03):
        """Print text with typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def print_banner(self):
        """Display the DeFi Genie banner"""
        banner = """
    ╔═══════════════════════════════════════╗
    ║           🧞‍♂️ DeFi Genie 🧞‍♂️           ║
    ║      Your Magical DeFi Companion      ║
    ╚═══════════════════════════════════════╝
        """
        print(banner)
        
    def introduce_self(self):
        """Friendly introduction with personality"""
        self.typewriter_print("\n✨ *POOF!* ✨")
        time.sleep(0.5)
        self.typewriter_print("\nGreetings, intrepid DeFi explorer! 🌟")
        self.typewriter_print("I am the DeFi Genie, summoned to grant your wishes for financial wisdom!")
        self.typewriter_print("\n🎯 I can illuminate the path through the mystical world of Decentralized Finance,")
        self.typewriter_print("   from the treasures of staking rewards to the bountiful harvests of yield farming! 💰")
        self.typewriter_print("\nBut first, tell me, what is your spirit for adventure...?")
        
    def get_risk_appetite(self):
        """Ask user about their risk tolerance using numerical input"""
        self.typewriter_print("\n🎲 YOUR SPIRIT FOR ADVENTURE 🎲")
        self.typewriter_print("═" * 40)
        
        options = {
            '1': 'A Cautious Explorer 🛡️  (I prefer safe, steady voyages)',
            '2': 'A Bold Adventurer 🎯   (I embrace calculated risks for greater rewards)',
            '3': 'A Daring Treasure Hunter 🚀 (I seek the highest fortunes, whatever the peril!)'
        }
        
        print("\nHow would you describe your approach to the treasures of DeFi?")
        for key, desc in options.items():
            print(f"  {key}. {desc}")
            
        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice in options:
                risk_map = {'1': 'low', '2': 'medium', '3': 'high'}
                self.user_risk_appetite = risk_map[choice]
                self.typewriter_print(f"\n✅ Understood! A {options[choice].split(' ')[2]} you are. Your wish is my command!")
                break
            else:
                print("❌ Please select a valid number from the scrolls (1, 2, or 3)")
                
    def show_menu(self):
        """Display the main menu of services"""
        self.typewriter_print("\n🎪 THE GENIE'S MENU OF MARVELS 🎪")
        self.typewriter_print("═" * 40)
        
        menu_items = [
            "1. 📊 Gaze into the Staking Crystal Ball",
            "2. 💹 Chart the Stars of ROI",
            "3. 🌾 Unearth Yield Farming Secrets",
            "4. 🛡️  Weave a Shield of Insurance",
            "5. 🚪 Return to the Mortal World"
        ]
        
        print("\nWhat secrets shall we uncover together?")
        for item in menu_items:
            print(f"  {item}")
            
        return input("\nEnter your choice (1-5): ").strip()
        
    def staking_calculator(self):
        """Calculate staking rewards"""
        self.typewriter_print("\n📊 THE STAKING CRYSTAL BALL 📊")
        self.typewriter_print("═" * 40)
        
        suitable_pools = {k: v for k, v in self.static_data['staking_pools'].items() 
                          if v['risk'] == self.user_risk_appetite or self.user_risk_appetite == 'high'}
        
        if not suitable_pools:
            suitable_pools = self.static_data['staking_pools']
            
        print(f"\n🎯 As a {self.user_risk_appetite} risk-taker, the Crystal Ball reveals these pools for you:")
        print("\nAvailable Staking Pools:")
        for i, (pool, data) in enumerate(suitable_pools.items(), 1):
            risk_emoji = {'low': '🟢', 'medium': '🟡', 'high': '🔴'}
            print(f"  {i}. {pool}")
            print(f"     APY: {data['apy']}% | Risk: {risk_emoji[data['risk']]} {data['risk'].title()}")
            print(f"     Minimum to Stake: {data['min_amount']} tokens")
            
        try:
            amount = float(input("\n💰 How many coins do you wish to stake?: "))
            duration = int(input("⏰ For how many suns and moons (in days)?: "))
            
            print(f"\n🧮 GAZING INTO THE FUTURE... YOUR {duration}-DAY STAKING PROJECTIONS:")
            print("─" * 50)
            
            for pool, data in suitable_pools.items():
                if amount >= data['min_amount']:
                    daily_rate = data['apy'] / 365 / 100
                    projected_return = amount * daily_rate * duration
                    final_amount = amount + projected_return
                    
                    print(f"\n{pool}:")
                    print(f"  💵 Your Stake: ${amount:,.2f}")
                    print(f"  📈 Your Projected Reward: ${projected_return:,.2f}")
                    print(f"  💎 Your Final Treasure: ${final_amount:,.2f}")
                    print(f"  📊 Annual Percentage Yield: {data['apy']}%")
                    
        except ValueError:
            print("❌ The Crystal Ball is cloudy... Please provide valid numbers!")
            
    def roi_simulator(self):
        """Simulate ROI across different scenarios"""
        self.typewriter_print("\n💹 CHARTING THE STARS OF ROI 💹")
        self.typewriter_print("═" * 40)
        
        try:
            initial_investment = float(input("\n💰 What is the initial treasure you wish to invest ($)?: "))
            
            scenarios = {
                'Cautious Explorer': {'monthly_return': 0.5, 'volatility': 0.1},
                'Bold Adventurer': {'monthly_return': 2.0, 'volatility': 0.3},
                'Daring Treasure Hunter': {'monthly_return': 5.0, 'volatility': 0.8}
            }
            
            print(f"\n📊 The stars predict the following fortunes for your ${initial_investment:,.2f}:")
            print("═" * 60)
            
            for scenario, data in scenarios.items():
                print(f"\n{scenario.upper()} STRATEGY:")
                print("─" * 30)
                
                current_amount = initial_investment
                for month in [1, 3, 6, 12]:
                    monthly_growth = data['monthly_return'] / 100
                    for _ in range(month):
                        current_amount *= (1 + monthly_growth)
                        
                    roi_percent = ((current_amount - initial_investment) / initial_investment) * 100
                    print(f"  After {month:2d} month(s): ${current_amount:8,.2f} (ROI: {roi_percent:+6.1f}%)")
                    current_amount = initial_investment
                    
        except ValueError:
            print("❌ The stars are not aligned... Please provide a valid investment amount!")
            
    def yield_farming_advice(self):
        """Provide yield farming recommendations"""
        self.typewriter_print("\n🌾 UNEARTHING YIELD FARMING SECRETS 🌾")
        self.typewriter_print("═" * 40)
        
        suitable_farms = {}
        if self.user_risk_appetite == 'low':
            suitable_farms = {k: v for k, v in self.static_data['yield_farms'].items() 
                              if v['risk'] in ['low']}
        elif self.user_risk_appetite == 'medium':
            suitable_farms = {k: v for k, v in self.static_data['yield_farms'].items() 
                              if v['risk'] in ['low', 'medium']}
        else:
            suitable_farms = self.static_data['yield_farms']
            
        print(f"\n🎯 The most bountiful harvests for a {self.user_risk_appetite.title()} adventurer:")
        print("═" * 70)
        
        sorted_farms = sorted(suitable_farms.items(), key=lambda x: x[1]['apy'], reverse=True)
        
        for i, (farm, data) in enumerate(sorted_farms, 1):
            risk_emoji = {'low': '🟢', 'medium': '🟡', 'high': '🔴'}
            print(f"\n{i}. {farm}")
            print(f"   📈 Annual Percentage Yield: {data['apy']}%")
            print(f"   🎯 Risk Level: {risk_emoji[data['risk']]} {data['risk'].title()}")
            print(f"   💰 Total Value Locked (TVL): ${data['tvl']}")
            
            if data['risk'] == 'low':
                print(f"   💡 Genie's Whisper: A tranquil stream of steady, predictable returns!")
            elif data['risk'] == 'medium':
                print(f"   💡 Genie's Whisper: A river of opportunity with a fine balance of risk and reward.")
            else:
                print(f"   💡 Genie's Whisper: A tempest of high risk and high reward - watch the tides closely!")
                
        try:
            choice = input(f"\nWould you like to foresee the returns for any of these farms? (1-{len(sorted_farms)} or 0 to skip): ")
            if choice.isdigit() and 1 <= int(choice) <= len(sorted_farms):
                selected_farm = sorted_farms[int(choice) - 1]
                farm_data = selected_farm[1]
                
                amount = float(input(f"\n💰 How much will you invest in the {selected_farm[0]} farm?: $"))
                
                print(f"\n🧮 FORESEEING YOUR HARVEST:")
                print("─" * 40)
                
                for period in [1, 7, 30, 90, 365]:
                    daily_rate = farm_data['apy'] / 365 / 100
                    returns = amount * daily_rate * period
                    total = amount + returns
                    
                    period_name = f"{period} day{'s' if period > 1 else ''}"
                    print(f"  {period_name:>8}: ${returns:8.2f} profit (Total: ${total:8.2f})")
                    
        except (ValueError, IndexError):
            print("Skipping the harvest forecast...")
            
    def insurance_simulation(self):
        """Simulate insurance pool coverage"""
        self.typewriter_print("\n🛡️ WEAVING A SHIELD OF INSURANCE 🛡️")
        self.typewriter_print("═" * 40)
        
        print("\nProtect your hard-won treasure with a shield of insurance!")
        print("\nAvailable Magical Shields:")
        
        for i, (pool, data) in enumerate(self.static_data['insurance_pools'].items(), 1):
            risk_emoji = {'low': '🟢', 'medium': '🟡', 'high': '🔴'}
            print(f"\n{i}. {pool}")
            print(f"   🛡️  Coverage Strength: {data['coverage_ratio']*100}%")
            print(f"   💳 Annual Tribute: {data['premium']}%")
            print(f"   🎯 Risk Rating: {risk_emoji[data['risk']]} {data['risk'].title()}")
            
        try:
            portfolio_value = float(input("\n💰 What is the value of the treasure you wish to shield ($)?: "))
            
            print(f"\n📊 ANALYZING THE SHIELD'S STRENGTH FOR ${portfolio_value:,.2f}:")
            print("═" * 60)
            
            for pool, data in self.static_data['insurance_pools'].items():
                annual_premium = portfolio_value * (data['premium'] / 100)
                coverage_amount = portfolio_value * data['coverage_ratio']
                uncovered_amount = portfolio_value - coverage_amount
                
                print(f"\n{pool.upper()}:")
                print(f"  💳 Annual Tribute: ${annual_premium:,.2f}")
                print(f"  🛡️  Shielded Amount: ${coverage_amount:,.2f}")
                print(f"  ⚠️  Unshielded Amount: ${uncovered_amount:,.2f}")
                print(f"  📊 Monthly Cost: ${annual_premium/12:,.2f}")
                
                if data['risk'] == 'low':
                    print(f"  💡 Genie's Assessment: The most steadfast shield, with a lower risk of claim denial.")
                elif data['risk'] == 'medium':
                    print(f"  💡 Genie's Assessment: A well-balanced shield of cost and reliability.")
                else:
                    print(f"  💡 Genie's Assessment: A more affordable shield, but with a higher risk should you need to make a claim.")
                    
        except ValueError:
            print("❌ The magic is failing... Please provide a valid portfolio value!")
            
    def farewell(self):
        """Say goodbye to the user"""
        self.typewriter_print("\n✨ Thank you for seeking the wisdom of the DeFi Genie! ✨")
        self.typewriter_print("🧞‍♂️ May your yields be ever bountiful and your risks always calculated!")
        self.typewriter_print("💰 Remember: My whispers are for educational purposes - always Do Your Own Research!")
        self.typewriter_print("\n*With a final nod, the genie swirls back into the lamp...* 🏺")
        
    def run(self):
        """Main bot loop"""
        self.print_banner()
        self.introduce_self()
        self.get_risk_appetite()
        
        while True:
            try:
                choice = self.show_menu()
                
                if choice == '1':
                    self.staking_calculator()
                elif choice == '2':
                    self.roi_simulator()
                elif choice == '3':
                    self.yield_farming_advice()
                elif choice == '4':
                    self.insurance_simulation()
                elif choice == '5':
                    self.farewell()
                    break
                else:
                    print("❌ An invalid choice! Please select a number from 1 to 5 from the Genie's menu.")
                    
                input("\nPress Enter to return to the Genie's Menu of Marvels...")
                print("\n" + "="*50)
                
            except KeyboardInterrupt:
                print("\n\n🧞‍♂️ The Genie senses your urgency to depart... Farewell!")
                break
            except Exception as e:
                print(f"\n❌ A wild sandstorm has appeared! Something went wrong: {e}")
                print("Let's try that again...")

def main():
    """Entry point for the DeFi Genie bot"""
    print("🚀 Summoning the DeFi Genie...")
    time.sleep(1)
    
    genie = DeFiGenie()
    genie.run()

if __name__ == "__main__":
    main()