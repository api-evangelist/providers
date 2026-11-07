---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 69.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Apps API from Cracked API — 6 operation(s) for apps.
  name: Cracked API Apps API
  slug: cracked-apps-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Auth API from Cracked API — 1 operation(s) for auth.
  name: Cracked API Auth API
  slug: cracked-auth-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Batches API from Cracked API — 4 operation(s) for batches.
  name: Cracked API Batches API
  slug: cracked-batches-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Datasets API from Cracked API — 2 operation(s) for datasets.
  name: Cracked API Datasets API
  slug: cracked-datasets-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Discover API from Cracked API — 1 operation(s) for discover.
  name: Cracked API Discover API
  slug: cracked-discover-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Inspect API from Cracked API — 1 operation(s) for inspect.
  name: Cracked API Inspect API
  slug: cracked-inspect-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Providers API from Cracked API — 1 operation(s) for providers.
  name: Cracked API Providers API
  slug: cracked-providers-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Referrals API from Cracked API — 1 operation(s) for referrals.
  name: Cracked API Referrals API
  slug: cracked-referrals-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Refunds API from Cracked API — 1 operation(s) for refunds.
  name: Cracked API Refunds API
  slug: cracked-refunds-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Relay API from Cracked API — 4 operation(s) for relay.
  name: Cracked API Relay API
  slug: cracked-relay-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Run API from Cracked API — 1 operation(s) for run.
  name: Cracked API Run API
  slug: cracked-run-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Runs API from Cracked API — 3 operation(s) for runs.
  name: Cracked API Runs API
  slug: cracked-runs-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Schedules API from Cracked API — 2 operation(s) for schedules.
  name: Cracked API Schedules API
  slug: cracked-schedules-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Secrets API from Cracked API — 3 operation(s) for secrets.
  name: Cracked API Secrets API
  slug: cracked-secrets-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The Wallet API from Cracked API — 2 operation(s) for wallet.
  name: Cracked API Wallet API
  slug: cracked-wallet-api
- baseURL: https://cracked.ai/v1
  baseurl_source: declared
  description: The X402 API from Cracked API — 1 operation(s) for x402.
  name: Cracked API X402 API
  slug: cracked-x402-api
artifact_total: 30
asyncapis:
- description: ''
  name: Cracked Webhooks
  slug: cracked-webhooks
common:
- group: other
  href: https://artifacts.apis.io/cracked/capabilities/cracked-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cracked-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://cracked.ai/mcp
- group: agent
  title: ''
  type: AgentSkill
  url: https://cracked.ai/SKILL.md
- group: agent
  title: ''
  type: MCPServer
  url: https://cracked.ai/mcp/public
- group: company
  title: ''
  type: Website
  url: https://www.cracked.ai/
- group: auth
  href: https://artifacts.apis.io/cracked/security/cracked-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cracked-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cracked/security/cracked-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cracked-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cracked/security/cracked-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cracked-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cracked/authentication/cracked-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cracked-authentication.yml
- group: build
  href: https://artifacts.apis.io/cracked/packages/cracked-packages.yml
  title: ''
  type: Packages
  url: packages/cracked-packages.yml
- group: build
  href: https://artifacts.apis.io/cracked/packages/cracked-packages.yml
  title: ''
  type: SDKs
  url: packages/cracked-packages.yml
- group: agent
  href: https://artifacts.apis.io/cracked/well-known/cracked-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cracked-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cracked/mcp/cracked-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cracked-mcp.yml
- group: build
  href: https://artifacts.apis.io/cracked/mcp/cracked-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cracked-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/cracked/a2a/cracked-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cracked-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cracked/llms/cracked-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cracked-llms.txt
- group: agent
  href: https://artifacts.apis.io/cracked/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/cracked/overlays/cracked-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cracked-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cracked/conformance/cracked-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cracked-conformance.yml
