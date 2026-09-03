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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Exotel Agentic Access
  operation_count: 12
  slug: exotel-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- baseURL: wss://your-bot-host.example.com
  baseurl_source: declared
  description: Documented WebSocket (wss://) voice-streaming API. When a call reaches a Voicebot or Stream applet, Exotel opens a secure WebSocket to your endpoint and streams base64 linear-PCM audio in ~100 ms fram
  name: Exotel AgentStream Voice Streaming API
  slug: exotel-agentstream-voice-streaming-api
- baseURL: https://api.exotel.com/v1/Accounts
  baseurl_source: declared
  description: Retrieve details of past and in-progress calls.
  name: Exotel Call Details API
  slug: exotel-call-details-api
- baseURL: https://api.exotel.com/v1/Accounts
  baseurl_source: declared
  description: Create and manage bulk outbound call campaigns (v2).
  name: Exotel Campaigns API
  slug: exotel-campaigns-api
- baseURL: https://api.exotel.com/v1/Accounts
  baseurl_source: declared
  description: Look up telecom metadata for phone numbers.
  name: Exotel Numbers API
  slug: exotel-numbers-api
- baseURL: https://api.exotel.com/v1/Accounts
  baseurl_source: declared
  description: Send SMS and retrieve message details.
  name: Exotel SMS API
  slug: exotel-sms-api
- baseURL: https://api.exotel.com/v1/Accounts
  baseurl_source: declared
  description: Place and control outbound voice calls.
  name: Exotel Voice API
  slug: exotel-voice-api
artifact_total: 21
asyncapis:
- description: Exotel AgentStream (also surfaced through the Voicebot and Stream applets) is a documented public WebSocket API for real-time voice media streaming during a call. When a call hits a Voicebot/Stream ap
  name: Exotel AgentStream Voice Streaming API
  slug: exotel-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Exotel Call Details API
  slug: open-exotel-call-details-api
- collection_type: open
  name: Exotel Call Details Campaigns API
  slug: open-exotel-campaigns-api
- collection_type: open
  name: Exotel Call Details Numbers API
  slug: open-exotel-numbers-api
- collection_type: open
  name: Exotel Call Details SMS API
  slug: open-exotel-sms-api
- collection_type: open
  name: Exotel Call Details Voice API
  slug: open-exotel-voice-api
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
random_paper: 6
rate_limits:
- limit_count: 5
  name: Exotel Rate Limits
  slug: exotel-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Exotel API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: exotel-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 24.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 31.6
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
