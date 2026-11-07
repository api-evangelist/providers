---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
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
  score: 42.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RESTful API for managing AI releases, RAG knowledge bases, fine‑tuning, transcripts, and more.
  name: Divinci AI API
  slug: divinci-ai-api
- baseURL: https://api.divinci.ai/api/v1
  baseurl_source: declared
  description: RESTful API for managing AI releases, RAG knowledge bases, fine-tuning, transcripts, and more. Authenticate with an API key via the `X-Api-Key` header or a Bearer token.
  name: Divinci AI API API
  slug: divinci-ai-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/divinci-app/rules/divinci-app-rules.yml
  title: ''
  type: Spectral
  url: rules/divinci-app-rules.yml
- group: design
  href: https://artifacts.apis.io/divinci-app/json-ld/divinci-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/divinci-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/divinci-app/vocabulary/divinci-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/divinci-app-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/divinci-app/plans/divinci-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/divinci-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/divinci-app/data-model/divinci-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/divinci-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/divinci-app/cli/divinci-app-cli.yml
  title: ''
  type: CLI
  url: cli/divinci-app-cli.yml
- group: operate
  href: https://artifacts.apis.io/divinci-app/changelog/divinci-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/divinci-app-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://divinci.ai/security/
- group: auth
  href: https://artifacts.apis.io/divinci-app/authentication/divinci-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/divinci-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/divinci-app/errors/divinci-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/divinci-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/divinci-app/conformance/divinci-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/divinci-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/divinci-app/llms/divinci-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/divinci-app-llms.txt
- group: other
  href: https://artifacts.apis.io/divinci-app/a2a/divinci-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/divinci-app-a2a.yml
- group: auth
  href: https://artifacts.apis.io/divinci-app/well-known/divinci-app-staging-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/divinci-app-staging-security.txt
- group: auth
  href: https://artifacts.apis.io/divinci-app/well-known/divinci-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/divinci-app-security.txt
- group: auth
  href: https://artifacts.apis.io/divinci-app/well-known/divinci-app-divinci-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/divinci-app-divinci-security.txt
- group: auth
  href: https://artifacts.apis.io/divinci-app/well-known/divinci-app-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/divinci-app-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/divinci-app/well-known/divinci-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/divinci-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/divinci-app/hosts/divinci-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/divinci-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/divinci-app/vendors/divinci-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/divinci-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/divinci-app/packages/divinci-app-packages.yml
  title: ''
  type: SDKs
  url: packages/divinci-app-packages.yml
- group: build
  href: https://artifacts.apis.io/divinci-app/packages/divinci-app-packages.yml
  title: ''
  type: Packages
  url: packages/divinci-app-packages.yml
- group: auth
  href: https://artifacts.apis.io/divinci-app/security/divinci-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/divinci-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/divinci-app/security/divinci-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divinci-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://divinci.app/
- group: docs
  title: ''
  type: Documentation
  url: https://divinci.ai/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://divinci.ai/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://divinci.ai/roadmap/
- group: company
  title: ''
  type: Blog
  url: https://divinci.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://divinci.ai/support/
created: '2026-11-06'
description: Divinci offers an AI platform that transforms websites into custom AI assistants. Users can paste a link and instantly receive a tailored AI that reflects their content and branding, complete with logo integration. The service is free to start, requires no credit card, and aims to provide quick, personalized AI experiences for businesses and individuals.
image: https://divinci.app/images/davinci-painter-robot-800w.webp
json_schemas:
- name: AudioTranscript
  property_count: 10
  slug: divinci-app-audio-transcript
- name: FineTuneJob
  property_count: 9
  slug: divinci-app-fine-tune-job
- name: HtmlPage
  property_count: 8
  slug: divinci-app-html-page
- name: RagFile
  property_count: 10
  slug: divinci-app-rag-file
- name: Release
  property_count: 11
  slug: divinci-app-release
- name: Thread
  property_count: 7
  slug: divinci-app-thread
jsonld:
- class_count: 17
  name: Divinci App Context
  property_count: 70
  slug: divinci-app-context
layout: provider
modified: '2026-11-06'
name: Divinci
nav: Providers
network: true
overview: 'Divinci publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API API, and 1 more. Tagged areas include Website Integration, Conversational AI, No-Code, Customer Service, and phone integration.


  The Divinci catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Divinci''s developer surface includes CLI, changelog, authentication, documentation, pricing, engineering blog, support, and 23 more developer resources.'
plans:
- name: Divinci App Plans Pricing
  plan_count: 4
  slug: divinci-app-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Divinci API Rules
  rule_count: 61
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 7
  slug: divinci-app-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 49.5
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Divinci App Authentication
  slug: divinci-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Divinci App Domain Security
  slug: divinci-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Divinci App Vulnerability Disclosure
  slug: divinci-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: divinci-app
tags:
- Website Integration
- Conversational AI
- No-Code
- Customer Service
- phone integration
website: https://divinci.app/
---
