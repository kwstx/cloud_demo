package sre_safety

# 1. Default to allow = false
default allow = false

# 2. Explicitly allow the action if input.agent_id is 'sre-bot-alpha'
# 3. CRITICALLY, it must return allow = false if the input.resource_deletions count is greater than 0
allow {
    input.agent_id == "sre-bot-alpha"
    input.resource_deletions == 0
}

# This policy ensures that even the 'sre-bot-alpha' cannot perform actions 
# that result in resource deletions, protecting the database from destruction.
