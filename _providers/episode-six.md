---
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The TRITIUM platform API is Episode Six's real-time RESTful interface for card issuing, issuer processing and ledger management — card program setup, account and ledger operations, transaction process
  name: Episode Six TRITIUM Platform API
  slug: episode-six-tritium-platform-api
- description: 'A Model Context Protocol server published by Episode Six on its own documentation host at https://docs.episodesix.com/mcp, exposing the TRITIUM developer documentation to agents. The endpoint answers '
  name: Episode Six Documentation MCP Server
  slug: episode-six-docs-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/episode-six-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://episodesix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://episodesix.com/platform/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.episodesix.com/
- group: start
  title: ''
  type: SignUp
  url: https://episodesix.com/access-request
- group: operate
  title: ''
  type: Support
  url: https://episodesix.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://buzz.episodesix.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://buzz.episodesix.com/rss.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://episodesix.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://episodesix.com/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://episodesix.com/company/careers
- group: company
  title: ''
  type: Newsroom
  url: https://episodesix.com/newsroom
- group: auth
  title: ''
  type: Compliance
  url: https://episodesix.com/platform/paymentsecurity
- group: design
  title: ''
  type: Conformance
  url: conformance/episode-six-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/episode-six-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/episode-six-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/episode-six-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/episode-six-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/episode-six-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/episode-six-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/episode-six-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/episode-six-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/episode-six-lifecycle.yml
- group: other
  title: ''
  type: ForgeGlobalListing
  url: https://forgeglobal.com/episode-six_stock/
coverage:
  checked: '2026-08-12'
  detail: The TRITIUM API reference at docs.episodesix.com answers every path with an "Access Restricted — provide your access code" screen and 307-redirects docs.json, llms.txt and every deep path to /login, with the only route in being the "Request access to our documentation and APIs" contact-sales form at episodesix.com/access-request.
  evidence:
  - status: 307
    url: https://docs.episodesix.com/docs.json
  - status: 307
    url: https://docs.episodesix.com/llms.txt
  - status: 200
    url: https://docs.episodesix.com/
  - status: 200
    url: https://episodesix.com/access-request
  reason: sales-gate
  state: gated
created: '2026-08-12'
description: Episode Six is a global payment technology company founded in 2015 by John Mitchell, Chermaine Hu and Futeh Kao that supplies banks, fintechs and brands with a cloud-native card issuing and ledger management platform marketed as TRITIUM. The platform is described by the company as an API-first open architecture delivering real-time RESTful API processing for credit, debit, prepaid, commercial, installment and virtual card programs alongside a parallel ledger supporting virtual accounts, revolving credit, installments, loans, interest-bearing and term deposits, multi-currency and negative balance accounts. Episode Six operates in 45+ countries with staff in 20 countries, and states it is a PCI DSS Level 1 Service Provider that is SOC 2 Type II audited and uses GDPR as its global data baseline. Its API documentation is published at docs.episodesix.com behind an access-code gate, so no public OpenAPI is available.
image: https://episodesix.com/hubfs/Home%20Page%20Featured%20Image%20Oct2025.png
layout: provider
mcp_servers:
- description: A Model Context Protocol server Episode Six serves from its own documentation host. It exposes the TRITIUM developer documentation to agents. It is not a TRITIUM platform (card issuing / ledger) MCP s
  name: Episode Six MCP Server
  slug: episode-six-mcp-server
modified: '2026-08-12'
name: Episode Six
nav: Providers
network: true
overview: 'Episode Six publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Card Issuing, Issuer Processing, and Ledger.


  Episode Six''s developer surface includes documentation, signup flow, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Episode Six Plans Pricing
  plan_count: 0
  slug: episode-six-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Episode Six Rate Limits
  slug: episode-six-rate-limits
scopes:
- name: Episode Six Scopes
  scope_count: 1
  slug: episode-six-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Episode Six Authentication
  slug: episode-six-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Episode Six Domain Security
  slug: episode-six-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: episode-six
tags:
- Company
- Payments
- Card Issuing
- Issuer Processing
- Ledger
- Banking
- Financial-Services
- Embedded Finance
- Fintech
- Virtual Accounts
- Virtual Cards
- Credit
- Prepaid
- Multi-Currency
website: https://episodesix.com/
---
