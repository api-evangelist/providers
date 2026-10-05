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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bosie/refs/heads/main/llms/bosie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bosie-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bosie/refs/heads/main/well-known/bosie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bosie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bosie/refs/heads/main/hosts/bosie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bosie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bosie/refs/heads/main/vendors/bosie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bosie-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bosie.co/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bosie.co/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bosie.co/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bosie/refs/heads/main/security/bosie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bosie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bosie.co
coverage:
  checked: '2026-10-02'
  detail: Bosie is an e‑commerce knitwear retailer using Shopify, and no Bosie‑owned API contracts were found.
  evidence:
  - status: 200
    url: https://bosie.co
  reason: not-a-software-company
  state: none
created: '2026-10-02'
description: Bosie Knitwear is a Scottish apparel brand offering handcrafted wool garments, including sweaters, cardigans, and accessories. The company operates an e‑commerce site at bosie.co, shipping internationally and showcasing collections such as Shetland, Chunky Fishermen, and Cashmere. It emphasizes heritage, quality materials, and sustainable production.
layout: provider
modified: '2026-10-02'
name: Bosie
nav: Providers
network: true
overview: Bosie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Knitwear, Apparel, E-Commerce, and Scotland.
random_paper: 2
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bosie Domain Security
  slug: bosie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bosie
tags:
- Company
- Knitwear
- Apparel
- E-Commerce
- Scotland
website: https://bosie.co
---
