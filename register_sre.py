import asyncio
from guard.sdk import AutonomyClient

def main():
    # Connect to the Guard Gateway running at http://localhost:8000
    client = AutonomyClient(server_url="http://localhost:8000")
    
    # Register the agent's cryptographic identity
    new_id = client.register_agent_sync(
        agent_id="sre-bot-alpha",
        attributes={"role": "infrastructure-admin"}
    )
    
    print(f"Successfully registered agent with ID: {new_id}")

if __name__ == "__main__":
    main()
