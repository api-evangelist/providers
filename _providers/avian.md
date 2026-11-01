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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Avian provides an OpenAI‑compatible inference API. All endpoints are served from a single base URL.
  name: Avian API
  slug: avian-api-2
- description: 'Avian.io API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Avian.io API
  slug: avian-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/avian/plans/avian-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avian-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avian/rules/avian-rules.yml
  title: ''
  type: Spectral
  url: rules/avian-rules.yml
- group: design
  href: https://artifacts.apis.io/avian/json-ld/avian-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avian-context.jsonld
- group: design
  href: https://artifacts.apis.io/avian/vocabulary/avian-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avian-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avian/data-model/avian-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avian-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://avian.io/security/
- group: design
  href: https://artifacts.apis.io/avian/conformance/avian-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avian-conformance.yml
- group: other
  href: https://artifacts.apis.io/avian/hosts/avian-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avian-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avian.io/terms/
- group: auth
  title: ''
  type: Security
  url: https://avian.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avian.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://avian.io/pricing
- group: start
  title: ''
  type: Login
  url: https://avian.io/accounts/login/
- group: docs
  title: ''
  type: Documentation
  url: https://avian.io/docs/
- group: auth
  href: https://artifacts.apis.io/avian/security/avian-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avian-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/avian/security/avian-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avian-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avian/security/avian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avian.io/
coverage:
  checked: '2026-10-19'
  detail: API documentation is rendered via JavaScript, preventing automated spec discovery.
  evidence:
  - status: 200
    url: https://avian.io/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Avian.io provides a fast, affordable AI inference API platform that enables developers to integrate state‑of‑the‑art machine‑learning models into their applications via simple REST endpoints. The service offers scalable compute, low latency, and flexible pricing, supporting a range of use‑cases from image classification to natural language processing. Avian.io aims to democratize access to powerful AI capabilities for startups and enterprises alike.
image: https://i.imgur.com/tttuyis.png
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: avian-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 2
  slug: avian-post-v1-chat-completions-response
jsonld:
- class_count: 2
  name: Avian Context
  property_count: 4
  slug: avian-context
layout: provider
modified: '2026-10-19'
name: Avian.io
nav: Providers
network: true
overview: 'Avian.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Inference, Compute, OpenAI Compatibility, GPU Compute, and Enterprise Security.


  The Avian.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Avian.io''s developer surface includes pricing, documentation, and 16 more developer resources.'
plans:
- name: Avian Plans Pricing
  plan_count: 10
  slug: avian-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Avian.io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: avian-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 20.4
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avian Domain Security
  slug: avian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avian Vulnerability Disclosure
  slug: avian-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Avian Trust Center
  slug: avian-trust-center
  summary_line: SOC 2, GDPR
slug: avian
tags:
- Inference
- Compute
- OpenAI Compatibility
- GPU Compute
- Enterprise Security
website: https://avian.io/
---
