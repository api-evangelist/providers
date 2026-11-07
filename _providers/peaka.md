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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Peaka data integration platform
  name: Peaka Gateway API
  slug: peaka-gateway-api
- baseURL: https://partner.peaka.studio/api/v1
  baseurl_source: declared
  description: The Peaka Partner API is a powerful gateway that lets you seamlessly integrate Peaka's features into your own applications and services. With secure access provided through a unique API key, you can l
  name: Peaka Gateway API API
  slug: peaka-gateway-api-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/peaka/rules/peaka-rules.yml
  title: ''
  type: Spectral
  url: rules/peaka-rules.yml
- group: design
  href: https://artifacts.apis.io/peaka/json-ld/peaka-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/peaka-context.jsonld
- group: design
  href: https://artifacts.apis.io/peaka/vocabulary/peaka-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/peaka-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/peaka/plans/peaka-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peaka-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/peaka/data-model/peaka-data-model.yml
  title: ''
  type: DataModel
  url: data-model/peaka-data-model.yml
- group: auth
  href: https://artifacts.apis.io/peaka/authentication/peaka-authentication.yml
  title: ''
  type: Authentication
  url: authentication/peaka-authentication.yml
- group: design
  href: https://artifacts.apis.io/peaka/errors/peaka-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/peaka-problem-types.yml
- group: design
  href: https://artifacts.apis.io/peaka/conformance/peaka-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peaka-conformance.yml
- group: agent
  href: https://artifacts.apis.io/peaka/llms/peaka-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/peaka-llms.txt
- group: other
  href: https://artifacts.apis.io/peaka/a2a/peaka-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/peaka-a2a.yml
- group: other
  href: https://artifacts.apis.io/peaka/hosts/peaka-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peaka-hosts.yml
- group: other
  href: https://artifacts.apis.io/peaka/vendors/peaka-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peaka-vendors.yml
- group: build
  href: https://artifacts.apis.io/peaka/packages/peaka-packages.yml
  title: ''
  type: SDKs
  url: packages/peaka-packages.yml
- group: build
  href: https://artifacts.apis.io/peaka/packages/peaka-packages.yml
  title: ''
  type: Packages
  url: packages/peaka-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.peaka.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peaka.com/terms-and-conditions/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.peaka.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peakacom
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.peaka.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.peaka.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.peaka.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.peaka.com\
- group: docs
  title: ''
  type: APIReference
  url: https://www.peaka.com/docs/api-reference/
- group: auth
  href: https://artifacts.apis.io/peaka/security/peaka-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peaka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peaka.com/
created: '2026-10-21'
description: Peaka provides a platform that integrates data from various sources—including databases, SaaS tools, NoSQL stores, and APIs—into a unified, AI‑ready data product. Users can create governed, reusable data assets through a single prompt, accelerating analytics and AI initiatives while ensuring data governance and compliance.
image: https://www.peaka.com/processed_images/peaka-meta-hero.98bb895990cdf1d9.png
json_schemas:
- name: ConnectionConfiguration
  property_count: 10
  slug: peaka-connection-configuration
- name: ExportJobResponse
  property_count: 21
  slug: peaka-export-job-response
- name: ExportRequest
  property_count: 6
  slug: peaka-export-request
- name: QueryExecuteRequest
  property_count: 7
  slug: peaka-query-execute-request
- name: QueryRequest
  property_count: 6
  slug: peaka-query-request
- name: Table
  property_count: 8
  slug: peaka-table
jsonld:
- class_count: 86
  name: Peaka Context
  property_count: 185
  slug: peaka-context
layout: provider
modified: '2026-10-21'
name: Peaka
nav: Providers
network: true
overview: 'Peaka publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Gateway API API, and 1 more. Tagged areas include Company, Data Integration, Governance, and Analytics.


  The Peaka catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Peaka''s developer surface includes authentication, pricing, changelog, engineering blog, documentation, API reference, and 19 more developer resources.'
plans:
- name: Peaka Plans Pricing
  plan_count: 3
  slug: peaka-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Peaka API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: peaka-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 46.1
    contract_governance: 35.6
    contract_quality: 57.3
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 52.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/peaka/peaka-2026-11-03T141041.png
security:
- kind: authentication
  name: Peaka Authentication
  slug: peaka-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Peaka Domain Security
  slug: peaka-domain-security
  summary_line: TLSv1.3 · DMARC
slug: peaka
tags:
- Company
- Data Integration
- Governance
- Analytics
website: https://peaka.com/
---
