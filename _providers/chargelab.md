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
- description: API for EV charging station data, reservations, billing and analytics.
  name: ChargeLab API
  slug: chargelab-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chargelab/refs/heads/main/vendors/chargelab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chargelab-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chargelab/refs/heads/main/hosts/chargelab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargelab-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/chargelab
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chargelab/refs/heads/main/security/chargelab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargelab-domain-security.yml
coverage:
  checked: '2026-10-08'
  detail: API spec endpoints return 403 or JavaScript shells, no machine‑readable OpenAPI found.
  evidence:
  - status: 403
    url: https://api.chargelab.co/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Chargelab is a fintech startup focused on providing innovative charging solutions for electric vehicles. The company aims to simplify the EV charging experience through a robust API platform that enables developers to integrate charging station data, availability, pricing, and transaction processing into their applications. Chargelab’s services include real‑time station status, reservation management, billing integration, and analytics, targeting fleet operators, mobility providers, and consumer apps. While still early in its public rollout, the company positions itself as a bridge between EV infrastructure and digital services, emphasizing scalability, security, and developer-friendly documentation.
layout: provider
modified: '2026-10-08'
name: Chargelab
nav: Providers
network: true
overview: Chargelab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, ev-charging, Startups, and mobility.
random_paper: 19
score:
  band: minimal
  composite: 3.2
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
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chargelab Domain Security
  slug: chargelab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargelab
tags:
- Fintech
- ev-charging
- Startups
- mobility
website: https://equityzen.com/company/chargelab
---
