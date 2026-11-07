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
    auth_clarity: false
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
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.bravos-ai.com
  baseurl_source: declared
  description: 'Bravos AI API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bravos AI API
  slug: bravos-ai-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/bravos-ai-com/plans/bravos-ai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bravos-ai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bravos-ai-com/rules/bravos-ai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bravos-ai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bravos-ai-com/json-ld/bravos-ai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bravos-ai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bravos-ai-com/vocabulary/bravos-ai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bravos-ai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bravos-ai-com/data-model/bravos-ai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bravos-ai-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bravos-ai-com/conformance/bravos-ai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bravos-ai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bravos-ai-com/llms/bravos-ai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bravos-ai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bravos-ai-com/hosts/bravos-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bravos-ai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bravos-ai-com/vendors/bravos-ai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bravos-ai-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bravos-ai-com/security/bravos-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bravos-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bravos-ai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bravos-ai.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://bravos-ai.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://bravos-ai.com/developers
- group: company
  title: ''
  type: Blog
  url: https://bravos-ai.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bravos-ai.com/legal/terminos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bravos-ai.com/legal/privacidad
- group: start
  title: ''
  type: SignUp
  url: https://app.bravos-ai.com/register?lang=es
coverage:
  checked: '2026-11-03'
  detail: API documentation pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://bravos-ai.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bravos AI provides customizable AI-powered chatbots for businesses, integrating with platforms like WordPress, Shopify, WooCommerce, and WhatsApp. It offers a 7‑day free trial, multi‑language support, and tools to train bots on a company’s website, catalog, and documents, enabling automated customer interactions and sales assistance.
image: https://bravos-ai.com/images/og-image.png
json_schemas:
- name: PostIntegrationsCustomWebhookBotidRequest
  property_count: 2
  slug: bravos-ai-com-post-integrations-custom-webhook-botid-request
- name: PostIntegrationsCustomWebhookBotidResponse
  property_count: 5
  slug: bravos-ai-com-post-integrations-custom-webhook-botid-response
jsonld:
- class_count: 2
  name: Bravos Ai Com Context
  property_count: 6
  slug: bravos-ai-com-context
layout: provider
modified: '2026-11-02'
name: Bravos AI
nav: Providers
network: true
overview: 'Bravos AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Chatbots, Customer Service, E-Commerce, and Spanish.


  The Bravos AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bravos AI''s developer surface includes documentation, API reference, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Bravos Ai Com Plans Pricing
  plan_count: 12
  slug: bravos-ai-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Bravos AI API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: bravos-ai-com-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 20.2
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bravos Ai Com Domain Security
  slug: bravos-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bravos-ai-com
tags:
- Artificial Intelligence
- Chatbots
- Customer Service
- E-Commerce
- Spanish
website: https://bravos-ai.com/
---
