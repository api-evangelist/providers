---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Inkeep Agentic Access
  operation_count: 5
  slug: inkeep-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 2
apis:
- description: REST management surface for the Inkeep Agents framework - create and operate agents, sub-agents, projects, tools, MCP servers, conversations, and feedback for building no-code or TypeScript-SDK AI age
  name: Inkeep Agents / Management API
  slug: inkeep-agents-management-api
- baseURL: https://api.inkeep.com/v1
  baseurl_source: declared
  description: Log conversations, feedback, and custom interaction events.
  name: Inkeep Analytics API
  slug: inkeep-analytics-api
- baseURL: https://api.inkeep.com
  baseurl_source: declared
  description: The Challenge API from Inkeep — 1 operation(s) for challenge.
  name: Inkeep Challenge API
  slug: inkeep-challenge-api
- baseURL: https://api.inkeep.com
  baseurl_source: declared
  description: The Chat Sessions API from Inkeep — 2 operation(s) for chat sessions.
  name: Inkeep Chat Sessions API
  slug: inkeep-chat-sessions-api
- baseURL: https://api.inkeep.com
  baseurl_source: declared
  description: The Hello API from Inkeep — 1 operation(s) for hello.
  name: Inkeep Hello API
  slug: inkeep-hello-api
- baseURL: https://api.inkeep.com
  baseurl_source: declared
  description: The Chat Completions API from Inkeep — 2 operation(s) for chat completions.
  name: Inkeep Chat Completions API
  slug: inkeep-chat-completions-api
artifact_total: 18
asyncapis:
- description: AsyncAPI 2.6 description of Inkeep's **chat completion streaming** surface. Inkeep does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.inkeep.com
  name: Inkeep Chat Completions Streaming (HTTP + SSE)
  slug: inkeep-asyncapi
collections:
- collection_type: open
  name: Inkeep AI & Analytics API
  slug: open-inkeep-analytics-api
- collection_type: open
  name: Inkeep AI & Analytics Chat API
  slug: open-inkeep-chat-api
- collection_type: open
  name: Inkeep AI & Analytics API
  slug: open-inkeep
common:
- group: agent
  href: https://artifacts.apis.io/inkeep/agentic-access/inkeep-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inkeep-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/inkeep/security/inkeep-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/inkeep-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/inkeep/security/inkeep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inkeep-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/inkeep/authentication/inkeep-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inkeep-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inkeep
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inkeep
- group: company
  title: ''
  type: Website
  url: https://inkeep.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inkeep.com
- group: commercial
  href: https://artifacts.apis.io/inkeep/plans/inkeep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inkeep-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/inkeep/rate-limits/inkeep-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inkeep-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/inkeep/finops/inkeep-finops.yml
  title: ''
  type: FinOps
  url: finops/inkeep-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://inkeep.com/blog/rss.xml
created: '2026-06-20'
description: Inkeep is an AI support and agent platform for documentation and products. Its developer platform exposes an OpenAI-compatible RAG / chat completions API over your own content, an Analytics API for logging conversations, feedback, and events, and an Agents / management surface for building and operating AI agents and copilot experiences.
finops:
- has_sources: true
  method: generated
  name: Inkeep Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: inkeep-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inkeep.png
layout: provider
modified: '2026-06-20'
name: Inkeep
nav: Providers
network: true
overview: 'Inkeep publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Challenge API, Chat Sessions API, and 3 more. Tagged areas include Artificial Intelligence, Support, RAG, Agents, and Documentation.


  The Inkeep catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Inkeep''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Inkeep Plans Pricing
  plan_count: 4
  slug: inkeep-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Inkeep Rate Limits
  slug: inkeep-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Inkeep — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: inkeep-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 52.1
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/inkeep/inkeep-2026-06-20T183352.png
security:
- kind: authentication
  name: Inkeep Authentication
  slug: inkeep-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inkeep Domain Security
  slug: inkeep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Inkeep Trust Center
  slug: inkeep-trust-center
  summary_line: SOC 2, GDPR
slug: inkeep
tags:
- Artificial Intelligence
- Support
- RAG
- Agents
- Documentation
- Real-Time
website: https://inkeep.com
---
