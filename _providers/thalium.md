---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Persistent memory and reasoning API platform
  name: Thalium API
  slug: thalium-api-2
- description: 'SYSGRAFT API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: SYSGRAFT API
  slug: thalium-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/thalium/plans/thalium-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thalium-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/thalium/rules/thalium-rules.yml
  title: ''
  type: Spectral
  url: rules/thalium-rules.yml
- group: design
  href: https://artifacts.apis.io/thalium/vocabulary/thalium-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thalium-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/thalium/changelog/thalium-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thalium-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://thalium.io/security
- group: auth
  href: https://artifacts.apis.io/thalium/authentication/thalium-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thalium-authentication.yml
- group: design
  href: https://artifacts.apis.io/thalium/conformance/thalium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thalium-conformance.yml
- group: other
  href: https://artifacts.apis.io/thalium/hosts/thalium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thalium-hosts.yml
- group: other
  href: https://artifacts.apis.io/thalium/vendors/thalium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thalium-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://thalium.io/security
- group: start
  title: ''
  type: Login
  url: https://thalium.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://thalium.io/changelog
- group: auth
  href: https://artifacts.apis.io/thalium/security/thalium-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thalium-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/thalium/security/thalium-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thalium-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thalium/security/thalium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thalium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thalium.io/
- group: docs
  title: ''
  type: Documentation
  url: https://thalium.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://thalium.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://thalium.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://thalium.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thalium.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thalium.io/privacy
created: '2026-10-19'
description: Thalium provides a persistent memory and reasoning API platform that enables applications to store state, orchestrate workflows, and enforce governance without building custom infrastructure. It offers a simple API for memory, reasoning, and security, with free tier access and clear pricing, emphasizing data privacy by not using customer data to train models.
layout: provider
modified: '2026-10-19'
name: SYSGRAFT
nav: Providers
network: true
overview: 'SYSGRAFT is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Privacy, Memory API, and Orchestration.


  The SYSGRAFT catalog on APIs.io includes 1 Spectral governance ruleset.


  SYSGRAFT''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, and 16 more developer resources.'
plans:
- name: Thalium Plans Pricing
  plan_count: 5
  slug: thalium-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: SYSGRAFT API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: thalium-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.8
    catalog_earned_first_party: 12.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 10.5
    developer_ergonomics: 26.2
    discoverability: 53.6
    operational_transparency: 13.2
  previous_composite: 44.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/thalium/thalium-2026-11-03T144521.png
security:
- kind: authentication
  name: Thalium Authentication
  slug: thalium-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thalium Domain Security
  slug: thalium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thalium Vulnerability Disclosure
  slug: thalium-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Thalium Trust Center
  slug: thalium-trust-center
  summary_line: SOC 2, GDPR
slug: thalium
tags:
- Company
- Artificial Intelligence
- Privacy
- Memory API
- Orchestration
website: https://thalium.io/
---
