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
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST/MCP API for Brain On BNB AI providing various blockchain tools and data.
  name: Brain On BNB AI API
  slug: brain-on-bnb-ai-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/brainonbnb-com/llms/brainonbnb-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainonbnb-com-llms.txt
- group: other
  href: https://artifacts.apis.io/brainonbnb-com/a2a/brainonbnb-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brainonbnb-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/brainonbnb-com/mcp/brainonbnb-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brainonbnb-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/brainonbnb-com/hosts/brainonbnb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainonbnb-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brainonbnb-com/vendors/brainonbnb-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainonbnb-com-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://brainonbnb.com/roadmap
- group: auth
  href: https://artifacts.apis.io/brainonbnb-com/security/brainonbnb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainonbnb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainonbnb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://brainonbnb.com/skill.md
- group: docs
  title: ''
  type: APIReference
  url: https://brainonbnb.com/api-registry.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brainonbnb.com/registry
- group: start
  title: ''
  type: GettingStarted
  url: https://brainonbnb.com/skill.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mmxrealQQ
created: '2026-10-29'
description: Brain On BNB AI (BOBAI) is a meme‑coin project on the BNB Smart Chain that provides a suite of open‑source, on‑chain tools and agents. It offers a public REST/MCP API, a DeFi agent that manages a PancakeSwap V3 position, a token‑price dashboard, a pool scanner, an AI‑driven agent marketplace (Brain Plaza), NFT buy‑drop, and various utility services. All code is open‑source on GitHub, and the platform emphasizes transparency with verifiable on‑chain data, no private keys, and read‑only access. The project’s website, documentation, and API references are hosted at brainonbnb.com.
image: https://brainonbnb.com/logo-200x200.png
layout: provider
mcp_servers:
- description: Remote MCP server at brainonbnb.com.
  name: brainonbnb-com MCP Server
  slug: brainonbnb-com-mcp-yml
modified: '2026-10-29'
name: brainonbnb-com
nav: Providers
network: true
overview: 'brainonbnb-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, DeFi, Memecoin, and Open Source.


  brainonbnb-com''s developer surface includes documentation, API reference, getting-started guide, and 10 more developer resources.'
plans:
- name: Brainonbnb Com Plans Pricing
  plan_count: 0
  slug: brainonbnb-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Brainonbnb Com Rate Limits
  slug: brainonbnb-com-rate-limits
scopes:
- name: Brainonbnb Com Scopes
  scope_count: 0
  slug: brainonbnb-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.6
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/brainonbnb-com/brainonbnb-com-2026-11-03T122440.png
security:
- kind: authentication
  name: Brainonbnb Com Authentication
  slug: brainonbnb-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Brainonbnb Com Domain Security
  slug: brainonbnb-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brainonbnb-com
tags:
- Company
- Blockchain
- DeFi
- Memecoin
- Open Source
- BNB Chain
website: https://brainonbnb.com/
---
