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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Connected Cannabis storefronts (Shopify Storefront API)
  name: Connected Cannabis API
  slug: connected-cannabis-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connected-cannabis/refs/heads/main/llms/connected-cannabis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connected-cannabis-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connected-cannabis/refs/heads/main/well-known/connected-cannabis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connected-cannabis-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connected-cannabis/refs/heads/main/hosts/connected-cannabis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connected-cannabis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connected-cannabis/refs/heads/main/vendors/connected-cannabis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connected-cannabis-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connectedcannabisco.com/pages/tos-privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://connectedcannabisco.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connected-cannabis/refs/heads/main/security/connected-cannabis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connected-cannabis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connectedcannabisco.com/
created: '2026-10-10'
description: Connected Cannabis is a retail cannabis brand operating storefronts in Sacramento, Stockton, and San Francisco. The company offers a curated selection of flower, vapes, pre-rolls, extracts, edibles, and merchandise through its online ordering platform. It emphasizes quality, sustainability, and community engagement, providing customers with detailed strain information and a loyalty program. Connected Cannabis aims to enhance the cannabis shopping experience with convenient pickup options and a modern e‑commerce site.
image: http://connectedcannabisco.com/cdn/shop/files/Connected-Script-Outlined-800x400-0744d81.png?v=1691604778
layout: provider
modified: '2026-10-10'
name: Connected Cannabis
nav: Providers
network: true
overview: Connected Cannabis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cannabis, Retail, E-Commerce, California, and Dispensary.
random_paper: 19
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Connected Cannabis Domain Security
  slug: connected-cannabis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connected-cannabis
tags:
- Cannabis
- Retail
- E-Commerce
- California
- Dispensary
website: https://connectedcannabisco.com/
---
