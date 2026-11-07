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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AIGROW API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AIGROW API
  slug: aigrow-gg-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/aigrow-gg/rules/aigrow-gg-rules.yml
  title: ''
  type: Spectral
  url: rules/aigrow-gg-rules.yml
- group: design
  href: https://artifacts.apis.io/aigrow-gg/json-ld/aigrow-gg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aigrow-gg-context.jsonld
- group: design
  href: https://artifacts.apis.io/aigrow-gg/vocabulary/aigrow-gg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aigrow-gg-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aigrow-gg/data-model/aigrow-gg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aigrow-gg-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aigrow.gg/security
- group: design
  href: https://artifacts.apis.io/aigrow-gg/conformance/aigrow-gg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aigrow-gg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aigrow-gg/llms/aigrow-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aigrow-gg-llms.txt
- group: auth
  href: https://artifacts.apis.io/aigrow-gg/well-known/aigrow-gg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aigrow-gg-security.txt
- group: agent
  href: https://artifacts.apis.io/aigrow-gg/well-known/aigrow-gg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aigrow-gg-well-known.yml
- group: other
  href: https://artifacts.apis.io/aigrow-gg/hosts/aigrow-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aigrow-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/aigrow-gg/vendors/aigrow-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aigrow-gg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aigrow.gg/terms
- group: operate
  title: ''
  type: Support
  url: https://aigrow.gg/help
- group: operate
  title: ''
  type: StatusPage
  url: https://aigrow.gg/status
- group: auth
  title: ''
  type: Security
  url: https://aigrow.gg/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aigrow.gg/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://aigrow.gg/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://aigrow.gg/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://aigrow.gg/google-business-profile-setup
- group: auth
  href: https://artifacts.apis.io/aigrow-gg/security/aigrow-gg-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aigrow-gg-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aigrow-gg/security/aigrow-gg-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aigrow-gg-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aigrow-gg/security/aigrow-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aigrow-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aigrow.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://aigrow.gg/get-started
- group: company
  title: ''
  type: Blog
  url: https://aigrow.gg/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://aigrow.gg/plans
- group: start
  title: ''
  type: SignUp
  url: https://aigrow.gg/auth/login
coverage:
  checked: '2026-11-01'
  detail: Provider documentation is HTML only and OpenAPI endpoints return error 526, so no machine‑readable spec is available.
  evidence:
  - status: 526
    url: https://api.aigrow.gg/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AIGROW provides AI‑powered growth solutions for businesses, offering services such as AI‑generated naming, automated work processes, AI audits, and AI‑driven visibility tools. Their platform includes AI operations, local fixes, visibility checks, press‑release distribution, and ready‑made AI solutions, all delivered through a subscription model. The company aims to help clients leverage generative AI to enhance marketing, SEO, and operational efficiency across various industries.
image: https://aigrow.gg/og/default.jpg?v=3
json_schemas:
- name: PostChatCompletionsRequest
  property_count: 2
  slug: aigrow-gg-post-chat-completions-request
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: aigrow-gg-post-v1-chat-completions-request
- name: PostV1MessagesRequest
  property_count: 3
  slug: aigrow-gg-post-v1-messages-request
jsonld:
- class_count: 3
  name: Aigrow Gg Context
  property_count: 3
  slug: aigrow-gg-context
layout: provider
modified: '2026-11-01'
name: AIGROW
nav: Providers
network: true
overview: 'AIGROW is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, SEO, Automation, and Growth.


  The AIGROW catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIGROW''s developer surface includes support, changelog, getting-started guide, documentation, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AIGROW API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aigrow-gg-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 20.1
    developer_ergonomics: 14.3
    discoverability: 58.0
    operational_transparency: 21.1
  previous_composite: 40.3
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
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aigrow Gg Domain Security
  slug: aigrow-gg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aigrow Gg Vulnerability Disclosure
  slug: aigrow-gg-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aigrow Gg Trust Center
  slug: aigrow-gg-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: aigrow-gg
tags:
- Artificial Intelligence
- Marketing
- SEO
- Automation
- Growth
- Company
website: https://aigrow.gg/
---
