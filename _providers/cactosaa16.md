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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cactosaa16/refs/heads/main/plans/cactosaa16-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cactosaa16-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cactosaa16/refs/heads/main/hosts/cactosaa16-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cactosaa16-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cactosaa16/refs/heads/main/vendors/cactosaa16-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cactosaa16-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://cactos.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cactos.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://cactos.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://cactos.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cactosaa16/refs/heads/main/security/cactosaa16-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cactosaa16-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cactos.com
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.cactos.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Cactosaa16, operating as Cactos, is a Finnish startup delivering smart battery energy storage systems for commercial and grid‑scale applications. Their platform optimises energy use, shifts consumption to low‑price periods, and enables participation in electricity markets, helping customers reduce costs and increase resilience.
image: https://cdn.prod.website-files.com/674b02957275f722dd749506/690ca1723bdb3af3178d1b1a_product-og.jpg
layout: provider
modified: '2026-10-06'
name: Cactosaa16
nav: Providers
network: true
overview: 'Cactosaa16 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Storage, Finland, Startups, and Battery.


  Cactosaa16''s developer surface includes support, pricing, and 7 more developer resources.'
plans:
- name: Cactosaa16 Plans Pricing
  plan_count: 1
  slug: cactosaa16-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cactosaa16 Domain Security
  slug: cactosaa16-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cactosaa16
tags:
- Energy
- Storage
- Finland
- Startups
- Battery
- Company
website: https://cactos.com
---
