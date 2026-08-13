---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sharebite-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sharebite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sharebite.com/
- group: operate
  title: ''
  type: Support
  url: https://sharebite.com/support
- group: company
  title: ''
  type: Blog
  url: https://sharebite.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://sharebite.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.sharebite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sharebite.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sharebite.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://sharebite.com/cookie-policy
- group: company
  title: ''
  type: Press
  url: https://sharebite.com/press
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sharebite.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sharebite-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sharebite-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sharebite-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sharebite.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sharebite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.sharebite.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sharebite_stock/
coverage:
  checked: '2026-08-05'
  detail: Sharebite markets enterprise API integration (its Envoy partner listing syncs office attendance data into meal programs) but publishes no developer surface at all — /developers, /docs, /api and /integrations all 404, none of the 441 URLs in its sitemap is a developer page, api./docs./developers.sharebite.com do not resolve, and the only stated route to an integration is the contact-sales form at /get-started.
  evidence:
  - status: 404
    url: https://sharebite.com/developers
  - status: 404
    url: https://sharebite.com/api
  - status: 200
    url: https://sharebite.com/sitemap.xml
  - status: 200
    url: https://sharebite.com/get-started
  - status: 403
    url: https://app.sharebite.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: 'Sharebite, Inc. is a New York City-based corporate meal benefits platform, founded in 2016 by Dilip Rao and Mohsin Memon, that lets employers fund and administer employee food programs across office, hybrid, and fully remote workforces in the United States, Canada, and the United Kingdom. Its products are Sharebite Passport (a programmatic virtual meal card usable anywhere Visa or Mastercard is accepted, with per-employee budgets and geographic and time-of-day ordering rules), Sharebite Stations (curated group ordering for office teams), Corporate Catering, and Engage. Every meal ordered on the platform triggers a donated meal through Feeding America and City Harvest partnerships — more than 15 million meals to date. Sharebite publishes a SafeBase/Drata trust center naming SOC 2, PCI DSS, GDPR and CCPA posture, a public status page, and an llms.txt, but it operates no public developer portal: the enterprise integration surface it markets (including a partner integration with
  Envoy that syncs office attendance data) is reachable only through its contact-sales flow.'
image: https://cdn.prod.website-files.com/679129c320865ab5a29b412c/68d703a414c41ace6156ac22_sharebite-homepage-og.png
layout: provider
modified: '2026-08-05'
name: Sharebite
nav: Providers
network: true
overview: 'Sharebite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Employee Benefits, Corporate Meal Benefits, and Human Resources.


  Sharebite''s developer surface includes support, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 111
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 25.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Sharebite Domain Security
  slug: sharebite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sharebite Vulnerability Disclosure
  slug: sharebite-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Sharebite Trust Center
  slug: sharebite-trust-center
  summary_line: SOC 2, PCI DSS, GDPR, CCPA
slug: sharebite
tags:
- Company
- Food
- Employee Benefits
- Corporate Meal Benefits
- Human Resources
- Workplace
- Food Delivery
- Catering
- Prepaid Cards
- FoodTech
- SaaS
website: https://sharebite.com/
---
