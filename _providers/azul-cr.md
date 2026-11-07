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
- description: Costa Rica business data — public remote MCP server (read-only, no auth required for search)
  name: Azul CR MCP
  slug: azul-cr-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/azul-cr/llms/azul-cr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azul-cr-llms.txt
- group: build
  href: https://artifacts.apis.io/azul-cr/mcp/azul-cr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/azul-cr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/azul-cr/mcp/azul-cr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/azul-cr-mcp.yml
- group: other
  href: https://artifacts.apis.io/azul-cr/hosts/azul-cr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azul-cr-hosts.yml
- group: other
  href: https://artifacts.apis.io/azul-cr/vendors/azul-cr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azul-cr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/azul-cr/security/azul-cr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azul-cr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://azul.cr/
- group: docs
  title: ''
  type: Documentation
  url: https://azul.cr/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://azul.cr/llms.txt
- group: start
  title: ''
  type: Login
  url: https://azul.cr/business/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azul.cr/terminos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azul.cr/privacy
- group: operate
  title: ''
  type: Support
  url: https://azul.cr/preguntas
created: '2026-11-02'
description: Azul CR es la plataforma de negocios de Costa Rica. Encuentra cualquier negocio, producto, oferta o empleo — al instante por WhatsApp. Directorio completo de Costa Rica. La plataforma de negocios de Costa Rica. Encuentra cualquier negocio — al instante por WhatsApp.
image: https://azul.cr/brand/azul-logo-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at azul.cr over HTTP; 6 tools listed.
  name: Azul CR MCP Server
  slug: azul-cr
modified: '2026-11-02'
name: Azul CR
nav: Providers
network: true
overview: 'Azul CR is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Directory, WhatsApp, Costa Rica, Business, and Marketplace.


  Azul CR''s developer surface includes documentation, API reference, support, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - costa-rica
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 17.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Azul Cr Domain Security
  slug: azul-cr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: azul-cr
tags:
- Directory
- WhatsApp
- Costa Rica
- Business
- Marketplace
website: https://azul.cr/
---
