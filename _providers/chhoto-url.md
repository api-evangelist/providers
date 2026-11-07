---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: A lightweight, self‑hosted URL shortener service providing endpoints to create, retrieve, and manage short links.
  name: Chhoto URL API
  slug: chhoto-url-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/chhoto-url/hosts/chhoto-url-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chhoto-url-hosts.yml
- group: other
  href: https://artifacts.apis.io/chhoto-url/vendors/chhoto-url-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chhoto-url-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chhoto-url/security/chhoto-url-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chhoto-url-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chhoto.link
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SinTan1729
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/SinTan1729/chhoto-url/blob/main/docs/INSTALLATION.md
- group: start
  title: ''
  type: Demo
  url: https://demo.chhoto.link
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://chhoto.link
  - status: 200
    url: https://github.com/SinTan1729/chhoto-url
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Chhoto URL is a lightweight, self‑hosted URL shortener written in Rust. It provides a fast, open‑source service for creating short links, with a tiny container image and low resource usage. The project is maintained by SinTan1729 and released under the MIT license.
image: https://chhoto.link/static/assets/banner.png
layout: provider
modified: '2026-10-28'
name: Chhoto URL
nav: Providers
network: true
overview: 'Chhoto URL is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include URL Shorteners, Rust, Open Source, Self-Hosted, and MIT License.


  Chhoto URL''s developer surface includes documentation and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chhoto-url/chhoto-url-2026-11-03T124007.png
security:
- kind: domain-security
  name: Chhoto Url Domain Security
  slug: chhoto-url-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: chhoto-url
tags:
- URL Shorteners
- Rust
- Open Source
- Self-Hosted
- MIT License
website: https://chhoto.link
---
