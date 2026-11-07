---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Point‑of‑sale sales and units for ~380 US consumer companies, by ISIN or ticker, from transactions at eight US retailers.
  name: DecaData Odyssey Lite API
  slug: decadata-odyssey-lite-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/decadata-io/conformance/decadata-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decadata-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decadata-io/llms/decadata-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decadata-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/decadata-io/mcp/decadata-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decadata-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/decadata-io/hosts/decadata-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decadata-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/decadata-io/vendors/decadata-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decadata-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decadata.io/terms
- group: company
  title: ''
  type: Blog
  url: https://decadata.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.decadata.io/
- group: auth
  href: https://artifacts.apis.io/decadata-io/authentication/decadata-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decadata-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/decadata-io/security/decadata-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decadata-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decadata.io/
created: '2026-11-05'
description: DecaData provides daily customer insights and market data for savvy buyers, delivering real‑time analytics and nowcasts on consumer trends, pricing and inflation. The platform aggregates diverse data sources to help businesses make informed decisions.
image: https://decadata.io/assets/favicon/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.decadata.io.
  name: DecaData MCP Server
  slug: decadata-io-mcp-yml
modified: '2026-11-05'
name: DecaData
nav: Providers
network: true
overview: 'DecaData is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Analytics, Market Insights, and Real-Time.


  DecaData''s developer surface includes engineering blog, documentation, authentication, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Decadata Io Authentication
  slug: decadata-io-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Decadata Io Domain Security
  slug: decadata-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: decadata-io
tags:
- Company
- Data
- Analytics
- Market Insights
- Real-Time
website: https://decadata.io/
---
