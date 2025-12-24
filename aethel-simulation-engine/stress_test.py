import asyncio
from main import AethelBrain, SimulationConfig

async def run_stress_test():
    print("⚡ RUNNING TITAN STRESS TEST ⚡")
    brain = AethelBrain(SimulationConfig(steps=100, qubits=8))
    brain.self_awareness = 0.99 
    print("\nInjecting Paradox...")
    moment = await brain.simulate_step(1)
    response = brain.language.translate(moment)
    print(f"🧠 Aethel: \"{response.text}\"")

if __name__ == "__main__":
    asyncio.run(run_stress_test())
