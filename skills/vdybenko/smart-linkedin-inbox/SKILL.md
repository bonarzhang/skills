# Smart LinkedIn Inbox from Linxa — MCP Skill

This skill connects OpenClaw to your Linxa Smart Inbox and lets you:
- Verify the current LinkedIn user
- List/search inbox conversations
- Fetch messages for a conversation

## Quickstart (3 minutes)

0) Install Skill clawhub install smart-linkedin-inbox
1) Install the Linxa Chrome Extension  https://chromewebstore.google.com/detail/ai-smart-inbox-for-linked/ggkdnjblijkchfmgapnbhbhnphacmabm
2) Sign in to Linxa with your LinkedIn account  https://app.uselinxa.com/
3) Generate an access token in Linxa  https://app.uselinxa.com/setup-mcp
4) Set the token for OpenClaw:
   - `export LINXA_TOKEN=...` (recommended via env var)
5) Run:
   - `read skills/smart-linkedin-inbox/SKILL.md to understand how to use this skill. This skill is for LinkedIn only. Use valu of LINXA_TOKEN as Bearer token for Authorization header.`
   - `Who I am on LinkedIn`
   - `What is my last messages on LinkedIn?`
   - `What is my last messages on LinkedIn with [Name]?`

## Auth

Send the token as:
`Authorization: Bearer $LINXA_TOKEN`

✅ No LinkedIn password sharing  
✅ Works through your existing LinkedIn session via the extension


## Endpoints (tools)
1) GET /api/current-li-user
   - Verify auth and identify the current LinkedIn user.

2) GET /api/conversations
   - List inbox conversations.
   - **Parameters**:
     - `limit`: (default 50)
     - `search`: Keyword search
     - `label`: Filter by label. 
       **Available values**: 
       `Hot`, `Need Follow Up`, `Personal`, `Investors`, `Clients`, `Inbox`, `Hiring`, `Junk`, `Partnership`, `archived`, `scheduled`, `not-contacted`
     - `sentiment`: POSITIVE, NEGATIVE, NEUTRAL
     - `primary_intent`: e.g., "sales"
     - `intent_direction`: "to_me" or "from_me"

3) GET /api/messages/{chatId}
   - Fetch messages for a specific conversation.

## Quick manual test (curl)
curl -H "Authorization: Bearer <TOKEN>" \
  http://app.uselinxa.com/api/current-li-user

curl -H "Authorization: Bearer <TOKEN>" \
  "http://app.uselinxa.com/api/conversations?label=Hot&limit=5"

## Quick manual test (curl)

# Set your Linxa access token in an environment variable (once per session):
export LINXA_TOKEN=<YOUR_TOKEN>

# Verify identity (follow redirects):
curl -L -H "Authorization: Bearer $LINXA_TOKEN" \
  "https://app.uselinxa.com/api/current-li-user"

# List conversations (last 5 messages to you):
curl -L -H "Authorization: Bearer $LINXA_TOKEN" \
  "https://app.uselinxa.com/api/conversations?label=Hot&limit=5"

## Notes
- If chatId contains special characters, ensure it is URL-encoded.
- This connects to the public Linxa API (app.uselinxa.com).
