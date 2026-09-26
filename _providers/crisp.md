---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Crisp Agentic Access
  operation_count: 14
  slug: crisp-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.crisp.chat/v1/plugin/connect/endpoints
  baseurl_source: declared
  description: Crisp realtime surface combining HTTP Web Hooks (signed plugin hooks and unsigned website hooks) and the Socket.IO RTM API. Both deliver the same conversational, people, campaign, browsing, call, iden
  name: Crisp Realtime (Webhooks + RTM) v1
  slug: crisp-realtime-api
- baseURL: https://api.crisp.chat/v1
  baseurl_source: declared
  description: The Conversations API from Crisp — 9 operation(s) for conversations.
  name: Crisp Conversations API
  slug: crisp-conversations-api
- baseURL: https://api.crisp.chat/v1
  baseurl_source: declared
  description: The Website API from Crisp — 3 operation(s) for website.
  name: Crisp Website API
  slug: crisp-website-api
artifact_total: 15
asyncapis:
- description: 'AsyncAPI description of Crisp''s two realtime delivery surfaces: * **Web Hooks (v1)** — HTTP POST callbacks delivered to a subscriber URL registered on a Crisp website or Crisp plugin. Payload envelope'
  name: Crisp Realtime Surface (Webhooks + RTM)
  slug: crisp-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crisp REST API v1 Conversations API
  slug: open-crisp-conversations-api
- collection_type: open
  name: Crisp REST API v1 Conversations Website API
  slug: open-crisp-website-api
- collection_type: open
  name: Crisp REST API v1
  slug: open-crisp
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/capabilities/crisp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/crisp-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/agentic-access/crisp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crisp-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/security/crisp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crisp-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/authentication/crisp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crisp-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crisp-im
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crisp-im
- group: company
  title: ''
  type: Website
  url: https://crisp.chat/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crisp.chat/references/rest-api/v1/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/plans/crisp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crisp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/rate-limits/crisp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crisp-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/finops/crisp-finops.yml
  title: ''
  type: FinOps
  url: finops/crisp-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://crisp.chat/en/blog/
created: '2026-05-08'
description: Crisp is a customer messaging platform offering live chat, shared inbox, helpdesk, chatbot, and CRM features for businesses of all sizes.
finops:
- name: Crisp Finops
  service_category: Customer Support
  slug: crisp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crisp.png
layout: provider
modified: '2026-05-30'
name: Crisp
nav: Providers
network: true
overview: 'Crisp publishes 3 APIs on the [APIs.io](https://apis.io/) network: Realtime (Webhooks + RTM) v1, Conversations API, and Website API. Tagged areas include Customer Service, Live Chat, Help Desk, Messaging, and Chatbots.


  The Crisp catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Crisp''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Crisp Plans Pricing
  plan_count: 1
  slug: crisp-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Crisp Rate Limits
  slug: crisp-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Crisp API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: crisp-asyncapi-spectral-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 53.9
    developer_ergonomics: 23.8
    discoverability: 60.0
    operational_transparency: 15.8
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/crisp/refs/heads/main/screenshots/crisp-2026-06-20T175235.png
security:
- kind: authentication
  name: Crisp Authentication
  slug: crisp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crisp Domain Security
  slug: crisp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: crisp
tags:
- Customer Service
- Live Chat
- Help Desk
- Messaging
- Chatbots
- Real-Time
website: https://crisp.chat/
---
