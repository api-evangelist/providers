---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Trydatabook Com Agentic Access
  operation_count: 14
  slug: trydatabook-com-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.databook.com
  baseurl_source: declared
  description: DatabookAI REST API integrates DatabookAI's intelligence into applications.
  name: DatabookAI REST API
  slug: databookai-rest-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/trydatabook-com/agentic-access/trydatabook-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trydatabook-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/trydatabook-com/rules/trydatabook-com-rules.yml
  title: ''
  type: Spectral
  url: rules/trydatabook-com-rules.yml
- group: design
  href: https://artifacts.apis.io/trydatabook-com/json-ld/trydatabook-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trydatabook-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/trydatabook-com/vocabulary/trydatabook-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trydatabook-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trydatabook-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trydatabook-com/data-model/trydatabook-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trydatabook-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/trydatabook-com/errors/trydatabook-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trydatabook-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trydatabook-com/conformance/trydatabook-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trydatabook-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/trydatabook-com/overlays/trydatabook-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trydatabook-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trydatabook-com/llms/trydatabook-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trydatabook-com-llms.txt
- group: other
  href: https://artifacts.apis.io/trydatabook-com/hosts/trydatabook-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trydatabook-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trydatabook-com/vendors/trydatabook-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trydatabook-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://databook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://databook.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://trydatabook.com/blog/
- group: auth
  href: https://artifacts.apis.io/trydatabook-com/authentication/trydatabook-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trydatabook-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trydatabook-com/security/trydatabook-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trydatabook-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://databook.com/
created: '2026-10-25'
description: Databook provides a data platform that aggregates, normalizes, and delivers business intelligence datasets via APIs. Founded to simplify access to curated data, it serves enterprises seeking reliable, up-to-date information for analytics, reporting, and decision-making. Backed by notable venture partners, Databook focuses on scalability, security, and developer-friendly integrations.
image: https://databook.com/images/og/home-gtm-decision-system.jpg
json_schemas:
- name: ChatRequest
  property_count: 2
  slug: trydatabook-com-chat-request
- name: GeneratedAssetItem
  property_count: 9
  slug: trydatabook-com-generated-asset-item
- name: GetJobByIdResponse
  property_count: 6
  slug: trydatabook-com-get-job-by-id-response
- name: LibraryListItem
  property_count: 5
  slug: trydatabook-com-library-list-item
- name: PostReasoningResponse
  property_count: 4
  slug: trydatabook-com-post-reasoning-response
- name: TypesenseSearchResult
  property_count: 4
  slug: trydatabook-com-typesense-search-result
jsonld:
- class_count: 34
  name: Trydatabook Com Context
  property_count: 47
  slug: trydatabook-com-context
layout: provider
modified: '2026-10-25'
name: Databook
nav: Providers
network: true
overview: 'Databook publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: DatabookAI REST API. Tagged areas include Company, Data Platform, Business Intelligence, APIs, and Venture-backed.


  The Databook catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Databook''s developer surface includes engineering blog, authentication, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Databook API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: trydatabook-com-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 60.7
    developer_ergonomics: 16.1
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Trydatabook Com Authentication
  slug: trydatabook-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trydatabook Com Domain Security
  slug: trydatabook-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: trydatabook-com-batch-create-job
  slug: trydatabook-com-batch-create-job
- name: trydatabook-com-generate-and-retrieve-asset
  slug: trydatabook-com-generate-and-retrieve-asset
slug: trydatabook-com
tags:
- Company
- Data Platform
- Business Intelligence
- APIs
- Venture-backed
website: https://databook.com/
---
