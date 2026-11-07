---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Translate API from TranslateMyImage — 1 operation(s) for translate.
  name: TranslateMyImage Translate API
  slug: translatemyimage-translate-api
artifact_total: 6
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://translatemyimage.com/legal-notice
- group: commercial
  href: https://artifacts.apis.io/translatemyimage/plans/translatemyimage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/translatemyimage-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/translatemyimage/rules/translatemyimage-rules.yml
  title: ''
  type: Spectral
  url: rules/translatemyimage-rules.yml
- group: design
  href: https://artifacts.apis.io/translatemyimage/json-ld/translatemyimage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/translatemyimage-context.jsonld
- group: design
  href: https://artifacts.apis.io/translatemyimage/vocabulary/translatemyimage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/translatemyimage-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/translatemyimage/data-model/translatemyimage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/translatemyimage-data-model.yml
- group: design
  href: https://artifacts.apis.io/translatemyimage/conformance/translatemyimage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/translatemyimage-conformance.yml
- group: agent
  href: https://artifacts.apis.io/translatemyimage/llms/translatemyimage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/translatemyimage-llms.txt
- group: other
  href: https://artifacts.apis.io/translatemyimage/hosts/translatemyimage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/translatemyimage-hosts.yml
- group: other
  href: https://artifacts.apis.io/translatemyimage/vendors/translatemyimage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/translatemyimage-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://translatemyimage.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://translatemyimage.com/changelog
- group: auth
  href: https://artifacts.apis.io/translatemyimage/security/translatemyimage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/translatemyimage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://translatemyimage.com
- group: docs
  title: ''
  type: Documentation
  url: https://translatemyimage.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://translatemyimage.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://translatemyimage.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://translatemyimage.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://translatemyimage.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://translatemyimage.com/auth/login
coverage:
  checked: '2026-10-12'
  detail: API documentation is publicly accessible but provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://translatemyimage.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: TranslateMyImage provides an AI‑powered service that translates text embedded in images while preserving the original layout. Users can upload PNG, JPG, or WEBP files up to 10 MB, select a target language, and receive a translated image for download. The platform offers a Pro plan with API access, allowing developers to integrate image translation into applications via a simple REST endpoint that accepts multipart/form‑data and returns the translated image. Features include batch processing, language detection, and a preview step before finalizing the translation.
image: https://translatemyimage.com/images/og-image.png
json_schemas:
- name: GetApiTranslateResponse
  property_count: 2
  slug: translatemyimage-get-api-translate-response
jsonld:
- class_count: 1
  name: Translatemyimage Context
  property_count: 2
  slug: translatemyimage-context
layout: provider
modified: '2026-10-12'
name: TranslateMyImage
nav: Providers
network: true
overview: 'TranslateMyImage is listed with 1 API on the [APIs.io](https://apis.io/) network: Translate API. Tagged areas include Artificial Intelligence, Image Processing, Translation, REST, and Software-as-a-Service.


  The TranslateMyImage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TranslateMyImage''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Translatemyimage Plans Pricing
  plan_count: 6
  slug: translatemyimage-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: TranslateMyImage API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: translatemyimage-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 18.0
    developer_ergonomics: 15.5
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 36.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/translatemyimage/translatemyimage-2026-11-03T145033.png
security:
- kind: domain-security
  name: Translatemyimage Domain Security
  slug: translatemyimage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: translatemyimage
tags:
- Artificial Intelligence
- Image Processing
- Translation
- REST
- Software-as-a-Service
website: https://translatemyimage.com
---
