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
  href: https://raw.githubusercontent.com/api-evangelist/bostaldrugdelivery/refs/heads/main/hosts/bostaldrugdelivery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bostaldrugdelivery-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bostaldrugdelivery/refs/heads/main/vendors/bostaldrugdelivery-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bostaldrugdelivery-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bostaldrugdelivery/refs/heads/main/security/bostaldrugdelivery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bostaldrugdelivery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bostaldrugdelivery
coverage:
  checked: '2026-10-03'
  detail: No public website or developer documentation could be located for Bostaldrugdelivery.
  evidence:
  - status: 403
    url: https://equityzen.com/company/bostaldrugdelivery
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Bostaldrugdelivery is a company identified in the API Evangelist secondary‑market harvest. No public website or official documentation could be located after exhaustive searches, including the listed EquityZen profile which returned access‑denied. Consequently, the company currently appears only as a stub entry without verifiable online presence, and no API endpoints, documentation, or contact details are publicly available.
layout: provider
modified: '2026-10-03'
name: Bostaldrugdelivery
nav: Providers
network: true
overview: Bostaldrugdelivery is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Delivery, Healthcare, and Logistics.
random_paper: 11
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
  name: Bostaldrugdelivery Domain Security
  slug: bostaldrugdelivery-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bostaldrugdelivery
tags:
- Company
- Pharmacy
- Delivery
- Healthcare
- Logistics
website: https://equityzen.com/company/bostaldrugdelivery
---
