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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Dateio API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Dateio API
  slug: tapix-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/tapix/rules/tapix-rules.yml
  title: ''
  type: Spectral
  url: rules/tapix-rules.yml
- group: design
  href: https://artifacts.apis.io/tapix/json-ld/tapix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tapix-context.jsonld
- group: design
  href: https://artifacts.apis.io/tapix/vocabulary/tapix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tapix-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tapix/data-model/tapix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tapix-data-model.yml
- group: design
  href: https://artifacts.apis.io/tapix/conformance/tapix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tapix-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tapix/llms/tapix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tapix-llms.txt
- group: other
  href: https://artifacts.apis.io/tapix/hosts/tapix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tapix-hosts.yml
- group: other
  href: https://artifacts.apis.io/tapix/vendors/tapix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tapix-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tapix.io/
- group: auth
  href: https://artifacts.apis.io/tapix/security/tapix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tapix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tapix.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tapix.io/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tapix.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tapix.io/guides/getting-started-with-tapix
- group: operate
  title: ''
  type: Support
  url: https://www.tapix.io/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/6519bc1f17cd8731e2feeab4/67a5e458e6bbc30a3f23d0a1_2024_11_25_Dateio_privacy_policy.pdf
coverage:
  checked: '2026-10-21'
  detail: Documentation pages return JavaScript shells with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://tapix.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: 'Dateio (brand: Tapix) provides payment data enrichment services, turning raw transaction data into actionable insights for fintechs and banks. Their platform enriches card payments, A2A transfers, QR payments, and open banking data with merchant names, logos, categories, locations, and more, supporting use cases like credit scoring, fraud detection, and personalized banking experiences. The company emphasizes real‑time updates, high scalability, and easy integration via well‑documented APIs.'
image: https://cdn.prod.website-files.com/6519bc1f17cd8731e2feeab4/66f2cd2113178ccf86ddb7d4_Tapix_OG.png
json_schemas:
- name: GetAtmsCompleteFindnearbyResponse
  property_count: 38
  slug: tapix-get-atms-complete-findnearby-response
- name: GetInvalidationsItemRangeResponse
  property_count: 2
  slug: tapix-get-invalidations-item-range-response
- name: GetInvalidationsResponse
  property_count: 2
  slug: tapix-get-invalidations-response
- name: PostV6FeedbackResponse
  property_count: 2
  slug: tapix-post-v6-feedback-response
- name: PostV6SuggestionsRequest
  property_count: 1
  slug: tapix-post-v6-suggestions-request
- name: PostV6SuggestionsResponse
  property_count: 2
  slug: tapix-post-v6-suggestions-response
jsonld:
- class_count: 7
  name: Tapix Context
  property_count: 9
  slug: tapix-context
layout: provider
modified: '2026-10-21'
name: Dateio
nav: Providers
network: true
overview: 'Dateio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, and Data Enrichment.


  The Dateio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dateio''s developer surface includes documentation, getting-started guide, support, and 13 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Dateio API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: tapix-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 17.9
    discoverability: 55.4
    operational_transparency: 7.9
  previous_composite: 23.2
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 11.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tapix/tapix-2026-11-03T144318.png
security:
- kind: domain-security
  name: Tapix Domain Security
  slug: tapix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tapix
tags:
- Company
- Fintech
- Payments
- Data Enrichment
website: https://tapix.io/
---
