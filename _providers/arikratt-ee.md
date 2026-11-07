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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free MCP API providing access to Estonian company data via authenticated calls.
  name: Ärikratt MCP
  slug: rikratt-mcp
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/arikratt-ee/llms/arikratt-ee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arikratt-ee-llms.txt
- group: agent
  href: https://artifacts.apis.io/arikratt-ee/mcp/arikratt-ee-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arikratt-ee-mcp.yml
- group: other
  href: https://artifacts.apis.io/arikratt-ee/hosts/arikratt-ee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arikratt-ee-hosts.yml
- group: other
  href: https://artifacts.apis.io/arikratt-ee/vendors/arikratt-ee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arikratt-ee-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://arikratt.ee/et/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arikratt.ee/et/privacy
- group: auth
  href: https://artifacts.apis.io/arikratt-ee/security/arikratt-ee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arikratt-ee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arikratt.ee/
- group: docs
  title: ''
  type: Documentation
  url: https://arikratt.ee/en/info
- group: docs
  title: ''
  type: APIReference
  url: https://arikratt.ee/.well-known/api-catalog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arikratt.ee/en/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://arikratt.ee/en/info
- group: agent
  title: ''
  type: WellKnown
  url: https://arikratt.ee/.well-known/mcp/server-card.json
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires OAuth or API key, returning 401 without credentials.
  evidence:
  - status: 401
    url: https://arikratt.ee/mcp
  - status: 200
    url: https://arikratt.ee/.well-known/mcp/server-card.json
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Ärikratt is a free, anonymous explorer of public Estonian company data, offering sector, regional, grant and procurement information. It presents only public company‑level data, each figure with unit, period and source, and never substitutes missing values with zero. Users can browse without an account; optional accounts provide free MCP keys. The service aggregates data from official registers, ensuring up‑to‑date facts for companies, sectors, regions, grants and public procurement.
image: https://arikratt.ee/og.png
json_schemas:
- name: Ärikratt
  property_count: 0
  slug: arikratt-ee-mcp
layout: provider
mcp_servers:
- description: Remote MCP server at arikratt.ee.
  name: Ärikratt MCP Server
  slug: arikratt-ee-mcp-yml
modified: '2026-11-01'
name: Ärikratt
nav: Providers
network: true
overview: 'Ärikratt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Estonia, Business, and Data.


  Ärikratt''s developer surface includes support, documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - estonia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 18.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arikratt Ee Domain Security
  slug: arikratt-ee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: arikratt-ee
tags:
- Company
- Estonia
- Business
- Data
website: https://arikratt.ee/
---
