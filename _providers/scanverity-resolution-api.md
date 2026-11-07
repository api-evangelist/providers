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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://scanverity.com
  baseurl_source: spec
  description: Create and poll account-scoped assessment resources.
  name: Scanverity Resolution API Resolution assessments API
  slug: scanverity-resolution-api-resolution-assessments-api
- baseURL: https://scanverity.com
  baseurl_source: spec
  description: Read account-scoped monthly reconciled usage totals and their cursor-paginated evidence events.
  name: Scanverity Resolution API Resolution usage API
  slug: scanverity-resolution-api-resolution-usage-api
- baseURL: https://scanverity.com
  baseurl_source: spec
  description: Register account- and environment-scoped signed endpoints, inspect append-only delivery evidence and request non-billable redelivery.
  name: Scanverity Resolution API Webhook endpoints API
  slug: scanverity-resolution-api-webhook-endpoints-api
artifact_total: 18
asyncapis:
- description: ''
  name: Scanverity Resolution Api Webhooks
  slug: scanverity-resolution-api-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://scanverity.com/mcp
- group: commercial
  href: https://artifacts.apis.io/scanverity-resolution-api/plans/scanverity-resolution-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scanverity-resolution-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/scanverity-resolution-api/rate-limits/scanverity-resolution-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scanverity-resolution-api-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/scanverity-resolution-api/capabilities/scanverity-resolution-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scanverity-resolution-api-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/scanverity-resolution-api/overlays/scanverity-resolution-api-resolution-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scanverity-resolution-api-resolution-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/scanverity-resolution-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.scanverity.com/
- group: auth
  href: https://artifacts.apis.io/scanverity-resolution-api/security/scanverity-resolution-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scanverity-resolution-api-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scanverity.com/en/resolution-api
- group: docs
  title: ''
  type: Documentation
  url: https://scanverity.com/resolution-api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scanverity.com/resolution-api/docs
- group: agent
  href: https://artifacts.apis.io/scanverity-resolution-api/llms/scanverity-resolution-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scanverity-resolution-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/scanverity-resolution-api/well-known/scanverity-resolution-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scanverity-resolution-api-well-known.yml
- group: other
  href: https://artifacts.apis.io/scanverity-resolution-api/well-known/scanverity-resolution-api-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/scanverity-resolution-api-api-catalog.json
- group: other
  title: ''
  type: X-APIsJSON
  url: https://scanverity.com/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://scanverity.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://scanverity.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://scanverity.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scanverity.com/en/legal/resolution-api-addendum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scanverity.com/en/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://scanverity.com/en/contact
- group: company
  title: ''
  type: Blog
  url: https://scanverity.com/research
- group: company
  title: ''
  type: BlogRSS
  url: https://scanverity.com/feed.xml
created: '2026-09-04'
description: An independent Polymarket intelligence platform, operated by KotIQ OÜ, providing resolution-risk assessments on prediction markets through a documented OpenAPI 3.1 REST API. Resolution risk is the chance a market settles in a way its title does not lead a reader to expect — ambiguous rule language, an unverifiable resolution source, or a title that diverges from the rules. The API is an async create-and-poll surface with signed webhooks, a deterministic sandbox fixture catalog, a reconciled usage ledger, four deny-by-default token scopes and a required Idempotency-Key on its only billable write. The contract, an APIs.json index and an RFC 9727 api-catalog are all publicly retrievable; runtime access is private beta and feature-gated, so live calls require an entitled, allowlisted account. Read-only research only — no order placement, no custody, no trading advice.
examples:
- key_count: 7
  name: Scanverity Resolution Api Examples
  slug: scanverity-resolution-api-examples
finops:
- has_sources: true
  method: derived
  name: Scanverity Resolution Api Finops
  primary_unit: newly released assessment
  service_category: ''
  slug: scanverity-resolution-api-finops
  template: false
image: https://scanverity.com/icon-512.png
layout: provider
mcp_servers:
- description: Scanverity's own hosted MCP server (registry com.scanverity/resolution-rules). Requires an approved account; setup at https://scanverity.com/connectors. Adding the connector does not grant API or paid
  name: Scanverity hosted MCP server
  slug: scanverity-hosted-mcp-server
modified: '2026-09-04'
name: Scanverity Resolution API
nav: Providers
network: true
overview: 'Scanverity Resolution API publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Resolution assessments API, Resolution usage API, and Webhook endpoints API. Tagged areas include Prediction Markets, Resolution Risk, Market Intelligence, Due Diligence, and Webhook.


  The Scanverity Resolution API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Scanverity Resolution API''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
plans:
- name: Scanverity Resolution Api Plans Pricing
  plan_count: 13
  slug: scanverity-resolution-api-plans-pricing
- name: Scanverity Resolution Api Price Estimates
  plan_count: 0
  slug: scanverity-resolution-api-price-estimates
random_paper: 16
rate_limits:
- limit_count: 4
  name: Scanverity Resolution Api Rate Limits
  slug: scanverity-resolution-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Scanverity Resolution API API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 2
  slug: scanverity-resolution-api-rules
scopes:
- name: Scanverity Resolution Api Scopes
  scope_count: 4
  slug: scanverity-resolution-api-scopes
  summary_line: 4 scopes · bearer token (not OAuth)
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.5
    catalog_earned_first_party: 24.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 13.6
    contract_quality: 71.6
    developer_ergonomics: 54.2
    discoverability: 64.3
    operational_transparency: 47.4
  previous_composite: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/scanverity-resolution-api/scanverity-resolution-api-2026-10-11T125534.png
security:
- kind: authentication
  name: Scanverity Resolution Api Authentication
  slug: scanverity-resolution-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Scanverity Resolution Api Domain Security
  slug: scanverity-resolution-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: scanverity-assess-market
  slug: scanverity-resolution-api-assess-market
- name: scanverity-sandbox-fixtures
  slug: scanverity-resolution-api-sandbox
- name: scanverity-reconcile-usage
  slug: scanverity-resolution-api-usage-reconciliation
- name: scanverity-manage-webhooks
  slug: scanverity-resolution-api-webhooks
slug: scanverity-resolution-api
tags:
- Prediction Markets
- Resolution Risk
- Market Intelligence
- Due Diligence
- Webhook
- OpenAPI
- Fintech
- Risk Analytics
- Polymarket
- Event Contracts
- Agent Ready
website: https://www.scanverity.com/
---
