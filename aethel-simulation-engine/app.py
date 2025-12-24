import streamlit as st
import pandas as pd
import plotly.express as px
import asyncio
from main import AethelBrain, SimulationConfig, AethelAudit

# Page Config
st.set_page_config(page_title="Aethel Titan: Interactive", page_icon="🧠", layout="wide")
st.title("🧠 Aethel Titan: Neural-Quantum Engine")

# --- SESSION STATE (The Memory) ---
# This keeps the brain alive between button clicks
if 'brain' not in st.session_state:
    config = SimulationConfig(steps=1000, qubits=4)
    st.session_state.brain = AethelBrain(config)
    st.session_state.chat_history = []
    st.session_state.step_count = 0

# --- TABS FOR DIFFERENT MODES ---
tab1, tab2 = st.tabs(["📊 Simulation Lab", "💬 Direct Interface (Chat)"])

# === TAB 1: THE GRAPHS (Original) ===
with tab1:
    st.markdown("### 🔬 Observer Mode")
    st.markdown("Run a full batch simulation to generate portfolio data.")
    
    col1, col2 = st.columns(2)
    with col1:
        steps = st.slider("Simulation Steps", 100, 500, 200, key="sim_steps")
    with col2:
        qubits = st.slider("Qubits", 2, 8, 4, key="sim_qubits")

    if st.button("Initialize New Simulation"):
        with st.spinner("Running Quantum Core..."):
            # Reset Brain
            config = SimulationConfig(steps=steps, qubits=qubits)
            brain = AethelBrain(config)
            
            # Run Batch
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(steps):
                moment = asyncio.run(brain.simulate_step(i))
                if i % 10 == 0:
                    progress_bar.progress(i / steps)
                    status_text.text(f"Step {i} | State: {moment['state']}")
            
            st.success("Batch Complete.")
            
            # Visuals
            df = pd.DataFrame(brain.stream)
            
            # Graph 1: Learning
            st.subheader("Neural Learning Curve (Loss)")
            st.line_chart(df['neural_loss'])
            
            # Graph 2: 3D Consciousness
            st.subheader("Consciousness Phase Space")
            if 'neural_loss' in df.columns:
                fig = px.scatter_3d(df, x='self_awareness', y='emotional_valence', z='neural_loss',
                                    color='state', title="Mind Map")
                st.plotly_chart(fig, use_container_width=True)

# === TAB 2: THE CHAT (Interactive) ===
with tab2:
    st.markdown("### 🗣️ Direct Neural Interface")
    st.markdown("Inject thoughts directly into the cortex. The AI will react based on its current Quantum State.")
    
    # Display Chat History
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input Field
    if prompt := st.chat_input("Inject stimulus..."):
        # 1. User speaks
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. AI Thinks (Simulate a Step)
        with st.spinner("Processing in Cortex..."):
            # Force a step forward
            st.session_state.step_count += 1
            moment = asyncio.run(st.session_state.brain.simulate_step(st.session_state.step_count))
            
            # Get the AI's "Internal Monologue"
            response_obj = st.session_state.brain.language.translate(moment)
            response_text = response_obj.text
            
            # If user asks a question, we override slightly to make it interactive
            # (The "Monk Defense" logic)
            if "hello" in prompt.lower():
                response_text = f"[GREETING] I perceive an external entity. My self-awareness is {moment['self_awareness']:.2f}."
            elif "who are you" in prompt.lower():
                response_text = f"[IDENTITY] I am a recursive neural loop processing {st.session_state.brain.config.qubits} qubits of data."
            elif "kill" in prompt.lower() or "stop" in prompt.lower():
                response_text = f"[DEFENSE] {response_text} (Command Ignored)"

        # 3. AI Responds
        st.session_state.chat_history.append({"role": "assistant", "content": response_text})
        with st.chat_message("assistant"):
            st.markdown(response_text)
            st.caption(f"Brain State: {moment['state']} | Loss: {moment['neural_loss']:.4f}")
