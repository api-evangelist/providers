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
  href: https://raw.githubusercontent.com/api-evangelist/arocell2a9d/refs/heads/main/llms/arocell2a9d-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arocell2a9d-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arocell2a9d/refs/heads/main/well-known/arocell2a9d-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arocell2a9d-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arocell2a9d/refs/heads/main/hosts/arocell2a9d-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arocell2a9d-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arocell2a9d/refs/heads/main/vendors/arocell2a9d-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arocell2a9d-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arocellus.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arocellus.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://arocellus.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arocell2a9d/refs/heads/main/security/arocell2a9d-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arocell2a9d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arocellus.com
coverage:
  checked: 2026-09-26
  detail: GraphQL endpoint exists but schema is generic Shopify and not owned by Arocell.
  evidence:
  - status: 200
    url: https://arocellus.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Arocell2a9d, operating under the brand AROCELLUS, is a Korean‑origin beauty and lifestyle e‑commerce company offering premium skincare, cosmetics, jewelry and fashion items. The Shopify‑powered site showcases a range of products such as serums, cleansers, masks, and accessories, emphasizing advanced bio‑formulations and natural ingredients. It provides free shipping in the U.S. over $75 and maintains policies for refunds, privacy, and terms of service.
layout: provider
modified: '2026-09-26'
name: Arocell2a9d
nav: Providers
network: true
overview: Arocell2a9d is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, E-Commerce, Skincare, and Lifestyle.
random_paper: 8
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
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
  provenance:
    mcp: unknown
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
  name: Arocell2A9D Domain Security
  slug: arocell2a9d-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arocell2a9d
tags:
- Company
- Beauty
- E-Commerce
- Skincare
- Lifestyle
website: https://arocellus.com
---
