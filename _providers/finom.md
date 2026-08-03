---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://finom.co
- group: commercial
  title: ''
  type: Pricing
  url: https://finom.co/de-de/pricing
- group: company
  title: ''
  type: Blog
  url: https://finom.co/de-de/blog
- group: operate
  title: ''
  type: Support
  url: https://help.finom.co/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.finom.co/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.finom.co/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finom-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finom-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/finom-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/finom-security.txt
- group: auth
  title: ''
  type: Security
  url: https://finom.co/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/finom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finom-domain-security.yml
created: '2026-07-17'
description: Finom is a European fintech headquartered in Amsterdam that provides business banking, invoicing, and financial management for entrepreneurs, freelancers, and SMEs. Operating as a licensed Electronic Money Institution (EMI) supervised by De Nederlandsche Bank (DNB), Finom offers multi-currency business accounts, 24/7 SEPA Instant and SWIFT payments, direct debits, Visa Business physical and virtual cards with up to 3% cashback, compliant e-invoicing (ZUGFeRD, XRechnung), and integrations with accounting platforms such as DATEV, Lexware, sevDesk, Xero, and QuickBooks. It serves Germany, France, Italy, Spain, and the Netherlands with region-specific tooling. Finom does not currently publish a public developer API program; this profile captures its public discovery, security, and operational surface (llms.txt, security.txt / Intigriti VDP, domain security, status page).
image: https://finom.co/preview/index_en.png
layout: provider
modified: '2026-07-19'
name: Finom
nav: Providers
network: true
overview: 'Finom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Business Banking, Payments, and Invoicing.


  Finom''s developer surface includes pricing, engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 62
score:
  band: emerging
  composite: 16.7
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finom/refs/heads/main/screenshots/finom-2026-07-25T214540.png
security:
- kind: domain-security
  name: Finom Domain Security
  slug: finom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Finom Vulnerability Disclosure
  slug: finom-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: finom
tags:
- Company
- Fintech
- Business Banking
- Payments
- Invoicing
- Accounting
- SEPA
- SME
- Europe
- Financial Management
website: https://finom.co
---
