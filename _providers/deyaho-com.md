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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Deyaho API as documented publicly: 34 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Deyaho API
  slug: deyaho-com-api
artifact_total: 11
asyncapis:
- description: ''
  name: Deyaho Com Webhooks
  slug: deyaho-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/deyaho-com/rules/deyaho-com-rules.yml
  title: ''
  type: Spectral
  url: rules/deyaho-com-rules.yml
- group: design
  href: https://artifacts.apis.io/deyaho-com/json-ld/deyaho-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deyaho-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/deyaho-com/vocabulary/deyaho-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deyaho-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deyaho-com/asyncapi/deyaho-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deyaho-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/deyaho-com/data-model/deyaho-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deyaho-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/deyaho-com/conformance/deyaho-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deyaho-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deyaho-com/llms/deyaho-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deyaho-com-llms.txt
- group: other
  href: https://artifacts.apis.io/deyaho-com/hosts/deyaho-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deyaho-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.deyaho.com/login
- group: auth
  href: https://artifacts.apis.io/deyaho-com/security/deyaho-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deyaho-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deyaho.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deyaho.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://deyaho.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://deyaho.com/en/blog
created: '2026-11-05'
description: Deyaho provides AI-powered voice and text agents for businesses, operating 24/7 in 30 languages. Their solutions automate customer service, sales, and management across various sectors, offering multilingual support and integration capabilities for enterprises seeking intelligent automation.
image: https://deyaho.com/og-home.jpg
json_schemas:
- name: GetApiV1AgentsCkq1Response
  property_count: 9
  slug: deyaho-com-get-api-v1-agents-ckq1-response
- name: GetApiV1ExportResponse
  property_count: 7
  slug: deyaho-com-get-api-v1-export-response
- name: GetExportResponse
  property_count: 7
  slug: deyaho-com-get-export-response
- name: PatchAgentsIdRequest
  property_count: 9
  slug: deyaho-com-patch-agents-id-request
- name: PostAgentsRequest
  property_count: 5
  slug: deyaho-com-post-agents-request
- name: PutIntegrationsWebhookRequest
  property_count: 3
  slug: deyaho-com-put-integrations-webhook-request
jsonld:
- class_count: 33
  name: Deyaho Com Context
  property_count: 44
  slug: deyaho-com-context
layout: provider
modified: '2026-11-05'
name: Deyaho
nav: Providers
network: true
overview: 'Deyaho is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Voice, Text, Multilingual, and Automation.


  The Deyaho catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Deyaho''s developer surface includes documentation, pricing, engineering blog, and 11 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Deyaho API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 3
  slug: deyaho-com-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 35.6
    contract_quality: 35.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deyaho Com Domain Security
  slug: deyaho-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deyaho-com
tags:
- Artificial Intelligence
- Voice
- Text
- Multilingual
- Automation
- Company
website: https://deyaho.com/
---
