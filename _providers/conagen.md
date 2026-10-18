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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conagen/refs/heads/main/hosts/conagen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conagen-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conagen.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conagen.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://conagen.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conagen/refs/heads/main/security/conagen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conagen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conagen.com
coverage:
  checked: '2026-10-10'
  detail: Conagen provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://conagen.com
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Conagen, Inc. is a synthetic biology and biomanufacturing company that engineers microbes to produce natural products with precision. They develop strain and organism platforms, scale microbial fermentation, and create ingredients for food, flavors, cosmetics, nutraceuticals, and pharmaceuticals. Their mission is to advance sustainable manufacturing of high‑value chemicals using engineered biology.
image: https://conagen.com/wp-content/themes/jld/images/fb.png
layout: provider
modified: '2026-10-10'
name: Conagen
nav: Providers
network: true
overview: Conagen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Synthetic Biology, Biomanufacturing, Biotechnology, Engineering, and Food Ingredients.
random_paper: 5
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 6
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Conagen Domain Security
  slug: conagen-domain-security
  summary_line: TLSv1.3
slug: conagen
tags:
- Synthetic Biology
- Biomanufacturing
- Biotechnology
- Engineering
- Food Ingredients
website: https://conagen.com
---
