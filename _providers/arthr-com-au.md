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
    agent_card: near-conformant
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
  score: 9.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Mortgage calculators for AI assistants via MCP server.
  name: Arthr MCP API
  slug: arthr-mcp-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/arthr-com-au/llms/arthr-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arthr-com-au-llms.txt
- group: other
  href: https://artifacts.apis.io/arthr-com-au/a2a/arthr-com-au-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/arthr-com-au-a2a.yml
- group: agent
  href: https://artifacts.apis.io/arthr-com-au/mcp/arthr-com-au-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arthr-com-au-mcp.yml
- group: other
  href: https://artifacts.apis.io/arthr-com-au/hosts/arthr-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arthr-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/arthr-com-au/vendors/arthr-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arthr-com-au-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.arthr.com.au
- group: auth
  href: https://artifacts.apis.io/arthr-com-au/security/arthr-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arthr-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arthr.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arthr.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arthr.com.au/privacy
created: '2026-11-01'
description: Arthr is an Australian mortgage brokerage that leverages AI to help the next generation of Australians secure home loans, refinance, and manage mortgage-related costs. Founded by Graeme Pillemer and Jeremy Fisher, the service is provided through 1st Street Financial, a licensed credit representative (ABN 39 697 205 486, Credit Rep No 490057, ACL 389328).
image: https://www.arthr.com.au/brand-kit/logos/mark-1024.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.arthr.com.au.
  name: Arthr MCP Server
  slug: arthr-com-au-mcp-yml
modified: '2026-11-01'
name: Arthr
nav: Providers
network: true
overview: Arthr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mortgage, Brokerage, Artificial Intelligence, Australia, and Fintech.
plans:
- name: Arthr Com Au Plans Pricing
  plan_count: 0
  slug: arthr-com-au-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Arthr Com Au Rate Limits
  slug: arthr-com-au-rate-limits
scopes:
- name: Arthr Com Au Scopes
  scope_count: 0
  slug: arthr-com-au-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 13.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 22.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arthr Com Au Authentication
  slug: arthr-com-au-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arthr Com Au Domain Security
  slug: arthr-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arthr-com-au
tags:
- Mortgage
- Brokerage
- Artificial Intelligence
- Australia
- Fintech
website: https://arthr.com.au/
---
