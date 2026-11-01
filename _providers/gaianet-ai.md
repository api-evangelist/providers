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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'GaiaNet API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: GaiaNet API
  slug: gaianet-ai-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/gaianet-ai/rules/gaianet-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/gaianet-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/gaianet-ai/json-ld/gaianet-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gaianet-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/gaianet-ai/vocabulary/gaianet-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gaianet-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gaianet-ai/data-model/gaianet-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gaianet-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/gaianet-ai/authentication/gaianet-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gaianet-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/gaianet-ai/conformance/gaianet-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gaianet-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gaianet-ai/llms/gaianet-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gaianet-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/gaianet-ai/well-known/gaianet-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gaianet-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/gaianet-ai/hosts/gaianet-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gaianet-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/gaianet-ai/vendors/gaianet-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gaianet-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gaianet.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.gaianet.ai/about-gaianet/privacy-and-security
- group: company
  title: ''
  type: Blog
  url: https://www.gaianet.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gaianet.ai/getting-started-as-a-developer/contribute-to-the-open-source-project
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gaianet.ai/
- group: auth
  href: https://artifacts.apis.io/gaianet-ai/security/gaianet-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gaianet-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gaianet.ai/
coverage:
  checked: '2026-10-20'
  detail: Developer docs are rendered via Docusaurus JavaScript, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://developer.gaianet.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: 'GaiaNet is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: gaianet-ai-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 6
  slug: gaianet-ai-post-v1-chat-completions-response
- name: PostV1EmbeddingsResponse
  property_count: 4
  slug: gaianet-ai-post-v1-embeddings-response
- name: PostV1InfoResponse
  property_count: 5
  slug: gaianet-ai-post-v1-info-response
- name: PostV1ModelsResponse
  property_count: 2
  slug: gaianet-ai-post-v1-models-response
- name: PostV1RetrieveResponse
  property_count: 3
  slug: gaianet-ai-post-v1-retrieve-response
jsonld:
- class_count: 9
  name: Gaianet Ai Context
  property_count: 18
  slug: gaianet-ai-context
layout: provider
modified: '2026-10-20'
name: GaiaNet
nav: Providers
network: true
overview: 'GaiaNet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Decentralization, Artificial Intelligence, Privacy, Security, and Governance.


  The GaiaNet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GaiaNet''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: GaiaNet API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: gaianet-ai-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 35.7
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gaianet Ai Authentication
  slug: gaianet-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gaianet Ai Domain Security
  slug: gaianet-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gaianet-ai
tags:
- Decentralization
- Artificial Intelligence
- Privacy
- Security
- Governance
- Networks
website: https://gaianet.ai/
---
