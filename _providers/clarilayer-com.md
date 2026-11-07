---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for ClariLayer providing access to memory layer features for AI applications.
  name: ClariLayer API
  slug: clarilayer-api
- baseURL: https://app.clarilayer.com
  baseurl_source: declared
  description: 'ClariLayer API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ClariLayer API
  slug: clarilayer-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/clarilayer-com/rules/clarilayer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/clarilayer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/clarilayer-com/json-ld/clarilayer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clarilayer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/clarilayer-com/vocabulary/clarilayer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clarilayer-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clarilayer-com/data-model/clarilayer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clarilayer-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/clarilayer-com/cli/clarilayer-com-cli.yml
  title: ''
  type: CLI
  url: cli/clarilayer-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/clarilayer-com/authentication/clarilayer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clarilayer-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/clarilayer-com/conformance/clarilayer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clarilayer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clarilayer-com/llms/clarilayer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clarilayer-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/clarilayer-com/well-known/clarilayer-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarilayer-com-security.txt
- group: auth
  href: https://artifacts.apis.io/clarilayer-com/well-known/clarilayer-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clarilayer-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/clarilayer-com/well-known/clarilayer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clarilayer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clarilayer-com/hosts/clarilayer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clarilayer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clarilayer-com/vendors/clarilayer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clarilayer-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarilayer.com/terms
- group: auth
  title: ''
  type: Security
  url: https://clarilayer.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarilayer.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clarilayer.com/pricing
- group: start
  title: ''
  type: Login
  url: https://clarilayer.com/auth/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://clarilayer.com/docs
- group: company
  title: ''
  type: Blog
  url: https://clarilayer.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://clarilayer.com/docs/reference/saas-metrics
- group: start
  title: ''
  type: GettingStarted
  url: https://clarilayer.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/clarilayer-com/security/clarilayer-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clarilayer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clarilayer-com/security/clarilayer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarilayer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clarilayer.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation is public but no machine‑readable OpenAPI, GraphQL or AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://clarilayer.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ClariLayer provides a memory layer for AI applications, allowing selected past conversations, decisions, rules, and preferences to be stored and recalled across projects and sessions. It offers durable work context with source and applicability, optional separate authorization, and integrates via MCP with Claude AI and compatible clients. The service is free, hosted on a web platform, and includes features like corrections, scoped forgetting, and specialist analytics integration.
image: https://clarilayer.com/opengraph-image?v=3
json_schemas:
- name: DeleteApiApiKeys11111111222243338444555555555555Response
  property_count: 1
  slug: clarilayer-com-delete-api-api-keys11111111222243338444555555555555-response
- name: GetApiV1MetricsIdContractResponse
  property_count: 2
  slug: clarilayer-com-get-api-v1-metrics-id-contract-response
- name: GetApiV1MetricsIdResponse
  property_count: 2
  slug: clarilayer-com-get-api-v1-metrics-id-response
- name: GetApiV1MetricsResponse
  property_count: 3
  slug: clarilayer-com-get-api-v1-metrics-response
jsonld:
- class_count: 4
  name: Clarilayer Com Context
  property_count: 4
  slug: clarilayer-com-context
layout: provider
modified: '2026-11-03'
name: ClariLayer
nav: Providers
network: true
overview: 'ClariLayer is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The ClariLayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClariLayer''s developer surface includes CLI, authentication, pricing, documentation, engineering blog, API reference, getting-started guide, and 18 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: ClariLayer API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: clarilayer-com-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 34.5
    discoverability: 55.4
    operational_transparency: 5.3
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clarilayer Com Authentication
  slug: clarilayer-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Clarilayer Com Domain Security
  slug: clarilayer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Clarilayer Com Vulnerability Disclosure
  slug: clarilayer-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clarilayer-com
tags:
- Company
website: https://clarilayer.com/
---
