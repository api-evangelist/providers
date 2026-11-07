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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.bridgetown.builders
  baseurl_source: declared
  description: 'Bridge Town core API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bridge Town core API
  slug: core-api
- baseURL: https://api.bridgetown.builders
  baseurl_source: declared
  description: 'Bridge Town getting started API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bridge Town getting started API
  slug: getting-started-api
- baseURL: https://api.bridgetown.builders
  baseurl_source: declared
  description: 'Bridge Town guides API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Bridge Town guides API
  slug: guides-api
artifact_total: 19
common:
- group: commercial
  href: https://artifacts.apis.io/bridgetown-builders/plans/bridgetown-builders-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bridgetown-builders-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bridgetown-builders/rules/bridgetown-builders-rules.yml
  title: ''
  type: Spectral
  url: rules/bridgetown-builders-rules.yml
- group: design
  href: https://artifacts.apis.io/bridgetown-builders/json-ld/bridgetown-builders-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bridgetown-builders-context.jsonld
- group: design
  href: https://artifacts.apis.io/bridgetown-builders/vocabulary/bridgetown-builders-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bridgetown-builders-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bridgetown-builders/data-model/bridgetown-builders-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bridgetown-builders-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bridgetown.builders/security
- group: auth
  href: https://artifacts.apis.io/bridgetown-builders/authentication/bridgetown-builders-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bridgetown-builders-authentication.yml
- group: design
  href: https://artifacts.apis.io/bridgetown-builders/conformance/bridgetown-builders-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bridgetown-builders-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bridgetown-builders/llms/bridgetown-builders-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bridgetown-builders-llms.txt
- group: auth
  href: https://artifacts.apis.io/bridgetown-builders/well-known/bridgetown-builders-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bridgetown-builders-security.txt
- group: auth
  href: https://artifacts.apis.io/bridgetown-builders/well-known/bridgetown-builders-bridgetown-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bridgetown-builders-bridgetown-security.txt
- group: agent
  href: https://artifacts.apis.io/bridgetown-builders/well-known/bridgetown-builders-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bridgetown-builders-well-known.yml
- group: other
  href: https://artifacts.apis.io/bridgetown-builders/hosts/bridgetown-builders-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgetown-builders-hosts.yml
- group: other
  href: https://artifacts.apis.io/bridgetown-builders/vendors/bridgetown-builders-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridgetown-builders-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bridgetown.builders/status
- group: auth
  title: ''
  type: Security
  url: https://www.bridgetown.builders/security
- group: start
  title: ''
  type: Login
  url: https://www.bridgetown.builders/signin
- group: auth
  href: https://artifacts.apis.io/bridgetown-builders/security/bridgetown-builders-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bridgetown-builders-trust-center.yml
- group: other
  title: ''
  type: Image
  url: https://www.bridgetown.builders/og/home.png
- group: docs
  title: ''
  type: Documentation
  url: https://www.bridgetown.builders/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bridgetown.builders/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bridgetown.builders/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.bridgetown.builders/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bridgetown.builders/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bridgetown.builders/privacy
- group: auth
  href: https://artifacts.apis.io/bridgetown-builders/security/bridgetown-builders-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bridgetown-builders-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bridgetown-builders/security/bridgetown-builders-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgetown-builders-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgetown.builders/
coverage:
  checked: '2026-11-03'
  detail: GraphQL endpoint https://api.bridgetown.builders/graphql returns 401 Unauthorized, requiring authentication.
  evidence:
  - status: 401
    url: https://api.bridgetown.builders/graphql
  reason: auth-required
  state: gated
created: '2026-11-03'
description: Bridge Town, built by Knightian Labs, offers version‑controlled financial planning and analysis (FP&A) tools. It provides AI‑assisted, transparent, durable financial models for finance teams, enabling collaborative budgeting, forecasting, and scenario analysis with version history and auditability. The platform emphasizes data integrity, security, and ease of integration with existing financial data sources, aiming to modernize corporate finance workflows.
image: https://www.bridgetown.builders/og/home.png
json_schemas:
- name: GetApiFeedResponse
  property_count: 2
  slug: bridgetown-builders-get-api-feed-response
- name: PatchApiTenantRequest
  property_count: 1
  slug: bridgetown-builders-patch-api-tenant-request
- name: PostApiInvitesRequest
  property_count: 2
  slug: bridgetown-builders-post-api-invites-request
- name: PostApiModelsModelnameDataSourcesUploadSessionsRequest
  property_count: 5
  slug: bridgetown-builders-post-api-models-modelname-data-sources-upload-sessions-request
- name: PostApiModelsModelnameDataSourcesUploadSessionsResponse
  property_count: 6
  slug: bridgetown-builders-post-api-models-modelname-data-sources-upload-sessions-response
- name: PostApiModelsModelnameExcelConversionsUploadSessionsResponse
  property_count: 3
  slug: bridgetown-builders-post-api-models-modelname-excel-conversions-upload-sessions-response
- name: PostApiModelsModelnameRunsResponse
  property_count: 7
  slug: bridgetown-builders-post-api-models-modelname-runs-response
- name: PostApiTokensRequest
  property_count: 2
  slug: bridgetown-builders-post-api-tokens-request
- name: PostMcpRequest
  property_count: 3
  slug: bridgetown-builders-post-mcp-request
jsonld:
- class_count: 15
  name: Bridgetown Builders Context
  property_count: 32
  slug: bridgetown-builders-context
layout: provider
modified: '2026-11-03'
name: Bridge Town
nav: Providers
network: true
overview: 'Bridge Town is listed with 3 APIs on the [APIs.io](https://apis.io/) network: core API, getting started API, and guides API. Tagged areas include Finance, Artificial Intelligence, FP&A, Collaboration, and Version Control.


  The Bridge Town catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bridge Town''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Bridgetown Builders Plans Pricing
  plan_count: 2
  slug: bridgetown-builders-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Bridge Town API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: bridgetown-builders-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 23.8
    discoverability: 71.4
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bridgetown Builders Authentication
  slug: bridgetown-builders-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bridgetown Builders Domain Security
  slug: bridgetown-builders-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Bridgetown Builders Vulnerability Disclosure
  slug: bridgetown-builders-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bridgetown Builders Trust Center
  slug: bridgetown-builders-trust-center
  summary_line: SOC 2, GDPR
slug: bridgetown-builders
tags:
- Finance
- Artificial Intelligence
- FP&A
- Collaboration
- Version Control
- Company
website: https://bridgetown.builders/
---
