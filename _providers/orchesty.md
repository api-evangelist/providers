---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Orchesty.io 2.0 API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Orchesty.io 2.0 API
  slug: 2.0-api
- description: 'Orchesty.io 3.0 API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Orchesty.io 3.0 API
  slug: 3.0-api
artifact_total: 20
asyncapis:
- description: ''
  name: Orchesty Webhooks
  slug: orchesty-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/orchesty/plans/orchesty-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orchesty-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/orchesty/rules/orchesty-rules.yml
  title: ''
  type: Spectral
  url: rules/orchesty-rules.yml
- group: design
  href: https://artifacts.apis.io/orchesty/json-ld/orchesty-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/orchesty-context.jsonld
- group: design
  href: https://artifacts.apis.io/orchesty/vocabulary/orchesty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/orchesty-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/orchesty/asyncapi/orchesty-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/orchesty-webhooks.yml
- group: design
  href: https://artifacts.apis.io/orchesty/data-model/orchesty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orchesty-data-model.yml
- group: auth
  href: https://artifacts.apis.io/orchesty/authentication/orchesty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orchesty-authentication.yml
- group: design
  href: https://artifacts.apis.io/orchesty/conformance/orchesty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orchesty-conformance.yml
- group: other
  href: https://artifacts.apis.io/orchesty/hosts/orchesty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orchesty-hosts.yml
- group: auth
  href: https://artifacts.apis.io/orchesty/scopes/orchesty-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/orchesty-scopes.yml
- group: auth
  href: https://artifacts.apis.io/orchesty/security/orchesty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orchesty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orchesty.io/
- group: docs
  title: ''
  type: Documentation
  url: https://orchesty.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://orchesty.io/docs/3.0/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://orchesty.io/docs/3.0/getting-started/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://orchesty.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.orchesty.io/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orchesty.io/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orchesty.io/legal/privacy-policy
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are JavaScript-rendered and no machine-readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://orchesty.io/docs/3.0/reference/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Orchesty.io provides an open integration platform that enables developers to build scalable, asynchronous workflows and integrations across systems. The platform offers a streaming-first engine, a marketplace for connectors, AI‑assisted bootstrap tools, and a multi‑tenant MCP server for secure agent access. It supports both community and enterprise editions, with features like SSO, monitoring, and customizable extensions, making it suitable for modern integration workloads.
image: https://orchesty.io/OG.png
json_schemas:
- name: GetDataResponse
  property_count: 1
  slug: orchesty-get-data-response
- name: PatchApiNodesIdRequest
  property_count: 1
  slug: orchesty-patch-api-nodes-id-request
- name: PostBatchKeyActionRequest
  property_count: 1
  slug: orchesty-post-batch-key-action-request
- name: PostConnectorIdActionRequest
  property_count: 1
  slug: orchesty-post-connector-id-action-request
- name: PostConnectorMyConnectorActionTestRequest
  property_count: 1
  slug: orchesty-post-connector-my-connector-action-test-request
- name: PostCustomNodeDataTransformerActionRequest
  property_count: 4
  slug: orchesty-post-custom-node-data-transformer-action-request
- name: PostCustomNodeIdProcessRequest
  property_count: 1
  slug: orchesty-post-custom-node-id-process-request
- name: PostMcpManifestJsonRequest
  property_count: 2
  slug: orchesty-post-mcp-manifest-json-request
- name: PostMcpManifestJsonResponse
  property_count: 3
  slug: orchesty-post-mcp-manifest-json-response
- name: PostWebhookApplicationsShopifyUsersTestExampleComSubscribeRe
  property_count: 2
  slug: orchesty-post-webhook-applications-shopify-users-test-example-com-subscribe-re
- name: PostWebhookTopologiesTopo123NodesNode456TokenAbc123Def456Req
  property_count: 3
  slug: orchesty-post-webhook-topologies-topo123-nodes-node456-token-abc123-def456-req
jsonld:
- class_count: 14
  name: Orchesty Context
  property_count: 16
  slug: orchesty-context
layout: provider
modified: '2026-10-18'
name: Orchesty.io
nav: Providers
network: true
overview: 'Orchesty.io is listed with 2 APIs on the [APIs.io](https://apis.io/) network: 2.0 API and 3.0 API. Tagged areas include Integration, Platform, Automation, Artificial Intelligence, and Open Source.


  The Orchesty.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Orchesty.io''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Orchesty Plans Pricing
  plan_count: 3
  slug: orchesty-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Orchesty.io API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: orchesty-rules
scopes:
- name: Orchesty Scopes
  scope_count: 2
  slug: orchesty-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 32.8
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 42.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/orchesty/orchesty-2026-11-03T140731.png
security:
- kind: authentication
  name: Orchesty Authentication
  slug: orchesty-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Orchesty Domain Security
  slug: orchesty-domain-security
  summary_line: TLSv1.3 · DMARC
slug: orchesty
tags:
- Integration
- Platform
- Automation
- Artificial Intelligence
- Open Source
website: https://orchesty.io/
---
