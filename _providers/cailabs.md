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
  href: https://raw.githubusercontent.com/api-evangelist/cailabs/refs/heads/main/hosts/cailabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cailabs-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cailabs.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cailabs.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.cailabs.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cailabs/refs/heads/main/security/cailabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cailabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cailabs.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cailabs.com
  - status: 403
    url: https://equityzen.com/company/cailabs
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Cailabs designs and manufactures advanced optical ground systems for laser communications, providing line‑of‑sight optical terminals, optical ground stations, and related technologies for aerospace and defense applications. Their portfolio includes laser welding, additive manufacturing, and directed‑energy solutions, serving both government and commercial customers worldwide.
image: https://www.cailabs.com/logo.pngs/heads/main/apis.yml
layout: provider
modified: '2026-10-06'
name: Cailabs
nav: Providers
network: true
overview: 'Cailabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Defense, Optical Communications, and Laser Technology.


  Cailabs'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
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
  name: Cailabs Domain Security
  slug: cailabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cailabs
tags:
- Company
- Aerospace
- Defense
- Optical Communications
- Laser Technology
website: https://www.cailabs.com
---
