---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debtbook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.debtbook.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/debtbook_stock/
- group: operate
  title: ''
  type: Support
  url: https://support.debtbook.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.debtbook.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.debtbook.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.debtbook.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.debtbook.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.debtbook.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.debtbook.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.debtbook.com/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.debtbook.com/legal
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.debtbook.com/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/debtbook-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.debtbook.com/
- group: auth
  title: ''
  type: Security
  url: https://www.debtbook.com/vdp
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.debtbook.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.debtbook.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.debtbook.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/debtbook-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/debtbook-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/debtbook-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/debtbook-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/debtbook-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/debtbook-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/debtbook-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/debtbook-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/debtbook-packages.yml
created: '2026-08-04'
description: DebtBook (a trademark of Fifth Asset, Inc., Charlotte, NC) is a cloud-based treasury and accounting software platform built for public finance teams — state and local government, K-12 and higher education, healthcare, and nonprofits. The platform covers debt management, cash management, investment management, contract management, and lease/subscription accounting under GASB 87, GASB 96 and ASC 842, plus an AI layer (Insights and the Marty analyst) that produces daily briefings and plain-English answers over an organization's treasury data. DebtBook's Cash Management product pulls real-time bank account data into the platform through a secure API integration powered by Koxa's Treasury Gateway, connecting customers to accounts at PNC, Regions Bank, Bank of America, JPMorgan, Wells Fargo and a growing list of US banks. As of this profile DebtBook publishes no public developer portal, no API reference, and no machine-readable API contract — its API surface is an inbound, contracted
  integration governed by published API integration terms rather than a self-service developer program.
image: https://www.debtbook.com/hs-fs/hubfs/DB-Logo_Blue-MD.png
layout: provider
modified: '2026-08-04'
name: DebtBook
nav: Providers
network: true
overview: 'DebtBook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Treasury Management, Government, Public Finance, and Debt Management.


  DebtBook''s developer surface includes support, engineering blog, pricing, signup flow, legal docs, changelog, authentication, and 21 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 34.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debtbook/refs/heads/main/screenshots/debtbook-2026-08-07T164221.png
security:
- kind: authentication
  name: Debtbook Authentication
  slug: debtbook-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Debtbook Domain Security
  slug: debtbook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Debtbook Vulnerability Disclosure
  slug: debtbook-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Debtbook Trust Center
  slug: debtbook-trust-center
  summary_line: SOC 1 Type 1, SOC 1 Type 2, SOC 2 Type 1, SOC 2 Type 2, CSA STAR Level One
slug: debtbook
tags:
- Company
- Treasury Management
- Government
- Public Finance
- Debt Management
- Cash Management
- Accounting
- Lease Accounting
- Investment Management
- Non-Profit
- Higher Education
- Healthcare
- Software-as-a-Service
website: https://www.debtbook.com/
---
