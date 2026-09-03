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
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightyear-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightyear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lightyear.com
- group: company
  title: ''
  type: About
  url: https://lightyear.com/en-eu/about
- group: commercial
  title: ''
  type: Pricing
  url: https://lightyear.com/en-eu/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lightyear.com/en-eu/signup
- group: start
  title: ''
  type: Login
  url: https://lightyear.com/en-eu/login
- group: company
  title: ''
  type: Blog
  url: https://lightyear.com/en-eu/blog
- group: operate
  title: ''
  type: Support
  url: https://lightyear.com/en-eu/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://lightyear.com/en-eu/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lightyear.com/en-eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightyear.com/en-eu/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://lightyear.com/en-eu/cookie-policy
- group: auth
  title: ''
  type: Disclosures
  url: https://lightyear.com/en-eu/disclosures
- group: other
  title: ''
  type: Accessibility
  url: https://lightyear.com/en-eu/accessibility-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightyear.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.lightyear.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/go_lightyear
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/gb/app/lightyear-investing/id1562105616
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.golightyear.mobile
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightyear-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightyear-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightyear-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightyear-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://lightyear.com/en-eu/blog/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightyear-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightyear-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://lightyear.com/en-eu/disclosures
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightyear-llms.txt
created: '2026-07-17'
description: Lightyear is a European retail investing platform founded by former Wise (TransferWise) employees Martin Sokk and Mihkel Aamer, offering commission-light access to roughly 6,000 stocks, ETFs, money market funds, bonds and crypto, plus interest-bearing cash "Vaults" managed with BlackRock and J.P. Morgan money market funds. The service runs through mobile apps (iOS and Android) and a web app, with a separate Lightyear for Business offering. Lightyear UK Ltd is authorised by the UK Financial Conduct Authority (FRN 987226) and Lightyear Europe AS is regulated by the Estonian Financial Supervision Authority, with operations in London and Tallinn. Lightyear does not publish a public developer API or developer portal; its api.lightyear.com host serves the first-party apps and publishes an RFC 8414 OAuth 2.0 authorization server metadata document for an internal MCP scope.
image: https://lightyear.com/cms/OG_Default_EN_7a4714f5fe.png
layout: provider
mcp_servers:
- description: ''
  name: Lightyear MCP Server
  slug: lightyear-mcp-server
modified: '2026-07-19'
name: Lightyear
nav: Providers
network: true
overview: 'Lightyear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Investing, Brokerage, and Stocks.


  Lightyear''s developer surface includes pricing, signup flow, engineering blog, support, authentication, changelog, and 23 more developer resources.'
random_paper: 3
scopes:
- name: Lightyear Scopes
  scope_count: 1
  slug: lightyear-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 31.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 66.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Lightyear Authentication
  slug: lightyear-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lightyear Domain Security
  slug: lightyear-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lightyear
tags:
- Company
- Financial-Services
- Investing
- Brokerage
- Stocks
- ETFs
- Fintech
- Wealth Management
- Europe
website: https://lightyear.com
---
