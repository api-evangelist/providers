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
- description: Curevo provides a healthcare marketplace platform; API details are not publicly documented.
  name: Curevo API
  slug: curevo-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/curevo/refs/heads/main/plans/curevo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curevo-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curevo/refs/heads/main/hosts/curevo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curevo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curevo/refs/heads/main/vendors/curevo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curevo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curevo.in/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curevo.in/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://curevo.in/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://curevo.in/press
- group: company
  title: ''
  type: Blog
  url: https://curevo.in/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curevo/refs/heads/main/security/curevo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curevo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curevo.in
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing common spec URLs on curevo.in and api.curevo.in.
  evidence:
  - status: 404
    url: https://curevo.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curevo is a clinical‑stage biotechnology company that operates a global healthcare marketplace, connecting patients with verified medical centers, doctors, and wellness providers across more than 150 countries. The platform offers a range of treatments—from cardiology and oncology to regenerative therapies such as stem cell, hyperbaric oxygen, and blood ozonation—facilitating transparent pricing, tele‑assist AI support, and end‑to‑end medical travel coordination.
image: https://curevo.in/opengraph-image?be1d53ca97d5c87f
layout: provider
modified: '2026-10-12'
name: Curevo
nav: Providers
network: true
overview: 'Curevo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Marketplace, Biotechnology, Global, and Telehealth.


  Curevo''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Curevo Plans Pricing
  plan_count: 3
  slug: curevo-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curevo Domain Security
  slug: curevo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curevo
tags:
- Healthcare
- Marketplace
- Biotechnology
- Global
- Telehealth
website: https://curevo.in
---
