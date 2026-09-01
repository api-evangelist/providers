---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Successor API surface of the Ultimate.ai platform after the Zendesk acquisition - Chat, Ticket, and Widget Escalation APIs with matching webhooks, plus Data Export and Delete User Data. Requires the A
  name: Zendesk AI Agents API (formerly Ultimate.ai)
  slug: zendesk-ai-agents-api-formerly-ultimateai
- description: The original Ultimate.ai Public API on chat.ultimate.ai - Chat Automation (POST /api/v2/automation), Intent Recognition (POST /api/intents), and Delete User Data (POST /api/gdpr/delete-user-data) - do
  name: Ultimate.ai Public API (legacy, retired)
  slug: ultimateai-public-api-legacy-retired
artifact_total: 5
asyncapis:
- description: ''
  name: Ultimateai Ai Agents Webhooks
  slug: ultimateai-ai-agents-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://ultimate.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/documentation/ai-agents
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zendesk.com/api-reference/ai-agents/introduction/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ultimateai
- group: auth
  title: ''
  type: Authentication
  url: authentication/ultimateai-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ultimateai-ai-agents-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ultimateai-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ultimateai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ultimateai-domain-security.yml
created: '2026-07-17'
description: Ultimate.ai was a Helsinki- and Berlin-based customer support automation platform - virtual agents and chatbots with intent recognition and agent-assist - backed by HV Capital and Techstars. Zendesk acquired Ultimate.ai in 2024 and the product now ships as Zendesk AI agents (the "AI agents - Advanced" add-on); ultimate.ai redirects to zendesk.com and the successor AI Agents APIs (Chat, Ticket, Widget Escalation, Data Export, Delete User Data plus webhooks) are documented on developer.zendesk.com, with API keys still generated from the Ultimate.ai dashboard. The legacy Ultimate.ai Public API on chat.ultimate.ai is retired.
image: https://avatars.githubusercontent.com/u/82862471?v=4
layout: provider
modified: '2026-07-21'
name: Ultimate.ai
nav: Providers
network: true
overview: 'Ultimate.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, Customer-Support, Conversational AI, and Chatbots.


  The Ultimate.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ultimate.ai''s developer surface includes documentation, API reference, authentication, and 6 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ultimateai Authentication
  slug: ultimateai-authentication
  summary_line: http-basic/apiKey · 4 schemes
- kind: domain-security
  name: Ultimateai Domain Security
  slug: ultimateai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ultimateai
tags:
- Company
- Ai Enterprise Software
- Customer-Support
- Conversational AI
- Chatbots
- AI Agents
- Automation
- Acquired
website: https://ultimate.ai/
---
