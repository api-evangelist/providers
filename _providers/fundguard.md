---
access_model:
  confidence: medium
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: A Model Context Protocol server served from FundGuard's own corporate web host via the WordPress MCP adapter, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-res
  name: FundGuard Website MCP Server
  slug: fundguard-website-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fundguard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fundguard.com/product/
- group: operate
  title: ''
  type: Support
  url: https://www.fundguard.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.fundguard.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://www.fundguard.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fundguard.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FundGuard
- group: start
  title: ''
  type: SignUp
  url: https://www.fundguard.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fundguard.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fundguard.com/privacy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.fundguard.com/cookie-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.fundguard.com/digital-operational-resilience-act/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fundguard/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FundGuard
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@FundGuardInsights
- group: company
  title: ''
  type: Careers
  url: https://www.fundguard.com/careers/
- group: other
  title: ''
  type: MediaKit
  url: https://www.fundguard.com/media-kit/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fundguard-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fundguard-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fundguard-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fundguard-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fundguard-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fundguard-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fundguard-llms.txt
created: '2026-08-01'
description: FundGuard is an AI-powered, cloud-native investment accounting operating system for asset managers, asset owners, custodian banks and fund administrators. A single real-time accounting engine acts as the core system of record across Fund Accounting/ABOR, Investment Accounting/IBOR and Private Markets portfolio accounting, supporting mutual funds, ETFs, hedge funds, insurance products and pension funds with multi-book views (ABOR, IBOR, GAAP, tax, performance, currency and custom), shadow and contingent NAV, reconciliation, Report Studio and AI-driven anomaly detection with suggested resolutions. Founded 2018, headquartered in New York with offices in Dedham MA, Tel Aviv and London; backed by Citi, State Street, Key1 Capital, Blumberg Capital, Euclidean Capital, Hamilton Lane, LionBird and Team8, and running on AWS and Microsoft Azure. The platform is marketed as API-first for front- and middle-office integration with portfolio management systems, custodians, administrators and
  data providers, but as of this pass FundGuard publishes no public developer portal, API reference or machine-readable API contract — the customer knowledge base at kb.fundguard.com is behind a login and the product runs on per-tenant hosts.
image: https://www.fundguard.com/wp-content/uploads/2020/08/fundguard-logo-cropped.svg
layout: provider
mcp_servers:
- description: ''
  name: FundGuard MCP Server
  slug: fundguard-mcp-server
modified: '2026-08-01'
name: FundGuard
nav: Providers
network: true
overview: 'FundGuard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include investment-accounting, Fund Accounting, ibor, abor, and NAV.


  FundGuard''s developer surface includes documentation, support, engineering blog, signup flow, YouTube channel, authentication, and 19 more developer resources.'
random_paper: 15
scopes:
- name: Fundguard Scopes
  scope_count: 1
  slug: fundguard-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fundguard/refs/heads/main/screenshots/fundguard-2026-08-07T165522.png
security:
- kind: authentication
  name: Fundguard Authentication
  slug: fundguard-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fundguard Domain Security
  slug: fundguard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fundguard
tags:
- investment-accounting
- Fund Accounting
- ibor
- abor
- NAV
- Asset Management
- portfolio-accounting
- Private Markets
- Financial-Services
- Fintech
- Software-as-a-Service
- Artificial Intelligence
- MCP
website: https://www.fundguard.com/
---
