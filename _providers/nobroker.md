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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nobroker-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/nobroker-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nobroker-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.nobroker.in
- group: company
  title: ''
  type: Blog
  url: https://www.nobroker.in/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.nobroker.in/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nobroker.in/nb/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nobroker.in/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nobroker.in/privacy
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/nobroker-stock
coverage:
  checked: '2026-08-04'
  detail: NoBroker ships only end-user web and mobile products — there is no developer portal, api./developer./docs.nobroker.in do not resolve at all, and the application endpoints the site itself calls under /api/v1 through /api/v5 are explicitly Disallow-ed in robots.txt; every /.well-known/* path on www.nobroker.in answers 200 with the Angular app shell rather than a document.
  evidence:
  - status: 0
    url: https://developer.nobroker.in/
  - status: 404
    url: https://www.nobroker.in/openapi.json
  - status: 200
    url: https://www.nobroker.in/robots.txt
  - status: 200
    url: https://www.nobroker.in/.well-known/agent-card.json
  - status: 404
    url: https://www.nobrokerhood.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: 'NoBroker Technologies Solutions Pvt Ltd is an Indian proptech company, founded in 2013 and headquartered in Bengaluru, that operates a brokerage-free real estate marketplace connecting property owners directly with tenants and buyers across Indian metros. Beyond listings for flats, houses, villas, plots, PGs and commercial space, NoBroker sells adjacent home services — rental and lease agreement drafting, legal assistance, packers and movers, painting and cleaning, home loans and rent payments — and operates NoBrokerHood, a gated-community and housing-society management / ERP product covering visitor management, billing, accounting and complaints. NoBroker became India''s first proptech unicorn in 2021. The company ships software only as an end-user web and mobile product: as of this profile it publishes no public developer program, no API reference and no machine-readable specification, and its application endpoints under /api/v1..v5 are explicitly disallowed in robots.txt.'
image: https://assets.nobroker.in/static/img/logo.png
layout: provider
modified: '2026-08-04'
name: NoBroker
nav: Providers
network: true
overview: 'NoBroker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, PropTech, Property Rental, and Marketplace.


  NoBroker''s developer surface includes engineering blog, support, pricing, and 7 more developer resources.'
random_paper: 75
score:
  band: emerging
  composite: 14.5
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Nobroker Domain Security
  slug: nobroker-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nobroker
tags:
- Company
- Real Estate
- PropTech
- Property Rental
- Marketplace
- Home Services
- Society Management
- India
website: https://www.nobroker.in
---