- group: design
  href: https://artifacts.apis.io/cracked/errors/cracked-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cracked-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cracked/lifecycle/cracked-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cracked-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://cracked.ai/status
- group: auth
  href: https://artifacts.apis.io/cracked/scopes/cracked-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cracked-scopes.yml
- group: auth
  title: ''
  type: Security
  url: https://cracked.ai/security
- group: start
  href: https://artifacts.apis.io/cracked/sandbox/cracked-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cracked-sandbox.yml
- group: design
  href: https://artifacts.apis.io/cracked/conventions/cracked-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cracked-conventions.yml
- group: design
  href: https://artifacts.apis.io/cracked/conventions/cracked-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cracked-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cracked/changelog/cracked-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cracked-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://cracked.ai/changelog
- group: build
  href: https://artifacts.apis.io/cracked/cli/cracked-cli.yml
  title: ''
  type: CLI
  url: cli/cracked-cli.yml
- group: design
  href: https://artifacts.apis.io/cracked/data-model/cracked-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cracked-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/cracked/plans/cracked-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cracked-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cracked/rate-limits/cracked-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cracked-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cracked/asyncapi/cracked-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cracked-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cracked.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cracked.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://cracked.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cracked.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cracked.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cracked.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cracked.ai/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://cracked.ai/postman/cracked.postman_collection.json
- group: operate
  title: ''
  type: Support
  url: mailto:support@cracked.ai
created: '2026-09-03'
description: 'Cracked is a tool router for AI agents: one API key and one prepaid balance to discover, inspect, run and poll thousands of third-party tools. It exposes 9,521 endpoints from 1,183 providers plus 50,000+ Apify actors, publishing measured success rate, median latency and per-call price per tool.'
finops:
- has_sources: true
  method: derived
  name: Cracked Finops
  primary_unit: 3-week sprint
  service_category: ''
  slug: cracked-finops
  template: false
image: https://cracked.ai/brand/icon.png
layout: provider
mcp_servers:
- description: ''
  name: Cracked API MCP Server
  slug: mcp
- description: ''
  name: Cracked API MCP Server
  slug: public
modified: '2026-09-03'
name: Cracked API
nav: Providers
network: true
overview: 'Cracked API publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Auth API, Batches API, and 13 more. Tagged areas include AI Agents, Agent Tools, MCP, Tool Router, and API Aggregator.


  The Cracked API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cracked API''s developer surface includes authentication, sandbox, changelog, CLI, API reference, getting-started guide, pricing, and 36 more developer resources.'
plans:
- name: Cracked Plans Pricing
  plan_count: 4
  slug: cracked-plans-pricing
- name: Cracked Price Estimates
  plan_count: 0
  slug: cracked-price-estimates
random_paper: 21
rate_limits:
- limit_count: 3
  name: Cracked Rate Limits
  slug: cracked-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Cracked API API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 3
  slug: cracked-rules
scopes:
- name: Cracked Scopes
  scope_count: 4
  slug: cracked-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 53.7
    developer_ergonomics: 88.1
    discoverability: 75.0
    operational_transparency: 81.6
  previous_composite: 73.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cracked/cracked-2026-10-11T103321.png
security:
- kind: authentication
  name: Cracked Authentication
  slug: cracked-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cracked Domain Security
  slug: cracked-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cracked Vulnerability Disclosure
  slug: cracked-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cracked Trust Center
  slug: cracked-trust-center
  summary_line: trust center published
skill_count: 1
skills:
- name: cracked
  slug: cracked-skill
slug: cracked
tags:
- AI Agents
- Agent Tools
- MCP
- Tool Router
- API Aggregator
- Web Search
- Web Scraping
- Data Enrichment
- Llms.txt
- Agent Skills
- Pay-per-call
- Aggregator
- Lead Generation
- AI Models
- Developer Tools
- Leadgen
- SEO
- social-media-data
- E-Commerce
- Weather
- A2A
website: https://www.cracked.ai/
---
