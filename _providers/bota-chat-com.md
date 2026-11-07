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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Bota's automated WhatsApp and phone reservation handling for rent‑a‑car businesses.
  name: Bota Chat API
  slug: bota-chat-api
- baseURL: https://mcp.bota-chat.com
  baseurl_source: declared
  description: 'Bota API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bota API
  slug: bota-chat-com-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/bota-chat-com/plans/bota-chat-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bota-chat-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bota-chat-com/rules/bota-chat-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bota-chat-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bota-chat-com/json-ld/bota-chat-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bota-chat-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bota-chat-com/vocabulary/bota-chat-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bota-chat-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bota-chat-com/data-model/bota-chat-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bota-chat-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bota-chat-com/conformance/bota-chat-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bota-chat-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bota-chat-com/llms/bota-chat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bota-chat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bota-chat-com/hosts/bota-chat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bota-chat-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bota-chat.com/en/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.bota-chat.com/web-auth/es/signup?product=bota
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bota-chat.com/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bota-chat.com/en/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bota-chat.com/en/developers
- group: auth
  href: https://artifacts.apis.io/bota-chat-com/security/bota-chat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bota-chat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bota-chat.com/
coverage:
  checked: '2026-11-03'
  detail: The developer portal provides HTML documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.bota-chat.com/en/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Bota provides automated WhatsApp and phone reservation handling for rent‑a‑car businesses, operating 24/7 and integrating with reservation systems. It enables customers to inquire, quote, and confirm bookings via chat or call, streamlining the rental process.
image: https://www.bota-chat.com/es/opengraph-image
json_schemas:
- name: PostApiPublicDevelopersSandboxIdVerifyRequest
  property_count: 1
  slug: bota-chat-com-post-api-public-developers-sandbox-id-verify-request
- name: PostApiPublicDevelopersSandboxRequest
  property_count: 3
  slug: bota-chat-com-post-api-public-developers-sandbox-request
- name: PostMcpRequest
  property_count: 3
  slug: bota-chat-com-post-mcp-request
jsonld:
- class_count: 3
  name: Bota Chat Com Context
  property_count: 7
  slug: bota-chat-com-context
layout: provider
modified: '2026-11-03'
name: Bota
nav: Providers
network: true
overview: 'Bota is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Car Rental, AI Automation, WhatsApp, voice-calls, and Booking Engine.


  The Bota catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bota''s developer surface includes signup flow, pricing, and 13 more developer resources.'
plans:
- name: Bota Chat Com Plans Pricing
  plan_count: 4
  slug: bota-chat-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Bota API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: bota-chat-com-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bota Chat Com Domain Security
  slug: bota-chat-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bota-chat-com
tags:
- Car Rental
- AI Automation
- WhatsApp
- voice-calls
- Booking Engine
- Conversational AI
- Omnichannel
website: https://bota-chat.com/
---
