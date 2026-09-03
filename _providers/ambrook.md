---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.6
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://ambrook.com
- group: commercial
  title: ''
  type: Pricing
  url: https://ambrook.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ambrook.com/overview/get-started
- group: start
  title: ''
  type: Login
  url: https://ambrook.com/login
- group: company
  title: ''
  type: Blog
  url: https://ambrook.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.ambrook.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ambrook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambrook.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ambrook
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ambrook-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ambrook-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ambrook-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ambrook-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ambrook-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambrook-domain-security.yml
created: '2026-07-17'
description: Ambrook is financial management software for farms, ranches, and the trades — construction, trucking, manufacturing, and the interconnected businesses that produce, build, and move physical goods. Founded in 2020 and based in New York, it combines bookkeeping, invoicing, payments, and inventory in one platform, with Schedule F/C tax alignment, enterprise tagging for tracking profitability by business line, and cost-per-head livestock tracking. Positioned as a QuickBooks alternative for agriculture and margin-sensitive industries, Ambrook pairs a full-featured mobile app with U.S.-based, ag-centric support. It also operates an OAuth-gated Model Context Protocol (MCP) server that lets AI agents connect to a business's Ambrook data via a read-only GraphQL surface. Ambrook raised a $26.1M Series A and is backed by investors including Homebrew.
image: https://ambrook.com/img/share/default-og.png
layout: provider
mcp_servers:
- description: Ambrook operates a hosted Model Context Protocol (MCP) server that lets AI agents connect to a farm/trade business's Ambrook accounting data. Access is gated by an OAuth 2.1 authorization-code flow (P
  name: Ambrook MCP Server
  slug: ambrook-mcp-server
modified: '2026-07-17'
name: Ambrook
nav: Providers
network: true
overview: 'Ambrook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Agriculture, Accounting, and Bookkeeping.


  Ambrook''s developer surface includes pricing, signup flow, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 12
scopes:
- name: Ambrook Scopes
  scope_count: 5
  slug: ambrook-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 21.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ambrook/refs/heads/main/screenshots/ambrook-2026-07-25T200036.png
security:
- kind: authentication
  name: Ambrook Authentication
  slug: ambrook-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ambrook Domain Security
  slug: ambrook-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ambrook
tags:
- Company
- Fintech
- Agriculture
- Accounting
- Bookkeeping
- Payments
- Farm Management
- MCP
website: https://ambrook.com
---
