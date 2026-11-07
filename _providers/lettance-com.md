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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lettance Com Agentic Access
  operation_count: 9
  slug: lettance-com-agentic-access
  summary_line: 9 operations
api_count: 2
apis:
- description: Public read‑only API for landlord rules, council licensing and related data.
  name: Lettance Public API
  slug: lettance-public-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/lettance-com/rules/lettance-com-rules.yml
  title: ''
  type: Spectral
  url: rules/lettance-com-rules.yml
- group: design
  href: https://artifacts.apis.io/lettance-com/json-ld/lettance-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lettance-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/lettance-com/vocabulary/lettance-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lettance-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lettance-com/conformance/lettance-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lettance-com-conformance.yml
- group: start
  title: ''
  type: SignUp
  url: https://lettance.com/register
- group: commercial
  href: https://artifacts.apis.io/lettance-com/plans/lettance-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lettance-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lettance-com/data-model/lettance-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lettance-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/lettance-com/errors/lettance-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lettance-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/lettance-com/llms/lettance-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lettance-com-llms.txt
- group: other
  href: https://artifacts.apis.io/lettance-com/hosts/lettance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lettance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lettance-com/vendors/lettance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lettance-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lettance-com/security/lettance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lettance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lettance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lettance.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://lettance.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://lettance.com/support
- group: start
  title: ''
  type: GettingStarted
  url: https://lettance.com/developers#get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lettance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lettance.com/privacy
created: '2026-10-30'
description: Lettance.com is a technology company offering a platform that enables businesses to manage and automate their leasing and subscription services. The company provides APIs for handling contracts, payments, customer data, and analytics, allowing integration with existing enterprise systems. Their solutions aim to streamline recurring revenue models, improve operational efficiency, and deliver insights into subscription performance. Lettance focuses on flexibility, scalability, and compliance with industry standards, supporting developers with comprehensive documentation and SDKs.
image: https://lettance.com/icon-512
json_schemas:
- name: AreaMarketResponse
  property_count: 2
  slug: lettance-com-area-market-response
- name: CheckResponse
  property_count: 2
  slug: lettance-com-check-response
- name: CompareResponse
  property_count: 2
  slug: lettance-com-compare-response
- name: CouncilListResponse
  property_count: 2
  slug: lettance-com-council-list-response
- name: PlanResponse
  property_count: 2
  slug: lettance-com-plan-response
- name: RuleListResponse
  property_count: 2
  slug: lettance-com-rule-list-response
jsonld:
- class_count: 28
  name: Lettance Com Context
  property_count: 128
  slug: lettance-com-context
layout: provider
modified: '2026-10-30'
name: lettance-com
nav: Providers
network: true
overview: 'lettance-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Lettance Public API. Tagged areas include Company, Leasing, Subscription, and Automation.


  The lettance-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lettance-com''s developer surface includes signup flow, documentation, pricing, support, getting-started guide, and 14 more developer resources.'
plans:
- name: Lettance Com Plans Pricing
  plan_count: 2
  slug: lettance-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Lettance Com Rate Limits
  slug: lettance-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: lettance-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: lettance-com-rules
scopes:
- name: Lettance Com Scopes
  scope_count: 0
  slug: lettance-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.8
    catalog_earned_first_party: 8.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 13.1
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/lettance-com/lettance-com-2026-11-03T134820.png
security:
- kind: authentication
  name: Lettance Com Authentication
  slug: lettance-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lettance Com Domain Security
  slug: lettance-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: lettance
  slug: lettance-com-lettance
slug: lettance-com
tags:
- Company
- Leasing
- Subscription
- Automation
website: https://lettance.com/
---
