---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cafedev Co Agentic Access
  operation_count: 4
  slug: cafedev-co-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.cafedev.co/v1
  baseurl_source: declared
  description: The Companies API from CafeDev — 2 operation(s) for companies.
  name: CafeDev Companies API
  slug: cafedev-co-companies-api
- baseURL: https://api.cafedev.co/v1
  baseurl_source: declared
  description: The Jobs API from CafeDev — 2 operation(s) for jobs.
  name: CafeDev Jobs API
  slug: cafedev-co-jobs-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/cafedev-co/agentic-access/cafedev-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cafedev-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cafedev-co/rules/cafedev-co-rules.yml
  title: ''
  type: Spectral
  url: rules/cafedev-co-rules.yml
- group: design
  href: https://artifacts.apis.io/cafedev-co/json-ld/cafedev-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cafedev-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/cafedev-co/vocabulary/cafedev-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cafedev-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cafedev-co/data-model/cafedev-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cafedev-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/cafedev-co/errors/cafedev-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cafedev-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cafedev-co/conformance/cafedev-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cafedev-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cafedev-co/llms/cafedev-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cafedev-co-llms.txt
- group: other
  href: https://artifacts.apis.io/cafedev-co/hosts/cafedev-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cafedev-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/cafedev-co/vendors/cafedev-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cafedev-co-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.cafedev.co/docs
- group: company
  title: ''
  type: Blog
  url: https://cafedev.co/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://cafedev.co/developers/
- group: auth
  href: https://artifacts.apis.io/cafedev-co/security/cafedev-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cafedev-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cafedev.co/
created: '2026-11-03'
description: CafeDev is a job aggregation platform focused on tech roles in Latin America. It collects real tech job listings directly from company career pages and hiring platforms, presenting them in Spanish with filters for remote, technology, and seniority. The service is free for job seekers, without sponsored listings, and provides email alerts for new matches.
json_schemas:
- name: Company
  property_count: 11
  slug: cafedev-co-company
- name: JobDetail
  property_count: 26
  slug: cafedev-co-job-detail
- name: Job
  property_count: 21
  slug: cafedev-co-job
jsonld:
- class_count: 3
  name: Cafedev Co Context
  property_count: 32
  slug: cafedev-co-context
layout: provider
modified: '2026-11-03'
name: CafeDev
nav: Providers
network: true
overview: 'CafeDev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Companies API and Jobs API. Tagged areas include Company, Technology, Job, Latin America, and Aggregator.


  The CafeDev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CafeDev''s developer surface includes documentation, engineering blog, API reference, and 12 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: CafeDev API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: cafedev-co-rules
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 49.5
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cafedev Co Domain Security
  slug: cafedev-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cafedev-co
tags:
- Company
- Technology
- Job
- Latin America
- Aggregator
- Free
website: https://cafedev.co/
---
