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
  href: https://raw.githubusercontent.com/api-evangelist/apifox/refs/heads/main/hosts/apifox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apifox-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apifox/refs/heads/main/packages/apifox-packages.yml
  title: ''
  type: SDKs
  url: packages/apifox-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apifox/refs/heads/main/packages/apifox-packages.yml
  title: ''
  type: Packages
  url: packages/apifox-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apifox/refs/heads/main/security/apifox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apifox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apifox.com/
created: '2026-10-03'
description: Apifox provides an integrated platform for API design, documentation, debugging, mock servers, and automated testing. It enables teams to collaboratively create, manage, and test APIs with visual tools, supporting OpenAPI specifications and offering features such as AI‑assisted design, CI/CD integration, and extensive import/export capabilities. The service aims to boost development efficiency by up to tenfold, positioning itself as a comprehensive alternative to separate tools like Postman, Swagger, and JMeter.
layout: provider
modified: '2026-10-03'
name: Apifox
nav: Providers
network: true
overview: Apifox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mock and CI/CD.
random_paper: 9
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apifox Domain Security
  slug: apifox-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apifox
tags:
- Mock
- CI/CD
website: https://apifox.com/
---
