---
access_model:
  confidence: low
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/livermore-club/llms/livermore-club-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/livermore-club-llms.txt
- group: agent
  href: https://artifacts.apis.io/livermore-club/mcp/livermore-club-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/livermore-club-mcp.yml
- group: other
  href: https://artifacts.apis.io/livermore-club/hosts/livermore-club-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livermore-club-hosts.yml
- group: other
  href: https://artifacts.apis.io/livermore-club/vendors/livermore-club-vendors.yml
  title: ''
  type: Vendors
  url: vendors/livermore-club-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unitedstates
- group: start
  title: ''
  type: DeveloperPortal
  url: https://livermore.club/en/developers
- group: auth
  href: https://artifacts.apis.io/livermore-club/security/livermore-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livermore-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://livermore.club/
created: '2026-10-30'
description: Livermore Club provides free, bilingual access to SEC-derived data, including insider trades from over 950,000 Form 4 filings, institutional 13F holdings for thousands of institutions, and super‑investor activity. Updated daily, the platform offers searchable data for U.S. and Taiwan markets, empowering investors and analysts with transparent, up‑to‑date financial disclosures.
image: https://livermore.club/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at livermore.club.
  name: livermore-club MCP Server
  slug: livermore-club-mcp-yml
modified: '2026-10-30'
name: livermore-club
nav: Providers
network: true
overview: livermore-club is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Insider Trading, and Investment.
random_paper: 8
rate_limits:
- limit_count: 0
  name: Livermore Club Rate Limits
  slug: livermore-club-rate-limits
scopes:
- name: Livermore Club Scopes
  scope_count: 0
  slug: livermore-club-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/livermore-club/livermore-club-2026-11-03T134947.png
security:
- kind: authentication
  name: Livermore Club Authentication
  slug: livermore-club-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Livermore Club Domain Security
  slug: livermore-club-domain-security
  summary_line: TLSv1.3 · DMARC
slug: livermore-club
tags:
- Company
- Finance
- Data
- Insider Trading
- Investment
website: https://livermore.club/
---
