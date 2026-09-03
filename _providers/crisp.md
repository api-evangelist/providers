---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
  title: ''
  type: CapabilityMap
  url: capabilities/crisp-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crisp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crisp-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/crisp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crisp-rate-limits.yml
- group: commercial
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
random_paper: 20
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
  composite: 31.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 72.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 58.3
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 11.4
    operational_transparency: 15.8
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
website: https://crisp.chat/
---
