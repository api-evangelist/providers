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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for Gram conversational AI platform, documented on Speakeasy resources.
  name: Gram API
  slug: gram-api
- baseURL: https://ai.speakeasy.com
  baseurl_source: declared
  description: 'Gram (by Speakeasy) API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Gram (by Speakeasy) API
  slug: getgram-api
artifact_total: 8
asyncapis:
- description: ''
  name: Getgram Webhooks
  slug: getgram-webhooks
common:
- group: design
  href: https://artifacts.apis.io/getgram/rules/getgram-rules.yml
  title: ''
  type: Spectral
  url: rules/getgram-rules.yml
- group: design
  href: https://artifacts.apis.io/getgram/json-ld/getgram-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getgram-context.jsonld
- group: design
  href: https://artifacts.apis.io/getgram/vocabulary/getgram-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getgram-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getgram/asyncapi/getgram-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/getgram-webhooks.yml
- group: design
  href: https://artifacts.apis.io/getgram/data-model/getgram-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getgram-data-model.yml
- group: build
  href: https://artifacts.apis.io/getgram/cli/getgram-cli.yml
  title: ''
  type: CLI
  url: cli/getgram-cli.yml
- group: auth
  href: https://artifacts.apis.io/getgram/authentication/getgram-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getgram-authentication.yml
- group: design
  href: https://artifacts.apis.io/getgram/conformance/getgram-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getgram-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getgram/llms/getgram-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getgram-llms.txt
- group: auth
  href: https://artifacts.apis.io/getgram/well-known/getgram-speakeasy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getgram-speakeasy-security.txt
- group: auth
  href: https://artifacts.apis.io/getgram/well-known/getgram-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getgram-security.txt
- group: auth
  href: https://artifacts.apis.io/getgram/well-known/getgram-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getgram-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/getgram/well-known/getgram-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getgram-app-security.txt
- group: auth
  href: https://artifacts.apis.io/getgram/well-known/getgram-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getgram-api-security.txt
- group: auth
  href: https://artifacts.apis.io/getgram/well-known/getgram-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getgram-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/getgram/well-known/getgram-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getgram-well-known.yml
- group: other
  href: https://artifacts.apis.io/getgram/hosts/getgram-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getgram-hosts.yml
- group: other
  href: https://artifacts.apis.io/getgram/vendors/getgram-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getgram-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.getgram.ai/
- group: auth
  href: https://artifacts.apis.io/getgram/security/getgram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getgram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://speakeasy.com/
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI or other machine-readable contract found at API hosts despite HTTP 200 responses.
  evidence:
  - status: 200
    url: https://api.getgram.ai/openapi.json
  - status: 200
    url: https://api.getgram.ai/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Gram (by Speakeasy) provides a conversational AI platform that enables developers to integrate natural language understanding, intent detection, and response generation into their applications. The service offers robust APIs for building chatbots, voice assistants, and automated customer support, supporting multiple languages and channels. Gram emphasizes privacy, scalability, and easy onboarding, allowing businesses to quickly prototype and deploy AI-driven communication solutions.
image: https://app.getgram.ai/og-image.png?v=1
json_schemas:
- name: PostRpcTelemetrySearchlogsRequest
  property_count: 1
  slug: getgram-post-rpc-telemetry-searchlogs-request
jsonld:
- class_count: 1
  name: Getgram Context
  property_count: 1
  slug: getgram-context
layout: provider
modified: '2026-10-17'
name: Gram (by Speakeasy)
nav: Providers
network: true
overview: 'Gram (by Speakeasy) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Conversational AI, Chatbots, and Platform.


  The Gram (by Speakeasy) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gram (by Speakeasy)''s developer surface includes CLI, authentication, documentation, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Gram (by Speakeasy) API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: getgram-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 26.8
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 24.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getgram Authentication
  slug: getgram-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Getgram Domain Security
  slug: getgram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getgram
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Chatbots
- Platform
website: https://speakeasy.com/
---
