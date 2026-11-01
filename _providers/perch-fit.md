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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation for Perch, part of Catapult, accessible via the Perch product page.
  name: Perch API
  slug: perch-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/perch-fit/hosts/perch-fit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/perch-fit-hosts.yml
- group: other
  href: https://artifacts.apis.io/perch-fit/vendors/perch-fit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/perch-fit-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.catapult.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.catapult.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.catapult.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.catapult.com/newsroom
- group: auth
  href: https://artifacts.apis.io/perch-fit/security/perch-fit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perch-fit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.catapult.com/perch
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the provider’s API host.
  evidence:
  - status: 404
    url: https://api.perch.fit/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Perch, now part of Catapult, provides athlete monitoring and performance analytics solutions for sports teams and individual athletes. Their platform offers video analysis, wearable sensor integration, and data-driven insights to improve training, injury prevention, and competitive performance across multiple sports.
image: https://www.catapult.com/wp-content/uploads/2025/07/Perch-hardware-in-action.jpg
layout: provider
modified: '2026-10-29'
name: Perch
nav: Providers
network: true
overview: 'Perch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Athlete-Monitoring, Analytics, and Video-Analysis.


  Perch''s developer surface includes support, pricing, and 6 more developer resources.'
random_paper: 10
scopes:
- name: Perch Fit Scopes
  scope_count: 0
  slug: perch-fit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Perch Fit Authentication
  slug: perch-fit-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Perch Fit Domain Security
  slug: perch-fit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: perch-fit
tags:
- Company
- Sports
- Athlete-Monitoring
- Analytics
- Video-Analysis
website: https://www.catapult.com/perch
---
