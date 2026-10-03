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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Bitbrand digital marketplace API
  name: Bitbrand API
  slug: bitbrand-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitbrand/refs/heads/main/hosts/bitbrand-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitbrand-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitbrand/refs/heads/main/vendors/bitbrand-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitbrand-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitbrand.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitbrand.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitbrand
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbrand/refs/heads/main/security/bitbrand-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitbrand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitbrand.com/
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI or other machine-readable contract found on api.bitbrand.com or www.bitbrand.com.
  evidence:
  - status: 0
    url: https://api.bitbrand.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bitbrand is a digital marketplace specializing in watch faces and collectible digital art. The platform showcases a variety of themed collections, ranging from kawaii characters to collaborations with artists and brands. Users can browse, purchase, and download watch face designs for smart devices, with detailed artist profiles and licensing information provided for each collection.
layout: provider
modified: '2026-09-28'
name: Bitbrand
nav: Providers
network: true
overview: Bitbrand publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 2
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitbrand Domain Security
  slug: bitbrand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitbrand
tags:
- Company
website: https://www.bitbrand.com/
---
