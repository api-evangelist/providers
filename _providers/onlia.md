---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onlia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.onlia.ca/
- group: company
  title: ''
  type: About
  url: https://www.onlia.ca/about
- group: company
  title: ''
  type: Blog
  url: https://www.onlia.ca/magazine/blogs
- group: company
  title: ''
  type: BlogRSS
  url: https://www.onlia.ca/magazine/blogs?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.onlia.ca/support
- group: other
  title: ''
  type: Claims
  url: https://www.onlia.ca/claims
- group: start
  title: ''
  type: Portal
  url: https://app.onlia.ca/
- group: company
  title: ''
  type: Partners
  url: https://www.onlia.ca/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onlia.ca/about/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onlia.ca/about/conditions-of-use
- group: auth
  title: ''
  type: Disclosure
  url: https://www.onlia.ca/broker-disclosure
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.onlia.ca/faqs
- group: other
  title: ''
  type: Accessibility
  url: https://www.onlia.ca/about/accessibility
- group: commercial
  title: ''
  type: PaymentAgreement
  url: https://www.onlia.ca/payment-agreement
- group: other
  title: ''
  type: FraudReporting
  url: https://www.onlia.ca/help/report-fraud
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/onlia-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onlia-llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: 'Onlia is a Canadian digital insurance brokerage, operating as the registered business name of Onlia Agency Inc. and backed by Southampton Financial Inc. (the Southampton group of companies). It sells personal lines direct to consumers online and by phone — auto (car, motorcycle, ATV, snowmobile, trailer, motorhome), property (home, condo, tenant, landlord, second home, mobile home) and lifestyle lines (boat, pet, life, travel, seasonal) — plus group and bundle programs. Onlia does not underwrite; it places business with a panel of Canadian carriers disclosed publicly on its broker-disclosure page, including Aviva, Gore Mutual, Economical/Definity, Pembridge, Pafco, Echelon, Wawanesa, Unica, Forward, Premier, Facility Association (Intact) and APOLLO. Its home market is Canada, concentrated in Ontario, where market conduct sits with FSRA while OSFI supervises the federally-regulated carriers behind the policies. API posture, recorded honestly: Onlia publishes NO public developer
  portal and NO self-serve API. developer., developers., docs. and api. under onlia.ca do not resolve, and /developers, /api, /developer and /integrations on the marketing site all return 404. The only quote/bind/issue/FNOL surface is app.onlia.ca, a consumer-facing Angular single-page app running on a white-labelled Ignite Insurance policy administration platform whose backend is private to the app. The one "partner" page is a B2B marketing page inviting affinity discount partnerships by email, with no technical onboarding. No ACORD, AL3, ACORD XML or NGDS reference appears anywhere on the public site. The app''s own bundle shows the private backend runs on MuleSoft Anypoint CloudHub ESB services (auto and home policy, authentication, documents, VIN/MVR, claims) plus an Ignite Insurance authentication service — real REST plumbing behind the SPA, but undocumented, uncredentialed and not offered to third parties, so no API entry is claimed here.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Onlia
nav: Providers
network: true
overview: 'Onlia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Insurtech, and Broker.


  Onlia''s developer surface includes engineering blog, support, developer portal, and 16 more developer resources.'
random_paper: 39
score:
  band: emerging
  composite: 15.2
  delta: -1.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Onlia Domain Security
  slug: onlia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onlia
tags:
- Insurance
- Canada
- Property and Casualty
- Insurtech
- Broker
- Personal Lines
- Auto Insurance
- Home Insurance
- Direct to Consumer
- Ontario
website: https://www.onlia.ca/
---
