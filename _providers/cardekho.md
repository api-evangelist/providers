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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cardekho/refs/heads/main/llms/cardekho-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardekho-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cardekho/refs/heads/main/hosts/cardekho-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardekho-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cardekho/refs/heads/main/vendors/cardekho-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardekho-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardekho.com/info/terms_and_condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardekho.com/info/privacy_policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cardekho.com/news/general/mg-hector-blackstorm-and-snowstorm-are-back-reintroduced-at-rs-1999-lakh-36770.htm
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cardekho/refs/heads/main/security/cardekho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardekho-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardekho.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.cardekho.com/mcp
  - status: 403
    url: https://careers.cardekho.com/mcp
  - status: 403
    url: https://stimg.cardekho.com/mcp
  - status: 200
    url: https://www.cardekho.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cardekho is an Indian automotive technology platform offering comprehensive car buying, selling, and ownership services. It provides detailed car specifications, price comparisons, dealer listings, and tools for used‑car valuation, helping consumers make informed decisions across new and pre‑owned vehicle markets. The site also features extensive car reviews, EV information, and a dealer network across major Indian cities, enhancing the overall car ownership experience.
image: https://stimg.cardekho.com/pwa/img/Desktop-logo.svg
layout: provider
modified: '2026-10-07'
name: Cardekho
nav: Providers
network: true
overview: Cardekho is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Marketplace, India, and CarTech.
random_paper: 19
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardekho Domain Security
  slug: cardekho-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardekho
tags:
- Company
- Automotive
- Marketplace
- India
- CarTech
website: https://www.cardekho.com
---
