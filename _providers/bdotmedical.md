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
  href: https://raw.githubusercontent.com/api-evangelist/bdotmedical/refs/heads/main/hosts/bdotmedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bdotmedical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bdotmedical/refs/heads/main/vendors/bdotmedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bdotmedical-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bdotmedical/refs/heads/main/security/bdotmedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bdotmedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bdotmedical
coverage:
  checked: '2026-09-27'
  detail: The provider's website renders only via JavaScript and no machine‑readable API spec was found.
  evidence:
  - status: 200
    url: https://bdotmed.co.jp/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Bdotmedical is a healthcare technology company focused on providing advanced medical data analytics and telehealth integration solutions. It offers APIs that enable secure access to patient data, device telemetry, and analytics services for healthcare providers and developers. The platform aims to improve clinical decision-making and operational efficiency through interoperable, standards‑based interfaces.
layout: provider
modified: '2026-09-27'
name: Bdotmedical
nav: Providers
network: true
overview: Bdotmedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Data Analytics, Telehealth, and MedicalTech.
random_paper: 0
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bdotmedical Domain Security
  slug: bdotmedical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bdotmedical
tags:
- Healthcare
- Data Analytics
- Telehealth
- MedicalTech
website: https://equityzen.com/company/bdotmedical
---
