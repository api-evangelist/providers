---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: FinetuneDB provides an AI fine‑tuning platform with endpoints for datasets, fine‑tuning jobs, model serving and evaluations.
  name: FinetuneDB API
  slug: finetunedb-api-2
- baseURL: https://app.finetunedb.com/api/v1
  baseurl_source: declared
  description: 'FinetuneDB API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: FinetuneDB API
  slug: finetunedb-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/finetunedb/plans/finetunedb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finetunedb-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/finetunedb/rules/finetunedb-rules.yml
  title: ''
  type: Spectral
  url: rules/finetunedb-rules.yml
- group: design
  href: https://artifacts.apis.io/finetunedb/json-ld/finetunedb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/finetunedb-context.jsonld
- group: design
  href: https://artifacts.apis.io/finetunedb/vocabulary/finetunedb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/finetunedb-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/finetunedb/data-model/finetunedb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finetunedb-data-model.yml
- group: design
  href: https://artifacts.apis.io/finetunedb/conformance/finetunedb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finetunedb-conformance.yml
- group: agent
  href: https://artifacts.apis.io/finetunedb/llms/finetunedb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finetunedb-llms.txt
- group: other
  href: https://artifacts.apis.io/finetunedb/a2a/finetunedb-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/finetunedb-a2a.yml
- group: agent
  href: https://artifacts.apis.io/finetunedb/well-known/finetunedb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finetunedb-well-known.yml
- group: other
  href: https://artifacts.apis.io/finetunedb/hosts/finetunedb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finetunedb-hosts.yml
- group: other
  href: https://artifacts.apis.io/finetunedb/vendors/finetunedb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finetunedb-vendors.yml
- group: build
  href: https://artifacts.apis.io/finetunedb/packages/finetunedb-packages.yml
  title: ''
  type: SDKs
  url: packages/finetunedb-packages.yml
- group: build
  href: https://artifacts.apis.io/finetunedb/packages/finetunedb-packages.yml
  title: ''
  type: Packages
  url: packages/finetunedb-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finetunedb
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.finetunedb.com/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finetunedb.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/finetunedb/security/finetunedb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finetunedb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finetunedb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finetunedb.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://finetunedb.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://finetunedb.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finetunedb.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finetunedb.com/privacy-policy
coverage:
  checked: '2026-10-20'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL files were found on the provider's hosts.
  evidence:
  - status: 200
    url: https://docs.finetunedb.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: FinetuneDB provides an AI fine‑tuning platform that enables users to build custom large language models quickly using their own data. The service offers collaborative dataset editing, model management, and secure deployment, targeting developers and enterprises seeking to improve performance and reduce costs. FinetuneDB was recently acquired by Opper AI, expanding its capabilities and market reach. The platform includes features such as multi‑model handling, security controls, pricing tiers, extensive documentation, and use‑case case studies.
image: https://finetunedb.com/assets/images/graphics/sharing-image.png
json_schemas:
- name: PostLogsRequest
  property_count: 14
  slug: finetunedb-post-logs-request
jsonld:
- class_count: 1
  name: Finetunedb Context
  property_count: 14
  slug: finetunedb-context
layout: provider
modified: '2026-10-20'
name: FinetuneDB
nav: Providers
network: true
overview: 'FinetuneDB is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Platform, and Fine-Tuning.


  The FinetuneDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FinetuneDB''s developer surface includes getting-started guide, API reference, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Finetunedb Plans Pricing
  plan_count: 3
  slug: finetunedb-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: FinetuneDB API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: finetunedb-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 20.9
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.7
  provenance:
    conformance: derived
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/finetunedb/finetunedb-2026-11-03T132027.png
security:
- kind: domain-security
  name: Finetunedb Domain Security
  slug: finetunedb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finetunedb
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Platform
- Fine-Tuning
website: https://finetunedb.com/
---
