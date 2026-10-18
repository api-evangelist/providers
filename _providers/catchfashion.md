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
- description: Theme service for Career page API
  name: Theme Service API
  slug: theme-service-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/catchfashion/refs/heads/main/conformance/catchfashion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/catchfashion-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catchfashion/refs/heads/main/llms/catchfashion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catchfashion-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catchfashion/refs/heads/main/well-known/catchfashion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catchfashion-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catchfashion/refs/heads/main/hosts/catchfashion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchfashion-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catchfashion/refs/heads/main/vendors/catchfashion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catchfashion-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catchfashion.nl/pages/privacybeleid
- group: company
  title: ''
  type: Newsroom
  url: https://catchfashion.nl/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catchfashion/refs/heads/main/security/catchfashion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchfashion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchfashion.nl
created: '2026-10-07'
description: Catchfashion is an online fashion retailer based in the Netherlands, offering women’s clothing from brands such as VERO MODA, VILA, Object, Pieces, and Noisy May. The store provides a wide range of sizes and includes a Curve line for plus-size fashion, serving customers with a curated selection of apparel and accessories.
image: http://catchfashion.nl/cdn/shop/files/CATCH_LOGO_S_1.svg?v=1769690932
layout: provider
modified: '2026-10-07'
name: Catchfashion
nav: Providers
network: true
overview: Catchfashion is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Retail, E-Commerce, and Netherlands.
random_paper: 5
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catchfashion Domain Security
  slug: catchfashion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catchfashion
tags:
- Company
- Fashion
- Retail
- E-Commerce
- Netherlands
website: https://catchfashion.nl
---
