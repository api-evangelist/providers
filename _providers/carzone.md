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
- description: Carzone automotive marketplace API
  name: Carzone API
  slug: carzone-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carzone/refs/heads/main/hosts/carzone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carzone-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carzone/refs/heads/main/vendors/carzone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carzone-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carzone.ie/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.carzone.ie/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carzone.ie/terms-and-conditions/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carzone/refs/heads/main/security/carzone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carzone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carzone.ie
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.carzone.ie/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carzone is an Irish online marketplace for buying and selling new and used cars, motorcycles, and commercial vehicles. The platform offers vehicle listings, price comparisons, financing options, insurance services, and tools such as vehicle valuation and history checks. It serves both private sellers and dealers across Ireland, providing a comprehensive digital car marketplace experience.
image: https://www.carzone.ie/resources-frontend/assets/img/brand/logo-png.png
layout: provider
modified: '2026-10-07'
name: Carzone
nav: Providers
network: true
overview: Carzone is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Automotive, Ireland, and Cars.
random_paper: 6
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carzone Domain Security
  slug: carzone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carzone
tags:
- Company
- Marketplace
- Automotive
- Ireland
- Cars
website: https://www.carzone.ie
---
