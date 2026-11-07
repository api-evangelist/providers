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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Audio/video AI assistant API
  name: BibiGPT API
  slug: bibigpt-api
- baseURL: https://api.bibigpt.co/api
  baseurl_source: declared
  description: 音视频 AI 学习助理的开放 API，加速音视频内容的信息提取，借助 AI 直接采取行动。
  name: BibiGPT OpenAPI 规范 API
  slug: bibigpt-openapi-api
artifact_total: 6
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://bibigpt.co/pricing
- group: design
  href: https://artifacts.apis.io/bibigpt-co/rules/bibigpt-co-rules.yml
  title: ''
  type: Spectral
  url: rules/bibigpt-co-rules.yml
- group: design
  href: https://artifacts.apis.io/bibigpt-co/json-ld/bibigpt-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bibigpt-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/bibigpt-co/vocabulary/bibigpt-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bibigpt-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bibigpt-co/conformance/bibigpt-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bibigpt-co-conformance.yml
- group: design
  href: https://artifacts.apis.io/bibigpt-co/data-model/bibigpt-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bibigpt-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/bibigpt-co/conventions/bibigpt-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bibigpt-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/bibigpt-co/errors/bibigpt-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bibigpt-co-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bibigpt-co/llms/bibigpt-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bibigpt-co-llms.txt
- group: other
  href: https://artifacts.apis.io/bibigpt-co/a2a/bibigpt-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bibigpt-co-a2a.yml
- group: auth
  href: https://artifacts.apis.io/bibigpt-co/well-known/bibigpt-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bibigpt-co-security.txt
- group: auth
  href: https://artifacts.apis.io/bibigpt-co/well-known/bibigpt-co-chatimg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bibigpt-co-chatimg-security.txt
- group: auth
  href: https://artifacts.apis.io/bibigpt-co/well-known/bibigpt-co-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bibigpt-co-api-security.txt
- group: agent
  href: https://artifacts.apis.io/bibigpt-co/well-known/bibigpt-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bibigpt-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/bibigpt-co/hosts/bibigpt-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bibigpt-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/bibigpt-co/vendors/bibigpt-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bibigpt-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bibigpt.co/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://bibigpt.co/.well-known/security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bibigpt.co/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://bibigpt.co/user/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JimmyLv
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bibigpt.co/getting-started/bibigpt-menu-guide
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bibigpt.co/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://bibigpt.co/blog/category/changelog
- group: company
  title: ''
  type: Blog
  url: https://bibigpt.co/blog/posts
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bibigpt.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bibigpt.co/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/bibigpt-co/security/bibigpt-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bibigpt-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bibigpt-co/security/bibigpt-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bibigpt-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bibigpt.co/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://bibigpt.co/swagger.json
  - status: null
    url: https://api.bibigpt.co/swagger.json
  - status: null
    url: https://docs.bibigpt.co/mcp
  - status: 401
    url: https://bibigpt.co/api/mcp
  - status: 401
    url: https://api.bibigpt.co/api/mcp
  - status: 200
    url: https://bibigpt.co/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BibiGPT is an AI‑powered audio/video summarizer and knowledge assistant that transforms YouTube, Bilibili, podcasts, meetings, and local media into searchable summaries, transcripts, mindmaps, and chat. It offers free usage, supports multiple languages, and provides a web interface across platforms.
image: https://bibigpt.co/og-image.png?v=2023-04-26
jsonld:
- class_count: 5
  name: Bibigpt Co Context
  property_count: 3
  slug: bibigpt-co-context
layout: provider
modified: '2026-11-02'
name: BibiGPT
nav: Providers
network: true
overview: 'BibiGPT publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including OpenAPI 规范 API, and 1 more. Tagged areas include Artificial Intelligence, VideoSummarization, Multilingual, Free, and Web App.


  The BibiGPT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BibiGPT''s developer surface includes pricing, getting-started guide, changelog, engineering blog, documentation, API reference, and 24 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: BibiGPT API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: bibigpt-co-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 34.7
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bibigpt Co Domain Security
  slug: bibigpt-co-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bibigpt Co Vulnerability Disclosure
  slug: bibigpt-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bibigpt-co
tags:
- Artificial Intelligence
- VideoSummarization
- Multilingual
- Free
- Web App
website: https://bibigpt.co/
---
