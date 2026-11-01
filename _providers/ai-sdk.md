---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Google Cloud AI provides a comprehensive suite of artificial intelligence services and tools, including generative models, vision, language, and agent platforms.
  name: Google AI SDK
  slug: google-ai-sdk
- description: 'Google API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Google API
  slug: ai-sdk-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/ai-sdk/rules/ai-sdk-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-sdk-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-sdk/json-ld/ai-sdk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ai-sdk-context.jsonld
- group: design
  href: https://artifacts.apis.io/ai-sdk/vocabulary/ai-sdk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-sdk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ai-sdk/data-model/ai-sdk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-sdk-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ai-sdk/changelog/ai-sdk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ai-sdk-changelog.yml
- group: design
  href: https://artifacts.apis.io/ai-sdk/conformance/ai-sdk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-sdk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-sdk/well-known/ai-sdk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-sdk-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai-sdk/hosts/ai-sdk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-sdk-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: auth
  title: ''
  type: Security
  url: https://accounts.google.com/ServiceLogin?hl=en-US&continue=https://myaccount.google.com/intro/security
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1356324702:1792442243144326
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloud.google.com/docs/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.android.com/ai-in-android
- group: auth
  href: https://artifacts.apis.io/ai-sdk/security/ai-sdk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-sdk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ai-sdk/security/ai-sdk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-sdk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/ai
coverage:
  checked: '2026-10-19'
  detail: Documentation at https://cloud.google.com/ai/docs/reference/rest provides only HTML pages with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://cloud.google.com/ai/docs/reference/rest
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Google Cloud AI provides a comprehensive suite of artificial intelligence services and tools, including generative models, vision, language, and agent platforms. The AI SDK enables developers to integrate these capabilities into applications, offering scalable, secure, and enterprise‑ready solutions across Google Cloud. It supports model selection, fine‑tuning, and deployment, with robust governance, cost controls, and multi‑modal capabilities, empowering businesses to build intelligent, automated workflows.
image: https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png
json_schemas:
- name: PostV1BetaModelsGemini35FlashGeneratecontentRequest
  property_count: 1
  slug: ai-sdk-post-v1-beta-models-gemini35-flash-generatecontent-request
jsonld:
- class_count: 1
  name: Ai Sdk Context
  property_count: 1
  slug: ai-sdk-context
layout: provider
modified: '2026-10-19'
name: Google
nav: Providers
network: true
overview: 'Google is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cloud, Machine Learning, and SDK.


  The Google catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google''s developer surface includes changelog, sandbox, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Ai Sdk Rate Limits
  slug: ai-sdk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Google API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ai-sdk-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Sdk Domain Security
  slug: ai-sdk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ai Sdk Vulnerability Disclosure
  slug: ai-sdk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ai-sdk
tags:
- Company
- Artificial Intelligence
- Cloud
- Machine Learning
- SDK
website: https://cloud.google.com/ai
---
