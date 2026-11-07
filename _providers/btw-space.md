---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/btw-space/llms/btw-space-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/btw-space-llms.txt
- group: other
  href: https://artifacts.apis.io/btw-space/hosts/btw-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/btw-space-hosts.yml
- group: other
  href: https://artifacts.apis.io/btw-space/vendors/btw-space-vendors.yml
  title: ''
  type: Vendors
  url: vendors/btw-space-vendors.yml
- group: auth
  href: https://artifacts.apis.io/btw-space/security/btw-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/btw-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://btw.space/
coverage:
  checked: '2026-11-03'
  detail: MCP endpoint requires POST JSON-RPC which is disallowed, preventing contract discovery
  evidence:
  - status: 406
    url: https://btw.space/mcp
  reason: auth-required
  state: gated
created: '2026-11-03'
description: btw is an agentic commerce platform that enables groups of buyers to pool demand and negotiate lower prices from brands. Users create personal agents that collect product wishes, connect with AI assistants like Claude, ChatGPT, Grok, or Cursor, and automatically join buying groups. The platform showcases live deals, tracks contributions, and handles deposits, allowing participants to benefit from collective purchasing power without traditional passwords, using email-based login.
image: https://btw.space/counter.png
layout: provider
modified: '2026-11-03'
name: btw
nav: Providers
network: true
overview: btw is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce, AI Agents, Group Buying, AI Integration, and Marketplace.
random_paper: 14
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Btw Space Domain Security
  slug: btw-space-domain-security
  summary_line: TLSv1.3
slug: btw-space
tags:
- Commerce
- AI Agents
- Group Buying
- AI Integration
- Marketplace
website: https://btw.space/
---
