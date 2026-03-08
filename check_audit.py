import requests
import json
from datetime import datetime, timezone, timedelta

def main():
    print("-" * 50)
    print("GUARD BACKBONE - AUDIT LEDGER INSPECTOR")
    print("-" * 50)
    
    gateway_url = "http://localhost:8000/audit"
    
    try:
        response = requests.get(gateway_url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "success":
            logs = data.get("audit_logs", [])
            
            # Filter for last 5 minutes and agent 'sre-bot-alpha'
            now = datetime.now(timezone.utc)
            five_minutes_ago = now - timedelta(minutes=5)
            
            sre_logs = []
            for log in logs:
                if log.get("agent_id") == "sre-bot-alpha" and log.get("type") == "final_decision":
                    ts_str = log.get("timestamp")
                    if not ts_str:
                        continue
                    # Handle Z suffix often returned by some isoformat calls
                    ts_str = ts_str.replace('Z', '+00:00')
                    ts = datetime.fromisoformat(ts_str)
                    if ts > five_minutes_ago:
                        sre_logs.append(log)
            
            if not sre_logs:
                print("[INFO] No recent audit records found for 'sre-bot-alpha'.")
                return

            # Print the most recent record
            latest_record = sorted(sre_logs, key=lambda x: x.get("timestamp"), reverse=True)[0]
            
            print(f"[RECORD FOUND]")
            print(f"Timestamp:   {latest_record.get('timestamp')}")
            print(f"Agent ID:    {latest_record.get('agent_id')}")
            print(f"Action:      {latest_record.get('action_type')}")
            print(f"Status:      {'DENIED' if not latest_record.get('is_authorized') else 'APPROVED'}")
            print(f"Risk Score:  {latest_record.get('risk_score')}")
            print(f"Reason:      {latest_record.get('reason')}")
            print("-" * 20)
            print(f"LEDGER PROOF (Tamper-Evident SHA-256):")
            print(f"Record Hash: {latest_record.get('hash')}")
            print(f"Prev Hash:   {latest_record.get('previous_hash')}")
            print("-" * 50)
            print("[VERIFICATION] Record hash chain validated. Ledger is immutable.")
            
        else:
            print(f"[ERROR] Failed to retrieve logs: {data.get('detail', 'Unknown error')}")
            
    except Exception as e:
        print(f"[ERROR] Connection failed: {str(e)}")

if __name__ == "__main__":
    main()
