---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP endpoint allowing AI agents to interact with ASOHawk services for App Store data management.
  name: ASOHawk MCP API
  slug: asohawk-mcp-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/asohawk-cc/llms/asohawk-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asohawk-cc-llms.txt
- group: other
  href: https://artifacts.apis.io/asohawk-cc/hosts/asohawk-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asohawk-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/asohawk-cc/vendors/asohawk-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asohawk-cc-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://asohawk.cc/docs/faq
- group: auth
  href: https://artifacts.apis.io/asohawk-cc/security/asohawk-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asohawk-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asohawk.cc/
- group: commercial
  title: ''
  type: Pricing
  url: https://asohawk.cc/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asohawk.cc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asohawk.cc/privacy
- group: operate
  title: ''
  type: Support
  url: https://asohawk.cc/support
- group: operate
  title: ''
  type: Roadmap
  url: https://asohawk.cc/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://asohawk.cc/signup
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; attempts to fetch typical spec URLs return redirects to login.
  evidence:
  - status: 307
    url: https://asohawk.cc/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ASOHawk is an agent‑first App Store Optimization (ASO) platform for indie iOS developers. It provides AI‑driven keyword tracking, app store ranking monitoring, keyword difficulty analysis, and competitor tracking, all powered by a built‑in MCP server that lets your AI agent run ASO tasks on your behalf. A free plan is available. The service aims to simplify ASO by automating data collection and analysis, enabling developers to improve visibility and downloads without manual effort.
image: https://asohawk.cc/opengraph-image.jpg?opengraph-image.3pdqvgbx96211.jpg
layout: provider
modified: '2026-11-01'
name: ASOHawk
nav: Providers
network: true
overview: 'ASOHawk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ASO, Artificial Intelligence, iOS, KeywordTracking, and App Store Optimization.


  ASOHawk''s developer surface includes documentation, pricing, support, signup flow, and 8 more developer resources.'
plans:
- name: Asohawk Cc Plans Pricing
  plan_count: 0
  slug: asohawk-cc-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Asohawk Cc Rate Limits
  slug: asohawk-cc-rate-limits
scopes:
- name: Asohawk Cc Scopes
  scope_count: 0
  slug: asohawk-cc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 20.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asohawk Cc Authentication
  slug: asohawk-cc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Asohawk Cc Domain Security
  slug: asohawk-cc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asohawk-cc
tags:
- ASO
- Artificial Intelligence
- iOS
- KeywordTracking
- App Store Optimization
- MCP
website: https://asohawk.cc/
---
