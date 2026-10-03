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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/animab/refs/heads/main/hosts/animab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animab-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/animab/refs/heads/main/vendors/animab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animab-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://animab.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/animab/refs/heads/main/security/animab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animab.com
- group: docs
  title: ''
  type: Documentation
  url: https://animab.com/technology
- group: other
  title: ''
  type: Image
  url: https://animab.com/favicon.ico
created: '2026-09-24'
description: Animab is a biotechnology company that develops oral antibody technologies to improve gut health in livestock, particularly piglets during the post‑weaning stage. By mimicking secretory IgA, its products aim to reduce infections, lower antimicrobial use, and enhance animal performance, supporting sustainable agriculture and better feed conversion.
layout: provider
modified: '2026-09-24'
name: Animab
nav: Providers
network: true
overview: 'Animab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Animal Health, Livestock, Oral Antibodies, and Gut Health.


  Animab''s developer surface includes documentation and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Animab Domain Security
  slug: animab-domain-security
  summary_line: TLSv1.3 · HSTS
slug: animab
tags:
- Biotechnology
- Animal Health
- Livestock
- Oral Antibodies
- Gut Health
website: https://animab.com
---
