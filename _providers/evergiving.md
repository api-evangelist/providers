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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.evergiving.com
  baseurl_source: declared
  description: 'EverGiving API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: EverGiving API
  slug: evergiving-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/evergiving/plans/evergiving-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/evergiving-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/evergiving/rules/evergiving-rules.yml
  title: ''
  type: Spectral
  url: rules/evergiving-rules.yml
- group: design
  href: https://artifacts.apis.io/evergiving/json-ld/evergiving-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/evergiving-context.jsonld
- group: design
  href: https://artifacts.apis.io/evergiving/vocabulary/evergiving-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/evergiving-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/evergiving/data-model/evergiving-data-model.yml
  title: ''
  type: DataModel
  url: data-model/evergiving-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.evergiving.com/security/
- group: design
  href: https://artifacts.apis.io/evergiving/conformance/evergiving-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evergiving-conformance.yml
- group: other
  href: https://artifacts.apis.io/evergiving/hosts/evergiving-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evergiving-hosts.yml
- group: other
  href: https://artifacts.apis.io/evergiving/vendors/evergiving-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evergiving-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.evergiving.com/security
- group: auth
  href: https://artifacts.apis.io/evergiving/security/evergiving-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/evergiving-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/evergiving/security/evergiving-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evergiving-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evergiving.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.evergiving.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.evergiving.com/developer
- group: docs
  title: ''
  type: APIReference
  url: https://www.evergiving.com/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.evergiving.com/try-us
- group: operate
  title: ''
  type: Support
  url: https://www.evergiving.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://medium.com/blog-evergiving-com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evergiving.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evergiving.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evergiving.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/evergiving/workspace/evergiving-api
coverage:
  checked: '2026-10-27'
  detail: The Evergiving developer site provides HTML documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files are publicly accessible.
  evidence:
  - status: 301
    url: https://www.evergiving.com/openapi.json
  - status: 301
    url: https://www.evergiving.com/api/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: EverGiving provides an end‑to‑end fundraising platform that enables regular giving campaigns for charities and nonprofits. The solution supports campaign creation, donor management, payment processing, reporting, and integrations with tools like Salesforce and Google Data Studio. It offers a public API for developers to access campaign data, donor information, and transaction records, facilitating custom integrations and analytics.
image: https://www.evergiving.com/img/logo_evergiving-fullcol.png
json_schemas:
- name: PostV1TeamsRequest
  property_count: 15
  slug: evergiving-post-v1-teams-request
- name: PostV1TeamsResponse
  property_count: 9
  slug: evergiving-post-v1-teams-response
- name: PostV1UsersRequest
  property_count: 9
  slug: evergiving-post-v1-users-request
- name: PostV1UsersResponse
  property_count: 7
  slug: evergiving-post-v1-users-response
- name: PostV4LeadsRequest
  property_count: 6
  slug: evergiving-post-v4-leads-request
- name: PostV4LeadsResponse
  property_count: 7
  slug: evergiving-post-v4-leads-response
jsonld:
- class_count: 7
  name: Evergiving Context
  property_count: 39
  slug: evergiving-context
layout: provider
modified: '2026-10-27'
name: EverGiving
nav: Providers
network: true
overview: 'EverGiving is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Non-Profit, and Integration.


  The EverGiving catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EverGiving''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Evergiving Plans Pricing
  plan_count: 10
  slug: evergiving-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: EverGiving API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: evergiving-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 59.2
    contract_governance: 35.6
    contract_quality: 24.8
    developer_ergonomics: 25.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 44.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/evergiving/evergiving-2026-11-03T131653.png
security:
- kind: domain-security
  name: Evergiving Domain Security
  slug: evergiving-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Evergiving Trust Center
  slug: evergiving-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: evergiving
tags:
- Company
- Fundraising
- Non-Profit
- Integration
website: https://evergiving.com/
---
