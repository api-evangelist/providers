---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/soniox/changelog/soniox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/soniox-changelog.yml
- group: auth
  href: https://artifacts.apis.io/soniox/authentication/soniox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/soniox-authentication.yml
- group: operate
  href: https://artifacts.apis.io/soniox/lifecycle/soniox-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/soniox-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/soniox/lifecycle/soniox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/soniox-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/soniox/conformance/soniox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/soniox-conformance.yml
- group: agent
  href: https://artifacts.apis.io/soniox/llms/soniox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soniox-llms.txt
- group: other
  href: https://artifacts.apis.io/soniox/hosts/soniox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soniox-hosts.yml
- group: build
  href: https://artifacts.apis.io/soniox/packages/soniox-packages.yml
  title: ''
  type: SDKs
  url: packages/soniox-packages.yml
- group: build
  href: https://artifacts.apis.io/soniox/packages/soniox-packages.yml
  title: ''
  type: Packages
  url: packages/soniox-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soniox.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://app.soniox.com/help-center
- group: start
  title: ''
  type: SignUp
  url: https://console.soniox.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soniox.com/policies/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://soniox.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soniox
- group: start
  title: ''
  type: GettingStarted
  url: https://soniox.com/docs/stt/get-started
- group: company
  title: ''
  type: Blog
  url: https://soniox.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soniox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://soniox.com/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/soniox/security/soniox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soniox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soniox.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://soniox.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Soniox provides a multilingual speech AI platform offering real‑time speech‑to‑text, text‑to‑speech and translation APIs in over 60 languages. The service emphasizes low‑latency streaming, high accuracy with native‑speaker models, and seamless language switching for live voice applications, targeting developers building voice‑enabled products.
image: https://soniox.com/og/logo_soniox_v2.png
layout: provider
modified: '2026-10-27'
name: Soniox
nav: Providers
network: true
overview: 'Soniox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Speech AI, Multilingual, Real-Time, and Streaming.


  Soniox''s developer surface includes changelog, authentication, support, signup flow, pricing, getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 46.4
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/soniox/soniox-2026-11-03T143553.png
security:
- kind: authentication
  name: Soniox Authentication
  slug: soniox-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Soniox Domain Security
  slug: soniox-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soniox
tags:
- Speech AI
- Multilingual
- Real-Time
- Streaming
website: https://soniox.com/
---
