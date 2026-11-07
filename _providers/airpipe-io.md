---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: API reference for AirPipe platform, documented at the developer docs.
  name: AirPipe API
  slug: airpipe-api
- baseURL: https://app.airpipe.io
  baseurl_source: declared
  description: 'Air Pipe Examples API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Air Pipe Examples API
  slug: examples-api
- baseURL: https://app.airpipe.io
  baseurl_source: declared
  description: 'Air Pipe tutorial API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Air Pipe tutorial API
  slug: tutorial-api
artifact_total: 20
common:
- group: operate
  href: https://artifacts.apis.io/airpipe-io/rate-limits/airpipe-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airpipe-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/airpipe-io/rules/airpipe-io-rules.yml
  title: ''
  type: Spectral
  url: rules/airpipe-io-rules.yml
- group: design
  href: https://artifacts.apis.io/airpipe-io/json-ld/airpipe-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/airpipe-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/airpipe-io/vocabulary/airpipe-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/airpipe-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/airpipe-io/data-model/airpipe-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airpipe-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/airpipe-io/authentication/airpipe-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airpipe-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/airpipe-io/conformance/airpipe-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airpipe-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/airpipe-io/llms/airpipe-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airpipe-io-llms.txt
- group: other
  href: https://artifacts.apis.io/airpipe-io/hosts/airpipe-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airpipe-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/airpipe-io/vendors/airpipe-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airpipe-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airpipe.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airpipe.io/privacy/
- group: company
  title: ''
  type: Blog
  url: https://airpipe.io/blog/
- group: auth
  href: https://artifacts.apis.io/airpipe-io/security/airpipe-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airpipe-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airpipe.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airpipe.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airpipe.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.airpipe.io/docs/install
- group: commercial
  title: ''
  type: Pricing
  url: https://airpipe.io/#pricing
coverage:
  detail: Documentation is served as JavaScript-rendered pages, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://docs.airpipe.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Air Pipe provides a unified backend platform for building APIs, workflow automation, and AI agents. It offers a single binary service with built‑in OpenAPI, Prometheus metrics, OpenTelemetry tracing, webhooks, real‑time MQTT/WebSocket support, and MCP tool integration. Users can self‑host or run in the cloud, configure authentication via JWT or API keys, and leverage AI‑assisted config generation. The platform targets backend engineers, B2B API teams, and AI/MCP developers, emphasizing extensibility, observability, and secure defaults.
image: https://airpipe.io/banner1.jpg
json_schemas:
- name: GetGraphqlUsersResponse
  property_count: 4
  slug: airpipe-io-get-graphql-users-response
- name: GetTutorialCsvCatToApiResponse
  property_count: 1
  slug: airpipe-io-get-tutorial-csv-cat-to-api-response
- name: GetTutorialJsonCatToApiResponse
  property_count: 2
  slug: airpipe-io-get-tutorial-json-cat-to-api-response
- name: GetTutorialXmlCatToApiResponse
  property_count: 1
  slug: airpipe-io-get-tutorial-xml-cat-to-api-response
- name: PostApiPostsCreateRequest
  property_count: 6
  slug: airpipe-io-post-api-posts-create-request
- name: PostApiUsersCreateRequest
  property_count: 3
  slug: airpipe-io-post-api-users-create-request
- name: PostJobsStatusResponse
  property_count: 7
  slug: airpipe-io-post-jobs-status-response
- name: PostJobsSubmitResponse
  property_count: 2
  slug: airpipe-io-post-jobs-submit-response
- name: PostTutorialWebhookRequest
  property_count: 2
  slug: airpipe-io-post-tutorial-webhook-request
- name: PostTutorialWebhookResponse
  property_count: 2
  slug: airpipe-io-post-tutorial-webhook-response
- name: PostYourOrgUuidStagingTutorialWebhookResponse
  property_count: 2
  slug: airpipe-io-post-your-org-uuid-staging-tutorial-webhook-response
- name: PutApiPostsUpdateRequest
  property_count: 4
  slug: airpipe-io-put-api-posts-update-request
jsonld:
- class_count: 37
  name: Airpipe Io Context
  property_count: 40
  slug: airpipe-io-context
layout: provider
modified: '2026-11-01'
name: Air Pipe
nav: Providers
network: true
overview: 'Air Pipe is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Examples API, tutorial API, and 1 more. Tagged areas include Platform, Automation, Artificial Intelligence, Backend, and Company.


  The Air Pipe catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Air Pipe''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, and 13 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 1
  name: Airpipe Io Rate Limits
  slug: airpipe-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Air Pipe API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 1
  slug: airpipe-io-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 27.4
    discoverability: 62.5
    operational_transparency: 21.1
  previous_composite: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Airpipe Io Authentication
  slug: airpipe-io-authentication
  summary_line: 9 schemes
- kind: domain-security
  name: Airpipe Io Domain Security
  slug: airpipe-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airpipe-io
tags:
- Platform
- Automation
- Artificial Intelligence
- Backend
- Company
website: https://airpipe.io/
---
