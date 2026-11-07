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
    agent_card: flavored
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only Model Context Protocol (MCP) server providing search, facets, vintage data and product details for ARVI SA's wine catalog.
  name: ARVI Catalog MCP
  slug: arvi-catalog-mcp
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/arvi-ch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/arvi-ch/llms/arvi-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arvi-ch-llms.txt
- group: other
  href: https://artifacts.apis.io/arvi-ch/a2a/arvi-ch-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/arvi-ch-a2a.yml
- group: auth
  href: https://artifacts.apis.io/arvi-ch/well-known/arvi-ch-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arvi-ch-mcp-security.txt
- group: other
  href: https://artifacts.apis.io/arvi-ch/hosts/arvi-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arvi-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/arvi-ch/vendors/arvi-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arvi-ch-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arvi.ch/en/terms-conditions
- group: start
  title: ''
  type: SignUp
  url: https://arvi.ch/register?returnUrl=%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arvi.ch/privacy-policy
- group: auth
  href: https://artifacts.apis.io/arvi-ch/security/arvi-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arvi-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arvi.ch/
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.arvi.ch/
- group: agent
  title: ''
  type: WellKnown
  url: https://arvi.ch/.well-known/mcp.json
- group: agent
  title: ''
  type: WellKnown
  url: https://arvi.ch/.well-known/agent-skills/index.json
- group: agent
  title: ''
  type: WellKnown
  url: https://arvi.ch/.well-known/api-catalog
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://mcp.arvi.ch/api/mcp
  - status: 200
    url: https://arvi.ch/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ARVI SA operates a premium online wine shop offering a curated selection of over 5,000 fine and rare wines from renowned regions such as Bordeaux, Burgundy, and Tuscany. Based in Switzerland, the company provides secure shipping and 24‑hour delivery throughout the country. Customers can browse an extensive catalog, filter by producer, vintage, price, and region, and purchase directly through the website. The platform emphasizes high‑quality service, authenticity guarantees, and a seamless shopping experience for wine enthusiasts and collectors.
image: https://arvi.ch/images/thumbs/0026553_logo.gif
layout: provider
mcp_servers:
- description: ''
  name: ARVI SA MCP Server
  slug: https-mcp-arvi-ch
modified: '2026-11-01'
name: ARVI SA
nav: Providers
network: true
overview: 'ARVI SA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wine, E-Commerce, Retail, Switzerland, and Premium.


  ARVI SA''s developer surface includes signup flow and 14 more developer resources.'
plans:
- name: Arvi Ch Plans Pricing
  plan_count: 0
  slug: arvi-ch-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Arvi Ch Rate Limits
  slug: arvi-ch-rate-limits
scopes:
- name: Arvi Ch Scopes
  scope_count: 0
  slug: arvi-ch-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 75.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 18.2
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arvi Ch Authentication
  slug: arvi-ch-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arvi Ch Domain Security
  slug: arvi-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: arvi-wine-catalog
  slug: arvi-ch-wine-catalog
slug: arvi-ch
tags:
- Wine
- E-Commerce
- Retail
- Switzerland
- Premium
website: https://arvi.ch/
---
