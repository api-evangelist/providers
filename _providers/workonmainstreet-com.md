---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/workonmainstreet-com/mcp/workonmainstreet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/workonmainstreet-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/workonmainstreet-com/hosts/workonmainstreet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/workonmainstreet-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/workonmainstreet-com/security/workonmainstreet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workonmainstreet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://workonmainstreet.com/
- group: company
  title: ''
  type: Blog
  url: https://mainstreet.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mainstreet.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mainstreet.com/terms-of-service
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.mainstreet.com/
coverage:
  checked: '2026-10-29'
  detail: The provider's main site returns a JavaScript shell and the developer portal is a SPA, preventing machine-readable API discovery.
  evidence:
  - status: 200
    url: https://workonmainstreet.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: MainStreet is a private holding company that invests in durable businesses across key sectors such as software, AI, infrastructure, sports and entertainment, and finance. It acquires companies, provides operational support, and holds them for the long term, focusing on sustainable growth and reinvestment of profits. The firm emphasizes transparent offers, quick acquisition processes, and maintaining founder involvement, aiming to build lasting value for its portfolio companies.
image: https://mainstreet.com/opengraph.png
layout: provider
mcp_servers:
- description: Remote MCP server at dashboard.mainstreet.com.
  name: MainStreet MCP Server
  slug: workonmainstreet-com-mcp-yml
modified: '2026-10-29'
name: MainStreet
nav: Providers
network: true
overview: 'MainStreet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HoldingCompany, Investment, PrivateEquity, Portfolio, and Technology.


  MainStreet''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Workonmainstreet Com Plans Pricing
  plan_count: 0
  slug: workonmainstreet-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Workonmainstreet Com Rate Limits
  slug: workonmainstreet-com-rate-limits
scopes:
- name: Workonmainstreet Com Scopes
  scope_count: 0
  slug: workonmainstreet-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Workonmainstreet Com Authentication
  slug: workonmainstreet-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Workonmainstreet Com Domain Security
  slug: workonmainstreet-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: workonmainstreet-com
tags:
- HoldingCompany
- Investment
- PrivateEquity
- Portfolio
- Technology
website: https://workonmainstreet.com/
---
