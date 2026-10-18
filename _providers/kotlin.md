---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.3
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Core Kotlin standard library with collections, I/O, and utility functions.
  name: Kotlin Standard Library API
  slug: stdlib
- description: Library support for Kotlin coroutines with async/await patterns.
  name: Kotlin Coroutines API
  slug: coroutines
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kotlin/refs/heads/main/plans/kotlin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kotlin-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kotlin/refs/heads/main/rate-limits/kotlin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kotlin-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kotlin/refs/heads/main/finops/kotlin-finops.yml
  title: ''
  type: FinOps
  url: finops/kotlin-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kotlin/refs/heads/main/security/kotlin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kotlin-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jetbrains
- group: company
  title: ''
  type: Website
  url: https://kotlinlang.org/
- group: docs
  title: ''
  type: Documentation
  url: https://kotlinlang.org/docs/home.html
- group: company
  title: ''
  type: Blog
  url: https://blog.jetbrains.com/kotlin/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JetBrains/kotlin
- group: operate
  title: ''
  type: Community
  url: https://kotlinlang.org/community/
- group: agent
  title: ''
  type: LlmsText
  url: https://kotlinlang.org/llms.txt
created: '2024-01-01'
description: Kotlin is a modern, concise, and safe programming language for the JVM, Android, and multiplatform development. It is developed by JetBrains and provides full interoperability with Java. Kotlin's standard library and ecosystem offer rich APIs for building applications across all platforms.
finops:
- has_sources: false
  method: generated
  name: Kotlin Finops
  primary_unit: ''
  service_category: API
  slug: kotlin-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kotlin.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.kotlinlang.org over HTTP; 2 tools listed.
  name: Kotlin MCP Server
  slug: kotlin
modified: '2026-04-28'
name: Kotlin
nav: Providers
network: true
overview: 'Kotlin is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Android, JVM, Kotlin, Multiplatform, and Programming Language.


  Kotlin''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Kotlin Plans Pricing
  plan_count: 3
  slug: kotlin-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Kotlin Rate Limits
  slug: kotlin-rate-limits
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 14.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/kotlin/refs/heads/main/screenshots/kotlin-2026-06-20T184140.png
security:
- kind: domain-security
  name: Kotlin Domain Security
  slug: kotlin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kotlin
tags:
- Android
- JVM
- Kotlin
- Multiplatform
- Programming Language
website: https://kotlinlang.org/
---
