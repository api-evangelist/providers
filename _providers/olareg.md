---
agent_readiness:
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: build
  href: https://artifacts.apis.io/olareg/cli/olareg-cli.yml
  title: ''
  type: CLI
  url: cli/olareg-cli.yml
- group: operate
  href: https://artifacts.apis.io/olareg/changelog/olareg-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/olareg-changelog.yml
- group: design
  href: https://artifacts.apis.io/olareg/conformance/olareg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/olareg-conformance.yml
- group: other
  href: https://artifacts.apis.io/olareg/hosts/olareg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/olareg-hosts.yml
- group: other
  href: https://artifacts.apis.io/olareg/vendors/olareg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/olareg-vendors.yml
- group: build
  href: https://artifacts.apis.io/olareg/packages/olareg-packages.yml
  title: ''
  type: SDKs
  url: packages/olareg-packages.yml
- group: build
  href: https://artifacts.apis.io/olareg/packages/olareg-packages.yml
  title: ''
  type: Packages
  url: packages/olareg-packages.yml
- group: auth
  href: https://artifacts.apis.io/olareg/security/olareg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/olareg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://olareg.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/olareg
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/olareg/olareg
- group: docs
  title: ''
  type: Documentation
  url: https://olareg.org/install/
- group: auth
  title: ''
  type: Authentication
  url: https://olareg.org/auth/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/olareg/olareg/releases
coverage:
  checked: '2026-10-13'
  detail: olareg implements the OCI Distribution API but neither olareg.org (openapi.json 404, no API reference page) nor the olareg/olareg repo publishes a machine-readable contract; olareg.dev (the stub Website) did not answer and the GitHub repo homepage is olareg.org.
  evidence:
  - status: 404
    url: https://olareg.org/openapi.json
  - status: 404
    url: https://olareg.org/api/
  - status: 200
    url: https://olareg.org
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: olareg is an open-source (Apache-2.0) minimal OCI-conformant container registry that runs as a container, a standalone binary, or embedded in Go unit tests, storing content in the OCI Layout.
layout: provider
modified: '2026-10-13'
name: olareg
nav: Providers
network: true
overview: 'olareg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Container Registry, OCI, and Open Source.


  olareg''s developer surface includes CLI, changelog, documentation, authentication, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 26.8
    operational_transparency: 21.1
  previous_composite: 15.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Olareg Domain Security
  slug: olareg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: olareg
tags:
- Company
- Container Registry
- OCI
- Open Source
website: https://olareg.org
---
