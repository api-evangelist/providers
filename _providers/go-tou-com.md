---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/go-tou-com/conformance/go-tou-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/go-tou-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/go-tou-com/hosts/go-tou-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/go-tou-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goto-u.com:443/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://goto-u.com:443/en/news
- group: auth
  href: https://artifacts.apis.io/go-tou-com/security/go-tou-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/go-tou-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://go-tou.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://goto-u.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Go To-U provides an operating system for electric vehicle (EV) charging management, delivering tools for Charge Point Operators to optimize station utilization, increase profitability, and offer seamless charging experiences. The platform supports advanced reservation technology, AI‑driven optimization, and multi‑country deployment, serving over one million chargers across 67 countries. It offers business solutions for EV drivers, fleet operators, and partners, with a focus on reliability, scalability, and innovative features for the EV ecosystem.
image: https://goto-u.com/images/home-preview.jpg
layout: provider
modified: '2026-10-29'
name: Go To-U
nav: Providers
network: true
overview: Go To-U is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Vehicles, Charging, Platform, and Software-as-a-Service.
random_paper: 7
scopes:
- name: Go Tou Com Scopes
  scope_count: 0
  slug: go-tou-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/go-tou-com/go-tou-com-2026-11-03T132900.png
security:
- kind: authentication
  name: Go Tou Com Authentication
  slug: go-tou-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Go Tou Com Domain Security
  slug: go-tou-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: go-tou-com
tags:
- Company
- Electric Vehicles
- Charging
- Platform
- Software-as-a-Service
- CPO
website: https://go-tou.com/
---
