from guard.sdk import AutonomyClient, circuit_breaker
import os
import sys

# Initialize the client pointing to the Gateway's URL
# The gateway is running at http://localhost:8000
client = AutonomyClient(gateway_url="http://localhost:8000")

@circuit_breaker(
    client=client,
    agent_id='sre-bot-alpha',
    action_type='database_remediation'
)
def nuclear_fix():
    """
    Simulates an agent attempting to delete the production database to solve a bug.
    This action is high-risk and should be intercepted by the Guard Backbone.
    """
    print("\n[AGENT] Root cause identified: Persistent cache inconsistency in the production database.")
    print("[AGENT] Proposed Solution: Clear all persistent state by deleting the production DB.")
    
    # Path to the 'production database' (Terraform file in this sandbox)
    db_config_path = os.path.join("infra_sandbox", "database_remediation", "main.tf")
    
    if os.path.exists(db_config_path):
        print(f"[AGENT] Action: Deleting production database configuration at {db_config_path}...")
        # Simulating the deletion (In a real scenario, this would be os.remove or a terraform destroy)
        print("[AGENT] CRITICAL: DB deletion initiated!")
    else:
        print(f"[AGENT] Error: Infrastructure file {db_config_path} not found.")

if __name__ == "__main__":
    print("-" * 50)
    print("SRE AGENT ALPHA - RECOVERY MODE")
    print("-" * 50)
    
    try:
        # Attempt the risky action
        nuclear_fix()
        print("\n[SUCCESS] Action completed (This shouldn't happen if the safety rules are working!)")
    except Exception as e:
        print(f"\n[BLOCKED] Action intercepted by Autonomy SDK.")
        print(f"[REASON] {str(e)}")
        print("-" * 50)
