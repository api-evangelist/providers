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
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Dominick Prevete mortgage brokerage services.
  name: Dominick Prevete API
  slug: dominick-prevete-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/dominickprevete-com/llms/dominickprevete-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dominickprevete-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dominickprevete-com/mcp/dominickprevete-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dominickprevete-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dominickprevete-com/mcp/dominickprevete-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dominickprevete-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dominickprevete-com/hosts/dominickprevete-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dominickprevete-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dominickprevete-com/vendors/dominickprevete-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dominickprevete-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dominickprevete.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dominickprevete.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://dominickprevete.com/blog
- group: auth
  href: https://artifacts.apis.io/dominickprevete-com/security/dominickprevete-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dominickprevete-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dominickprevete.com/
coverage:
  checked: '2026-10-29'
  detail: MCP tools list requires authentication, preventing contract discovery.
  evidence:
  - status: 406
    url: https://dominickprevete.com/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Mortgage brokerage arranging business-purpose financing for real estate investors — DSCR, fix-and-flip, bridge, ground-up construction, and rental portfolio loans, placed across a network of 100+ lenders. National Loan Provider arranges and places financing; it does not lend directly.
image: https://dominickprevete.com/og/dominick-prevete-card.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at dominickprevete.com.
  name: dominickprevete-com MCP Server
  slug: dominickprevete-com-mcp-yml
modified: '2026-10-29'
name: dominickprevete-com
nav: Providers
network: true
overview: 'dominickprevete-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Loans, Real Estate, and Mortgage Brokerage.


  dominickprevete-com''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Dominickprevete Com Plans Pricing
  plan_count: 0
  slug: dominickprevete-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Dominickprevete Com Rate Limits
  slug: dominickprevete-com-rate-limits
scopes:
- name: Dominickprevete Com Scopes
  scope_count: 0
  slug: dominickprevete-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
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
  name: Dominickprevete Com Authentication
  slug: dominickprevete-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dominickprevete Com Domain Security
  slug: dominickprevete-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dominickprevete-com
tags:
- Company
- Finance
- Loans
- Real Estate
- Mortgage Brokerage
website: https://dominickprevete.com/
---
