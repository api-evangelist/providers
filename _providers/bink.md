---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: GraphQL API for Bink consumer brand.
  name: Bink GraphQL API
  slug: bink-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bink/refs/heads/main/llms/bink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bink-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bink/refs/heads/main/well-known/bink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bink-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bink/refs/heads/main/hosts/bink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bink-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bink/refs/heads/main/vendors/bink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bink-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://binkmade.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://binkmade.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://binkmade.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bink/refs/heads/main/security/bink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://binkmade.com
- group: docs
  title: ''
  type: Documentation
  url: https://binkmade.com/pages/about-bink
created: '2026-09-28'
description: Bink is a consumer brand focused on high‑quality, reusable glass water bottles and related accessories. Founded in 2021, the company emphasizes sustainable design, wellness, and functional aesthetics, offering a range of products such as stainless‑steel bottles, glass bottles, and custom drinkware for everyday use.
image: http://binkmade.com/cdn/shop/files/bink-water-bottle_18_b62efef8-7bc3-467a-bf53-cc886803debd.jpg?v=1774478359
layout: provider
modified: '2026-09-28'
name: Bink
nav: Providers
network: true
overview: 'Bink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Goods, Sustainable, Water Bottles, and E-Commerce.


  Bink''s developer surface includes documentation and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bink Domain Security
  slug: bink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bink
tags:
- Company
- Consumer Goods
- Sustainable
- Water Bottles
- E-Commerce
website: https://binkmade.com
---
