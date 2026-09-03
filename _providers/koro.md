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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.koro.com/
- group: company
  title: ''
  type: Website
  url: https://www.korodrogerie.de/
- group: operate
  title: ''
  type: Support
  url: https://help.koro.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KoRoHandelsGmbH
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.koro.com/bede/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.koro.com/bede/datenschutz
- group: start
  title: ''
  type: SignUp
  url: https://www.koro.com/account
- group: build
  title: ''
  type: Packages
  url: packages/koro-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/koro-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koro-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koro-domain-security.yml
created: '2026-07-17'
description: KoRo (KoRo Handels GmbH) is a Berlin-based direct-to-consumer food retailer that sells nuts, dried fruit, nut butters, snacks, protein products, baking ingredients and drugstore goods in bulk packaging at wholesale-style prices, shipping across Europe from country storefronts in Germany (korodrogerie.de), Austria, Switzerland, France, Italy and the Benelux/EU shop at koro.com. Founded in 2014 and backed by HV Capital and Partech, KoRo runs a headless commerce stack — a Shopware 6 backend fronted by a Nuxt storefront deployed on Vercel — and publishes its engineering work as open source through the KoRoHandelsGmbH GitHub organization, including a Nitro-based Shopware Store-API proxy and several Shopware 6 build-tooling packages on npm under the @korodrogerie scope. KoRo publishes no public developer portal, no documented partner or commerce API, and no API specifications; its Store-API surface is internal and gated behind per-sales-channel access keys.
image: https://www.koro.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: KoRo
nav: Providers
network: true
overview: 'KoRo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Food and Beverage, and Retail.


  KoRo''s developer surface includes support, signup flow, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koro/refs/heads/main/screenshots/koro-2026-07-25T224226.png
security:
- kind: domain-security
  name: Koro Domain Security
  slug: koro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: koro
tags:
- Company
- Consumer
- E-Commerce
- Food and Beverage
- Retail
- Direct to Consumer
- Germany
- Shopware
- Open-Source
website: https://www.koro.com/
---
