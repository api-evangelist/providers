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
- description: MCP API offering blood‑alcohol estimation tools.
  name: alcometer.de MCP
  slug: alcometer-de-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/alcometer-de/llms/alcometer-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alcometer-de-llms.txt
- group: agent
  href: https://artifacts.apis.io/alcometer-de/mcp/alcometer-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alcometer-de-mcp.yml
- group: other
  href: https://artifacts.apis.io/alcometer-de/hosts/alcometer-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alcometer-de-hosts.yml
- group: auth
  href: https://artifacts.apis.io/alcometer-de/security/alcometer-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alcometer-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alcometer.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.alcometer.de/fuer-entwickler/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alcometer.de/fuer-entwickler/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alcometer.de/fuer-entwickler/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alcometer.de/datenschutz/
- group: operate
  title: ''
  type: Support
  url: mailto:legal@webersheim.de
created: '2026-11-01'
description: Webersheim is a German digital agency behind the alcometer.de project, offering a free, open-source blood‑alcohol calculator (Promillerechner) for the public and as a Model Context Protocol (MCP) server for AI assistants. The service estimates blood‑alcohol concentration using Widmark’s formula, provides German drink‑driving limits, and includes tools for conversion and limits lookup, all without registration or authentication.
image: https://www.alcometer.de/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.alcometer.de.
  name: Webersheim MCP Server
  slug: alcometer-de-mcp-yml
modified: '2026-11-01'
name: Webersheim
nav: Providers
network: true
overview: 'Webersheim is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Alcohol, Health, Calculator, Germany, and MCP.


  Webersheim''s developer surface includes documentation, getting-started guide, support, and 7 more developer resources.'
random_paper: 2
scopes:
- name: Alcometer De Scopes
  scope_count: 0
  slug: alcometer-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 17.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alcometer De Authentication
  slug: alcometer-de-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alcometer De Domain Security
  slug: alcometer-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alcometer-de
tags:
- Alcohol
- Health
- Calculator
- Germany
- MCP
website: https://alcometer.de/
---
