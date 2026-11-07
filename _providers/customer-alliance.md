---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Customer Alliance Agentic Access
  operation_count: 22
  slug: customer-alliance-agentic-access
  summary_line: 22 operations · 7 acting
api_count: 1
apis:
- description: Review management, surveys & feedback for hospitality API.
  name: Customer Alliance API
  slug: customer-alliance-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: Score and rating aggregates.
  name: Customer Alliance Analytics API
  slug: customer-alliance-analytics-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: Push guests into a property (write-only; grants no read of guest data).
  name: Customer Alliance Guests API
  slug: customer-alliance-guests-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: Who the key is.
  name: Customer Alliance Identity API
  slug: customer-alliance-identity-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: AI recommendations, mentions and topics.
  name: Customer Alliance Insights API
  slug: customer-alliance-insights-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: Hierarchy discovery, and the property attributes that group your properties.
  name: Customer Alliance Nodes API
  slug: customer-alliance-nodes-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: Collected reviews and owner replies, and pushing reviews in from other platforms.
  name: Customer Alliance Reviews API
  slug: customer-alliance-reviews-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: Surveys, responses and answers (PII-free), and pushing responses in from other survey tools.
  name: Customer Alliance Surveys API
  slug: customer-alliance-surveys-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: The signed events Customer Alliance POSTs to your endpoints.
  name: Customer Alliance Webhook events API
  slug: customer-alliance-webhook-events-api
- baseURL: https://app.customer-alliance.com/api/v4
  baseurl_source: declared
  description: 'Manage outbound webhook endpoints and inspect deliveries. Account-scoped: these endpoints ignore the key''s node binding (unlike the read endpoints).'
  name: Customer Alliance Webhooks API
  slug: customer-alliance-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Customer Alliance Webhooks
  slug: customer-alliance-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/customer-alliance/agentic-access/customer-alliance-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/customer-alliance-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/customer-alliance/plans/customer-alliance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/customer-alliance-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/rules/customer-alliance-rules.yml
  title: ''
  type: Spectral
  url: rules/customer-alliance-rules.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/json-ld/customer-alliance-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/customer-alliance-context.jsonld
- group: design
  href: https://artifacts.apis.io/customer-alliance/vocabulary/customer-alliance-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/customer-alliance-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/customer-alliance/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/asyncapi/customer-alliance-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/customer-alliance-webhooks.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/data-model/customer-alliance-data-model.yml
  title: ''
  type: DataModel
  url: data-model/customer-alliance-data-model.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/conventions/customer-alliance-conventions.yml
  title: ''
  type: Conventions
  url: conventions/customer-alliance-conventions.yml
- group: auth
  href: https://artifacts.apis.io/customer-alliance/authentication/customer-alliance-authentication.yml
  title: ''
  type: Authentication
  url: authentication/customer-alliance-authentication.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/errors/customer-alliance-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/customer-alliance-problem-types.yml
- group: design
  href: https://artifacts.apis.io/customer-alliance/conformance/customer-alliance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/customer-alliance-conformance.yml
- group: agent
  href: https://artifacts.apis.io/customer-alliance/llms/customer-alliance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/customer-alliance-llms.txt
- group: agent
  href: https://artifacts.apis.io/customer-alliance/well-known/customer-alliance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/customer-alliance-well-known.yml
- group: other
  href: https://artifacts.apis.io/customer-alliance/hosts/customer-alliance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/customer-alliance-hosts.yml
- group: other
  href: https://artifacts.apis.io/customer-alliance/vendors/customer-alliance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/customer-alliance-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.customer-alliance.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.customer-alliance.com/en/news
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.customer-alliance.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.customer-alliance.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customer-alliance
- group: auth
  href: https://artifacts.apis.io/customer-alliance/security/customer-alliance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/customer-alliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://customer-alliance.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.customer-alliance.com/en/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.customer-alliance.com/en/pricing-and-packaging
- group: operate
  title: ''
  type: Contact
  url: https://www.customer-alliance.com/en/contact-us
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.customer-alliance.com/mcp
  - status: 200
    url: https://customer-alliance.com/
  reason: partner-login
  state: gated
created: '2026-10-27'
description: Customer Alliance provides stress‑free review management software for hotels and hospitality groups. Their platform centralises guest reviews from multiple travel platforms, offers customizable guest surveys, AI‑powered sentiment analysis, and detailed reporting to help hotels improve service and revenue. The solution supports multi‑property portfolios, enabling benchmarking across locations and roles such as general managers and revenue managers.
jsonld:
- class_count: 37
  name: Customer Alliance Context
  property_count: 109
  slug: customer-alliance-context
layout: provider
modified: '2026-10-27'
name: Customer Alliance
nav: Providers
network: true
overview: 'Customer Alliance publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Guests API, Identity API, and 7 more. Tagged areas include Company, Hospitality, Review Management, Software-as-a-Service, and Hotels.


  The Customer Alliance catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Customer Alliance''s developer surface includes authentication, getting-started guide, API reference, pricing, and 22 more developer resources.'
plans:
- name: Customer Alliance Plans Pricing
  plan_count: 4
  slug: customer-alliance-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Customer Alliance API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 2
  slug: customer-alliance-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 69.4
    developer_ergonomics: 23.2
    discoverability: 70.5
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/customer-alliance/customer-alliance-2026-11-03T125922.png
security:
- kind: authentication
  name: Customer Alliance Authentication
  slug: customer-alliance-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Customer Alliance Domain Security
  slug: customer-alliance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: customer-alliance-survey-workflow
  slug: customer-alliance-survey-workflow
slug: customer-alliance
tags:
- Company
- Hospitality
- Review Management
- Software-as-a-Service
- Hotels
website: https://customer-alliance.com/
---
