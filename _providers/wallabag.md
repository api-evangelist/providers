---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'wallabag API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: wallabag API
  slug: wallabag-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/wallabag/rules/wallabag-rules.yml
  title: ''
  type: Spectral
  url: rules/wallabag-rules.yml
- group: design
  href: https://artifacts.apis.io/wallabag/vocabulary/wallabag-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wallabag-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/wallabag/authentication/wallabag-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wallabag-authentication.yml
- group: design
  href: https://artifacts.apis.io/wallabag/conformance/wallabag-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wallabag-conformance.yml
- group: other
  href: https://artifacts.apis.io/wallabag/hosts/wallabag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wallabag-hosts.yml
- group: other
  href: https://artifacts.apis.io/wallabag/vendors/wallabag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wallabag-vendors.yml
- group: build
  href: https://artifacts.apis.io/wallabag/packages/wallabag-packages.yml
  title: ''
  type: SDKs
  url: packages/wallabag-packages.yml
- group: build
  href: https://artifacts.apis.io/wallabag/packages/wallabag-packages.yml
  title: ''
  type: Packages
  url: packages/wallabag-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wallabag.org/
- group: auth
  href: https://artifacts.apis.io/wallabag/security/wallabag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallabag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wallabag.org/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.wallabag.org/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.wallabag.org/developer/
- group: company
  title: ''
  type: Blog
  url: https://wallabag.org/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wallabag
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but provide no machine‑readable API contract.
  evidence:
  - status: 200
    url: https://doc.wallabag.org/developer/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Wallabag is an open-source, self‑hostable read‑it‑later application that lets users save web articles to read later across devices. It offers features like import from Pocket, extensions, mobile apps, and a web interface, emphasizing privacy with no ads or tracking. The project is community‑driven, providing documentation, API access, and regular releases.
image: https://wallabag.org/img/wallabag_preview.png
layout: provider
modified: '2026-10-28'
name: wallabag
nav: Providers
network: true
overview: 'wallabag is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, Read-it-later, Self-hosted, Privacy, and Community.


  The wallabag catalog on APIs.io includes 1 Spectral governance ruleset.


  wallabag''s developer surface includes authentication, documentation, API reference, engineering blog, and 11 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: wallabag API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: wallabag-rules
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wallabag Authentication
  slug: wallabag-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wallabag Domain Security
  slug: wallabag-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wallabag
tags:
- Open Source
- Read-it-later
- Self-hosted
- Privacy
- Community
website: https://wallabag.org/
---
