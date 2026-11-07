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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Syncthing API as documented publicly: 60 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Syncthing API
  slug: syncthing-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/syncthing/rules/syncthing-rules.yml
  title: ''
  type: Spectral
  url: rules/syncthing-rules.yml
- group: design
  href: https://artifacts.apis.io/syncthing/vocabulary/syncthing-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/syncthing-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/syncthing/conformance/syncthing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/syncthing-conformance.yml
- group: agent
  href: https://artifacts.apis.io/syncthing/llms/syncthing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syncthing-llms.txt
- group: auth
  href: https://artifacts.apis.io/syncthing/well-known/syncthing-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/syncthing-security.txt
- group: agent
  href: https://artifacts.apis.io/syncthing/well-known/syncthing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/syncthing-well-known.yml
- group: other
  href: https://artifacts.apis.io/syncthing/hosts/syncthing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syncthing-hosts.yml
- group: other
  href: https://artifacts.apis.io/syncthing/vendors/syncthing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/syncthing-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://syncthing.net/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/syncthing/syncthing/releases/latest
- group: auth
  href: https://artifacts.apis.io/syncthing/security/syncthing-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/syncthing-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/syncthing/security/syncthing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syncthing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syncthing.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syncthing.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syncthing.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syncthing.net/intro/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://forum.syncthing.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syncthing
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/syncthing/syncthing
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.syncthing.net/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Syncthing is an open-source continuous file synchronization program that securely syncs files across multiple devices in real time. It uses TLS encryption with perfect forward secrecy, operates without central servers, and provides a web GUI for configuration. The project is maintained by the Syncthing Foundation and supported by commercial partners, offering cross‑platform support for Windows, macOS, Linux, BSD, and more.
layout: provider
modified: '2026-10-28'
name: Syncthing
nav: Providers
network: true
overview: 'Syncthing is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include File Synchronization, Open Source, Cross-Platform, Encryption, and Peer-to-Peer.


  The Syncthing catalog on APIs.io includes 1 Spectral governance ruleset.


  Syncthing''s developer surface includes changelog, documentation, API reference, getting-started guide, support, and 14 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Syncthing API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: syncthing-rules
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.9
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/syncthing/syncthing-2026-11-03T144236.png
security:
- kind: domain-security
  name: Syncthing Domain Security
  slug: syncthing-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Syncthing Vulnerability Disclosure
  slug: syncthing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: syncthing
tags:
- File Synchronization
- Open Source
- Cross-Platform
- Encryption
- Peer-to-Peer
website: https://syncthing.net/
---
