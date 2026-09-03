---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gojo--company-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/gojo--company-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gojo--company-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gojo.co/
- group: company
  title: ''
  type: About
  url: https://gojo.co/corporate-information
- group: company
  title: ''
  type: Blog
  url: https://gojo.co/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://gojo.co/feed
- group: operate
  title: ''
  type: PressReleases
  url: https://gojo.co/press-releases
- group: company
  title: ''
  type: News
  url: https://gojo.co/gojo-in-the-news
- group: other
  title: ''
  type: Reports
  url: https://gojo.co/reports
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gojo.co/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gojo.co/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://gojo.co/join-us
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@gojogroup
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/gojo--company-stock
coverage:
  checked: '2026-08-22'
  detail: Gojo & Company is a microfinance holding company whose only web property is a WordPress corporate site — its 50-page sitemap contains no developer, docs, or API page, api./docs./developer. subdomains of gojo.co do not resolve in DNS, and the cloud core-banking platform it does build is internal to its group companies rather than a published developer surface.
  evidence:
  - status: 200
    url: https://gojo.co/page-sitemap.xml
  - status: 404
    url: https://gojo.co/developers
  - status: 404
    url: https://gojo.co/openapi.json
  - status: 404
    url: https://gojo.co/.well-known/agent-card.json
  - status: 200
    url: https://www.pasio.io/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Gojo & Company, Inc. is a Tokyo-headquartered financial inclusion holding company founded on 4 July 2014 by Taejun Shin and Sanjay Gandhi, with the stated ambition of becoming a "private-sector World Bank". Gojo raises capital from mission-aligned investors and deploys it into microfinance institutions and inclusive financial service providers across South Asia, Southeast Asia, Central Asia, the Caucasus and Africa, supplying not only equity and debt but also management, governance, risk and technology support to its group companies. It runs a Financial Diaries research programme on low-income household cashflows, the Pasio digital financial inclusion initiative, and a non-profit arm, the Gojo Foundation. Gojo is a certified B Corporation and reports under J-GAAP. It is a private company; its equity trades on secondary marketplaces such as Hiive. Gojo publishes no public developer program, API documentation, or machine-readable API contract — its digital financial infrastructure
  and cloud core banking work is internal to the group and its partner institutions.
image: https://gojo.co/wp-content/uploads/2025/05/gojo_logo150304-01-scaled.png
layout: provider
modified: '2026-08-22'
name: Gojo & Company
nav: Providers
network: true
overview: 'Gojo & Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Financial Inclusion, Microfinance, and Impact Investing.


  Gojo & Company''s developer surface includes engineering blog, product news, YouTube channel, and 12 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gojo--company/refs/heads/main/screenshots/gojo--company-2026-09-02T145621.png
security:
- kind: domain-security
  name: Gojo  Company Domain Security
  slug: gojo--company-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gojo--company
tags:
- Company
- Financial-Services
- Financial Inclusion
- Microfinance
- Impact Investing
- Holding Company
- Emerging Markets
- Japan
website: https://gojo.co/
---
