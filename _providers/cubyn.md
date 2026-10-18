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
api_count: 1
apis:
- description: Cubyn provides logistics services but ceased operations in 2024; no public developer portal or API documentation is available.
  name: Cubyn API
  slug: cubyn-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cubyn/refs/heads/main/plans/cubyn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cubyn-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cubyn/refs/heads/main/hosts/cubyn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cubyn-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cubyn/refs/heads/main/vendors/cubyn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cubyn-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cubyn/refs/heads/main/packages/cubyn-packages.yml
  title: ''
  type: SDKs
  url: packages/cubyn-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cubyn/refs/heads/main/packages/cubyn-packages.yml
  title: ''
  type: Packages
  url: packages/cubyn-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cubyn.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cubyn.com/startup-program/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.cubyn.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cubyn
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cubyn/refs/heads/main/security/cubyn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubyn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cubyn.com
coverage:
  checked: '2026-10-12'
  detail: Cubyn ceased operations in 2024 and provides no developer portal or API documentation.
  evidence:
  - status: 200
    url: https://www.cubyn.com
  reason: not-a-software-company
  state: none
created: '2026-10-11'
description: Cubyn is a Paris‑based logistics platform founded in 2014 that provides e‑commerce merchants with end‑to‑end fulfillment services, including parcel delivery, B2B shipments, freight, custom packaging, and reverse logistics. Their cloud‑based solution integrates with major marketplaces and shop platforms such as Shopify and Prestashop, offering real‑time inventory and order tracking. Cubyn ceased operations in 2024, but its former services aimed to give online retailers a high‑performance network for fast, cost‑effective deliveries worldwide.
image: http://images.ctfassets.net/h1tfe2ydso3g/7lPG0iJQA7qvTJ3DRX1pnt/e4c07ae1e57b3d5c1e1b58ac6591cd88/Name_Parcels_v3.png
layout: provider
modified: '2026-10-11'
name: Cubyn
nav: Providers
network: true
overview: 'Cubyn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Fulfillment, E-Commerce, and Paris.


  Cubyn''s developer surface includes pricing, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Cubyn Plans Pricing
  plan_count: 3
  slug: cubyn-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 5.3
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
  name: Cubyn Domain Security
  slug: cubyn-domain-security
  summary_line: TLSv1.3
slug: cubyn
tags:
- Logistics
- Fulfillment
- E-Commerce
- Paris
website: https://www.cubyn.com
---
