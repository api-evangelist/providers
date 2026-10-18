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
  href: https://raw.githubusercontent.com/api-evangelist/brooklyn-dumpling-shop/refs/heads/main/llms/brooklyn-dumpling-shop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brooklyn-dumpling-shop-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brooklyn-dumpling-shop/refs/heads/main/hosts/brooklyn-dumpling-shop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brooklyn-dumpling-shop-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brooklyn-dumpling-shop/refs/heads/main/vendors/brooklyn-dumpling-shop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brooklyn-dumpling-shop-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brooklyn-dumpling-shop/refs/heads/main/security/brooklyn-dumpling-shop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brooklyn-dumpling-shop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brooklyndumplingshop.com
coverage:
  checked: '2026-10-06'
  detail: The Brooklyn Dumpling Shop website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.brooklyndumplingshop.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Brooklyn Dumpling Shop is a modern Asian‑inspired fast‑casual restaurant brand that serves dumplings, bowls, and other Asian‑fusion dishes across the United States and Canada. Founded in 2021 in New York City, it has grown to multiple locations, retail partners, sports venues, and entertainment sites. The company offers online ordering, catering, a loyalty program, and franchise opportunities, aiming to make bite‑size foods a staple for a broad audience.
layout: provider
modified: '2026-10-06'
name: Brooklyn Dumpling Shop
nav: Providers
network: true
overview: Brooklyn Dumpling Shop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Fast Casual, Asian Fusion, and Dumplings.
random_paper: 10
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brooklyn Dumpling Shop Domain Security
  slug: brooklyn-dumpling-shop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brooklyn-dumpling-shop
tags:
- Company
- Restaurant
- Fast Casual
- Asian Fusion
- Dumplings
website: https://www.brooklyndumplingshop.com
---
