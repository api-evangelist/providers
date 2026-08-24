---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Unified REST API for embedding credit-building infrastructure, covering member enrollment, tradeline furnishing to the credit bureaus, and dispute status. Access is gated behind a demo/onboarding proc
  name: Kikoff Enterprise API
  slug: kikoff-enterprise-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kikoff-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://kikoff.com/vulnerability-disclosure-policy.pdf
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kikoff-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kikoff-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kikoff-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kikoff-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kikoff.com
- group: company
  title: ''
  type: Website
  url: https://kikoff.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.kikoff.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://kikoff.com/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://kikoff.com/frequently-asked-questions
- group: operate
  title: ''
  type: Support
  url: https://kikoff.com/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://kikoff.com/how-kikoff-works
- group: start
  title: ''
  type: SignUp
  url: https://kikoff.com/signup
- group: start
  title: ''
  type: Login
  url: https://kikoff.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kikoff.com/terms.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kikoff.com/privacy-policy.pdf
created: '2026-07-17'
description: Kikoff is a San Francisco-based consumer fintech, founded in 2019, that helps people build and repair credit. Its products include a Credit Account that furnishes tradelines to all three bureaus (Equifax, Experian, TransUnion), rent and bill reporting, credit monitoring and disputes, an AI Debt Negotiator, the Fynn AI credit coach, and an invite-only secured credit card, sold across Basic, Premium, and Ultimate subscription tiers. Kikoff Enterprise exposes a unified REST API covering member enrollment, tradeline furnishing, and dispute status so businesses can embed credit-building infrastructure. Backed by GGV Capital and Lightspeed Venture Partners.
image: https://cdn.prod.website-files.com/6917adb812aab3b38f8a8547/69f8d983cdfd88f45bb3d46b_kikoff_website%20preview%20(1).png
layout: provider
modified: '2026-07-19'
name: Kikoff
nav: Providers
network: true
overview: 'Kikoff publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit, Credit Building, and Credit Reporting.


  Kikoff''s developer surface includes engineering blog, pricing, support, getting-started guide, signup flow, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kikoff/refs/heads/main/screenshots/kikoff-2026-07-25T223738.png
security:
- kind: domain-security
  name: Kikoff Domain Security
  slug: kikoff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kikoff Vulnerability Disclosure
  slug: kikoff-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kikoff
tags:
- Company
- Fintech
- Credit
- Credit Building
- Credit Reporting
- Consumer Finance
- Personal Finance
- Lending
website: https://kikoff.com/
---
