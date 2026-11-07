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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API referenced in the site but no machine-readable contract found.
  name: DOJO+ API
  slug: dojo-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dojoplus-co/llms/dojoplus-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dojoplus-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/dojoplus-co/mcp/dojoplus-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dojoplus-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/dojoplus-co/hosts/dojoplus-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dojoplus-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/dojoplus-co/vendors/dojoplus-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dojoplus-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dojoplus.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dojoplus.co/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://dojoplus.co/news
- group: auth
  href: https://artifacts.apis.io/dojoplus-co/security/dojoplus-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dojoplus-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dojoplus.co/
coverage:
  checked: '2026-11-05'
  detail: The homepage returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://dojoplus.co/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: 'dojoplus-co is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://dojoplus.co/api/og?title=DOJO%2B
layout: provider
mcp_servers:
- description: Remote MCP server at www.dojoplus.co.
  name: DOJO+ MCP Server
  slug: dojoplus-co-mcp-yml
modified: '2026-11-05'
name: DOJO+
nav: Providers
network: true
overview: DOJO+ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gyms, Martial Arts, BJJ, MMA, and Muay Thai.
random_paper: 7
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dojoplus Co Domain Security
  slug: dojoplus-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dojoplus-co
tags:
- Gyms
- Martial Arts
- BJJ
- MMA
- Muay Thai
- Judo
- Affiliates
- Event
website: https://dojoplus.co/
---
