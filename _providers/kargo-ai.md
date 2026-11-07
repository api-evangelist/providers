---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.kargo.zone/public_graphql
  baseurl_source: declared
  description: Kargo's original public integration method, maintained for existing integrations and still the surface behind the Unified Endpoint API. Exposes queries for businesses, shipments, push messages and the
  name: Kargo Public GraphQL API
  slug: kargo-public-graphql-api
- baseURL: https://api.kargo.zone/public_graphql
  baseurl_source: declared
  description: The Documents API from Kargo — 1 operation(s) for documents.
  name: Kargo Documents API
  slug: kargo-ai-documents-api
- baseURL: https://api.kargo.zone/public_graphql
  baseurl_source: declared
  description: The SKU Master API from Kargo — 1 operation(s) for sku master.
  name: Kargo SKU Master API
  slug: kargo-ai-sku-master-api
artifact_total: 14
asyncapis:
- description: ''
  name: Kargo Push Webhooks
  slug: kargo-push-webhooks
collections:
- collection_type: postman
  name: Kargo Public GraphQL API
  slug: postman-kargo-public-graphql
common:
- group: other
  href: https://artifacts.apis.io/kargo-ai/capabilities/kargo-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kargo-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/kargo-ai/overlays/kargo-document-intake-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kargo-document-intake-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.kargo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kargo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kargo.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.kargo.zone/v1/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kargo.ai/basic_examples
- group: auth
  href: https://artifacts.apis.io/kargo-ai/authentication/kargo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kargo-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kargo.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mykargo
- group: start
  title: ''
  type: SignUp
  url: https://athena.mykargo.com/
- group: start
  title: ''
  type: Login
  url: https://athena.mykargo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kargo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kargo.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://info.mykargo.com/demo
- group: build
  title: ''
  type: Postman
  url: https://docs.kargo.ai/kargo-public-graphql.postman_collection.json
- group: start
  href: https://artifacts.apis.io/kargo-ai/sandbox/kargo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kargo-sandbox.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/asyncapi/kargo-push-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/kargo-push-webhooks.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/conventions/kargo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kargo-conventions.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/errors/kargo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kargo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/lifecycle/kargo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kargo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/conformance/kargo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kargo-conformance.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/data-model/kargo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kargo-data-model.yml
- group: auth
  href: https://artifacts.apis.io/kargo-ai/security/kargo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kargo-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/kargo-ai/well-known/kargo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kargo-well-known.yml
- group: other
  href: https://artifacts.apis.io/kargo-ai/well-known/kargo-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/kargo-openid-configuration.json
- group: build
  href: https://artifacts.apis.io/kargo-ai/packages/kargo-packages.yml
  title: ''
  type: Packages
  url: packages/kargo-packages.yml
- group: operate
  href: https://artifacts.apis.io/kargo-ai/rate-limits/kargo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kargo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kargo-ai/plans/kargo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kargo-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/kargo-ai/llms/kargo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kargo-llms.txt
- group: agent
  href: https://artifacts.apis.io/kargo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kargo-ai/conventions/kargo-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kargo-conventions.yml
- group: build
  href: https://artifacts.apis.io/kargo-ai/mcp/kargo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kargo-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/kargo-ai/examples/kargo-request-examples.yml
  title: ''
  type: Examples
  url: examples/kargo-request-examples.yml
- group: docs
  href: https://artifacts.apis.io/kargo-ai/graphql/kargo-public-graphql.graphql
  title: ''
  type: GraphQL
  url: graphql/kargo-public-graphql.graphql
- group: other
  title: ''
  type: HowItWorks
  url: https://www.kargo.ai/how-it-works
- group: company
  title: ''
  type: Careers
  url: https://www.kargo.ai/careers
created: '2026-08-23'
description: 'Kargo (Kargo Technologies, kargo.ai) builds an AI-powered smart loading dock for warehouses and distribution centers. Camera towers (Kargo Tower) and forklift-mounted cameras (Kargo Lift) apply computer vision to every pallet that moves through a dock door, reading LPN, SKU, lot code and expiration-date labels to automate shipping and receiving, verify loads and shipments, detect damage, and feed inventory visibility, shelf-life management, FSMA traceability, claims management, financial reconciliation and automated ASNs back into the customer WMS. Kargo publishes a public integration surface for that data exchange: a REST Document Intake API described by an OpenAPI 3.1 document, a public GraphQL API with open anonymous introspection, a single unified JSON endpoint, a webhook (push) API at shipment and pallet level plus a GraphQL subscription alternative, and flat-file ingest over email, SFTP or AS2. All programmatic access is Auth0 OAuth 2.0 client-credentials bearer tokens.'
finops:
- has_sources: true
  method: derived
  name: Kargo Ai Finops
  primary_unit: ''
  service_category: ''
  slug: kargo-ai-finops
  template: true
image: https://www.kargo.ai/assets/images/favicon/apple-touch-icon.png
layout: provider
modified: '2026-08-23'
name: Kargo
nav: Providers
network: true
overview: 'Kargo publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Public GraphQL API, Documents API, and SKU Master API. Tagged areas include Company, Logistics, Supply Chain, Warehouse, and Computer Vision.


  The Kargo catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kargo''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, support, and 30 more developer resources.'
plans:
- name: Kargo Plans Pricing
  plan_count: 0
  slug: kargo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Kargo Rate Limits
  slug: kargo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Kargo API Rules
  rule_count: 53
  severity_counts:
    error: 49
    hint: 0
    info: 3
    warn: 1
  slug: kargo-ai-rules
scopes:
- name: Kargo Scopes
  scope_count: 0
  slug: kargo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 67.4
    developer_ergonomics: 70.8
    discoverability: 71.4
    operational_transparency: 10.5
  previous_composite: 55.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/kargo-ai/kargo-2026-09-02T150020.png
security:
- kind: authentication
  name: Kargo Authentication
  slug: kargo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Kargo Domain Security
  slug: kargo-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: Maintain the Kargo SKU master
  slug: kargo-maintain-sku-master
- name: Schedule a Kargo shipment and validate it against what the dock sees
  slug: kargo-schedule-shipment-and-validate
slug: kargo-ai
tags:
- Company
- Logistics
- Supply Chain
- Warehouse
- Computer Vision
- Artificial Intelligence
- Shipping
- Inventory
- Industrial Automation
- Freight
- GraphQL
- Webhook
website: https://www.kargo.ai/
---
