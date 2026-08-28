---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.bitstack-app.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bitstack-app.com/en/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/bitstack-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitstack-app.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitstack-app.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.bitstack-app.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.bitstack-app.com/en/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitstackapp
- group: auth
  title: ''
  type: Compliance
  url: https://www.bitstack-app.com/en/regulatory-documents-hub
- group: design
  title: ''
  type: Conformance
  url: conformance/bitstack-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitstack-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitstack-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Bitstack ships only a consumer iOS/Android Bitcoin savings app; api.bitstack-app.com resolves but answers a bare empty-bodied 404 on every path including its own root, and none of the 1,687 URLs in the published sitemap is a developer, docs, or API page.
  evidence:
  - status: 404
    url: https://api.bitstack-app.com/openapi.json
  - status: 404
    url: https://api.bitstack-app.com/
  - status: 404
    url: https://www.bitstack-app.com/.well-known/agent-card.json
  - status: 0
    url: https://docs.bitstack-app.com/
  - status: 200
    url: https://www.bitstack-app.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Bitstack is a French consumer Bitcoin savings application operated by Bitstack Digital Assets SAS (Meyreuil, France), which lets retail users accumulate Bitcoin through automatic round-ups on everyday card purchases, recurring dollar-cost-averaging buys (hourly to monthly), one-off card buys from EUR 1, peer-to-peer transfers by phone number or email, a cash account with free SEPA instant transfers, and a Bitstack payment card that pays Bitcoin cashback. The company reports more than 350,000 users and over EUR 350M invested through the app. It is licensed as a Crypto-Assets Service Provider with the French Autorite des Marches Financiers (AMF) under number A2025-003 for exchange, order execution, custody and transfer of crypto-assets, and is a licensed agent of the electronic money institution Xpollens with the ACPR under number 747088. Bitstack publishes a public fee schedule and a regulatory documents hub, but ships no public developer API, developer portal, or machine-readable
  API contract of any kind: the product is delivered exclusively through its iOS and Android applications.'
image: https://cdn.prod.website-files.com/63ea3e6d2856ff83c7d77160/6710f4f300ea8bdff9e78518_favicon_bitstack.png
layout: provider
modified: '2026-08-17'
name: Bitstack
nav: Providers
network: true
overview: 'Bitstack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Bitcoin, Cryptocurrency, and Fintech.


  Bitstack''s developer surface includes pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Bitstack Plans Pricing
  plan_count: 7
  slug: bitstack-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Bitstack Rate Limits
  slug: bitstack-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Bitstack Domain Security
  slug: bitstack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitstack
tags:
- Company
- Blockchain
- Bitcoin
- Cryptocurrency
- Fintech
- Savings
- Consumer Finance
- Payments
- Mobile Application
- France
- Europe
- Regulated
website: https://www.bitstack-app.com/
---
