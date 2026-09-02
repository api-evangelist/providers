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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The OpenID Connect / OAuth 2.0 authorization surface behind MainStreet sign-in, served from login.mainstreet.com on an Auth0 tenant. It publishes a complete OIDC Discovery 1.0 document and an RFC 8414
  name: MainStreet Identity (OpenID Connect)
  slug: identity
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mainstreet.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mainstreet.ai/knowledge-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://mainstreet.ai/knowledge-hub/library/
- group: start
  title: ''
  type: GettingStarted
  url: https://mainstreet.ai/rd-credit.html
- group: operate
  title: ''
  type: Support
  url: https://help.mainstreet.com/
- group: company
  title: ''
  type: Blog
  url: https://mainstreet.ai/articles.html
- group: commercial
  title: ''
  type: Pricing
  url: https://mainstreet.ai/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mainstreet.com/welcome
- group: start
  title: ''
  type: Login
  url: https://login.mainstreet.com/u/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mainstreet.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mainstreet.ai/privacy.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://mainstreet.ai/updates.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mainstreet-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mainstreet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mainstreet-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mainstreet-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mainstreet-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/mainstreet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mainstreet-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mainstreet-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/mainstreet_stock/
created: '2026-08-04'
description: MainStreet is a US small-business tax-credit and back-office platform that identifies, calculates, and files R&D tax credits alongside a client's CPA. Its service covers qualified research expense (QRE) identification under IRC §41, the IRS four-part test, business-component documentation, Form 6765 preparation (including the mandatory Section G component-level reporting that begins with tax years starting after 31 December 2025), the §41(h) payroll-tax offset for pre-revenue startups, and state R&D credits across 30+ states. Beyond R&D it claims SECURE Act retirement-plan credits, the Small Business Health Care Tax Credit, and the Disabled Access Credit, and it sells adjacent back-office services — entity formation, banking, expense tracking, and bookkeeping and tax filing. MainStreet was founded in 2019 as a venture-backed R&D tax-credit fintech and was acquired by Employer.com in May 2025; the brand now operates as part of that back-office suite. MainStreet ships no public
  product API, developer portal, or OpenAPI definition — it is an API consumer (payroll data via Finch, document generation via Anvil) rather than an API producer. Its only public machine-readable contract is the OpenID Connect and RFC 8414 discovery pair served by its identity host.
image: https://www.mainstreet.com/opengraph.jpg
layout: provider
modified: '2026-08-04'
name: MainStreet
nav: Providers
network: true
overview: 'MainStreet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Tax Credits, Accounting, and Financial-Services.


  MainStreet''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 14 more developer resources.'
random_paper: 13
scopes:
- name: Mainstreet Scopes
  scope_count: 14
  slug: mainstreet-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/implicit/deviceCode
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.5
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mainstreet/refs/heads/main/screenshots/mainstreet-2026-08-07T171931.png
security:
- kind: authentication
  name: Mainstreet Authentication
  slug: mainstreet-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Mainstreet Domain Security
  slug: mainstreet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mainstreet
tags:
- Company
- Tax
- Tax Credits
- Accounting
- Financial-Services
- Small Business
- Fintech
- Bookkeeping
- Compliance
- Payroll
website: https://mainstreet.ai/
---
