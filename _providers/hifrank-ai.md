---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API for Frank customer research platform, documented in the developer guide.
  name: Frank Public API
  slug: frank-public-api
- baseURL: https://api.hifrank.ai
  baseurl_source: declared
  description: 'Frank API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Frank API
  slug: hifrank-ai-api
artifact_total: 14
asyncapis:
- description: ''
  name: Hifrank Ai Webhooks
  slug: hifrank-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/hifrank-ai/plans/hifrank-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hifrank-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hifrank-ai/rules/hifrank-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/hifrank-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/hifrank-ai/json-ld/hifrank-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hifrank-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/hifrank-ai/vocabulary/hifrank-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hifrank-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hifrank-ai/asyncapi/hifrank-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hifrank-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/hifrank-ai/data-model/hifrank-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hifrank-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hifrank-ai/authentication/hifrank-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hifrank-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/hifrank-ai/conformance/hifrank-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hifrank-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hifrank-ai/llms/hifrank-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hifrank-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/hifrank-ai/well-known/hifrank-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hifrank-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/hifrank-ai/hosts/hifrank-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hifrank-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/hifrank-ai/vendors/hifrank-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hifrank-ai-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hifrank.ai/docs/set-up-the-frank-webhook
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.hifrank.ai</dd
- group: auth
  href: https://artifacts.apis.io/hifrank-ai/security/hifrank-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hifrank-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hifrank.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.hifrank.ai/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://www.hifrank.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hifrank.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.hifrank.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hifrank.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hifrank.ai/terms-of-service
coverage:
  checked: '2026-11-05'
  detail: API documentation is rendered as HTML with no machine‑readable OpenAPI/AsyncAPI spec available.
  evidence:
  - status: 200
    url: https://www.hifrank.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Frank is an AI‑powered customer research platform that runs hundreds of moderated interviews overnight, delivering deep insights within 24 hours at up to 50× lower cost than traditional methods. Trusted by over 1,000 brands, it helps product, growth and research teams uncover customer needs at scale.
image: https://cdn.prod.website-files.com/69a70197ba94114928669352/69aac392aceab9c969a9e4f8_x%20cover.jpg
json_schemas:
- name: GetV1InterviewsIdResponse
  property_count: 9
  slug: hifrank-ai-get-v1-interviews-id-response
- name: GetV1ProductsIdResponse
  property_count: 7
  slug: hifrank-ai-get-v1-products-id-response
- name: GetV1ResearchesResearchidEmbedsTypeResponse
  property_count: 6
  slug: hifrank-ai-get-v1-researches-researchid-embeds-type-response
- name: GetV1ResearchesResearchidInterviewsResponse
  property_count: 8
  slug: hifrank-ai-get-v1-researches-researchid-interviews-response
- name: PostV1ResearchesRequest
  property_count: 5
  slug: hifrank-ai-post-v1-researches-request
- name: PutV1ProductsIdResponse
  property_count: 7
  slug: hifrank-ai-put-v1-products-id-response
jsonld:
- class_count: 21
  name: Hifrank Ai Context
  property_count: 39
  slug: hifrank-ai-context
layout: provider
modified: '2026-11-05'
name: Frank
nav: Providers
network: true
overview: 'Frank is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Research, InterviewAutomation, Market Insights, and Software-as-a-Service.


  The Frank catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Frank''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Hifrank Ai Plans Pricing
  plan_count: 1
  slug: hifrank-ai-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Frank API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: hifrank-ai-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 33.9
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hifrank Ai Authentication
  slug: hifrank-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hifrank Ai Domain Security
  slug: hifrank-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hifrank-ai
tags:
- Artificial Intelligence
- Customer Research
- InterviewAutomation
- Market Insights
- Software-as-a-Service
website: https://www.hifrank.ai
---
