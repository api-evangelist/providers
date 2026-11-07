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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DeepSFetch public API providing scraping, extraction, search and other web automation operations.
  name: DeepSFetch API
  slug: deepsfetch-api
- baseURL: https://api.deepsfetch.com
  baseurl_source: declared
  description: 'DeepSFetch public API and machine integration contracts. Dashboard-domain adapters declare their own servers. Provider limitations and operational guides: https://deepsfetch.com/docs'
  name: DeepSFetch API API
  slug: deepsfetch-api-api
artifact_total: 14
asyncapis:
- description: ''
  name: Deepsfetch Com Webhooks
  slug: deepsfetch-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/rules/deepsfetch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/deepsfetch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/json-ld/deepsfetch-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deepsfetch-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/vocabulary/deepsfetch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deepsfetch-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/conformance/deepsfetch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deepsfetch-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/deepsfetch-com/plans/deepsfetch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepsfetch-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/asyncapi/deepsfetch-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deepsfetch-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/data-model/deepsfetch-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deepsfetch-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/deepsfetch-com/cli/deepsfetch-com-cli.yml
  title: ''
  type: CLI
  url: cli/deepsfetch-com-cli.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/conventions/deepsfetch-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/deepsfetch-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/conventions/deepsfetch-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deepsfetch-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/deepsfetch-com/authentication/deepsfetch-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deepsfetch-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/deepsfetch-com/errors/deepsfetch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deepsfetch-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/deepsfetch-com/llms/deepsfetch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepsfetch-com-llms.txt
- group: other
  href: https://artifacts.apis.io/deepsfetch-com/hosts/deepsfetch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepsfetch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepsfetch-com/vendors/deepsfetch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepsfetch-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepsfetch.com/terms
- group: operate
  title: ''
  type: Support
  url: https://deepsfetch.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://deepsfetch.com/status
- group: start
  title: ''
  type: SignUp
  url: https://deepsfetch.com/signup
- group: start
  title: ''
  type: Sandbox
  url: https://deepsfetch.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepsfetch.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://deepsfetch.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://deepsfetch.com/docs/getting-started?lang=pt-BR
- group: docs
  title: ''
  type: APIReference
  url: https://deepsfetch.com/docs
- group: auth
  href: https://artifacts.apis.io/deepsfetch-com/security/deepsfetch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepsfetch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepsfetch.com/
created: '2026-11-05'
description: DeepSFetch offers a REST API that extracts web data for developers and AI agents. It provides operations to scrape, crawl, map, search and monitor public websites, returning clean Markdown, HTML or validated JSON. The platform includes features such as collections, change monitoring, structured extraction schemas, usage estimates and credit caps.
json_schemas:
- name: InteractRequest
  property_count: 14
  slug: deepsfetch-com-interact-request
- name: Job
  property_count: 9
  slug: deepsfetch-com-job
- name: N8nConfig
  property_count: 6
  slug: deepsfetch-com-n8n-config
- name: ScrapeRequest
  property_count: 18
  slug: deepsfetch-com-scrape-request
- name: SearchRequest
  property_count: 13
  slug: deepsfetch-com-search-request
- name: UrlJobRequest
  property_count: 15
  slug: deepsfetch-com-url-job-request
jsonld:
- class_count: 9
  name: Deepsfetch Com Context
  property_count: 41
  slug: deepsfetch-com-context
layout: provider
modified: '2026-11-05'
name: DeepSFetch
nav: Providers
network: true
overview: 'DeepSFetch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Data Extraction, AI Integration, Monitoring, and Collection.


  The DeepSFetch catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DeepSFetch''s developer surface includes CLI, authentication, support, signup flow, sandbox, pricing, getting-started guide, and 19 more developer resources.'
plans:
- name: Deepsfetch Com Plans Pricing
  plan_count: 4
  slug: deepsfetch-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DeepSFetch API Rules
  rule_count: 45
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 3
  slug: deepsfetch-com-rules
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 50.0
    discoverability: 53.6
    operational_transparency: 23.7
  provenance:
    conformance: derived
    mcp: derived
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
  name: Deepsfetch Com Authentication
  slug: deepsfetch-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Deepsfetch Com Domain Security
  slug: deepsfetch-com-domain-security
  summary_line: TLSv1.3
slug: deepsfetch-com
tags:
- Data Extraction
- AI Integration
- Monitoring
- Collection
website: https://deepsfetch.com/
---
