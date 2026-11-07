---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Machine Control Protocol (MCP) endpoint providing tool listings for Asyntai.
  name: MCP
  slug: mcp
- description: 'Asyntai API as documented publicly: 42 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Asyntai API
  slug: asyntai-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/asyntai-com/rate-limits/asyntai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asyntai-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/asyntai-com/plans/asyntai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asyntai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asyntai-com/rules/asyntai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asyntai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asyntai-com/json-ld/asyntai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asyntai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/asyntai-com/vocabulary/asyntai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asyntai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/asyntai-com/data-model/asyntai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asyntai-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/asyntai-com/authentication/asyntai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asyntai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/asyntai-com/errors/asyntai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asyntai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asyntai-com/conformance/asyntai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asyntai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asyntai-com/mcp/asyntai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asyntai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asyntai-com/well-known/asyntai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asyntai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asyntai-com/hosts/asyntai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asyntai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asyntai-com/vendors/asyntai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asyntai-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/asyntai-com/packages/asyntai-com-packages.yml
  title: ''
  type: SDKs
  url: packages/asyntai-com-packages.yml
- group: build
  href: https://artifacts.apis.io/asyntai-com/packages/asyntai-com-packages.yml
  title: ''
  type: Packages
  url: packages/asyntai-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asyntai.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asyntai.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asyntai
- group: auth
  href: https://artifacts.apis.io/asyntai-com/security/asyntai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asyntai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asyntai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asyntai.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://asyntai.com/documentation/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://asyntai.com/documentation/installation/
- group: company
  title: ''
  type: Blog
  url: https://asyntai.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://asyntai.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://asyntai.com/auth/
created: '2026-11-01'
description: Asyntai provides an AI‑powered chatbot assistant that can be embedded on any website to deliver instant, 24/7 customer support. Users can try a free tier with 50 messages, integrate with dozens of CMS platforms such as WordPress, Shopify, Magento, and customize the widget’s appearance and behavior. The service offers analytics, multilingual support, and scalable pricing plans for businesses of all sizes.
image: https://asyntai.com/static/images/og-image.png
json_schemas:
- name: GetApiV1ConversationsResponse
  property_count: 2
  slug: asyntai-com-get-api-v1-conversations-response
- name: GetKnowledgeAbc123DefResponse
  property_count: 10
  slug: asyntai-com-get-knowledge-abc123-def-response
- name: PostApiV1WebsitesResponse
  property_count: 3
  slug: asyntai-com-post-api-v1-websites-response
- name: PostChatRequest
  property_count: 3
  slug: asyntai-com-post-chat-request
- name: PostWebsitesRequest
  property_count: 4
  slug: asyntai-com-post-websites-request
- name: PutWebsitesIdInstructionsRequest
  property_count: 5
  slug: asyntai-com-put-websites-id-instructions-request
jsonld:
- class_count: 52
  name: Asyntai Com Context
  property_count: 48
  slug: asyntai-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at asyntai.com.
  name: Asyntai MCP Server
  slug: asyntai-com-mcp-yml
modified: '2026-11-01'
name: Asyntai
nav: Providers
network: true
overview: 'Asyntai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Chatbots, Customer Service, Software-as-a-Service, and Website Integration.


  The Asyntai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Asyntai''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Asyntai Com Plans Pricing
  plan_count: 2
  slug: asyntai-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Asyntai Com Rate Limits
  slug: asyntai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Asyntai API Rules
  rule_count: 44
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 6
  slug: asyntai-com-rules
scopes:
- name: Asyntai Com Scopes
  scope_count: 0
  slug: asyntai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 34.2
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asyntai Com Authentication
  slug: asyntai-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Asyntai Com Domain Security
  slug: asyntai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asyntai-com
tags:
- Artificial Intelligence
- Chatbots
- Customer Service
- Software-as-a-Service
- Website Integration
- Multilingual
website: https://asyntai.com/
---
