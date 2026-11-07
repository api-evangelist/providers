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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Lumen5 Agentic Access
  operation_count: 15
  slug: lumen5-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 1
apis:
- description: The Video Creation API from Lumen5 — 13 operation(s) for video creation.
  name: Lumen5 Video Creation API
  slug: lumen5-video-creation-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/lumen5/agentic-access/lumen5-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lumen5-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lumen5/rules/lumen5-rules.yml
  title: ''
  type: Spectral
  url: rules/lumen5-rules.yml
- group: design
  href: https://artifacts.apis.io/lumen5/json-ld/lumen5-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lumen5-context.jsonld
- group: design
  href: https://artifacts.apis.io/lumen5/vocabulary/lumen5-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lumen5-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lumen5/data-model/lumen5-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lumen5-data-model.yml
- group: design
  href: https://artifacts.apis.io/lumen5/conventions/lumen5-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lumen5-conventions.yml
- group: design
  href: https://artifacts.apis.io/lumen5/conventions/lumen5-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lumen5-conventions.yml
- group: design
  href: https://artifacts.apis.io/lumen5/errors/lumen5-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lumen5-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lumen5/conformance/lumen5-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lumen5-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lumen5/well-known/lumen5-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lumen5-well-known.yml
- group: other
  href: https://artifacts.apis.io/lumen5/hosts/lumen5-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lumen5-hosts.yml
- group: other
  href: https://artifacts.apis.io/lumen5/vendors/lumen5-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lumen5-vendors.yml
- group: build
  href: https://artifacts.apis.io/lumen5/packages/lumen5-packages.yml
  title: ''
  type: SDKs
  url: packages/lumen5-packages.yml
- group: build
  href: https://artifacts.apis.io/lumen5/packages/lumen5-packages.yml
  title: ''
  type: Packages
  url: packages/lumen5-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://lumen5.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumen5.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://help.lumen5.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lumen5.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumen5.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://lumen5.com/pricing/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lumen5.com/developers/api/
- group: docs
  title: ''
  type: Documentation
  url: https://help.lumen5.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lumen5
- group: auth
  href: https://artifacts.apis.io/lumen5/authentication/lumen5-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lumen5-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lumen5/security/lumen5-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumen5-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumen5.com/
coverage:
  checked: '2026-10-27'
  detail: Lumen5 developer pages load content via JavaScript, preventing machine-readable discovery.
  evidence:
  - status: 200
    url: https://lumen5.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Lumen5 is an AI-powered video creation platform that enables anyone, without training or experience, to easily create engaging video content within minutes. It automates the video production process, helping marketers, creators, and businesses produce videos at scale for social media, ads, and internal communications.
image: https://cdn.lumen5.com/lumen5-site-images/og-image.png
jsonld:
- class_count: 25
  name: Lumen5 Context
  property_count: 36
  slug: lumen5-context
layout: provider
modified: '2026-10-26'
name: Lumen5
nav: Providers
network: true
overview: 'Lumen5 publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Video Creation API. Tagged areas include Company.


  The Lumen5 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lumen5''s developer surface includes support, pricing, documentation, authentication, and 22 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Lumen5 API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: lumen5-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 19.7
    contract_governance: 19.7
    contract_quality: 46.1
    developer_ergonomics: 31.0
    discoverability: 39.3
    operational_transparency: 10.5
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lumen5/lumen5-2026-11-03T135113.png
security:
- kind: authentication
  name: Lumen5 Authentication
  slug: lumen5-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lumen5 Domain Security
  slug: lumen5-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lumen5
tags:
- Company
website: https://lumen5.com/
---
