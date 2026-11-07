---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.us.test.highnoteplatform.com
  baseurl_source: declared
  description: 'Highnote API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Highnote API
  slug: highnoteplatform-com-api
artifact_total: 11
asyncapis:
- description: ''
  name: Highnoteplatform Com Webhooks
  slug: highnoteplatform-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/highnoteplatform-com/rate-limits/highnoteplatform-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/highnoteplatform-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/highnoteplatform-com/plans/highnoteplatform-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/highnoteplatform-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/rules/highnoteplatform-com-rules.yml
  title: ''
  type: Spectral
  url: rules/highnoteplatform-com-rules.yml
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/json-ld/highnoteplatform-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/highnoteplatform-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/vocabulary/highnoteplatform-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/highnoteplatform-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/highnoteplatform-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/asyncapi/highnoteplatform-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/highnoteplatform-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/data-model/highnoteplatform-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/highnoteplatform-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/conventions/highnoteplatform-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/highnoteplatform-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/highnoteplatform-com/authentication/highnoteplatform-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/highnoteplatform-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/highnoteplatform-com/conformance/highnoteplatform-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/highnoteplatform-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/highnoteplatform-com/llms/highnoteplatform-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/highnoteplatform-com-llms.txt
- group: other
  href: https://artifacts.apis.io/highnoteplatform-com/hosts/highnoteplatform-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/highnoteplatform-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/highnoteplatform-com/vendors/highnoteplatform-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/highnoteplatform-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://highnote.com/agreements/terms
- group: operate
  title: ''
  type: Support
  url: https://support.highnote.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.highnote.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://highnote.com/agreements/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://highnote.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://highnote.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.highnote.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://highnote.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.highnote.com/docs/api-reference/query
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.highnote.com/docs/issuing/accounts/onboarding/application-denials
- group: docs
  title: ''
  type: Documentation
  url: https://docs.highnote.com/
- group: auth
  href: https://artifacts.apis.io/highnoteplatform-com/security/highnoteplatform-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/highnoteplatform-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://highnoteplatform.com
created: '2026-10-22'
description: Highnote provides a unified payments platform that enables companies to issue and manage card programs, accept payments, offer credit products, and move money across various rails. It serves businesses that need embedded finance solutions, including issuers, merchants, platforms, and vertical SaaS providers.
image: https://highnote.com/img/og/home-og.jpg
json_schemas:
- name: PostGraphqlRequest
  property_count: 1
  slug: highnoteplatform-com-post-graphql-request
- name: PostGraphqlResponse
  property_count: 2
  slug: highnoteplatform-com-post-graphql-response
jsonld:
- class_count: 2
  name: Highnoteplatform Com Context
  property_count: 3
  slug: highnoteplatform-com-context
layout: provider
modified: '2026-10-22'
name: Highnote
nav: Providers
network: true
overview: 'Highnote is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Issuing, Acquiring, Credit, Money Movement, and Embedded Finance.


  The Highnote catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Highnote''s developer surface includes authentication, support, pricing, changelog, engineering blog, API reference, getting-started guide, and 20 more developer resources.'
plans:
- name: Highnoteplatform Com Plans Pricing
  plan_count: 4
  slug: highnoteplatform-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Highnoteplatform Com Rate Limits
  slug: highnoteplatform-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Highnote API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: highnoteplatform-com-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 80.8
    catalog_earned_first_party: 24.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 29.5
    developer_ergonomics: 36.3
    discoverability: 74.1
    operational_transparency: 63.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/highnoteplatform-com/highnoteplatform-com-2026-11-03T133407.png
security:
- kind: authentication
  name: Highnoteplatform Com Authentication
  slug: highnoteplatform-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Highnoteplatform Com Domain Security
  slug: highnoteplatform-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: highnoteplatform-com-graphql-execute
  slug: highnoteplatform-com-graphql-execute
slug: highnoteplatform-com
tags:
- Issuing
- Acquiring
- Credit
- Money Movement
- Embedded Finance
- Spend Management
- Fleet Management
- Travel
website: https://highnoteplatform.com
---
