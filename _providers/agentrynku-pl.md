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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 8.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server providing market data from GPW; 6 public tools available without authentication.
  name: Agent Rynku MCP
  slug: agent-rynku-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/agentrynku-pl/plans/agentrynku-pl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentrynku-pl-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/agentrynku-pl/authentication/agentrynku-pl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentrynku-pl-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agentrynku-pl/llms/agentrynku-pl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentrynku-pl-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentrynku-pl/mcp/agentrynku-pl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentrynku-pl-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentrynku-pl/hosts/agentrynku-pl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentrynku-pl-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentrynku-pl/vendors/agentrynku-pl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentrynku-pl-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentrynku-pl/packages/agentrynku-pl-packages.yml
  title: ''
  type: SDKs
  url: packages/agentrynku-pl-packages.yml
- group: build
  href: https://artifacts.apis.io/agentrynku-pl/packages/agentrynku-pl-packages.yml
  title: ''
  type: Packages
  url: packages/agentrynku-pl-packages.yml
- group: start
  title: ''
  type: Login
  url: https://agentrynku.pl/login
- group: auth
  href: https://artifacts.apis.io/agentrynku-pl/security/agentrynku-pl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrynku-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrynku.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://agentrynku.pl/docs
- group: company
  title: ''
  type: Blog
  url: https://agentrynku.pl/blog
coverage:
  checked: '2026-11-01'
  detail: Documentation exists but provides no machine-readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://agentrynku.pl/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agent Rynku provides AI-driven analysis of ESPI and EBI communications for companies listed on the Warsaw Stock Exchange (GPW). It monitors quarterly results, price movements, and alerts via email or Telegram, offering free and paid plans. Users can add companies to a portfolio, receive contextual insights, and interact with an AI chat for personalized evaluations.
image: https://agentrynku.pl/brand/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentrynku.pl.
  name: Agent Rynku MCP Server
  slug: agentrynku-pl-mcp-yml
modified: '2026-11-01'
name: Agent Rynku
nav: Providers
network: true
overview: 'Agent Rynku is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, Poland, Stock Market, and GPW.


  Agent Rynku''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Agentrynku Pl Plans Pricing
  plan_count: 2
  slug: agentrynku-pl-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Agentrynku Pl Rate Limits
  slug: agentrynku-pl-rate-limits
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 18.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentrynku Pl Authentication
  slug: agentrynku-pl-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentrynku Pl Domain Security
  slug: agentrynku-pl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentrynku-pl
tags:
- Finance
- Artificial Intelligence
- Poland
- Stock Market
- GPW
website: https://agentrynku.pl/
---
