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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/barclays-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cards.barclaycardus.com/
- group: company
  title: ''
  type: About
  url: https://cards.barclaycardus.com/banking/about-us/
- group: company
  title: ''
  type: Blog
  url: https://cards.barclaycardus.com/banking/about-us/news-and-views/
- group: operate
  title: ''
  type: Support
  url: https://cards.barclaycardus.com/banking/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cards.barclaycardus.com/banking/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cards.barclaycardus.com/banking/terms-of-use/
- group: auth
  title: ''
  type: SecurityCenter
  url: https://www.barclaycardus.com/servicing/security-center
- group: other
  title: ''
  type: ParentCompany
  url: https://www.barclays.com/
created: '2026-07-23'
description: Barclays US is the United States consumer banking arm of Barclays PLC, operated through Barclays Bank Delaware, a Delaware state-chartered bank headquartered in Wilmington. Doing business as Barclays US (barclaysus.com redirects to cards.barclaycardus.com), it is one of the largest co-branded credit card issuers in the country, running highly customized card programs for major travel, airline, retail, and affinity partners (JetBlue, American Airlines, Wyndham, AARP, Gap, and others), alongside small-business cards, installment loans, point-of-sale financing, and a direct-to-consumer online savings and CD franchise. Unlike Barclays UK — which operates a mandated PSD2 Open Banking API Exchange at developer.barclays.com — the US consumer entity publishes no first-party public developer portal or downloadable API specification. US open finance is voluntary and fragmented, so consumer- permissioned account and card data from Barclays US is reached in practice through third-party
  data aggregators rather than a documented first-party API. No FDX-conformant data-access endpoint or formally stated CFPB Section 1033 posture is published on the US site as of this profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Barclays US
nav: Providers
network: true
overview: 'Barclays US is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Credit Cards, and Consumer Banking.


  Barclays US''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 46
score:
  band: minimal
  composite: 11.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/barclays-us/refs/heads/main/screenshots/barclays-us-2026-07-25T202401.png
security:
- kind: domain-security
  name: Barclays Us Domain Security
  slug: barclays-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barclays-us
tags:
- Financial Services
- Banking
- United States
- Credit Cards
- Consumer Banking
- Co-Brand Cards
- Open Finance
- Data Aggregation
website: https://cards.barclaycardus.com/
---
