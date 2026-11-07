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
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: TokenCompass provides a measurement layer for AI initiatives, aggregating spend across multiple AI providers.
  name: TokenCompass API
  slug: tokencompass-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/tokencompass/mcp/tokencompass-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tokencompass-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tokencompass/well-known/tokencompass-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tokencompass-well-known.yml
- group: other
  href: https://artifacts.apis.io/tokencompass/hosts/tokencompass-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tokencompass-hosts.yml
- group: other
  href: https://artifacts.apis.io/tokencompass/vendors/tokencompass-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tokencompass-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tokencompass/security/tokencompass-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tokencompass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tokencompass.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tokencompass.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tokencompass.ai/terms
coverage:
  checked: '2026-10-29'
  detail: Developer portal at https://app.tokencompass.ai redirects to a login page requiring authentication.
  evidence:
  - status: 200
    url: https://app.tokencompass.ai/login
  reason: partner-login
  state: gated
created: '2026-10-29'
description: TokenCompass provides a measurement layer for AI initiatives, aggregating spend across multiple AI providers such as Claude, Codex, and Cursor, and attributing usage and impact across the enterprise. It helps organizations prove the value of their AI transformation by delivering spend visibility, impact attribution, and multi‑provider analytics in a unified reporting platform.
image: https://tokencompass.ai/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at app.tokencompass.ai.
  name: TokenCompass MCP Server
  slug: tokencompass-mcp-yml
modified: '2026-10-29'
name: TokenCompass
nav: Providers
network: true
overview: TokenCompass is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Software-as-a-Service, Fintech, and Reporting.
random_paper: 7
scopes:
- name: Tokencompass Scopes
  scope_count: 0
  slug: tokencompass-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tokencompass/tokencompass-2026-11-03T144832.png
security:
- kind: authentication
  name: Tokencompass Authentication
  slug: tokencompass-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tokencompass Domain Security
  slug: tokencompass-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tokencompass
tags:
- Artificial Intelligence
- Analytics
- Software-as-a-Service
- Fintech
- Reporting
website: https://tokencompass.ai
---
