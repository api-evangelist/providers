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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Echo AI platform providing chatbot and AI agent capabilities.
  name: Echo AI API
  slug: echo-ai-api
- baseURL: https://auth.echoai.so/functions/v1/api
  baseurl_source: declared
  description: 'Echo AI API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Echo AI API
  slug: echoai-so-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/echoai-so/plans/echoai-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/echoai-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/echoai-so/rules/echoai-so-rules.yml
  title: ''
  type: Spectral
  url: rules/echoai-so-rules.yml
- group: design
  href: https://artifacts.apis.io/echoai-so/json-ld/echoai-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/echoai-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/echoai-so/vocabulary/echoai-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/echoai-so-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/echoai-so/data-model/echoai-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/echoai-so-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://echoai.so/security
- group: design
  href: https://artifacts.apis.io/echoai-so/conformance/echoai-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/echoai-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/echoai-so/llms/echoai-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/echoai-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/echoai-so/well-known/echoai-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/echoai-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/echoai-so/hosts/echoai-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/echoai-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/echoai-so/vendors/echoai-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/echoai-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://echoai.so/terms
- group: operate
  title: ''
  type: Support
  url: https://echoai.so/resources/help
- group: auth
  title: ''
  type: Security
  url: https://echoai.so/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://echoai.so/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://echoai.so/resources/news
- group: start
  title: ''
  type: GettingStarted
  url: https://echoai.so/resources/help/category/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://echoai.so/developers
- group: auth
  href: https://artifacts.apis.io/echoai-so/security/echoai-so-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/echoai-so-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/echoai-so/security/echoai-so-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/echoai-so-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/echoai-so/security/echoai-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/echoai-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://echoai.so/
- group: docs
  title: ''
  type: Documentation
  url: https://echoai.so/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://echoai.so/pricing
- group: company
  title: ''
  type: Blog
  url: https://echoai.so/e/blog
coverage:
  checked: '2026-11-06'
  detail: Developer portal provides only HTML docs with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://echoai.so/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Echo AI is a no‑code platform that lets businesses create autonomous AI agents in seconds. The service provides multi‑channel chatbots that can sell, book appointments, capture leads, and integrate with WhatsApp, Instagram, Messenger, Telegram, websites, Shopify and Stripe. It offers a free tier and paid plans with more channels, voice minutes, custom domains and team seats, positioning itself as an easy‑to‑use SaaS solution for AI‑driven customer engagement.
image: https://echoai.so/__l5e/assets-v1/30fb2e52-0056-441c-bb75-09ba729f2f6e/echo-web-cover-1920x1080.png
json_schemas:
- name: GetConfigResponse
  property_count: 5
  slug: echoai-so-get-config-response
- name: PostChatRequest
  property_count: 9
  slug: echoai-so-post-chat-request
- name: PostChatStreamRequest
  property_count: 9
  slug: echoai-so-post-chat-stream-request
- name: PostCheckoutRequest
  property_count: 9
  slug: echoai-so-post-checkout-request
- name: PostContactsRequest
  property_count: 7
  slug: echoai-so-post-contacts-request
- name: PostTicketsRequest
  property_count: 5
  slug: echoai-so-post-tickets-request
jsonld:
- class_count: 21
  name: Echoai So Context
  property_count: 42
  slug: echoai-so-context
layout: provider
modified: '2026-11-06'
name: Echo AI
nav: Providers
network: true
overview: 'Echo AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software-as-a-Service, Chatbots, No-Code, and Multi-Channel.


  The Echo AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Echo AI''s developer surface includes support, getting-started guide, documentation, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Echoai So Plans Pricing
  plan_count: 4
  slug: echoai-so-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Echo AI API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: echoai-so-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 38.1
    discoverability: 58.9
    operational_transparency: 10.5
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Echoai So Domain Security
  slug: echoai-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Echoai So Vulnerability Disclosure
  slug: echoai-so-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Echoai So Trust Center
  slug: echoai-so-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: echoai-so
tags:
- Artificial Intelligence
- Software-as-a-Service
- Chatbots
- No-Code
- Multi-Channel
website: https://echoai.so/
---
