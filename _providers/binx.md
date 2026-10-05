---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Binx Health platform providing access to STI testing services and integration points.
  name: Binx API
  slug: binx-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/binx/refs/heads/main/well-known/binx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/binx-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/binx/refs/heads/main/hosts/binx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/binx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/binx/refs/heads/main/vendors/binx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/binx-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.mybinxhealth.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mybinxhealth.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://mybinxhealth.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://mybinxhealth.com/team
- group: docs
  title: ''
  type: Documentation
  url: https://help.mybinxhealth.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/binx/refs/heads/main/security/binx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/binx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mybinxhealth.com
coverage:
  checked: '2026-09-28'
  detail: Help site renders via Salesforce with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://help.mybinxhealth.com/s/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Binx Health delivers point-of-care STI testing solutions that bring lab-quality diagnosis and treatment to a single visit. Their mission is to improve healthcare access through rapid, CLIA‑waived PCR testing for chlamydia and gonorrhea, enabling clinics, urgent care centers, and community health organizations to provide fast, accurate results on‑site. The platform integrates with EHR/LIS systems, supports antibiotic stewardship, and offers reimbursement assistance, aiming to reduce patient loss to follow‑up and enhance community health outcomes.
image: https://mybinxhealth.com/wp-content/uploads/2026/07/binx-on-counter_1-scaled-e1784737273991.jpg
layout: provider
modified: '2026-09-28'
name: Binx
nav: Providers
network: true
overview: 'Binx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Diagnostics, Point of Care, STI Testing, and CLIA-waived.


  Binx''s developer surface includes support, documentation, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Binx Domain Security
  slug: binx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: binx
tags:
- Healthcare
- Diagnostics
- Point of Care
- STI Testing
- CLIA-waived
- Company
website: https://mybinxhealth.com
---
