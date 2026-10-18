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
- description: GraphQL endpoint for Californianaturals providing product and order data.
  name: GraphQL API
  slug: graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/californianaturals/refs/heads/main/llms/californianaturals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/californianaturals-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/californianaturals/refs/heads/main/well-known/californianaturals-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/californianaturals-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/californianaturals/refs/heads/main/hosts/californianaturals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/californianaturals-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/californianaturals/refs/heads/main/vendors/californianaturals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/californianaturals-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thecalifornianaturals.com/pages/privacy-policy-terms-of-use
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/californianaturals/refs/heads/main/security/californianaturals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/californianaturals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thecalifornianaturals.com
created: '2026-10-06'
description: California Naturals (Californianaturals) is a women‑founded, California‑based personal care brand offering clean, naturally derived hair, body, and skincare products. Their lineup includes shampoos, conditioners, body washes, and bundles, all formulated without sulfates, parabens, silicones, and packaged in PCR‑plastic bottles. The company emphasizes eco‑conscious ingredients, cruelty‑free certification, and affordable pricing, shipping free on orders over $40.
image: https://thecalifornianaturals.com//thecalifornianaturals.com/cdn/shop/files/CaliforniaNaturals_Logo_FlowerMotif-01_6.png?v=1741048807&width=1200
layout: provider
modified: '2026-10-06'
name: Californianaturals
nav: Providers
network: true
overview: Californianaturals is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PersonalCare, CleanBeauty, WomenFounded, and California.
random_paper: 8
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 73.2
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
  name: Californianaturals Domain Security
  slug: californianaturals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: californianaturals
tags:
- Company
- PersonalCare
- CleanBeauty
- WomenFounded
- California
website: https://thecalifornianaturals.com
---
