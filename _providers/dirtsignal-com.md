---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public records intelligence for real estate acquisition. Code violations, active lien signals, judgments, and lis pendens across Florida counties.
  name: DirtSignal API
  slug: dirtsignal-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dirtsignal-com/plans/dirtsignal-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dirtsignal-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dirtsignal-com/conformance/dirtsignal-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dirtsignal-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/dirtsignal-com/mcp/dirtsignal-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dirtsignal-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dirtsignal-com/mcp/dirtsignal-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dirtsignal-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dirtsignal-com/well-known/dirtsignal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dirtsignal-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dirtsignal-com/hosts/dirtsignal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dirtsignal-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dirtsignal-com/vendors/dirtsignal-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dirtsignal-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://dirtsignal.com/status
- group: start
  title: ''
  type: Login
  url: https://dirtsignal.com/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://dirtsignal.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dirtsignal.com/api/docs
- group: auth
  href: https://artifacts.apis.io/dirtsignal-com/security/dirtsignal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dirtsignal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dirtsignal.com/
- group: docs
  title: ''
  type: Docs
  url: https://dirtsignal.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://dirtsignal.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dirtsignal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dirtsignal.com/privacy
- group: company
  title: ''
  type: About
  url: https://dirtsignal.com/about
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://dirtsignal.com/mcp
  - status: 200
    url: https://dirtsignal.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DirtSignal supplies weekly ranked leads of property distress sourced from public‑record filings such as code cases, lien filings, demolition orders, unsafe‑structure determinations, and tax delinquency. The leads include address, owner, status, jurisdiction, parcel match, and a link to the official record, and are delivered via email, dashboard, CSV export, API, or MCP connector. The service is aimed at acquisition teams, investors, and title companies that need actionable property‑risk data.
image: https://snapog.com/s/https%3A%2F%2Fdirtsignal.com%2F
layout: provider
mcp_servers:
- description: Remote MCP server at dirtsignal.com.
  name: DirtSignal MCP Server
  slug: dirtsignal-com-mcp-yml
modified: '2026-11-05'
name: DirtSignal
nav: Providers
network: true
overview: 'DirtSignal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate Leads, Property Distress, Public Records Data, CSV Export, and Dashboards.


  DirtSignal''s developer surface includes getting-started guide, API reference, pricing, and 15 more developer resources.'
plans:
- name: Dirtsignal Com Plans Pricing
  plan_count: 3
  slug: dirtsignal-com-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dirtsignal Com Domain Security
  slug: dirtsignal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dirtsignal-com
tags:
- Real Estate Leads
- Property Distress
- Public Records Data
- CSV Export
- Dashboards
- Investor
- Title Companies
website: https://dirtsignal.com/
---
