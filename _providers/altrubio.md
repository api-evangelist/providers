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
  href: https://raw.githubusercontent.com/api-evangelist/altrubio/refs/heads/main/hosts/altrubio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altrubio-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altrubio.com/altrubio/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.altrubio.com/altrubio/en/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altrubio/refs/heads/main/security/altrubio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altrubio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.altrubio.com/altrubio/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.altrubio.com/altrubio/en/science
- group: operate
  title: ''
  type: Support
  url: https://www.altrubio.com/altrubio/en/contact
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.altrubio.com/altrubio/en
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: AltruBio is a biotechnology company focused on developing first‑in‑class immunomodulators targeting immune system diseases. Their platform aims to create safer, more durable biologic treatments to improve patients’ lives, with a pipeline spanning preclinical to phase III clinical trials across multiple indications.
layout: provider
modified: '2026-09-24'
name: AltruBio
nav: Providers
network: true
overview: 'AltruBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Immunology, Therapeutics, and Clinical Trials.


  AltruBio''s developer surface includes documentation, support, and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 1.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altrubio Domain Security
  slug: altrubio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: altrubio
tags:
- Company
- Biotechnology
- Immunology
- Therapeutics
- Clinical Trials
website: https://www.altrubio.com/altrubio/en
---
