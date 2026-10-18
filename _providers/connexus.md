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
  href: https://raw.githubusercontent.com/api-evangelist/connexus/refs/heads/main/hosts/connexus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connexus-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connexus/refs/heads/main/security/connexus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connexus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connexusinc.org/
coverage:
  checked: '2026-10-10'
  detail: Connexus website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://connexusinc.org/
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Connexus, Inc. is a non‑profit licensed supported living agency based in Tennessee. It provides community‑based and family‑based services for children and adults with physical, mental, and developmental disabilities, including residential care, personal assistance, supported employment, and vocational rehabilitation. The organization focuses on nurturing, teaching, and strengthening individuals and families with respect and professionalism, aiming to help them reach their full potential.
image: https://connexusinc.org/wp-content/uploads/2026/08/cropped-Connexus-Logo-e1787910180412-1-32x32.png
layout: provider
modified: '2026-10-10'
name: Connexus
nav: Providers
network: true
overview: Connexus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Non-Profit, Healthcare, Social Services, Community Support, and Tennessee.
random_paper: 3
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Connexus Domain Security
  slug: connexus-domain-security
  summary_line: TLSv1.2
slug: connexus
tags:
- Non-Profit
- Healthcare
- Social Services
- Community Support
- Tennessee
website: https://connexusinc.org/
---
