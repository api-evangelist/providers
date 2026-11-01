---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: RelayGPU provides a unified AI compute API that routes workloads across direct and decentralized GPU infrastructure.
  name: RelayGPU API
  slug: relaygpu-api
- description: 'relaygpu-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: relaygpu-com API
  slug: relaygpu-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/relaygpu-com/rules/relaygpu-com-rules.yml
  title: ''
  type: Spectral
  url: rules/relaygpu-com-rules.yml
- group: design
  href: https://artifacts.apis.io/relaygpu-com/json-ld/relaygpu-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/relaygpu-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/relaygpu-com/vocabulary/relaygpu-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/relaygpu-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/relaygpu-com/data-model/relaygpu-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/relaygpu-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://relaygpu.com/legals/privacy
- group: auth
  href: https://artifacts.apis.io/relaygpu-com/authentication/relaygpu-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/relaygpu-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/relaygpu-com/errors/relaygpu-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/relaygpu-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/relaygpu-com/conformance/relaygpu-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/relaygpu-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/relaygpu-com/llms/relaygpu-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/relaygpu-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/relaygpu-com/well-known/relaygpu-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/relaygpu-com-security.txt
- group: agent
  href: https://artifacts.apis.io/relaygpu-com/well-known/relaygpu-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/relaygpu-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/relaygpu-com/hosts/relaygpu-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/relaygpu-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/relaygpu-com/vendors/relaygpu-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/relaygpu-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/relaygpu-com/security/relaygpu-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/relaygpu-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/relaygpu-com/security/relaygpu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relaygpu-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://relaygpu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.relaygpu.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.relaygpu.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://relaygpu.com/explore
- group: operate
  title: ''
  type: Support
  url: https://dashboard.relaygpu.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opengpunetwork
- group: commercial
  title: ''
  type: Pricing
  url: https://relaygpu.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relaygpu.com/legals/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relaygpu.com/legals/privacy
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint https://dashboard.relaygpu.com/mcp returns an HTML login page, indicating authentication is required.
  evidence:
  - status: 200
    url: https://dashboard.relaygpu.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: RelayGPU provides a unified AI compute API that routes workloads across direct and decentralized GPU infrastructure. It supports Chat, Image, Speech, and Multimodal models via an OpenAI‑compatible endpoint, offering cost optimization, reliability, and compliance features such as EU‑Sovereign tier. Founded in 2024, the service targets developers building generative AI applications.
image: https://relaygpu.com/logo.svg
json_schemas:
- name: PostApiOllamaChatRequest
  property_count: 2
  slug: relaygpu-com-post-api-ollama-chat-request
jsonld:
- class_count: 1
  name: Relaygpu Com Context
  property_count: 2
  slug: relaygpu-com-context
layout: provider
modified: '2026-10-31'
name: relaygpu-com
nav: Providers
network: true
overview: 'relaygpu-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Compute, GPU, and Cloud.


  The relaygpu-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  relaygpu-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 18 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: relaygpu-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: relaygpu-com-rules
scopes:
- name: Relaygpu Com Scopes
  scope_count: 0
  slug: relaygpu-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.1
    catalog_earned_first_party: 0.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 45.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Relaygpu Com Authentication
  slug: relaygpu-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Relaygpu Com Domain Security
  slug: relaygpu-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Relaygpu Com Vulnerability Disclosure
  slug: relaygpu-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: relaygpu-com
tags:
- Company
- AI
- Compute
- GPU
- Cloud
- API
website: https://relaygpu.com/
---
