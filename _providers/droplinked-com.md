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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Droplinked API provides endpoints for product catalog import, AI‑assistant search and store management. See the API Reference for details.
  name: Droplinked API
  slug: droplinked-api
- baseURL: https://apiv3.droplinked.com
  baseurl_source: declared
  description: 'Droplinked API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Droplinked API
  slug: droplinked-com-api
- baseURL: http://sandbox.mintlify.com
  baseurl_source: declared
  description: A sample API that uses a plant store as an example to demonstrate features in the OpenAPI specification
  name: Droplinked Openapi API
  slug: droplinked-openapi-api
artifact_total: 16
asyncapis:
- description: ''
  name: Droplinked Com Webhooks
  slug: droplinked-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/droplinked-com/rules/droplinked-com-rules.yml
  title: ''
  type: Spectral
  url: rules/droplinked-com-rules.yml
- group: design
  href: https://artifacts.apis.io/droplinked-com/json-ld/droplinked-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/droplinked-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/droplinked-com/vocabulary/droplinked-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/droplinked-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/droplinked-com/asyncapi/droplinked-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/droplinked-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/droplinked-com/data-model/droplinked-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/droplinked-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/droplinked-com/changelog/droplinked-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/droplinked-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/droplinked-com/authentication/droplinked-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/droplinked-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/droplinked-com/conformance/droplinked-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/droplinked-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/droplinked-com/llms/droplinked-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/droplinked-com-llms.txt
- group: other
  href: https://artifacts.apis.io/droplinked-com/a2a/droplinked-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/droplinked-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/droplinked-com/well-known/droplinked-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/droplinked-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/droplinked-com/hosts/droplinked-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/droplinked-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/droplinked-com/vendors/droplinked-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/droplinked-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/droplinked-com/packages/droplinked-com-packages.yml
  title: ''
  type: SDKs
  url: packages/droplinked-com-packages.yml
- group: build
  href: https://artifacts.apis.io/droplinked-com/packages/droplinked-com-packages.yml
  title: ''
  type: Packages
  url: packages/droplinked-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.droplinked.com/guides/library/whats-new
- group: docs
  title: ''
  type: APIReference
  url: https://docs.droplinked.com/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/droplinked
- group: auth
  href: https://artifacts.apis.io/droplinked-com/security/droplinked-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/droplinked-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://droplinked.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://droplinked.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://droplinked.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://droplinked.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://droplinked.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://droplinked.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://droplinked.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://droplinked.com/getting-started
coverage:
  checked: '2026-11-06'
  detail: OpenAPI spec at docs.droplinked.com/api-reference/openapi.json is unrelated to Droplinked, pointing to a sandbox host.
  evidence:
  - status: 200
    url: https://docs.droplinked.com/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Droplinked provides a platform for merchants to import product catalogs from Shopify or CSV files and create AI‑assistant searchable online stores. Their MCP server enables agents to query product data, supporting on‑chain commerce and structured data integration. The service targets e‑commerce businesses seeking AI‑driven product discovery and seamless catalog management.
image: https://droplinked.com/favicons/light/web-app-manifest-512x512.png
json_schemas:
- name: GetV1ApiInventoryOsStreamsStreamtypeSubscriptionsResponse
  property_count: 2
  slug: droplinked-com-get-v1-api-inventory-os-streams-streamtype-subscriptions-response
- name: NewPlant
  property_count: 3
  slug: droplinked-com-new-plant
- name: PatchLendingApplicationIdRequest
  property_count: 6
  slug: droplinked-com-patch-lending-application-id-request
- name: Plant
  property_count: 2
  slug: droplinked-com-plant
- name: PostAdminLendingApplicationIdDecisionRequest
  property_count: 3
  slug: droplinked-com-post-admin-lending-application-id-decision-request
- name: PostLendingApplicationResponse
  property_count: 3
  slug: droplinked-com-post-lending-application-response
- name: PostV1ApiInventoryOsStreamsStreamtypeSubscribeRequest
  property_count: 3
  slug: droplinked-com-post-v1-api-inventory-os-streams-streamtype-subscribe-request
- name: PostV1ApiInventoryOsStreamsStreamtypeSubscribeResponse
  property_count: 10
  slug: droplinked-com-post-v1-api-inventory-os-streams-streamtype-subscribe-response
jsonld:
- class_count: 10
  name: Droplinked Com Context
  property_count: 29
  slug: droplinked-com-context
layout: provider
modified: '2026-11-06'
name: Droplinked
nav: Providers
network: true
overview: 'Droplinked publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Openapi API, and 2 more. Tagged areas include E-Commerce, Artificial Intelligence, catalog-import, Online Store, and MCP.


  The Droplinked catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Droplinked''s developer surface includes changelog, authentication, API reference, documentation, pricing, engineering blog, getting-started guide, and 20 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Droplinked API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: droplinked-com-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 33.3
    developer_ergonomics: 59.5
    discoverability: 66.1
    operational_transparency: 28.9
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Droplinked Com Authentication
  slug: droplinked-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Droplinked Com Domain Security
  slug: droplinked-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: droplinked-com
tags:
- E-Commerce
- Artificial Intelligence
- catalog-import
- Online Store
- MCP
website: https://droplinked.com/
---
