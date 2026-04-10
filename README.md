# Advanced Coin Toss Game 🪙

## Overview\n**CLI**: Complex coin toss game (OOP, betting, stats, persistence, bias, streaks).\n**Streamlit Web App**: Browser-based interactive version with sliders/buttons, real-time stats/history.\n\nCLI Features:\n- OOP: `Coin`, `StatsTracker`\n- CLI modes, betting ($100 start), JSON persistence (`stats.json`)\n- ASCII visuals (colorama)\n\nStreamlit Features:\n- Sidebar: Bias slider, bet input, reset\n- Main: Metrics (balance/winrate/streaks), history table, HEADS/TAILS buttons\n- Animation, persistence across sessions
- **OOP Architecture**: `Coin` (biased tosses), `GameSession` (play logic), `StatsTracker` (JSON persistence)
- **CLI Interface**: `argparse` with modes (single, interactive, bestof, stats, history, reset)
- **Betting System**: Virtual currency ($100 start), win/loss tracking
- **Stats & Streaks**: Global persistence, win rate, longest/current streaks
- **Visuals**: ASCII flip animation, colored output (`colorama`)
- **Advanced Features**: Bias config, best-of-N series, history view, graceful exit

## Installation
```bash
pip install -r requirements.txt
```

## Quick Start\n```bash\n# Install deps\npython -m pip install -r requirements.txt\n\n# Run CLI interactive mode (default)\npython coin_toss.py\n\n# Run Streamlit Web App\nstreamlit run streamlit_coin_toss.py\n```

# Single toss with bias (60% heads)
python coin_toss.py --mode single --bias 0.6 --bet 10

# View stats
python coin_toss.py --mode stats

# Best of 5
python coin_toss.py --mode bestof --bestof 5 --bet 5

# History (last 20)
python coin_toss.py --mode history --history 20
```

## Interactive Mode Commands
```
> toss 10     # Toss with $10 bet
> bestof 7 5  # Best of 7, $5 bet
> stats       # Show stats
> history 15  # Last 15 tosses
> balance     # Current balance
> quit        # Exit (auto-saves)
```

## Stats Persistence
- File: `stats.json` (auto-created)
- Tracks: tosses, streaks, balance, history (last 100)

## Features Comparison
| Feature | Original | New |
|---------|----------|-----|
| Lines of Code | ~10 | ~300 |
| OOP | No | Yes (3 classes) |
| Persistence | No | JSON stats |
| CLI Args | No | Full argparse |
| Betting/Streaks | No | Yes |
| Visuals | Plain text | ASCII + Colors |
| Modes | Single blind | 6+ modes |

## Screenshots (Text-based)
```
=== GAME STATS ===
Total Tosses: 42
Heads: 25 (59.5%)
Tails: 17
Current Streak: HEADS x3
Longest Streak: TAILS x7
Balance: $145
==================
```

```
   ,--.     (flip animation)
  (_  _)  
  `--'    
  RESULT: HEADS  
yes, go ahead fearlessly
```

## Customization
- Bias: `--bias 0.7` (P(heads)=70%)
- Reset: `--mode reset`

Enjoy the upgraded complexity! 🎰


