---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://astroapi-5.divineapi.com
  baseurl_source: declared
  description: DivineAPI is a B2B astrology API offering over 300 endpoints across horoscope, tarot, Vedic and Western astrology, numerology, lifestyle, calculators and PDF reports.
  name: DivineAPI
  slug: divineapi
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/divineapi-com/plans/divineapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/divineapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/divineapi-com/conformance/divineapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/divineapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/divineapi-com/llms/divineapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/divineapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/divineapi-com/hosts/divineapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/divineapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/divineapi-com/vendors/divineapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/divineapi-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://divineapi.com/trust
- group: start
  title: ''
  type: Login
  url: https://divineapi.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.divineapi.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.divineapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/divineapi-com/security/divineapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divineapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://divineapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.divineapi.com
- group: commercial
  title: ''
  type: Pricing
  url: https://divineapi.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.divineapi.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.divineapi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://divineapi.com/terms-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://divineapi.com/privacy-policy
created: '2026-10-29'
description: DivineAPI provides a comprehensive Astrology API platform offering over 300 endpoints across horoscope, western and Vedic astrology, numerology, tarot, AI astrologer chatbot, and various widgets. It delivers detailed astrological data, charts, and compatibility insights for developers to integrate into applications, with a free 14‑day trial and flexible pricing.
image: https://divine-report-pdf.s3.amazonaws.com/api/content/1730617505-56874p4a.png
json_schemas:
- name: GetIndianApiV1GhataChakraResponse
  property_count: 14
  slug: divineapi-com-get-indian-api-v1-ghata-chakra-response
- name: GetIndianApiV1PitraDoshaResponse
  property_count: 14
  slug: divineapi-com-get-indian-api-v1-pitra-dosha-response
- name: GetIndianApiV2YogasResponse
  property_count: 14
  slug: divineapi-com-get-indian-api-v2-yogas-response
- name: GetWesternApiV1PlanetReturnsListResponse
  property_count: 4
  slug: divineapi-com-get-western-api-v1-planet-returns-list-response
- name: PostApiV1ReportsGenerateRequest
  property_count: 29
  slug: divineapi-com-post-api-v1-reports-generate-request
- name: PostApiV1WesternReportsGenerateRequest
  property_count: 47
  slug: divineapi-com-post-api-v1-western-reports-generate-request
jsonld:
- class_count: 55
  name: Divineapi Com Context
  property_count: 61
  slug: divineapi-com-context
layout: provider
modified: '2026-10-29'
name: divineapi-com
nav: Providers
network: true
overview: 'divineapi-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: DivineAPI. Tagged areas include Astrology, Data, Developers, and Platform.


  The divineapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  divineapi-com''s developer surface includes changelog, documentation, pricing, support, and 13 more developer resources.'
plans:
- name: Divineapi Com Plans Pricing
  plan_count: 6
  slug: divineapi-com-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: divineapi-com API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: divineapi-com-rules
scopes:
- name: Divineapi Com Scopes
  scope_count: 0
  slug: divineapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 58.8
    catalog_earned_first_party: 12.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 57.9
    contract_governance: 15.9
    contract_quality: 32.6
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 41.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 50.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/divineapi-com/divineapi-com-2026-11-03T130816.png
security:
- kind: authentication
  name: Divineapi Com Authentication
  slug: divineapi-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Divineapi Com Domain Security
  slug: divineapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: divineapi-com
tags:
- Astrology
- Data
- Developers
- Platform
website: https://divineapi.com/
---
