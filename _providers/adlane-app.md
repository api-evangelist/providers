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
- description: Read‑only MCP servers for Google Ads, Meta Ads, and Adlane accounts, providing tools to explore ad data via OAuth.
  name: Adlane MCP API
  slug: adlane-mcp-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/adlane-app/llms/adlane-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adlane-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/adlane-app/mcp/adlane-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adlane-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adlane-app/well-known/adlane-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adlane-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/adlane-app/hosts/adlane-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adlane-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/adlane-app/vendors/adlane-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adlane-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/adlane-app/packages/adlane-app-packages.yml
  title: ''
  type: SDKs
  url: packages/adlane-app-packages.yml
- group: build
  href: https://artifacts.apis.io/adlane-app/packages/adlane-app-packages.yml
  title: ''
  type: Packages
  url: packages/adlane-app-packages.yml
- group: auth
  href: https://artifacts.apis.io/adlane-app/security/adlane-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adlane-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adlane.app/
- group: docs
  title: ''
  type: Documentation
  url: https://adlane.app/guides/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adlane.app/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adlane.app/terms/
- group: start
  title: ''
  type: Login
  url: https://adlane.app/app/
coverage:
  checked: '2026-10-31'
  detail: MCP endpoints require OAuth authentication, returning 401 on unauthenticated requests.
  evidence:
  - status: 401
    url: https://adlane.app/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Adlane is an AI assistant for Google Ads and Meta Ads that helps users review campaign performance, research keywords, and draft campaigns in a single AI workspace. It offers read‑only MCP servers for Google Ads, Meta Ads, and Adlane accounts, providing tools to explore ad data, generate insights, and make informed decisions without changing campaigns.
image: https://adlane.app/social.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adlane.app requiring OAuth.
  name: Adlane MCP Server
  slug: adlane-app-mcp-yml
modified: '2026-10-31'
name: Adlane
nav: Providers
network: true
overview: 'Adlane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, Google Ads, Meta Ads, and MCP.


  Adlane''s developer surface includes documentation and 12 more developer resources.'
random_paper: 19
scopes:
- name: Adlane App Scopes
  scope_count: 0
  slug: adlane-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 18.5
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
security:
- kind: authentication
  name: Adlane App Authentication
  slug: adlane-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adlane App Domain Security
  slug: adlane-app-domain-security
  summary_line: TLSv1.3
slug: adlane-app
tags:
- Artificial Intelligence
- Advertising
- Google Ads
- Meta Ads
- MCP
website: https://adlane.app/
---
