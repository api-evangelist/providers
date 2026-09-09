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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: The SenseGlove Core API is a native C++ and C# library (SGCore namespace) that reads sensor and hand-pose data from, and sends force-feedback, vibrotactile and wrist-squeeze commands to, SenseGlove ha
  name: SenseGlove Core API
  slug: senseglove-core-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adjuvomotion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.senseglove.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.senseglove.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://senseglove.gitlab.io/SenseGloveDocs/
- group: docs
  title: ''
  type: APIReference
  url: https://senseglove.gitlab.io/SenseGloveDocs/native/core-api-intro.html
- group: start
  title: ''
  type: GettingStarted
  url: https://senseglove.gitlab.io/SenseGloveDocs/quick-start.html
- group: operate
  title: ''
  type: Support
  url: https://www.senseglove.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.senseglove.com/news-and-updates/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Adjuvo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.senseglove.com/shop/
- group: start
  title: ''
  type: Login
  url: https://www.senseglove.com/my-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.senseglove.com/terms-of-sale/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.senseglove.com/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/adjuvomotion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adjuvomotion-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adjuvomotion-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/adjuvomotion-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adjuvomotion-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adjuvomotion-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adjuvomotion-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adjuvomotion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adjuvomotion-rate-limits.yml
created: '2026-09-07'
description: 'Adjuvo Motion B.V. trades publicly as SenseGlove, a Dutch haptics company headquartered at the Katoenhuis in Rotterdam with engineering roots in Delft. It designs and manufactures force-feedback and vibrotactile gloves for virtual and extended reality — the Nova 2, the Nova and the DK1 — plus the R1 exoskeleton glove used for tele-robotics and imitation learning, sold into immersive training, virtual prototyping, academic research and humanoid robotics. Its developer surface is a native device API rather than a web service: a C++ and C# Core API in the SGCore namespace, the SGConnect communications library, the SenseCom desktop daemon, first-party Unity and Unreal Engine plugins, ROS 1 workspaces and a Python API for the R1. No public HTTP, REST or GraphQL API is published.'
image: https://www.senseglove.com/wp-content/uploads/2022/05/SenseGlove-home-featured.jpg
layout: provider
modified: '2026-09-07'
name: Adjuvo Motion
nav: Providers
network: true
overview: 'Adjuvo Motion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Haptics, Virtual Reality, Extended Reality, Robotics, and Hardware.


  Adjuvo Motion''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 15 more developer resources.'
plans:
- name: Adjuvomotion Plans Pricing
  plan_count: 0
  slug: adjuvomotion-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Adjuvomotion Rate Limits
  slug: adjuvomotion-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 48.8
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 24.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adjuvomotion Domain Security
  slug: adjuvomotion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adjuvomotion
tags:
- Haptics
- Virtual Reality
- Extended Reality
- Robotics
- Hardware
- SDK
- Simulation
- Training
- Teleoperation
- Wearables
website: https://www.senseglove.com/
---
