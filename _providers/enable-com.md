---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Enable API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Enable API
  slug: enable-com-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/enable-com/well-known/enable-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/enable-com-status-security.txt
- group: start
  title: ''
  type: Login
  url: https://apps.enable.com/en-US/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.enable.com/sections/quick-start
- group: design
  href: https://artifacts.apis.io/enable-com/rules/enable-com-rules.yml
  title: ''
  type: Spectral
  url: rules/enable-com-rules.yml
- group: design
  href: https://artifacts.apis.io/enable-com/vocabulary/enable-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/enable-com-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://developers.enable.com/articles/certifications-and-compliance
- group: design
  href: https://artifacts.apis.io/enable-com/conformance/enable-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/enable-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/enable-com/llms/enable-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enable-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/enable-com/well-known/enable-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enable-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/enable-com/hosts/enable-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enable-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/enable-com/vendors/enable-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enable-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enable.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.enable.com/resources/news/
- group: auth
  href: https://artifacts.apis.io/enable-com/security/enable-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/enable-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/enable-com/security/enable-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enable-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://enable.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.enable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.enable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.enable.com/api-reference
- group: operate
  title: ''
  type: Support
  url: https://help-center.enable.com/hc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.enable.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.enable.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.enable.com/privacy-notice
created: '2026-10-25'
description: Enable provides AI‑powered rebate and pricing management solutions for enterprises, helping procurement, finance and sales teams automate complex pricing, rebate calculations, and compliance. Their platform integrates with ERP, CRM and e‑commerce systems, offering analytics, AI insights, and a developer hub with REST APIs for data synchronization, reporting, and custom app development. Founded with backing from Insight Partners, Menlo Ventures, Norwest Venture Partners, and Sierra Ventures, Enable serves customers across distribution, health, manufacturing, retail, and food services.
image: https://www.enable.com/wp-content/uploads/2025/10/light-leak-1.webp
layout: provider
modified: '2026-10-25'
name: Enable
nav: Providers
network: true
overview: 'Enable is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Pricing, Rebate, and Software-as-a-Service.


  The Enable catalog on APIs.io includes 1 Spectral governance ruleset.


  Enable''s developer surface includes getting-started guide, documentation, API reference, support, pricing, and 18 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: Enable API Rules
  rule_count: 29
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 1
  slug: enable-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 40.8
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 21.4
    discoverability: 65.2
    operational_transparency: 18.4
  previous_composite: 35.2
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
    score: 15.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/enable-com/enable-com-2026-11-03T131504.png
security:
- kind: domain-security
  name: Enable Com Domain Security
  slug: enable-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Enable Com Trust Center
  slug: enable-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: enable-com
tags:
- Company
- Artificial Intelligence
- Pricing
- Rebate
- Software-as-a-Service
website: https://enable.com/
---
