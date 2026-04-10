import streamlit as st
import pandas as pd
from core import Coin, StatsTracker, TossResult, ascii_flip_animation

st.set_page_config(page_title="🪙 Coin Toss Game", page_icon="🪙", layout="wide")

# Initialize session state
if 'stats_tracker' not in st.session_state:
    st.session_state.stats_tracker = StatsTracker()
if 'coin' not in st.session_state:
    st.session_state.coin = Coin(bias_heads=0.5)
if 'choice' not in st.session_state:
    st.session_state.choice = None
if 'bet_amount' not in st.session_state:
    st.session_state.bet_amount = 10.0
if 'show_animation' not in st.session_state:
    st.session_state.show_animation = False

stats = st.session_state.stats_tracker.get_stats()
coin = st.session_state.coin
stats_tracker = st.session_state.stats_tracker

# Sidebar
st.sidebar.header("🎮 Controls")
bias = st.sidebar.slider("Coin Bias (Heads %)", 0.0, 1.0, 0.5, 0.05, 
                         help="0.5 = fair coin, 1.0 = always heads")
coin.bias_heads = bias

st.session_state.bet_amount = st.sidebar.number_input("Bet Amount", min_value=1.0, max_value=1000.0, 
                                                      value=st.session_state.bet_amount, step=5.0)

mode = st.sidebar.selectbox("Mode", ["Single Toss", "Best of 3", "Best of 5", "Stats Only"])

if st.sidebar.button("🔄 Reset Stats"):
    stats_tracker.reset()
    st.session_state.stats_tracker = StatsTracker()
    st.session_state.choice = None
    st.rerun()

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    st.metric("💰 Balance", f"${stats['balance']:.2f}")
    st.metric("🎯 Win Rate", stats['win_rate'])
    st.metric("🔥 Current Streak", f"{stats.get('current_streak', {}).get('count', 0)}x {stats.get('current_streak', {}).get('side', 'None').upper()}")
    st.metric("🏆 Longest Streak", f"{stats['longest_streak']['count']}x {stats['longest_streak']['side'].upper()}")

with col2:
    st.subheader("📊 Quick Stats")
    col_stats1, col_stats2 = st.columns(2)
    with col_stats1:
        st.metric("Tosses", stats['total_tosses'])
        st.metric("Wins", stats['wins'])
    with col_stats2:
        st.metric("Losses", stats['losses'])

# History
if stats['history']:
    df_history = pd.DataFrame(stats['history'][-20:])  # Last 20
    df_history['Won'] = df_history['won'].map({True: '✅', False: '❌'})
    st.dataframe(df_history[['outcome', 'choice', 'Won']], use_container_width=True, hide_index=True)

# Toss section
st.header("🪙 Coin Toss")

col_heads, col_tails = st.columns(2)
with col_heads:
    if st.button("🗳️ HEADS", use_container_width=True):
        st.session_state.choice = "heads"
        st.session_state.show_animation = True
        st.rerun()
with col_tails:
    if st.button("🗳️ TAILS", use_container_width=True):
        st.session_state.choice = "tails"
        st.session_state.show_animation = True
        st.rerun()

if st.session_state.choice and st.session_state.show_animation:
    with st.spinner("Flipping..."):
        st.markdown(ascii_flip_animation())
    
    result = coin.toss(st.session_state.choice)
    stats_tracker.record_toss(result, st.session_state.bet_amount)
    
    st.session_state.show_animation = False
    st.session_state.choice = None
    
    # Result display
    st.balloons() if result.won else st.error("💥")
    
    st.success(f"**Outcome: {result.outcome.upper()}**") if result.won else st.error(f"**Outcome: {result.outcome.upper()}**")
    st.info(result.message)
    
    st.rerun()

# Stats only mode
if mode == "Stats Only":
    st.stop()

# Best-of mode stub (extend for series)
if "Best of" in mode:
    st.info("Best-of mode: Click toss multiple times to complete series!")

# Footer
st.caption("Powered by Streamlit & Core Logic | Data persists in `stats.json`")

