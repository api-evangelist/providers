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
- description: API documentation not publicly machine-readable
  name: Cerecin API
  slug: cerecin-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cerecin/refs/heads/main/hosts/cerecin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cerecin-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cerecin/refs/heads/main/security/cerecin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerecin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cerecin.com
- group: docs
  title: ''
  type: Documentation
  url: https://cerecin.com/science
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cerecin.com/privacy-policy
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.cerecin.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cerecin is a neuroscience-focused healthcare company headquartered in Broomfield, Colorado, with additional offices in Singapore and Australia. It leverages the physiological ketone system to develop metabolic therapies for brain disorders, including rare pediatric epilepsy and Alzheimer’s disease. The firm has a diversified pipeline of products, strategic partnerships, and a scientific advisory board, aiming to address unmet medical needs in neurology through innovative drug delivery and formulation technologies.
layout: provider
modified: '2026-10-07'
name: Cerecin
nav: Providers
network: true
overview: 'Cerecin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Neuroscience, Healthcare, Metabolism, and Neurology.


  Cerecin''s developer surface includes documentation and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cerecin Domain Security
  slug: cerecin-domain-security
  summary_line: no transport/DNS hardening detected
slug: cerecin
tags:
- Company
- Neuroscience
- Healthcare
- Metabolism
- Neurology
website: https://cerecin.com
---
