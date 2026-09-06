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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zendrive
- group: docs
  title: ''
  type: Documentation
  url: https://zendrive-root.bitbucket.io/ios/docs/latest/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://react-native-zendrive-api-v2.netlify.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://react-native-zendrive-guide-v2.netlify.app/readme
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/zendrive/zendrive-sdk-ios-sample
- group: build
  title: ''
  type: Packages
  url: packages/zendrive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zendrive-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zendrive-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zendrive-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zendrive-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zendrive-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zendrive-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zendrive-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zendrive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zendrive-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zendrive-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zendrive-domain-security.yml
created: '2026-09-05'
description: 'Zendrive Inc. was a San Francisco mobility risk intelligence company that turned an ordinary smartphone into a telematics sensor. Its product was a mobile SDK, not an HTTP API: an app embedded the Zendrive SDK, which automatically detected the start and end of every drive, collected accelerometer, gyroscope and GPS data with minimal battery impact, raised in-process callbacks for trip and collision events, and uploaded the drive for scoring. Fleets, rideshare operators and auto insurers consumed the resulting analytics — collision detection and severity, distracted driving, speeding, star ratings — through a dashboard and an Analytics REST API, with rideshare insurance-period modelling and a US/EU data-residency selector. Intuit acquired Zendrive''s technology for Credit Karma''s Karma Drive in 2024 and the developer program was shut down: as probed 2026-09-05 every Zendrive host is dead. Only the SDK reference, sample apps and published packages survive.'
image: https://avatars.githubusercontent.com/u/9817922?v=4
layout: provider
modified: '2026-09-05'
name: Zendrive
nav: Providers
network: true
overview: 'Zendrive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telematics, Mobility, Insurance, and Automotive.


  Zendrive''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, sandbox, and 11 more developer resources.'
plans:
- name: Zendrive Plans Pricing
  plan_count: 0
  slug: zendrive-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Zendrive Rate Limits
  slug: zendrive-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Zendrive Authentication
  slug: zendrive-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zendrive Domain Security
  slug: zendrive-domain-security
  summary_line: no transport/DNS hardening detected
slug: zendrive
tags:
- Company
- Telematics
- Mobility
- Insurance
- Automotive
- Fleet Management
- Driving Behavior
- Mobile SDK
- Risk
- Acquired
---
