---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.p2flux.com
  baseurl_source: declared
  description: Unsigned calldata for the customer's own wallet to send.
  name: P2Flux API Cancellation API
  slug: p2flux-api-cancellation-api
- baseURL: https://api.p2flux.com
  baseurl_source: declared
  description: A single payment to a single recipient.
  name: P2Flux API One-time payments API
  slug: p2flux-api-one-time-payments-api
- baseURL: https://api.p2flux.com
  baseurl_source: declared
  description: Signed once by the customer, charged by your renewal job.
  name: P2Flux API Recurring payments API
  slug: p2flux-api-recurring-payments-api
- baseURL: https://api.p2flux.com
  baseurl_source: declared
  description: A transfer from the merchant's own wallet back to the wallet that paid.
  name: P2Flux API Refunds API
  slug: p2flux-api-refunds-api
- baseURL: https://api.p2flux.com
  baseurl_source: declared
  description: Liveness.
  name: P2Flux API Service API
  slug: p2flux-api-service-api
- baseURL: https://api.p2flux.com
  baseurl_source: declared
  description: The Subscriptions API from P2Flux API — 1 operation(s) for subscriptions.
  name: P2Flux API Subscriptions API
  slug: p2flux-api-subscriptions-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/p2flux-api/capabilities/p2flux-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/p2flux-api-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/p2flux-api/overlays/p2flux-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/p2flux-api-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/p2flux-api/security/p2flux-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/p2flux-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://p2flux.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://p2flux.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://p2flux.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://p2flux.com/docs/quickstart.html
- group: docs
  title: ''
  type: APIReference
  url: https://p2flux.com/docs/api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://p2flux.com/#pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://p2flux.com/status.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://p2flux.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://p2flux.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://p2flux.com/integration-enquiries.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/P2Flux
- group: agent
  title: ''
  type: LLMsTxt
  url: https://p2flux.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/p2flux-api/well-known/p2flux-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/p2flux-api-well-known.yml
- group: start
  title: ''
  type: APIOnboarding
  url: https://p2flux.com/.well-known/api-onboarding
- group: build
  href: https://artifacts.apis.io/p2flux-api/packages/p2flux-api-packages.yml
  title: ''
  type: Packages
  url: packages/p2flux-api-packages.yml
- group: build
  href: https://artifacts.apis.io/p2flux-api/packages/p2flux-api-packages.yml
  title: ''
  type: SDKs
  url: packages/p2flux-api-packages.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/components/p2flux-api-components.yml
  title: ''
  type: Components
  url: components/p2flux-api-components.yml
- group: start
  href: https://artifacts.apis.io/p2flux-api/sandbox/p2flux-api-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/p2flux-api-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/p2flux-api/rate-limits/p2flux-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/p2flux-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/p2flux-api/plans/p2flux-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/p2flux-api-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/conventions/p2flux-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/p2flux-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/conventions/p2flux-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/p2flux-api-conventions.yml
- group: auth
  href: https://artifacts.apis.io/p2flux-api/authentication/p2flux-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/p2flux-api-authentication.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/errors/p2flux-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/p2flux-api-problem-types.yml
- group: build
  href: https://artifacts.apis.io/p2flux-api/errors/p2flux-api-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/p2flux-api-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/conformance/p2flux-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/p2flux-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/lifecycle/p2flux-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/p2flux-api-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/p2flux-api/mcp/p2flux-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/p2flux-api-mcp.yml
- group: design
  href: https://artifacts.apis.io/p2flux-api/data-model/p2flux-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/p2flux-api-data-model.yml
- group: agent
  href: https://artifacts.apis.io/p2flux-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-15'
description: Non-custodial USDC payments API on the Base blockchain. Provides REST endpoints for one-time USDC payment intents with on-chain verification, recurring/subscription payments with merchant-triggered charges, and refunds. Payments are authorized per-request via HMAC-signed capabilities plus the payer's EIP-712 wallet signature — no signup, no dashboard, no issued credentials, and no custody of funds.
finops:
- has_sources: true
  method: derived
  name: P2Flux Api Finops
  primary_unit: payment
  service_category: ''
  slug: p2flux-api-finops
  template: false
image: https://p2flux.com/assets/apple-touch-icon.png
layout: provider
mcp_servers:
- description: P2Flux ships no MCP server. This is a DERIVED candidate tool list mapping the public REST operations to prospective MCP tools, provided as a starting point only. Nobody serves these as MCP tools today
  name: P2Flux API MCP Server
  slug: p2flux-api-mcp-yml
modified: '2026-09-15'
name: P2Flux API
nav: Providers
network: true
overview: 'P2Flux API publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cancellation API, One-time payments API, Recurring payments API, and 3 more. Tagged areas include Payments, Payment API, Cryptocurrency, Stablecoins, and USDC.


  The P2Flux API catalog on APIs.io includes 1 Spectral governance ruleset.


  P2Flux API''s developer surface includes documentation, getting-started guide, API reference, pricing, support, sandbox, authentication, and 26 more developer resources.'
plans:
- name: P2Flux Api Plans Pricing
  plan_count: 3
  slug: p2flux-api-plans-pricing
- name: P2Flux Api Price Estimates
  plan_count: 0
  slug: p2flux-api-price-estimates
random_paper: 8
rate_limits:
- limit_count: 13
  name: P2Flux Api Rate Limits
  slug: p2flux-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: P2Flux API API Rules
  rule_count: 59
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 7
  slug: p2flux-api-rules
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 46.4
    developer_ergonomics: 70.8
    discoverability: 67.9
    operational_transparency: 50.0
  previous_composite: 54.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/p2flux-api/p2flux-api-2026-10-11T112252.png
security:
- kind: authentication
  name: P2Flux Api Authentication
  slug: p2flux-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: P2Flux Api Domain Security
  slug: p2flux-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: p2flux-recurring-subscription
  slug: p2flux-api-recurring-subscription
- name: p2flux-refund-payment
  slug: p2flux-api-refund-payment
- name: p2flux-take-one-time-payment
  slug: p2flux-api-take-one-time-payment
slug: p2flux-api
tags:
- Payments
- Payment API
- Cryptocurrency
- Stablecoins
- USDC
- Base
- Recurring Payments
- Subscription
- Refunds
- Non-Custodial
website: https://p2flux.com/
---
