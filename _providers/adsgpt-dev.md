---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AdsGPT public API (undocumented machine‑readable spec).
  name: AdsGPT API
  slug: adsgpt-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/adsgpt-dev/authentication/adsgpt-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adsgpt-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adsgpt-dev/scopes/adsgpt-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adsgpt-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/adsgpt-dev/conformance/adsgpt-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adsgpt-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adsgpt-dev/llms/adsgpt-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adsgpt-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/adsgpt-dev/mcp/adsgpt-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adsgpt-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adsgpt-dev/well-known/adsgpt-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsgpt-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/adsgpt-dev/hosts/adsgpt-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adsgpt-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/adsgpt-dev/vendors/adsgpt-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adsgpt-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adsgpt-dev/security/adsgpt-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsgpt-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adsgpt.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adsgpt.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adsgpt.dev/quickstart/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adsgpt.dev/es/privacidad/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adsgpt.dev/es/terminos/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.adsgpt.dev/
coverage:
  checked: '2026-10-31'
  detail: Documentation is public but provides no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.adsgpt.dev/quickstart/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AdsGPT is an AI-powered advertising platform that creates, launches, and optimizes ad campaigns across Google, Instagram, TikTok, LinkedIn, and more. Users simply describe their product or provide a URL, and AdsGPT generates creatives, copy, targeting, and budgets, continuously optimizing spend for maximum ROI. The service supports multiple brands, offers free and paid plans, and integrates with major ad networks, providing a unified dashboard for campaign management and performance insights.
image: https://www.adsgpt.dev/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adsgpt.dev requiring OAuth.
  name: AdsGPT MCP Server
  slug: adsgpt-dev-mcp-yml
modified: '2026-11-01'
name: AdsGPT
nav: Providers
network: true
overview: 'AdsGPT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Artificial Intelligence, Marketing, and Automation.


  AdsGPT''s developer surface includes authentication, documentation, getting-started guide, and 12 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 0
  name: Adsgpt Dev Rate Limits
  slug: adsgpt-dev-rate-limits
scopes:
- name: Adsgpt Dev Scopes
  scope_count: 0
  slug: adsgpt-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adsgpt Dev Authentication
  slug: adsgpt-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adsgpt Dev Domain Security
  slug: adsgpt-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adsgpt-dev
tags:
- Company
- Advertising
- Artificial Intelligence
- Marketing
- Automation
- Platform
website: https://adsgpt.dev/
---
