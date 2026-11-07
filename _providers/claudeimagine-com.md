---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Claude Imagine API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Claude Imagine API
  slug: claudeimagine-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/claudeimagine-com/plans/claudeimagine-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claudeimagine-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/claudeimagine-com/rules/claudeimagine-com-rules.yml
  title: ''
  type: Spectral
  url: rules/claudeimagine-com-rules.yml
- group: design
  href: https://artifacts.apis.io/claudeimagine-com/json-ld/claudeimagine-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claudeimagine-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/claudeimagine-com/vocabulary/claudeimagine-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claudeimagine-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claudeimagine-com/data-model/claudeimagine-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claudeimagine-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/claudeimagine-com/authentication/claudeimagine-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/claudeimagine-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/claudeimagine-com/conformance/claudeimagine-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claudeimagine-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claudeimagine-com/llms/claudeimagine-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claudeimagine-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/claudeimagine-com/well-known/claudeimagine-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claudeimagine-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/claudeimagine-com/hosts/claudeimagine-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claudeimagine-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claudeimagine-com/vendors/claudeimagine-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claudeimagine-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claudeimagine.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claudeimagine.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://claudeimagine.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://claudeimagine.com/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://claudeimagine.com/docs/mcp
- group: auth
  href: https://artifacts.apis.io/claudeimagine-com/security/claudeimagine-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claudeimagine-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claudeimagine.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found despite probing documented API hosts.
  evidence:
  - status: error
    url: https://api.claudeimagine.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Claude Imagine provides AI image generation integrated with Claude via a web interface and MCP, offering subscription plans for creators to generate images and videos. Not affiliated with Anthropic, it adds visual capabilities to Claude workflows.
image: https://claudeimagine.com/preview.png
json_schemas:
- name: PostApiV1ImagesGenerationsRequest
  property_count: 3
  slug: claudeimagine-com-post-api-v1-images-generations-request
jsonld:
- class_count: 1
  name: Claudeimagine Com Context
  property_count: 3
  slug: claudeimagine-com-context
layout: provider
modified: '2026-11-03'
name: Claude Imagine
nav: Providers
network: true
overview: 'Claude Imagine is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Image Generation, Video Generation, and Credit-Pricing.


  The Claude Imagine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Claude Imagine''s developer surface includes authentication, pricing, documentation, getting-started guide, and 14 more developer resources.'
plans:
- name: Claudeimagine Com Plans Pricing
  plan_count: 3
  slug: claudeimagine-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Claude Imagine API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: claudeimagine-com-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Claudeimagine Com Authentication
  slug: claudeimagine-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Claudeimagine Com Domain Security
  slug: claudeimagine-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claudeimagine-com
tags:
- AI Image Generation
- Video Generation
- Credit-Pricing
website: https://claudeimagine.com/
---
