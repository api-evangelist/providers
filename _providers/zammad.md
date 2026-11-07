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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Zammad API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Zammad API
  slug: zammad-api
artifact_total: 9
common:
- group: other
  href: https://artifacts.apis.io/zammad/vendors/zammad-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zammad-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/zammad/plans/zammad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zammad-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zammad/rules/zammad-rules.yml
  title: ''
  type: Spectral
  url: rules/zammad-rules.yml
- group: design
  href: https://artifacts.apis.io/zammad/json-ld/zammad-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zammad-context.jsonld
- group: design
  href: https://artifacts.apis.io/zammad/vocabulary/zammad-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zammad-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zammad/data-model/zammad-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zammad-data-model.yml
- group: design
  href: https://artifacts.apis.io/zammad/conformance/zammad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zammad-conformance.yml
- group: other
  href: https://artifacts.apis.io/zammad/hosts/zammad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zammad-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://zammad.com/en/product/features/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zammad.com/en/company/terms
- group: operate
  title: ''
  type: Support
  url: https://support.zammad.com/help/en-us/3
- group: auth
  title: ''
  type: Security
  url: https://zammad.com/en/product/features/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zammad.com/en/company/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://zammad.com/en/company/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zammad
- group: operate
  title: ''
  type: ChangeLog
  url: https://zammad.com/en/product/releases
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zammad.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zammad.org/en/latest/
- group: auth
  href: https://artifacts.apis.io/zammad/security/zammad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zammad-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zammad/security/zammad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zammad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zammad.com/
- group: company
  title: ''
  type: Blog
  url: https://zammad.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zammad.com/en/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://zammad.com/en/getting-started
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found; the API documentation pages return 404 for spec URLs.
  evidence:
  - status: 404
    url: https://api.zammad.com/openapi.json
  - status: 404
    url: https://docs.zammad.org/en/latest/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Zammad provides an AI‑powered service platform for customer support, helpdesk and IT operations. It centralises communication across channels, adds AI‑driven efficiency, and offers a free trial for teams of any size. The platform combines human expertise with automation to deliver seamless support experiences.
image: https://zammad.com/media/assets/assets/images/1601169394-1792392622/sharing-preview-1200x630-crop-q85.jpg
json_schemas:
- name: GetApiV1TicketsSearchResponse
  property_count: 14
  slug: zammad-get-api-v1-tickets-search-response
- name: PostApiV1CtiInstanceRequest
  property_count: 6
  slug: zammad-post-api-v1-cti-instance-request
- name: PostApiV1CtiInstanceResponse
  property_count: 7
  slug: zammad-post-api-v1-cti-instance-response
jsonld:
- class_count: 3
  name: Zammad Context
  property_count: 21
  slug: zammad-context
layout: provider
modified: '2026-10-28'
name: Zammad
nav: Providers
network: true
overview: 'Zammad is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Support, Help Desk, Artificial Intelligence, and Customer Service.


  The Zammad catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zammad''s developer surface includes support, changelog, documentation, engineering blog, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Zammad Plans Pricing
  plan_count: 9
  slug: zammad-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Zammad API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: zammad-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 22.0
    developer_ergonomics: 19.0
    discoverability: 58.0
    operational_transparency: 19.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.9
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
screenshot: https://apis.io/screenshots/zammad/zammad-2026-11-03T150415.png
security:
- kind: domain-security
  name: Zammad Domain Security
  slug: zammad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zammad Vulnerability Disclosure
  slug: zammad-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zammad
tags:
- Company
- Support
- Help Desk
- Artificial Intelligence
- Customer Service
- Platform
website: https://zammad.com/
---
