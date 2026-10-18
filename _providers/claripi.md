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
  href: https://raw.githubusercontent.com/api-evangelist/claripi/refs/heads/main/hosts/claripi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claripi-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claripi.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/claripi/refs/heads/main/security/claripi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claripi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claripi.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://claripi.com
  - status: 403
    url: https://equityzen.com/company/claripi
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Claripi provides innovative solutions for medical imaging through AI-powered image processing, data analytics, and software tools. Founded in 2015, the company offers products such as Clari CT.AI, Clari Pulmo, and Clari SIGMAM, helping clinicians improve diagnosis, reduce radiation dose, and streamline workflows across radiology, pulmonology, and musculoskeletal imaging.
image: https://claripi.com/wp-content/uploads/2020/12/fdacleared.png
layout: provider
modified: '2026-10-08'
name: Claripi
nav: Providers
network: true
overview: Claripi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Imaging, Artificial Intelligence, Healthcare, and Software.
random_paper: 14
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claripi Domain Security
  slug: claripi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: claripi
tags:
- Company
- Medical Imaging
- Artificial Intelligence
- Healthcare
- Software
website: https://claripi.com
---
