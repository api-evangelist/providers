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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/scrypta-com-br/llms/scrypta-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrypta-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/scrypta-com-br/mcp/scrypta-com-br-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scrypta-com-br-mcp.yml
- group: other
  href: https://artifacts.apis.io/scrypta-com-br/hosts/scrypta-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrypta-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/scrypta-com-br/vendors/scrypta-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scrypta-com-br-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scrypta-com-br/security/scrypta-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrypta-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrypta.com.br/
- group: company
  title: ''
  type: Blog
  url: https://scrypta.com.br/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrypta.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrypta.com.br/privacidade
- group: commercial
  title: ''
  type: Pricing
  url: https://scrypta.com.br/assinar?plan=monthly
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://scrypta.com.br/mcp
  - status: 200
    url: https://scrypta.com.br/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Scrypta provides an MCP (Machine-Readable Catalog) server that makes Brazilian companies visible to AI agents. It offers free diagnostics, structured data generation, and an endpoint for AI agents to understand, cite, and recommend businesses. The platform includes blog, plans, FAQ, and contact options, aiming to improve AI visibility for enterprises in Brazil.
layout: provider
mcp_servers:
- description: Remote MCP server at scrypta.com.br.
  name: scrypta-com-br MCP Server
  slug: scrypta-com-br-mcp-yml
modified: '2026-10-29'
name: scrypta-com-br
nav: Providers
network: true
overview: 'scrypta-com-br is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Brazil, and Software-as-a-Service.


  scrypta-com-br''s developer surface includes engineering blog, pricing, and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scrypta-com-br/scrypta-com-br-2026-11-03T142855.png
security:
- kind: domain-security
  name: Scrypta Com Br Domain Security
  slug: scrypta-com-br-domain-security
  summary_line: TLSv1.3
slug: scrypta-com-br
tags:
- Company
- Artificial Intelligence
- MCP
- Brazil
- Software-as-a-Service
website: https://scrypta.com.br/
---
