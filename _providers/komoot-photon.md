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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/komoot-photon/conventions/komoot-photon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/komoot-photon-conventions.yml
- group: other
  href: https://artifacts.apis.io/komoot-photon/hosts/komoot-photon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/komoot-photon-hosts.yml
- group: other
  href: https://artifacts.apis.io/komoot-photon/vendors/komoot-photon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/komoot-photon-vendors.yml
- group: auth
  href: https://artifacts.apis.io/komoot-photon/security/komoot-photon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/komoot-photon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://photon.komoot.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/komoot/photon#readme
- group: docs
  title: ''
  type: APIReference
  url: https://photon.komoot.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/komoot/photon#readme
- group: operate
  title: ''
  type: Support
  url: mailto:photon@komoot.de
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/komoot
coverage:
  checked: '2026-10-28'
  detail: The provider's API reference page requires query parameters and no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec was found on any discovered host.
  evidence:
  - status: 404
    url: https://photon.komoot.io/openapi.json
  - status: 404
    url: https://photon.komoot.io/openapi.yaml
  - status: 404
    url: https://photon.komoot.io/swagger.json
  - status: 404
    url: https://photon.komoot.io/v1/openapi.json
  - status: 404
    url: https://photon.komoot.io/api-docs
  - status: 404
    url: https://photon.komoot.io/docs
  - status: 404
    url: https://photon.komoot.io/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Photon provides a fast, scalable, multilingual search-as-you-type geocoding service built on OpenStreetMap data and OpenSearch, offering forward and reverse geocoding via a simple HTTP API, with features such as typo tolerance, language preference, and result limiting, suitable for developers needing real-time location suggestions.
image: https://photon.komoot.io/static/img/photon_logo.png
layout: provider
modified: '2026-10-28'
name: Photon
nav: Providers
network: true
overview: 'Photon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding, OpenStreetMap, Search, Typeahead, and Open Source.


  Photon''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
plans:
- name: Komoot Photon Plans Pricing
  plan_count: 0
  slug: komoot-photon-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Komoot Photon Rate Limits
  slug: komoot-photon-rate-limits
scopes:
- name: Komoot Photon Scopes
  scope_count: 0
  slug: komoot-photon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/komoot-photon/komoot-photon-2026-11-03T134507.png
security:
- kind: authentication
  name: Komoot Photon Authentication
  slug: komoot-photon-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Komoot Photon Domain Security
  slug: komoot-photon-domain-security
  summary_line: TLSv1.2
slug: komoot-photon
tags:
- Geocoding
- OpenStreetMap
- Search
- Typeahead
- Open Source
- Location
website: https://photon.komoot.io/
---
