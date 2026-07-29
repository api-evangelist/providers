---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Exotel Agentic Access
  operation_count: 12
  slug: exotel-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 6
apis:
- description: Documented WebSocket (wss://) voice-streaming API. When a call reaches a Voicebot or Stream applet, Exotel opens a secure WebSocket to your endpoint and streams base64 linear-PCM audio in ~100 ms fram
  name: Exotel AgentStream Voice Streaming API
  slug: exotel-agentstream-voice-streaming-api
- description: Retrieve details of past and in-progress calls.
  name: Exotel Call Details API
  slug: exotel-call-details-api
- description: Create and manage bulk outbound call campaigns (v2).
  name: Exotel Campaigns API
  slug: exotel-campaigns-api
- description: Look up telecom metadata for phone numbers.
  name: Exotel Numbers API
  slug: exotel-numbers-api
- description: Send SMS and retrieve message details.
  name: Exotel SMS API
  slug: exotel-sms-api
- description: Place and control outbound voice calls.
  name: Exotel Voice API
  slug: exotel-voice-api
artifact_total: 15
asyncapis:
- description: Exotel AgentStream (also surfaced through the Voicebot and Stream applets) is a documented public WebSocket API for real-time voice media streaming during a call. When a call hits a Voicebot/Stream ap
  name: Exotel AgentStream Voice Streaming API
  slug: exotel-asyncapi
collections:
- collection_type: open
  name: Exotel API
  slug: open-exotel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exotel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exotel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exotel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exotel
- group: company
  title: ''
  type: Website
  url: https://exotel.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.exotel.com
- group: commercial
  title: ''
  type: Plans
  url: plans/exotel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exotel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/exotel-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://exotel.com/blog/
created: '2026-07-12'
description: Exotel is an Indian cloud telephony and customer-engagement (CPaaS) platform offering programmable voice, SMS, virtual numbers (ExoPhones), IVR/call flows, call campaigns, and call-center tooling. Its Twilio-style REST APIs place outbound calls (connect two numbers or connect a number to a call flow), send SMS, return call and number metadata, and manage campaigns, over region-specific subdomains (api.exotel.com for Singapore, api.in.exotel.com for Mumbai/India) using HTTP Basic auth with an API Key and API Token. Exotel AgentStream adds a documented WebSocket voice-streaming API for real-time voicebots.
finops:
- name: Exotel Finops
  service_category: Communications and Telephony
  slug: exotel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exotel.png
layout: provider
modified: '2026-07-12'
name: Exotel
nav: Providers
network: true
overview: 'Exotel publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AgentStream Voice Streaming API, Call Details API, Campaigns API, and 3 more. Tagged areas include Cloud Telephony, Voice, SMS, India, and CPaaS.


  The Exotel catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Exotel''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Exotel Plans Pricing
  plan_count: 4
  slug: exotel-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Exotel Rate Limits
  slug: exotel-rate-limits
rules:
- name: Exotel API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: exotel-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.2
  delta: -7.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 31.6
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/exotel/refs/heads/main/screenshots/exotel-2026-07-25T213905.png
security:
- kind: authentication
  name: Exotel Authentication
  slug: exotel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exotel Domain Security
  slug: exotel-domain-security
  summary_line: HSTS · DMARC
slug: exotel
tags:
- Cloud Telephony
- Voice
- SMS
- India
- CPaaS
- Call Center
- IVR
- Numbers
- Communications
- Customer Engagement
website: https://exotel.com
---
