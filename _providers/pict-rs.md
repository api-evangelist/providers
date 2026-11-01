---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Simple image hosting service API as described in the repository README.
  name: pict-rs API
  slug: pict-rs-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/pict-rs/well-known/pict-rs-codeberg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pict-rs-codeberg-security.txt
- group: design
  href: https://artifacts.apis.io/pict-rs/rules/pict-rs-rules.yml
  title: ''
  type: Spectral
  url: rules/pict-rs-rules.yml
- group: design
  href: https://artifacts.apis.io/pict-rs/vocabulary/pict-rs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pict-rs-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pict-rs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pict-rs/data-model/pict-rs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pict-rs-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pict-rs/changelog/pict-rs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pict-rs-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://codeberg.org/forgejo/governance/src/branch/main/SECURITY-POLICY.md
- group: auth
  href: https://artifacts.apis.io/pict-rs/authentication/pict-rs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pict-rs-authentication.yml
- group: design
  href: https://artifacts.apis.io/pict-rs/errors/pict-rs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pict-rs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pict-rs/conformance/pict-rs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pict-rs-conformance.yml
- group: auth
  href: https://artifacts.apis.io/pict-rs/well-known/pict-rs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pict-rs-security.txt
- group: agent
  href: https://artifacts.apis.io/pict-rs/well-known/pict-rs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pict-rs-well-known.yml
- group: other
  href: https://artifacts.apis.io/pict-rs/hosts/pict-rs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pict-rs-hosts.yml
- group: build
  href: https://artifacts.apis.io/pict-rs/packages/pict-rs-packages.yml
  title: ''
  type: SDKs
  url: packages/pict-rs-packages.yml
- group: build
  href: https://artifacts.apis.io/pict-rs/packages/pict-rs-packages.yml
  title: ''
  type: Packages
  url: packages/pict-rs-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://git.asonix.dog/asonix/pict-rs/releases
- group: auth
  href: https://artifacts.apis.io/pict-rs/security/pict-rs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pict-rs-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pict-rs/security/pict-rs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pict-rs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://git.asonix.dog/asonix/pict-rs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://git.asonix.dog/asonix/pict-rs
- group: docs
  title: ''
  type: Documentation
  url: https://git.asonix.dog/asonix/pict-rs/raw/branch/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://git.asonix.dog/asonix/pict-rs/raw/branch/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://git.asonix.dog/asonix/pict-rs/raw/branch/main/README.md
- group: operate
  title: ''
  type: Support
  url: https://matrix.to/#/#pictrs:matrix.asonix.dog?via=matrix.asonix.dog
- group: company
  title: ''
  type: Blog
  url: https://masto.asonix.dog/@asonix
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://masto.asonix.dog/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: API endpoints require an X-Api-Token header, and the documentation does not provide a public contract.
  evidence:
  - status: 200
    url: https://git.asonix.dog/asonix/pict-rs/raw/branch/main/README.md
  reason: partner-login
  state: gated
created: '2026-10-28'
description: pict-rs is an open-source, self-hosted image hosting service written in Rust. It provides a simple HTTP API for uploading, retrieving, and managing images, supporting features such as animated GIFs, video files, and configurable storage back‑ends. The project is maintained by the developer known as asonix and is hosted on a Forgejo instance, with documentation available in the repository README and a community chat on Matrix. It is licensed under AGPL‑3.0 and can be run via command‑line, Docker, or as a system service.
image: https://git.asonix.dog/asonix/pict-rs/-/summary-card
layout: provider
modified: '2026-10-28'
name: pict-rs
nav: Providers
network: true
overview: 'pict-rs publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Image Hosting, Rust, Open Source, API, and Self-hosted.


  The pict-rs catalog on APIs.io includes 1 Spectral governance ruleset.


  pict-rs'' developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Pict Rs Plans Pricing
  plan_count: 0
  slug: pict-rs-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Pict Rs Rate Limits
  slug: pict-rs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: pict-rs API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: pict-rs-rules
scopes:
- name: Pict Rs Scopes
  scope_count: 0
  slug: pict-rs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 70.7
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pict Rs Authentication
  slug: pict-rs-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Pict Rs Domain Security
  slug: pict-rs-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Pict Rs Vulnerability Disclosure
  slug: pict-rs-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-actions-run
  slug: pict-rs-get-actions-run
slug: pict-rs
tags:
- Image Hosting
- Rust
- Open Source
- API
- Self-hosted
website: https://git.asonix.dog/asonix/pict-rs
---
