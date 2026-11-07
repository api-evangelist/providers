---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Toolaby App Agentic Access
  operation_count: 9
  slug: toolaby-app-agentic-access
  summary_line: 9 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://toolaby.app/api/v1
  baseurl_source: declared
  description: The Analytics API from toolaby-app — 2 operation(s) for analytics.
  name: toolaby-app Analytics API
  slug: toolaby-app-analytics-api
- baseURL: https://toolaby.app/api/v1
  baseurl_source: declared
  description: The Customers API from toolaby-app — 2 operation(s) for customers.
  name: toolaby-app Customers API
  slug: toolaby-app-customers-api
- baseURL: https://toolaby.app/api/v1
  baseurl_source: declared
  description: The Grants API from toolaby-app — 2 operation(s) for grants.
  name: toolaby-app Grants API
  slug: toolaby-app-grants-api
- baseURL: https://toolaby.app/api/v1
  baseurl_source: declared
  description: The Uses API from toolaby-app — 1 operation(s) for uses.
  name: toolaby-app Uses API
  slug: toolaby-app-uses-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/toolaby-app/agentic-access/toolaby-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/toolaby-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/toolaby-app/plans/toolaby-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toolaby-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/rules/toolaby-app-rules.yml
  title: ''
  type: Spectral
  url: rules/toolaby-app-rules.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/json-ld/toolaby-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/toolaby-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/toolaby-app/vocabulary/toolaby-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/toolaby-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/toolaby-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/data-model/toolaby-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/toolaby-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/conventions/toolaby-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/toolaby-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/conventions/toolaby-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toolaby-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/toolaby-app/security/toolaby-app-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/toolaby-app-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/errors/toolaby-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toolaby-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/toolaby-app/conformance/toolaby-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toolaby-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/toolaby-app/llms/toolaby-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toolaby-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/toolaby-app/well-known/toolaby-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/toolaby-app-security.txt
- group: agent
  href: https://artifacts.apis.io/toolaby-app/well-known/toolaby-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/toolaby-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/toolaby-app/hosts/toolaby-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toolaby-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/toolaby-app/vendors/toolaby-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toolaby-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toolaby.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toolaby.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://toolaby.app/docs/plans
- group: start
  title: ''
  type: Login
  url: https://toolaby.app/dev/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://toolaby.app/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://toolaby.app/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://toolaby.app/docs/reference/api
- group: auth
  href: https://artifacts.apis.io/toolaby-app/authentication/toolaby-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toolaby-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/toolaby-app/security/toolaby-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/toolaby-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/toolaby-app/security/toolaby-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toolaby-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toolaby.app/
- group: docs
  title: ''
  type: Documentation
  url: https://toolaby.app/docs
created: '2026-10-30'
description: Toolaby provides a Chrome extension payment platform that lets developers collect licences, subscriptions, free trials, and paywalls directly through their own Stripe accounts. It charges a 0.5% transaction fee or a flat $25 per month per workspace, offering flexible pricing for SaaS products integrated into browser extensions. The service includes account management, licensing controls, and subscription handling, aiming to simplify monetization for extension developers.
image: https://toolaby.app/og.png
json_schemas:
- name: AnalyticsSummary
  property_count: 9
  slug: toolaby-app-analytics-summary
- name: AnalyticsTable
  property_count: 4
  slug: toolaby-app-analytics-table
- name: CustomerListItem
  property_count: 7
  slug: toolaby-app-customer-list-item
- name: Customer
  property_count: 8
  slug: toolaby-app-customer
- name: Grant
  property_count: 10
  slug: toolaby-app-grant
- name: Usage
  property_count: 13
  slug: toolaby-app-usage
jsonld:
- class_count: 9
  name: Toolaby App Context
  property_count: 46
  slug: toolaby-app-context
layout: provider
modified: '2026-10-30'
name: toolaby-app
nav: Providers
network: true
overview: 'toolaby-app publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Customers API, Grants API, and 1 more. Tagged areas include Company, Payments, Chrome Extension, Stripe, and Licensing.


  The toolaby-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  toolaby-app''s developer surface includes pricing, changelog, getting-started guide, API reference, authentication, documentation, and 23 more developer resources.'
plans:
- name: Toolaby App Plans Pricing
  plan_count: 2
  slug: toolaby-app-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: toolaby-app API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: toolaby-app-rules
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 32.6
    discoverability: 73.2
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/toolaby-app/toolaby-app-2026-11-03T145057.png
security:
- kind: authentication
  name: Toolaby App Authentication
  slug: toolaby-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Toolaby App Domain Security
  slug: toolaby-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Toolaby App Vulnerability Disclosure
  slug: toolaby-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: toolaby-app
tags:
- Company
- Payments
- Chrome Extension
- Stripe
- Licensing
website: https://toolaby.app/
---
