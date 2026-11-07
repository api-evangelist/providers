---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
- description: The Infere API is REST-based and supports all major AI operations, compatible with OpenAI API.
  name: Infere API
  slug: infere-api-2
- description: 'Snowball Studio Ltd. API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Snowball Studio Ltd. API
  slug: infere-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/infere/plans/infere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infere-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/infere/rules/infere-rules.yml
  title: ''
  type: Spectral
  url: rules/infere-rules.yml
- group: design
  href: https://artifacts.apis.io/infere/json-ld/infere-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/infere-context.jsonld
- group: design
  href: https://artifacts.apis.io/infere/vocabulary/infere-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/infere-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/infere/data-model/infere-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infere-data-model.yml
- group: design
  href: https://artifacts.apis.io/infere/conventions/infere-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infere-conventions.yml
- group: auth
  href: https://artifacts.apis.io/infere/authentication/infere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infere-authentication.yml
- group: design
  href: https://artifacts.apis.io/infere/conformance/infere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infere-conformance.yml
- group: other
  href: https://artifacts.apis.io/infere/hosts/infere-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infere-hosts.yml
- group: other
  href: https://artifacts.apis.io/infere/vendors/infere-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infere-vendors.yml
- group: auth
  href: https://artifacts.apis.io/infere/security/infere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infere-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infere.com/
- group: docs
  title: ''
  type: Documentation
  url: https://infere.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://infere.com/documentation/api-reference/
- group: company
  title: ''
  type: Blog
  url: https://infere.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://infere.com/documentation/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://infere.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infere.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infere.com/legal/terms
created: '2026-10-17'
description: Snowball Studio Ltd. (Infere) provides an AI observability and prompt management platform, offering tools for LLM monitoring, evaluation, prompt optimization, and cost governance. The company delivers a web‑based interface, API access, and extensive documentation covering getting started, API reference, pricing, and privacy policies. It serves developers building AI‑driven applications, helping them track model performance, manage prompts, and ensure compliance with data regulations.
image: https://infere.com/images/og-image.png
json_schemas:
- name: PostValidateTokenRequest
  property_count: 2
  slug: infere-post-validate-token-request
jsonld:
- class_count: 1
  name: Infere Context
  property_count: 2
  slug: infere-context
layout: provider
modified: '2026-10-17'
name: Snowball Studio Ltd.
nav: Providers
network: true
overview: 'Snowball Studio Ltd. is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Observability, Prompt Management, and LLM.


  The Snowball Studio Ltd. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Snowball Studio Ltd.''s developer surface includes authentication, documentation, API reference, engineering blog, getting-started guide, pricing, and 13 more developer resources.'
plans:
- name: Infere Plans Pricing
  plan_count: 8
  slug: infere-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Snowball Studio Ltd. API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: infere-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 59.4
    catalog_earned_first_party: 12.0
    catalog_gap: 55.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 17.6
    developer_ergonomics: 27.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 34.1
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/infere/infere-2026-11-03T133748.png
security:
- kind: authentication
  name: Infere Authentication
  slug: infere-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Infere Domain Security
  slug: infere-domain-security
  summary_line: TLSv1.3 · DMARC
slug: infere
tags:
- Company
- Artificial Intelligence
- Observability
- Prompt Management
- LLM
website: https://infere.com/
---
