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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: siGit platform API documented at the reference page.
  name: siGit API
  slug: sigit-api
artifact_total: 5
common:
- group: build
  href: https://artifacts.apis.io/sigit-si/cli/sigit-si-cli.yml
  title: ''
  type: CLI
  url: cli/sigit-si-cli.yml
- group: operate
  href: https://artifacts.apis.io/sigit-si/changelog/sigit-si-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sigit-si-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sigit.si/
- group: other
  href: https://artifacts.apis.io/sigit-si/hosts/sigit-si-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sigit-si-hosts.yml
- group: build
  href: https://artifacts.apis.io/sigit-si/packages/sigit-si-packages.yml
  title: ''
  type: SDKs
  url: packages/sigit-si-packages.yml
- group: build
  href: https://artifacts.apis.io/sigit-si/packages/sigit-si-packages.yml
  title: ''
  type: Packages
  url: packages/sigit-si-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://sigit.si/changelog
- group: auth
  href: https://artifacts.apis.io/sigit-si/security/sigit-si-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sigit-si-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sigit-si/security/sigit-si-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sigit-si-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sigit.si/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sigit.si/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sigit.si/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sigit.si/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getsigit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sigit.si/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sigit.si/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation at https://docs.sigit.si/reference is accessible but provides no machine‑readable API contract.
  evidence:
  - status: 200
    url: https://docs.sigit.si/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: siGit is a Git hosting platform for the AI era, offering versioned repositories and open‑weights model storage with full model cards and LFS‑backed files. It provides a unified UI where code and large AI models coexist, enabling developers to manage source code and massive model weights side‑by‑side. The platform exposes an Agent Client Protocol that lets AI coding agents interact directly with repositories, simplifying integration of AI workflows into standard development pipelines.
image: https://sigit.si/icon.png
layout: provider
modified: '2026-10-30'
name: sigit-si
nav: Providers
network: true
overview: 'sigit-si is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Git Hosting, AI, Version Control, and Model Storage.


  sigit-si''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 17
scopes:
- name: Sigit Si Scopes
  scope_count: 0
  slug: sigit-si-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sigit Si Authentication
  slug: sigit-si-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sigit Si Domain Security
  slug: sigit-si-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sigit Si Trust Center
  slug: sigit-si-trust-center
  summary_line: SOC 2, ISO 27001
slug: sigit-si
tags:
- Company
- Git Hosting
- AI
- Version Control
- Model Storage
- Open Source
website: https://sigit.si/
---
