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
- description: Brunt provides a storefront API via Shopify, but no provider-owned OpenAPI or GraphQL schema was found.
  name: Brunt API
  slug: brunt-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brunt/refs/heads/main/llms/brunt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brunt-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brunt/refs/heads/main/well-known/brunt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brunt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brunt/refs/heads/main/hosts/brunt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brunt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brunt/refs/heads/main/vendors/brunt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brunt-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.bruntworkwear.com/en-US
- group: docs
  title: ''
  type: Documentation
  url: https://help.bruntworkwear.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brunt/refs/heads/main/security/brunt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brunt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bruntworkwear.com/
created: '2026-10-06'
description: Brunt is a workwear and apparel company that designs, manufactures, and sells high‑quality boots, clothing, and accessories for professionals in demanding environments. Based in the United States, Brunt focuses on durability, safety, and comfort, offering a range of products from waterproof boots to insulated work pants. The brand emphasizes American‑made craftsmanship and a strong commitment to customer service and product innovation.
image: http://bruntworkwear.com/cdn/shop/files/BRUNT_Workwear_b7787f40-df8d-4fe2-9ad1-338b0b5282b0.jpg?v=1781637311
layout: provider
modified: '2026-10-06'
name: Brunt
nav: Providers
network: true
overview: 'Brunt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Workwear, Apparel, Manufacturing, Safety, and USA.


  Brunt''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 5
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
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Brunt Domain Security
  slug: brunt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brunt
tags:
- Workwear
- Apparel
- Manufacturing
- Safety
- USA
website: https://bruntworkwear.com/
---
