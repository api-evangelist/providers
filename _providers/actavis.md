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
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/actavis/refs/heads/main/security/actavis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actavis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actavis.co.id/
coverage:
  checked: '2026-09-13'
  detail: Actavis was absorbed into Teva in August 2016; www.actavis.com now resolves to Teva's 192.115.248.118, which refuses TCP 443 outright (ECONNREFUSED) and never answers HTTP, and actavis.bg redirects to teva.bg — the only reachable Actavis-branded host left is PT Actavis Indonesia's marketing site, which 404s every discovery path.
  evidence:
  - status: 0
    url: https://www.actavis.com/
  - status: 404
    url: https://www.actavis.co.id/.well-known/api-catalog
  - status: 200
    url: https://actavis.bg/
  - status: 404
    url: https://api.github.com/orgs/actavis
  reason: defunct
  state: none
created: '2026-09-13'
description: Actavis is a pharmaceutical manufacturer of generic, branded-generic and over-the-counter medicines that no longer exists as an independent company. Actavis plc renamed itself Allergan plc in June 2015, and on 2 August 2016 Teva Pharmaceutical Industries completed its acquisition of the Actavis Generics business for roughly $40.5 billion. What survives of the name is a product label and a handful of Teva regional affiliates such as PT Actavis Indonesia. The historic corporate domains (actavis.com, actavis.us, actavis.co.uk) are delegated to Teva nameservers and no longer answer HTTP at all, and actavis.bg redirects to teva.bg. Actavis published no developer program, no API, no SDKs and no machine-readable specification; in this industry "API" means Active Pharmaceutical Ingredient, not a software interface.
layout: provider
modified: '2026-09-13'
name: Actavis
nav: Providers
network: true
overview: Actavis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Generic Drugs, Healthcare, and Manufacturing.
random_paper: 21
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actavis Domain Security
  slug: actavis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: actavis
tags:
- Company
- Pharmaceuticals
- Generic Drugs
- Healthcare
- Manufacturing
- Acquired
website: https://www.actavis.co.id/
---
