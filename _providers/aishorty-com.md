---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Shorty API provides endpoints for usage, articles, transcriptions, jobs, subtitles, summaries, and webhooks.
  name: Shorty API
  slug: shorty-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aishorty-com/plans/aishorty-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aishorty-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://aishorty.com/terms
- group: design
  href: https://artifacts.apis.io/aishorty-com/conformance/aishorty-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aishorty-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aishorty-com/llms/aishorty-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aishorty-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/aishorty-com/well-known/aishorty-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aishorty-com-security.txt
- group: auth
  href: https://artifacts.apis.io/aishorty-com/well-known/aishorty-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aishorty-com-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/aishorty-com/well-known/aishorty-com-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aishorty-com-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/aishorty-com/well-known/aishorty-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aishorty-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aishorty-com/hosts/aishorty-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aishorty-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aishorty-com/vendors/aishorty-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aishorty-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://aishorty.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aishorty.com/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@aishorty/sdk
- group: start
  title: ''
  type: Login
  url: https://aishorty.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://aishorty.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://aishorty.com/agent-setup
- group: docs
  title: ''
  type: APIReference
  url: https://aishorty.com/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/aishorty-com/security/aishorty-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aishorty-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aishorty-com/security/aishorty-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aishorty-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aishorty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aishorty.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://aishorty.com/premium
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aishorty.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aishorty.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://aishorty.com/openapi.json
  - status: null
    url: https://dev.aishorty.com/openapi.json
  - status: 401
    url: https://aishorty.com/api/mcp
  - status: 401
    url: https://dev.aishorty.com/api/mcp
  - status: 200
    url: https://aishorty.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Shorty AI provides a suite of AI-powered tools for summarizing YouTube videos, converting files, compressing video, transcribing audio, and generating subtitles. Their platform offers a REST API and SDKs for developers to integrate summarization, transcription, and subtitle generation into applications, with support for webhooks, usage tracking, and AI agent integration.
image: https://aishorty.com/og/youtube-video-summarizer
layout: provider
modified: '2026-11-01'
name: Shorty AI
nav: Providers
network: true
overview: 'Shorty AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Summarization, Video, Transcription, and Subtitles.


  Shorty AI''s developer surface includes support, changelog, getting-started guide, API reference, documentation, pricing, and 18 more developer resources.'
plans:
- name: Aishorty Com Plans Pricing
  plan_count: 3
  slug: aishorty-com-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 37.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aishorty Com Domain Security
  slug: aishorty-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aishorty Com Vulnerability Disclosure
  slug: aishorty-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aishorty-com
tags:
- Artificial Intelligence
- Summarization
- Video
- Transcription
- Subtitles
website: https://aishorty.com/
---
