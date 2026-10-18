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
- description: Clinova provides a digital platform for dietitians to manage clients, appointments, payments and records.
  name: Clinova
  slug: clinova
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinova/refs/heads/main/hosts/clinova-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clinova-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinova/refs/heads/main/vendors/clinova-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clinova-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clinova/refs/heads/main/security/clinova-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clinova-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-10-09'
  detail: The website provides no OpenAPI, GraphQL, or other machine‑readable contract; only HTML pages describing features.
  evidence:
  - status: 200
    url: https://clinova.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Clinova is a healthcare technology company focused on delivering innovative digital solutions for clinical data management and patient engagement. The firm provides a platform that integrates electronic health records, telemedicine services, and analytics tools to improve care coordination and outcomes. Founded to address gaps in interoperability, Clinova aims to streamline workflows for providers and empower patients with secure access to their health information.
layout: provider
modified: '2026-10-08'
name: Clinova
nav: Providers
network: true
overview: Clinova is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Technology, Digital Health, ClinicalData, and Patient Engagement.
random_paper: 0
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: derived
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
  name: Clinova Domain Security
  slug: clinova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clinova
tags:
- Healthcare
- Technology
- Digital Health
- ClinicalData
- Patient Engagement
website: https://www.nasdaqprivatemarket.com/
---
