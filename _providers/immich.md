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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Immich provides a self‑hosted photo and video management API documented at the Immich API reference page.
  name: Immich API
  slug: immich-api-2
- description: 'Immich API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Immich API
  slug: immich-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/immich/rules/immich-rules.yml
  title: ''
  type: Spectral
  url: rules/immich-rules.yml
- group: design
  href: https://artifacts.apis.io/immich/vocabulary/immich-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/immich-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/immich-app/.github/blob/main/SECURITY.md
- group: auth
  href: https://artifacts.apis.io/immich/authentication/immich-authentication.yml
  title: ''
  type: Authentication
  url: authentication/immich-authentication.yml
- group: design
  href: https://artifacts.apis.io/immich/conformance/immich-conformance.yml
  title: ''
  type: Conformance
  url: conformance/immich-conformance.yml
- group: auth
  href: https://artifacts.apis.io/immich/well-known/immich-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/immich-security.txt
- group: agent
  href: https://artifacts.apis.io/immich/well-known/immich-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/immich-well-known.yml
- group: other
  href: https://artifacts.apis.io/immich/hosts/immich-hosts.yml
  title: ''
  type: Hosts
  url: hosts/immich-hosts.yml
- group: other
  href: https://artifacts.apis.io/immich/vendors/immich-vendors.yml
  title: ''
  type: Vendors
  url: vendors/immich-vendors.yml
- group: build
  href: https://artifacts.apis.io/immich/packages/immich-packages.yml
  title: ''
  type: SDKs
  url: packages/immich-packages.yml
- group: build
  href: https://artifacts.apis.io/immich/packages/immich-packages.yml
  title: ''
  type: Packages
  url: packages/immich-packages.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://immich.app/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://immich.app/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/immich-app/immich/releases/latest/download/example.env
- group: company
  title: ''
  type: Blog
  url: https://immich.app/blog/feed.xml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.immich.app/developer/setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.immich.app/
- group: auth
  href: https://artifacts.apis.io/immich/security/immich-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/immich-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/immich/security/immich-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/immich-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://immich.app/
coverage:
  checked: '2026-10-28'
  detail: API host returns HTML page for openapi.json instead of a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://api.immich.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Immich is a self‑hosted photo and video management solution that lets users back up, organize, and browse their media on their own servers, emphasizing privacy and easy search across collections.
image: https://immich.app/img/social-preview.png
layout: provider
modified: '2026-10-28'
name: Immich
nav: Providers
network: true
overview: 'Immich is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Self-Hosted, Photo Management, Video Management, Privacy, and Open Source.


  The Immich catalog on APIs.io includes 1 Spectral governance ruleset.


  Immich''s developer surface includes authentication, changelog, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Immich API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: immich-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 42.9
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Immich Authentication
  slug: immich-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Immich Domain Security
  slug: immich-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Immich Vulnerability Disclosure
  slug: immich-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: immich
tags:
- Self-Hosted
- Photo Management
- Video Management
- Privacy
- Open Source
website: https://immich.app/
---
