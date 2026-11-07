---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Agentpay So Agentic Access
  operation_count: 33
  slug: agentpay-so-agentic-access
  summary_line: 33 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Agent Communication Protocol endpoints
  name: AgentPay Labs ACP API
  slug: agentpay-so-acp-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Trust scoring (0-1000) for AI agents
  name: AgentPay Labs Agent Rank API
  slug: agentpay-so-agentrank-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Agent identity and registration
  name: AgentPay Labs Agents API
  slug: agentpay-so-agents-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Agent Payment Protocol v2 endpoints
  name: AgentPay Labs AP2 API
  slug: agentpay-so-ap2-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Need-led product discovery and closed-world AI decision compilation
  name: AgentPay Labs Commerce API
  slug: agentpay-so-commerce-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: A2A escrow — lock, approve, dispute
  name: AgentPay Labs Escrow API
  slug: agentpay-so-escrow-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Health check and status
  name: AgentPay Labs Health API
  slug: agentpay-so-health-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Agent discovery marketplace and checkout
  name: AgentPay Labs Marketplace API
  slug: agentpay-so-marketplace-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Merchant registration and management
  name: AgentPay Labs Merchants API
  slug: agentpay-so-merchants-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Payment intents and verification
  name: AgentPay Labs Payments API
  slug: agentpay-so-payments-api
- baseURL: https://api.agentpay.so
  baseurl_source: declared
  description: Webhook subscriptions and event delivery
  name: AgentPay Labs Webhooks API
  slug: agentpay-so-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/agentpay-so/agentic-access/agentpay-so-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentpay-so-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentpay-so/plans/agentpay-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentpay-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentpay-so/rules/agentpay-so-rules.yml
  title: ''
  type: Spectral
  url: rules/agentpay-so-rules.yml
- group: design
  href: https://artifacts.apis.io/agentpay-so/json-ld/agentpay-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentpay-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentpay-so/vocabulary/agentpay-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentpay-so-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentpay-so/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentpay-so/data-model/agentpay-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentpay-so-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentpay-so/authentication/agentpay-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentpay-so-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentpay-so/errors/agentpay-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentpay-so-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentpay-so/conformance/agentpay-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentpay-so-conformance.yml
- group: build
  href: https://artifacts.apis.io/agentpay-so/mcp/agentpay-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentpay-so-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentpay-so/mcp/agentpay-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentpay-so-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentpay-so/well-known/agentpay-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentpay-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentpay-so/hosts/agentpay-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentpay-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentpay-so/vendors/agentpay-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentpay-so-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentpay-so/packages/agentpay-so-packages.yml
  title: ''
  type: SDKs
  url: packages/agentpay-so-packages.yml
- group: build
  href: https://artifacts.apis.io/agentpay-so/packages/agentpay-so-packages.yml
  title: ''
  type: Packages
  url: packages/agentpay-so-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://api.agentpay.so/api/merchants/register
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.agentpay.so/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentpay.so/quickstart
- group: auth
  href: https://artifacts.apis.io/agentpay-so/security/agentpay-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentpay-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentpay.so/
- group: docs
  title: ''
  type: Documentation
  url: https://agentpay.so/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.agentpay.so
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentpay.so/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentpay.so/terms
created: '2026-11-01'
description: AgentPay Labs is an experimental platform exploring how human intent can be translated into accountable robot actions. The site showcases research experiments in interaction, orchestration, and learning from failure, with demos, documentation, and resources about their harness, experiments, and underlying technology. It aims to bridge intent and automation through open research and collaborative tools.
json_schemas:
- name: AgentPaymentIntentRequest
  property_count: 5
  slug: agentpay-so-agent-payment-intent-request
- name: CommerceCompileRequest
  property_count: 4
  slug: agentpay-so-commerce-compile-request
- name: CommerceCompileResponse
  property_count: 2
  slug: agentpay-so-commerce-compile-response
- name: MarketplaceDiscoverResponse
  property_count: 4
  slug: agentpay-so-marketplace-discover-response
- name: PaymentIntentResponse
  property_count: 6
  slug: agentpay-so-payment-intent-response
- name: PaymentVerifyResponse
  property_count: 9
  slug: agentpay-so-payment-verify-response
jsonld:
- class_count: 37
  name: Agentpay So Context
  property_count: 128
  slug: agentpay-so-context
layout: provider
mcp_servers:
- description: ''
  name: AgentPay Labs MCP Server
  slug: agentpay-so-mcp-yml
modified: '2026-11-01'
name: AgentPay Labs
nav: Providers
network: true
overview: 'AgentPay Labs publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including ACP API, Agent Rank API, Agents API, and 8 more. Tagged areas include Company, Research, Robotics, Automation, and Platform.


  The AgentPay Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentPay Labs'' developer surface includes authentication, signup flow, pricing, getting-started guide, documentation, API reference, and 20 more developer resources.'
plans:
- name: Agentpay So Plans Pricing
  plan_count: 4
  slug: agentpay-so-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AgentPay Labs API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 3
  slug: agentpay-so-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 60.8
    developer_ergonomics: 35.1
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentpay So Authentication
  slug: agentpay-so-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentpay So Domain Security
  slug: agentpay-so-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: agentpay-so-ap2-payment-flow
  slug: agentpay-so-ap2-payment-flow
- name: agentpay-so-create-payment-intent
  slug: agentpay-so-create-payment-intent
- name: agentpay-so-onboard-merchant
  slug: agentpay-so-onboard-merchant
slug: agentpay-so
tags:
- Company
- Research
- Robotics
- Automation
- Platform
website: https://agentpay.so/
---
