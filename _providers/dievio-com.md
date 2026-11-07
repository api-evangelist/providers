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
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic access to search and export leads via Dievio's B2B lead generation platform.
  name: Dievio API
  slug: dievio-api
- baseURL: https://dievio.com
  baseurl_source: declared
  description: 'Dievio API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dievio API
  slug: dievio-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/dievio-com/plans/dievio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dievio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dievio-com/rules/dievio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dievio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dievio-com/json-ld/dievio-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dievio-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dievio-com/vocabulary/dievio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dievio-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dievio-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dievio-com/data-model/dievio-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dievio-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dievio-com/conventions/dievio-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dievio-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dievio-com/authentication/dievio-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dievio-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dievio-com/conformance/dievio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dievio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dievio-com/llms/dievio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dievio-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dievio-com/well-known/dievio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dievio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dievio-com/hosts/dievio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dievio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dievio-com/vendors/dievio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dievio-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dievio.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dievio.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dievio.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://dievio.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://dievio.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dievio.com/api-reference/search
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dievio.com/getting-started/overview
- group: auth
  href: https://artifacts.apis.io/dievio-com/security/dievio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dievio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dievio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/59401719/2sBYHXQJMH
coverage:
  checked: '2026-11-05'
  detail: Documentation is public but no OpenAPI/AsyncAPI/GraphQL spec could be found despite probing known paths.
  evidence:
  - status: 200
    url: https://docs.dievio.com/api-reference/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dievio provides a B2B lead generation platform that enables users to build targeted contact lists using advanced filters for company data, email addresses, phone numbers, and LinkedIn profiles. The service offers a free tier and paid plans with higher limits, and includes an API for programmatic access to search and export leads. It positions itself as a data enrichment tool for sales and marketing teams, emphasizing ease of use and integration capabilities across various workflows.
image: https://dievio.com/hero-dashboard-dark.png
json_schemas:
- name: PostApiLinkedinExportRequest
  property_count: 9
  slug: dievio-com-post-api-linkedin-export-request
- name: PostApiLinkedinExportResponse
  property_count: 2
  slug: dievio-com-post-api-linkedin-export-response
- name: PostApiPreviewRequest
  property_count: 3
  slug: dievio-com-post-api-preview-request
- name: PostApiPublicSearchRequest
  property_count: 4
  slug: dievio-com-post-api-public-search-request
- name: PostApiPublicSearchResponse
  property_count: 14
  slug: dievio-com-post-api-public-search-response
jsonld:
- class_count: 5
  name: Dievio Com Context
  property_count: 27
  slug: dievio-com-context
layout: provider
modified: '2026-11-05'
name: Dievio
nav: Providers
network: true
overview: 'Dievio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Lead Generation, Sales, Marketing, and Data.


  The Dievio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dievio''s developer surface includes authentication, support, pricing, engineering blog, API reference, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Dievio Com Plans Pricing
  plan_count: 4
  slug: dievio-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Dievio API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: dievio-com-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 54.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dievio Com Authentication
  slug: dievio-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dievio Com Domain Security
  slug: dievio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dievio-com
tags:
- B2B
- Lead Generation
- Sales
- Marketing
- Data
website: https://dievio.com/
---
