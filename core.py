import random
import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

@dataclass
class TossResult:
    outcome: str
    choice: str
    won: bool
    message: str

class Coin:
    def __init__(self, bias_heads: float = 0.5):
        self.bias_heads = max(0.0, min(1.0, bias_heads))

    def toss(self, choice: str) -> TossResult:
        if self.bias_heads == 0.5:
            outcome = random.choice(['heads', 'tails'])
        else:
            outcome = 'heads' if random.random() < self.bias_heads else 'tails'
        
        won = (outcome == choice.lower())
        message = "yes, go ahead fearlessly" if won else "wait breathe, not all fights are destined to be fought"
        
        return TossResult(outcome=outcome, choice=choice.lower(), won=won, message=message)

class StatsTracker:
    def __init__(self, data_file: str = 'stats.json'):
        self.data_file = data_file
        self.stats = self._load_stats()

    def _load_stats(self) -> Dict:
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {
            'total_tosses': 0,
            'wins': 0,
            'losses': 0,
            'balance': 100.0,
            'history': [],
            'current_streak': {'side': None, 'count': 0},
            'longest_streak': {'side': None, 'count': 0}
        }

    def _save_stats(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.stats, f, indent=2)

    def record_toss(self, result: TossResult, bet: float = 10.0):
        self.stats['total_tosses'] += 1
        self.stats['history'].append({
            'outcome': result.outcome,
            'choice': result.choice,
            'won': result.won,
            'timestamp': random.randint(1000000000, 2000000000)  # Mock timestamp
        })
        if len(self.stats['history']) > 100:
            self.stats['history'] = self.stats['history'][-100:]

        if result.won:
            self.stats['wins'] += 1
            self.stats['balance'] += bet
        else:
            self.stats['losses'] += 1
            self.stats['balance'] -= bet * 0.5  # House edge

        # Update streaks
        side = result.outcome
        if self.stats['current_streak']['side'] == side:
            self.stats['current_streak']['count'] += 1
        else:
            self.stats['current_streak'] = {'side': side, 'count': 1}
        
        if (self.stats['current_streak']['count'] > 
            self.stats.get('longest_streak', {'count': 0})['count']):
            self.stats['longest_streak'] = self.stats['current_streak'].copy()

        self._save_stats()

    def get_stats(self) -> Dict:
        total = self.stats['total_tosses']
        win_rate = (self.stats['wins'] / total * 100) if total > 0 else 0
        stats = self.stats.copy()
        stats['win_rate'] = f"{win_rate:.1f}%"
        return stats

    def reset(self):
        self.stats = self._load_stats()  # Reset to defaults
        self._save_stats()

# Util for ASCII animation (CLI/Streamlit compatible)
def ascii_flip_animation():
    animations = [
        "   ,--.    ",
        "  (_  _)   ",
        "   `--'    ",
        "   FLIP!   "
    ]
    return "\\n".join(animations)

# Example usage for testing
if __name__ == "__main__":
    coin = Coin(bias_heads=0.5)
    stats = StatsTracker()
    result = coin.toss("heads")
    print(f"Outcome: {result.outcome}, Won: {result.won}")
    stats.record_toss(result)
    print(stats.get_stats())
