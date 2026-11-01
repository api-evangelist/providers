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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.river.ai
  baseurl_source: declared
  description: 'River AI, Inc. API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: River AI, Inc. API
  slug: river-ai-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/river-ai/rules/river-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/river-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/river-ai/json-ld/river-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/river-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/river-ai/vocabulary/river-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/river-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/river-ai/data-model/river-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/river-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/river-ai/changelog/river-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/river-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/river-ai/authentication/river-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/river-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/river-ai/conformance/river-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/river-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/river-ai/llms/river-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/river-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/river-ai/well-known/river-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/river-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/river-ai/well-known/river-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/river-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/river-ai/hosts/river-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/river-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/river-ai/vendors/river-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/river-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://river.ai/support
- group: auth
  title: ''
  type: Security
  url: https://river.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://river.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://river.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.river.ai/quickstart
- group: auth
  href: https://artifacts.apis.io/river-ai/security/river-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/river-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/river-ai/security/river-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/river-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://river.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.river.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://river.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://river.ai/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.river.ai/
- group: other
  title: ''
  type: Coverage
  url: https://river.ai/
created: '2026-10-18'
description: River AI, Inc. provides an AI-powered platform that helps businesses automate data extraction, analysis, and decision-making processes. Leveraging advanced machine learning models, the service offers real-time insights, predictive analytics, and customizable workflows for enterprises across various industries. The company focuses on delivering scalable, secure, and easy-to-integrate solutions that enhance operational efficiency and drive innovation.
image: https://river.ai/assets/og-river-monogram.jpg
json_schemas:
- name: GetV1ModelsResponse
  property_count: 1
  slug: river-ai-get-v1-models-response
- name: PostV1ChatCompletionsRequest
  property_count: 4
  slug: river-ai-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 2
  slug: river-ai-post-v1-chat-completions-response
jsonld:
- class_count: 3
  name: River Ai Context
  property_count: 6
  slug: river-ai-context
layout: provider
modified: '2026-10-18'
name: River AI, Inc.
nav: Providers
network: true
overview: 'River AI, Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Data Analytics, and Enterprise.


  The River AI, Inc. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  River AI, Inc.''s developer surface includes changelog, authentication, support, getting-started guide, documentation, pricing, engineering blog, and 18 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: River Ai Rate Limits
  slug: river-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: River AI, Inc. API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: river-ai-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 21.4
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: River Ai Authentication
  slug: river-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: River Ai Domain Security
  slug: river-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: River Ai Vulnerability Disclosure
  slug: river-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: river-ai
tags:
- Company
- Artificial Intelligence
- Automation
- Data Analytics
- Enterprise
website: https://river.ai/
---
