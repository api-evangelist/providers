---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
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
    error_semantics: documented
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP endpoint providing access to Japanese public data sources such as holiday calendars, corporate registration, nutrition information, and product recall data.
  name: Plugrail MCP
  slug: plugrail-mcp
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/plugrail-dev/rate-limits/plugrail-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plugrail-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/plugrail-dev/plans/plugrail-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plugrail-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/plugrail-dev/errors/plugrail-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plugrail-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/plugrail-dev/mcp/plugrail-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/plugrail-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/plugrail-dev/hosts/plugrail-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plugrail-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/plugrail-dev/vendors/plugrail-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plugrail-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/plugrail-dev/security/plugrail-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plugrail-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plugrail.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://plugrail.dev/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://plugrail.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plugrail.dev/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plugrail.dev/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plugrail
coverage:
  checked: '2026-10-29'
  detail: MCP endpoint https://jp-calendar.plugrail.dev/mcp requires authentication, returning 405/406, preventing contract retrieval.
  evidence:
  - status: 405
    url: https://jp-calendar.plugrail.dev/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Plugrail provides a suite of Model Context Protocol (MCP) servers that connect Japanese public data sources—such as holiday calendars, corporate registration, nutrition information, and product recall data—to AI agents. By exposing this data via streamable HTTP endpoints, developers can query authoritative information without needing to manage raw datasets. The service offers free anonymous access with rate‑limited usage and paid plans for higher volume, and it includes clear source citations and disclaimer notices. Plugrail aims to simplify integration of public sector data into AI‑driven workflows.
image: https://plugrail.dev/og.svg
layout: provider
mcp_servers:
- description: Remote MCP server at jp-calendar.plugrail.dev.
  name: plugrail-dev MCP Server
  slug: plugrail-dev-mcp-yml
modified: '2026-10-29'
name: plugrail-dev
nav: Providers
network: true
overview: 'plugrail-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Public Data, Japan, and AI Integration.


  plugrail-dev''s developer surface includes documentation, pricing, and 11 more developer resources.'
plans:
- name: Plugrail Dev Plans Pricing
  plan_count: 1
  slug: plugrail-dev-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Plugrail Dev Rate Limits
  slug: plugrail-dev-rate-limits
scopes:
- name: Plugrail Dev Scopes
  scope_count: 0
  slug: plugrail-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 68.3
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/plugrail-dev/plugrail-dev-2026-11-03T141318.png
security:
- kind: authentication
  name: Plugrail Dev Authentication
  slug: plugrail-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Plugrail Dev Domain Security
  slug: plugrail-dev-domain-security
  summary_line: TLSv1.3
slug: plugrail-dev
tags:
- Company
- MCP
- Public Data
- Japan
- AI Integration
website: https://plugrail.dev/
---
