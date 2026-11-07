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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: EcoBack API provides programmatic access to climate and energy advice data.
  name: EcoBack API
  slug: ecoback-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/getecoback-com/llms/getecoback-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getecoback-com-llms.txt
- group: build
  href: https://artifacts.apis.io/getecoback-com/mcp/getecoback-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/getecoback-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/getecoback-com/mcp/getecoback-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getecoback-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/getecoback-com/hosts/getecoback-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getecoback-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getecoback-com/vendors/getecoback-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getecoback-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/getecoback-com/security/getecoback-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getecoback-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getecoback.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getecoback.com/datenschutz.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getecoback.com/impressum.html
- group: operate
  title: ''
  type: Support
  url: https://getecoback.com/kontakt.html
coverage:
  checked: '2026-10-29'
  detail: API reference URL https://getecoback.com/api returns a redirect to a missing page, and no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 301
    url: https://getecoback.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: EcoBack provides a comprehensive climate and energy advice platform for households, offering free calculators and honest recommendations for cooling, heating, indoor air quality, and energy savings. The site helps users compare portable air conditioners, dehumidifiers, and heating solutions, and includes tools for heatwave alerts, frost warnings, and energy cost calculations.
image: https://getecoback.com/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at getecoback.com.
  name: getecoback-com MCP Server
  slug: getecoback-com-mcp-yml
modified: '2026-10-29'
name: getecoback-com
nav: Providers
network: true
overview: 'getecoback-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Homes, Climate, and Savings.


  getecoback-com''s developer surface includes support and 9 more developer resources.'
plans:
- name: Getecoback Com Plans Pricing
  plan_count: 0
  slug: getecoback-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Getecoback Com Rate Limits
  slug: getecoback-com-rate-limits
scopes:
- name: Getecoback Com Scopes
  scope_count: 0
  slug: getecoback-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getecoback-com/getecoback-com-2026-11-03T132702.png
security:
- kind: authentication
  name: Getecoback Com Authentication
  slug: getecoback-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Getecoback Com Domain Security
  slug: getecoback-com-domain-security
  summary_line: TLSv1.3
slug: getecoback-com
tags:
- Company
- Energy
- Homes
- Climate
- Savings
website: https://getecoback.com/
---
