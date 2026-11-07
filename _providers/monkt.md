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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Comprehensive API documentation for Monkt's document transformation services.
  name: Monkt API
  slug: monkt-api-2
- description: 'Monkt API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Monkt API
  slug: monkt-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/monkt/rules/monkt-rules.yml
  title: ''
  type: Spectral
  url: rules/monkt-rules.yml
- group: design
  href: https://artifacts.apis.io/monkt/json-ld/monkt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monkt-context.jsonld
- group: design
  href: https://artifacts.apis.io/monkt/vocabulary/monkt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monkt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/monkt/data-model/monkt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monkt-data-model.yml
- group: design
  href: https://artifacts.apis.io/monkt/conformance/monkt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monkt-conformance.yml
- group: other
  href: https://artifacts.apis.io/monkt/hosts/monkt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monkt-hosts.yml
- group: other
  href: https://artifacts.apis.io/monkt/vendors/monkt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monkt-vendors.yml
- group: build
  href: https://artifacts.apis.io/monkt/packages/monkt-packages.yml
  title: ''
  type: SDKs
  url: packages/monkt-packages.yml
- group: build
  href: https://artifacts.apis.io/monkt/packages/monkt-packages.yml
  title: ''
  type: Packages
  url: packages/monkt-packages.yml
- group: start
  title: ''
  type: Login
  url: https://monkt.com/accounts/login/
- group: auth
  href: https://artifacts.apis.io/monkt/security/monkt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monkt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monkt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://monkt.com/api/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://monkt.com/api/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://monkt.com/api/documentation/
- group: company
  title: ''
  type: Blog
  url: https://monkt.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://monkt.com/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monkt.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monkt.com/terms/
coverage:
  checked: '2026-10-18'
  detail: API documentation is provided as HTML pages without a downloadable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://monkt.com/api/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Monkt provides a platform that transforms documents such as PDFs, Word files, PowerPoint presentations, Excel spreadsheets, CSVs, web pages, and raw HTML into clean, AI‑ready markdown or structured JSON. The service enables developers to quickly convert content for use with large language models, build intelligent chatbots, and create AI‑powered applications. Features include file upload, URL ingestion, and a suite of conversion recipes covering a wide range of document types, all accessible via a web interface and API.
image: https://monkt.com/static/images/website.3bdde4aa1b77.jpg
json_schemas:
- name: PostApiPromptsRequest
  property_count: 3
  slug: monkt-post-api-prompts-request
- name: PostApiSchemasRequest
  property_count: 2
  slug: monkt-post-api-schemas-request
- name: PostArticleRequest
  property_count: 1
  slug: monkt-post-article-request
jsonld:
- class_count: 3
  name: Monkt Context
  property_count: 4
  slug: monkt-context
layout: provider
modified: '2026-10-18'
name: Monkt
nav: Providers
network: true
overview: 'Monkt is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Document Processing, and Automation.


  The Monkt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Monkt''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Monkt API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: monkt-rules
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 27.3
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/monkt/monkt-2026-11-03T135839.png
security:
- kind: domain-security
  name: Monkt Domain Security
  slug: monkt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: monkt
tags:
- Company
- Artificial Intelligence
- Document Processing
- Automation
website: https://monkt.com/
---
