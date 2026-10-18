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
  href: https://raw.githubusercontent.com/api-evangelist/ceribell/refs/heads/main/hosts/ceribell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceribell-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceribell/refs/heads/main/vendors/ceribell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceribell-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceribell/refs/heads/main/security/ceribell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceribell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/ceribell_stock/
coverage:
  checked: '2026-10-08'
  detail: The Ceribell website returns HTML that loads JavaScript to render content, preventing machine‑readable discovery of API specifications.
  evidence:
  - status: 200
    url: https://ceribell.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Ceribell is a medical technology company that develops and provides rapid, point‑of‑care EEG (electroencephalogram) monitoring solutions. Their platform enables clinicians to quickly assess brain activity in emergency and critical care settings, facilitating faster diagnosis and treatment decisions. Ceribell’s products are designed for use in hospitals, ambulances, and other acute care environments, offering cloud‑based analytics and real‑time alerts to support patient care.
layout: provider
modified: '2026-10-07'
name: Ceribell
nav: Providers
network: true
overview: Ceribell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MedicalTechnology, EEG, PointOfCare, and Health Tech.
random_paper: 20
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 4
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
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
  name: Ceribell Domain Security
  slug: ceribell-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ceribell
tags:
- Company
- MedicalTechnology
- EEG
- PointOfCare
- Health Tech
website: https://forgeglobal.com/ceribell_stock/
---
