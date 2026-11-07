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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides data endpoints for Southeast Asian e‑commerce, ride‑hailing, and market data via the SEA MCP platform.
  name: Sea MCP API
  slug: sea-mcp-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/seamcp-com/llms/seamcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seamcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/seamcp-com/well-known/seamcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seamcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/seamcp-com/hosts/seamcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seamcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/seamcp-com/vendors/seamcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seamcp-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SeaMCP
- group: auth
  href: https://artifacts.apis.io/seamcp-com/security/seamcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seamcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seamcp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seamcp.com/terms
coverage:
  checked: '2026-10-29'
  detail: OAuth protected resource requires authentication, preventing public access to the API.
  evidence:
  - status: 200
    url: https://seamcp.com/.well-known/oauth-protected-resource
  reason: partner-login
  state: gated
created: '2026-10-29'
description: SEA MCP (seamcp.com) provides Southeast Asia data for AI agents, aggregating publicly available information from platforms such as Shopee, Grab, and the Indonesia Stock Exchange (IDX). The service offers MCP endpoints that return structured data via simple HTTP URLs, enabling developers to integrate regional e‑commerce, ride‑hailing, and market data into AI applications without scraping. Users sign in with Google and receive a free quota of 100 tool calls per month. The platform emphasizes responsible use, with clear terms of service and usage limits. It is positioned as a data‑as‑a‑service layer for AI assistants operating in Southeast Asian markets.
layout: provider
modified: '2026-10-29'
name: seamcp-com
nav: Providers
network: true
overview: seamcp-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, Southeast Asia, Data, Artificial Intelligence, and Shopee.
plans:
- name: Seamcp Com Plans Pricing
  plan_count: 0
  slug: seamcp-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Seamcp Com Rate Limits
  slug: seamcp-com-rate-limits
scopes:
- name: Seamcp Com Scopes
  scope_count: 0
  slug: seamcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 69.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/seamcp-com/seamcp-com-2026-11-03T142905.png
security:
- kind: authentication
  name: Seamcp Com Authentication
  slug: seamcp-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Seamcp Com Domain Security
  slug: seamcp-com-domain-security
  summary_line: TLSv1.3
slug: seamcp-com
tags:
- MCP
- Southeast Asia
- Data
- Artificial Intelligence
- Shopee
- Grab
- IDX
website: https://seamcp.com/
---
