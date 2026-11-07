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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Send a task to one of your Crew agents and read the result.
  name: Dooza Crew Task API
  slug: dooza-crew-task-api
- baseURL: https://crew.dooza.ai
  baseurl_source: declared
  description: 'Send a task to one of your Crew agents and read the result. Get your API key in the app: account menu > API key.'
  name: Dooza Crew Task API V1 API
  slug: dooza-crew-task-api-v1-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/dooza-ai/rules/dooza-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dooza-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dooza-ai/json-ld/dooza-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dooza-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/dooza-ai/vocabulary/dooza-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dooza-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dooza-ai/conformance/dooza-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dooza-ai-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/dooza-ai/plans/dooza-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dooza-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dooza-ai/data-model/dooza-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dooza-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/dooza-ai/errors/dooza-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dooza-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dooza-ai/llms/dooza-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dooza-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/dooza-ai/hosts/dooza-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dooza-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dooza-ai/vendors/dooza-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dooza-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dooza.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dooza.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dooza.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://crew.dooza.ai/login
- group: company
  title: ''
  type: Blog
  url: https://www.dooza.ai/blog
- group: auth
  href: https://artifacts.apis.io/dooza-ai/security/dooza-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dooza-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dooza.ai/
created: '2026-11-05'
description: Dooza is an AI-native company that builds AI products and services for small businesses, including AI employees that have their own computer and browser. It offers Dooza Crew, custom AI agents, and managed AI services, providing automation for marketing, sales, support, and operations. The platform enables businesses to deploy AI employees that work alongside human staff, with real-time oversight and approval workflows.
image: https://www.dooza.ai/logo.png
json_schemas:
- name: Task
  property_count: 7
  slug: dooza-ai-task
jsonld:
- class_count: 1
  name: Dooza Ai Context
  property_count: 7
  slug: dooza-ai-context
layout: provider
modified: '2026-11-05'
name: Dooza
nav: Providers
network: true
overview: 'Dooza publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Crew Task API V1 API, and 1 more. Tagged areas include AI Employees, Automation, Customer Service, Insurance, and Trucking.


  The Dooza catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dooza''s developer surface includes pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Dooza Ai Plans Pricing
  plan_count: 2
  slug: dooza-ai-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Dooza API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: dooza-ai-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.2
    catalog_earned_first_party: 8.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 43.2
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dooza Ai Domain Security
  slug: dooza-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dooza-ai
tags:
- AI Employees
- Automation
- Customer Service
- Insurance
- Trucking
- Legal
- Medical Billing
website: https://dooza.ai/
---
