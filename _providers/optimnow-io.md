---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Optimnow Io Agentic Access
  operation_count: 2
  slug: optimnow-io-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://optimtoken.optimnow.io
  baseurl_source: declared
  description: The Llm Models API from optimnow-io — 1 operation(s) for llm models.
  name: optimnow-io Llm Models API
  slug: optimnow-io-llm-models-api
- baseURL: https://optimtoken.optimnow.io
  baseurl_source: declared
  description: The Pricing API from optimnow-io — 1 operation(s) for pricing.
  name: optimnow-io Pricing API
  slug: optimnow-io-pricing-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/optimnow-io/agentic-access/optimnow-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optimnow-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/optimnow-io/rules/optimnow-io-rules.yml
  title: ''
  type: Spectral
  url: rules/optimnow-io-rules.yml
- group: design
  href: https://artifacts.apis.io/optimnow-io/json-ld/optimnow-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/optimnow-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/optimnow-io/vocabulary/optimnow-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/optimnow-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/optimnow-io/data-model/optimnow-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/optimnow-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/optimnow-io/conformance/optimnow-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optimnow-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/optimnow-io/llms/optimnow-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimnow-io-llms.txt
- group: other
  href: https://artifacts.apis.io/optimnow-io/hosts/optimnow-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/optimnow-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/optimnow-io/vendors/optimnow-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/optimnow-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.optimnow.io/news
- group: auth
  href: https://artifacts.apis.io/optimnow-io/security/optimnow-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optimnow-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://optimnow.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.optimnow.io/guide
- group: docs
  title: ''
  type: Documentation
  url: https://www.optimnow.io/guide
- group: docs
  title: ''
  type: APIReference
  url: https://optimtoken.optimnow.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.optimnow.io/guide
- group: operate
  title: ''
  type: Support
  url: https://www.optimnow.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.optimnow.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OptimNow
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimnow.io/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimnow.io/privacypolicy
created: '2026-10-30'
description: OptimNow provides smart cloud financial operations (FinOps) services, leveraging AI-driven insights to help businesses optimize cloud spend, improve sustainability, and accelerate cost savings. Their offerings include cloud assessment, rapid optimization, governance, and ongoing enablement, targeting enterprises seeking measurable cloud cost reductions and sustainable operations.
image: https://static.wixstatic.com/media/891cf4_2661b26bd0c846139586dd6eeab8b146%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/891cf4_2661b26bd0c846139586dd6eeab8b146%7Emv2.jpg
json_schemas:
- name: ComputeInstance
  property_count: 0
  slug: optimnow-io-compute-instance
- name: LLMMeta
  property_count: 0
  slug: optimnow-io-llmmeta
- name: LLMModel
  property_count: 11
  slug: optimnow-io-llmmodel
- name: PricingMeta
  property_count: 0
  slug: optimnow-io-pricing-meta
jsonld:
- class_count: 1
  name: Optimnow Io Context
  property_count: 11
  slug: optimnow-io-context
layout: provider
modified: '2026-10-30'
name: optimnow-io
nav: Providers
network: true
overview: 'optimnow-io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Llm Models API and Pricing API. Tagged areas include Company, FinOps, CloudOptimization, AI, and Sustainability.


  The optimnow-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  optimnow-io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: optimnow-io API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: optimnow-io-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 56.3
    developer_ergonomics: 45.2
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Optimnow Io Domain Security
  slug: optimnow-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: optimnow-io
tags:
- Company
- FinOps
- CloudOptimization
- AI
- Sustainability
website: https://optimnow.io/
---
