---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
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
api_count: 2
apis:
- description: API for ChatterLab AI chatbot platform, providing endpoints for managing agents, data sources, and chat interactions.
  name: ChatterLab API
  slug: chatterlab-api
- description: 'ChatterLab API as documented publicly: 43 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ChatterLab API
  slug: chatterlab-ai-api
artifact_total: 13
asyncapis:
- description: ''
  name: Chatterlab Ai Webhooks
  slug: chatterlab-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/chatterlab-ai/plans/chatterlab-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chatterlab-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chatterlab-ai/rules/chatterlab-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/chatterlab-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/chatterlab-ai/json-ld/chatterlab-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chatterlab-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/chatterlab-ai/vocabulary/chatterlab-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chatterlab-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chatterlab-ai/asyncapi/chatterlab-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chatterlab-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/chatterlab-ai/data-model/chatterlab-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chatterlab-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/chatterlab-ai/conformance/chatterlab-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chatterlab-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chatterlab-ai/llms/chatterlab-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatterlab-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/chatterlab-ai/well-known/chatterlab-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatterlab-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/chatterlab-ai/hosts/chatterlab-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatterlab-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatterlab-ai/vendors/chatterlab-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatterlab-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatterlab.ai/en/privacy
- group: start
  title: ''
  type: Login
  url: https://chatterlab.ai/en/sign-in
- group: docs
  title: ''
  type: APIReference
  url: https://chatterlab.ai/en/docs/developers/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://chatterlab.ai/en/blog/how-to-price-chatbot-services-agency
- group: auth
  href: https://artifacts.apis.io/chatterlab-ai/security/chatterlab-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatterlab-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatterlab.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://chatterlab.ai/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://chatterlab.ai/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://chatterlab.ai/en/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://chatterlab.ai/api/mcp
  - status: 200
    url: https://chatterlab.ai/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Train an AI chatbot on your website, PDFs and docs. It answers from your own content, hosted in the EU, GDPR and AI Act compliant. Free plan available. ChatterLab provides a privacy‑first, European‑hosted solution for businesses to add conversational AI to their digital assets, with easy integration and customizable branding.
image: https://chatterlab.ai/en/opengraph-image
json_schemas:
- name: GetAgentsIdLeadsResponse
  property_count: 14
  slug: chatterlab-ai-get-agents-id-leads-response
- name: GetAgentsIdTicketsResponse
  property_count: 15
  slug: chatterlab-ai-get-agents-id-tickets-response
- name: PatchAgentsIdRequest
  property_count: 17
  slug: chatterlab-ai-patch-agents-id-request
- name: PostAgentsIdChatRequest
  property_count: 7
  slug: chatterlab-ai-post-agents-id-chat-request
- name: PostAgentsIdSourcesRequest
  property_count: 9
  slug: chatterlab-ai-post-agents-id-sources-request
- name: PostAgentsRequest
  property_count: 7
  slug: chatterlab-ai-post-agents-request
jsonld:
- class_count: 34
  name: Chatterlab Ai Context
  property_count: 86
  slug: chatterlab-ai-context
layout: provider
modified: '2026-11-04'
name: ChatterLab
nav: Providers
network: true
overview: 'ChatterLab is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Chatbots, GDPR, European, and Software-as-a-Service.


  The ChatterLab catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ChatterLab''s developer surface includes API reference, getting-started guide, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Chatterlab Ai Plans Pricing
  plan_count: 5
  slug: chatterlab-ai-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: ChatterLab API Rules
  rule_count: 45
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 2
  slug: chatterlab-ai-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 35.5
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
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
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chatterlab Ai Domain Security
  slug: chatterlab-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chatterlab-ai
tags:
- Artificial Intelligence
- Chatbots
- GDPR
- European
- Software-as-a-Service
- Company
website: https://chatterlab.ai/
---
