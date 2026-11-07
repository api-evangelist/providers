---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides public and management REST APIs for Exchange, Merchant Backend, Wallet Core, Core Bank, and other components.
  name: GNU Taler Core APIs
  slug: gnu-taler-core-apis
- baseURL: https://merchant-backend.demo.taler.net
  baseurl_source: declared
  description: 'GNU Taler API as documented publicly: 176 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: GNU Taler API
  slug: gnu-taler-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/gnu-taler/rules/gnu-taler-rules.yml
  title: ''
  type: Spectral
  url: rules/gnu-taler-rules.yml
- group: design
  href: https://artifacts.apis.io/gnu-taler/json-ld/gnu-taler-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gnu-taler-context.jsonld
- group: design
  href: https://artifacts.apis.io/gnu-taler/vocabulary/gnu-taler-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gnu-taler-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gnu-taler/data-model/gnu-taler-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gnu-taler-data-model.yml
- group: build
  href: https://artifacts.apis.io/gnu-taler/cli/gnu-taler-cli.yml
  title: ''
  type: CLI
  url: cli/gnu-taler-cli.yml
- group: auth
  href: https://artifacts.apis.io/gnu-taler/security/gnu-taler-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gnu-taler-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/gnu-taler/conformance/gnu-taler-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gnu-taler-conformance.yml
- group: auth
  href: https://artifacts.apis.io/gnu-taler/well-known/gnu-taler-taler-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gnu-taler-taler-security.txt
- group: auth
  href: https://artifacts.apis.io/gnu-taler/well-known/gnu-taler-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gnu-taler-security.txt
- group: agent
  href: https://artifacts.apis.io/gnu-taler/well-known/gnu-taler-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gnu-taler-well-known.yml
- group: other
  href: https://artifacts.apis.io/gnu-taler/hosts/gnu-taler-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gnu-taler-hosts.yml
- group: build
  href: https://artifacts.apis.io/gnu-taler/packages/gnu-taler-packages.yml
  title: ''
  type: SDKs
  url: packages/gnu-taler-packages.yml
- group: build
  href: https://artifacts.apis.io/gnu-taler/packages/gnu-taler-packages.yml
  title: ''
  type: Packages
  url: packages/gnu-taler-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.taler.net/en/news/index.html
- group: auth
  href: https://artifacts.apis.io/gnu-taler/security/gnu-taler-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gnu-taler-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gnu-taler/security/gnu-taler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gnu-taler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.taler.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taler.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.taler.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.taler.net/en/docs.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@taler.net
- group: company
  title: ''
  type: Blog
  url: https://www.taler.net/en/news/
coverage:
  checked: '2026-10-28'
  detail: Documentation provides API descriptions only as HTML pages, no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.taler.net/core/api-overview.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: GNU Taler is an open‑source, privacy‑preserving electronic cash system developed as part of the GNU project. It enables merchants to accept digital payments that are fully auditable for tax purposes while preserving payer anonymity. The system is built on cryptographic protocols and integrates with GNU tools. Taler supports multiple currencies, provides a RESTful API for payment processing, and is maintained by the GNUnet e.V. and Taler Systems SA. The project aims to offer a free, secure, and tax‑compliant alternative to traditional payment methods.
image: https://www.taler.net/images/favicon.png
json_schemas:
- name: GetMonitorResponse
  property_count: 11
  slug: gnu-taler-get-monitor-response
- name: PatchConversionRateClassesClassidRequest
  property_count: 10
  slug: gnu-taler-patch-conversion-rate-classes-classid-request
- name: PatchConversionRateClassesResponse
  property_count: 13
  slug: gnu-taler-patch-conversion-rate-classes-response
- name: PostConversionRateClassesRequest
  property_count: 10
  slug: gnu-taler-post-conversion-rate-classes-request
- name: PostConversionRateRequest
  property_count: 10
  slug: gnu-taler-post-conversion-rate-request
- name: PutDepositConfirmationRequest
  property_count: 16
  slug: gnu-taler-put-deposit-confirmation-request
jsonld:
- class_count: 120
  name: Gnu Taler Context
  property_count: 209
  slug: gnu-taler-context
layout: provider
modified: '2026-10-28'
name: GNU Taler
nav: Providers
network: true
overview: 'GNU Taler is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Ecash, Open Source, Finance, and Privacy.


  The GNU Taler catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GNU Taler''s developer surface includes CLI, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: GNU Taler API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: gnu-taler-rules
scopes:
- name: Gnu Taler Scopes
  scope_count: 0
  slug: gnu-taler-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 34.5
    discoverability: 58.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gnu-taler/gnu-taler-2026-11-03T133056.png
security:
- kind: authentication
  name: Gnu Taler Authentication
  slug: gnu-taler-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gnu Taler Domain Security
  slug: gnu-taler-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gnu Taler Vulnerability Disclosure
  slug: gnu-taler-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gnu-taler
tags:
- Payments
- Ecash
- Open Source
- Finance
- Privacy
website: https://www.taler.net/
---
