---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read the complete documentation for our REST API, Email to/from SMS, Kannel API, SMPP and HLR-lookup.
  name: GatewayAPI REST API
  slug: gatewayapi-rest-api
- baseURL: https://messaging.gatewayapi.com
  baseurl_source: declared
  description: 'GatewayAPI API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: GatewayAPI API
  slug: gatewayapi-api
artifact_total: 13
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gatewayapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://messaging.gatewayapi.com/redoc
- group: commercial
  href: https://artifacts.apis.io/gatewayapi/plans/gatewayapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gatewayapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gatewayapi/rules/gatewayapi-rules.yml
  title: ''
  type: Spectral
  url: rules/gatewayapi-rules.yml
- group: design
  href: https://artifacts.apis.io/gatewayapi/json-ld/gatewayapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gatewayapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/gatewayapi/vocabulary/gatewayapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gatewayapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gatewayapi/data-model/gatewayapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gatewayapi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/gatewayapi/authentication/gatewayapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gatewayapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/gatewayapi/conformance/gatewayapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gatewayapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gatewayapi/llms/gatewayapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gatewayapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/gatewayapi/well-known/gatewayapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gatewayapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/gatewayapi/hosts/gatewayapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatewayapi-hosts.yml
- group: build
  href: https://artifacts.apis.io/gatewayapi/packages/gatewayapi-packages.yml
  title: ''
  type: SDKs
  url: packages/gatewayapi-packages.yml
- group: build
  href: https://artifacts.apis.io/gatewayapi/packages/gatewayapi-packages.yml
  title: ''
  type: Packages
  url: packages/gatewayapi-packages.yml
- group: auth
  href: https://artifacts.apis.io/gatewayapi/security/gatewayapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatewayapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gatewayapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gatewayapi.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://gatewayapi.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://gatewayapi.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://gatewayapi.com/help-center/introduction/
- group: start
  title: ''
  type: SignUp
  url: https://gatewayapi.com/sign-up/
coverage:
  checked: '2026-10-27'
  detail: Documentation is served as a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://gatewayapi.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: GatewayAPI provides a global messaging API platform offering SMS, RCS, and email services. It enables developers to send messages worldwide with advanced security, compliance, and EU data sovereignty options. The platform includes virtual numbers, shortcodes, keyword handling, number lookup, and detailed analytics, supporting multiple programming languages and integrations.
image: https://gatewayapi.com/SoMe-Gatewayapi.jpg
json_schemas:
- name: DeleteRestMtsmsIdIntResponse
  property_count: 8
  slug: gatewayapi-delete-rest-mtsms-id-int-response
- name: PostExampleCallbackRequest
  property_count: 11
  slug: gatewayapi-post-example-callback-request
- name: PostRestEmailRequest
  property_count: 10
  slug: gatewayapi-post-rest-email-request
- name: PostRestHlrResponse
  property_count: 10
  slug: gatewayapi-post-rest-hlr-response
- name: PostRestMtsmsRequest
  property_count: 7
  slug: gatewayapi-post-rest-mtsms-request
- name: PostRestMtsmsResponse
  property_count: 8
  slug: gatewayapi-post-rest-mtsms-response
jsonld:
- class_count: 23
  name: Gatewayapi Context
  property_count: 47
  slug: gatewayapi-context
layout: provider
modified: '2026-10-26'
name: GatewayAPI
nav: Providers
network: true
overview: 'GatewayAPI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, SMS, and Communications.


  The GatewayAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GatewayAPI''s developer surface includes API reference, authentication, documentation, pricing, engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Gatewayapi Plans Pricing
  plan_count: 2
  slug: gatewayapi-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: GatewayAPI API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: gatewayapi-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 32.9
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 34.5
    discoverability: 55.4
    operational_transparency: 26.3
  previous_composite: 33.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 14.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gatewayapi/gatewayapi-2026-11-03T132517.png
security:
- kind: authentication
  name: Gatewayapi Authentication
  slug: gatewayapi-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Gatewayapi Domain Security
  slug: gatewayapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gatewayapi
tags:
- Company
- Messaging
- SMS
- Communications
website: https://gatewayapi.com/
---
