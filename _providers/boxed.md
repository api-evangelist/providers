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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boxed/refs/heads/main/hosts/boxed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boxed-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boxed/refs/heads/main/vendors/boxed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boxed-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boxed/refs/heads/main/security/boxed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boxed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boxed.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.boxed.com/mcp
  - status: null
    url: https://forgeglobal.com/boxed_stock/
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Boxed is a private company that completed a SPAC merger in December 2021 and is listed on the NYSE under the ticker BOXD. It operates in the e‑commerce sector, offering a curated selection of groceries and household items delivered directly to consumers. The company focuses on providing a premium online shopping experience with a focus on quality and convenience.
layout: provider
modified: '2026-10-03'
name: Boxed
nav: Providers
network: true
overview: Boxed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Grocery, Delivery, and SPAC.
random_paper: 2
score:
  band: minimal
  composite: 3.0
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
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boxed Domain Security
  slug: boxed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boxed
tags:
- Company
- E-Commerce
- Grocery
- Delivery
- SPAC
- NYSE
website: https://www.boxed.com
---
