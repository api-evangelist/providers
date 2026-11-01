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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Runcrate provides OpenAI‑compatible inference and GPU infrastructure APIs.
  name: Runcrate API
  slug: runcrate-api
- baseURL: https://api.runcrate.ai/v1
  baseurl_source: declared
  description: 'Runcrate exposes two API surfaces. The inference API at `https://api.runcrate.ai/v1` is OpenAI-compatible: it accepts the standard OpenAI SDK with the base URL changed. The infrastructure API at `http'
  name: Runcrate API API
  slug: runcrate-api-api
artifact_total: 14
asyncapis:
- description: ''
  name: Runcrate Webhooks
  slug: runcrate-webhooks
common:
- group: design
  href: https://artifacts.apis.io/runcrate/rules/runcrate-rules.yml
  title: ''
  type: Spectral
  url: rules/runcrate-rules.yml
- group: design
  href: https://artifacts.apis.io/runcrate/json-ld/runcrate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/runcrate-context.jsonld
- group: design
  href: https://artifacts.apis.io/runcrate/vocabulary/runcrate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/runcrate-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/runcrate/asyncapi/runcrate-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/runcrate-webhooks.yml
- group: design
  href: https://artifacts.apis.io/runcrate/data-model/runcrate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/runcrate-data-model.yml
- group: auth
  href: https://artifacts.apis.io/runcrate/security/runcrate-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/runcrate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/runcrate/authentication/runcrate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/runcrate-authentication.yml
- group: design
  href: https://artifacts.apis.io/runcrate/errors/runcrate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/runcrate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/runcrate/conformance/runcrate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/runcrate-conformance.yml
- group: agent
  href: https://artifacts.apis.io/runcrate/llms/runcrate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/runcrate-llms.txt
- group: auth
  href: https://artifacts.apis.io/runcrate/well-known/runcrate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/runcrate-security.txt
- group: auth
  href: https://artifacts.apis.io/runcrate/well-known/runcrate-runcrate-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/runcrate-runcrate-security.txt
- group: agent
  href: https://artifacts.apis.io/runcrate/well-known/runcrate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/runcrate-well-known.yml
- group: other
  href: https://artifacts.apis.io/runcrate/hosts/runcrate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runcrate-hosts.yml
- group: other
  href: https://artifacts.apis.io/runcrate/vendors/runcrate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runcrate-vendors.yml
- group: auth
  href: https://artifacts.apis.io/runcrate/security/runcrate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/runcrate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/runcrate/security/runcrate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runcrate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.runcrate.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.runcrate.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.runcrate.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.runcrate.ai/docs/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.runcrate.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.runcrate.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.runcrate.ai/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.runcrate.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.runcrate.ai/privacy
created: '2026-10-21'
description: Runcrate provides GPU-powered inference and compute platforms for AI agents. It offers OpenAI‑compatible APIs for large language models, dedicated GPU instances, storage volumes, and tools for training, fine‑tuning, and retrieval‑augmented generation. Customers can provision compute on demand, monitor usage, and integrate with popular frameworks via a unified API, enabling scalable, high‑performance AI workloads.
image: https://www.runcrate.ai/runcrate_branding/runcrate_banner.png
json_schemas:
- name: ChatCompletionRequest
  property_count: 12
  slug: runcrate-chat-completion-request
- name: InstanceCreateRequest
  property_count: 15
  slug: runcrate-instance-create-request
- name: Instance
  property_count: 14
  slug: runcrate-instance
- name: InstanceType
  property_count: 9
  slug: runcrate-instance-type
- name: StorageVolume
  property_count: 11
  slug: runcrate-storage-volume
- name: TranscriptionResponse
  property_count: 4
  slug: runcrate-transcription-response
jsonld:
- class_count: 34
  name: Runcrate Context
  property_count: 95
  slug: runcrate-context
layout: provider
modified: '2026-10-21'
name: Runcrate
nav: Providers
network: true
overview: 'Runcrate publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Artificial Intelligence, GPU, Inference, Compute, and Platform.


  The Runcrate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Runcrate''s developer surface includes authentication, documentation, getting-started guide, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Runcrate API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: runcrate-rules
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 70.8
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
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
- kind: authentication
  name: Runcrate Authentication
  slug: runcrate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Runcrate Domain Security
  slug: runcrate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Runcrate Vulnerability Disclosure
  slug: runcrate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: runcrate
tags:
- Artificial Intelligence
- GPU
- Inference
- Compute
- Platform
website: https://www.runcrate.ai/
---
