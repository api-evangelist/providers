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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Postalform Com Agentic Access
  operation_count: 44
  slug: postalform-com-agentic-access
  summary_line: 44 operations · 24 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Remote Model Context Protocol server at https://postalform.com/mcp (Streamable HTTP, wire protocol 2025-06-18, serverInfo postalform 0.1.0). initialize, tools/list and resources/list answer anonymousl
  name: PostalForm MCP Server
  slug: postalform-mcp-server
- description: 'Agent2Agent (A2A) surface: an agent card served from https://postalform.com/.well-known/agent-card.json (protocolVersion 1.0, JSONRPC binding, version 0.1.0, a2a-version: 1.0 response header) advertis'
  name: PostalForm A2A Agent
  slug: postalform-a2a-agent
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Api Keys API from PostalForm — 2 operation(s) for api keys.
  name: PostalForm Api Keys API
  slug: postalform-com-api-keys-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Credits API from PostalForm — 6 operation(s) for credits.
  name: PostalForm Credits API
  slug: postalform-com-credits-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Documents API from PostalForm — 2 operation(s) for documents.
  name: PostalForm Documents API
  slug: postalform-com-documents-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Letters API from PostalForm — 5 operation(s) for letters.
  name: PostalForm Letters API
  slug: postalform-com-letters-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Machine API from PostalForm — 17 operation(s) for machine.
  name: PostalForm Machine API
  slug: postalform-com-machine-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Postcards API from PostalForm — 4 operation(s) for postcards.
  name: PostalForm Postcards API
  slug: postalform-com-postcards-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Return Receipts API from PostalForm — 1 operation(s) for return receipts.
  name: PostalForm Return Receipts API
  slug: postalform-com-return-receipts-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Webhook Endpoints API from PostalForm — 3 operation(s) for webhook endpoints.
  name: PostalForm Webhook Endpoints API
  slug: postalform-com-webhook-endpoints-api
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: The Webhook Events API from PostalForm — 2 operation(s) for webhook events.
  name: PostalForm Webhook Events API
  slug: postalform-com-webhook-events-api
artifact_total: 22
asyncapis:
- description: ''
  name: Postalform Com Projects Webhooks
  slug: postalform-com-projects-webhooks
common:
- group: other
  href: https://artifacts.apis.io/postalform-com/capabilities/postalform-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/postalform-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/postalform-com/overlays/postalform-com-machine-payments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postalform-com-machine-payments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/postalform-com/overlays/postalform-com-projects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postalform-com-projects-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://postalform.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://projects.postalform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://postalform.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://postalform.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://postalform.com/developers/quickstart
- group: operate
  title: ''
  type: Support
  url: https://postalform.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://postalform.com/help
- group: company
  title: ''
  type: Blog
  url: https://blog.postalform.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.postalform.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postalform
- group: commercial
  title: ''
  type: Pricing
  url: https://postalform.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://projects.postalform.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postalform.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postalform.com/privacy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://postalform.com/acceptable-use
- group: operate
  title: ''
  type: StatusPage
  url: https://postalform.com/api/health
- group: operate
  href: https://artifacts.apis.io/postalform-com/changelog/postalform-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/postalform-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://blog.postalform.com/
- group: other
  title: ''
  type: APIsJson
  url: https://postalform.com/apis.json
- group: agent
  href: https://artifacts.apis.io/postalform-com/llms/postalform-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postalform-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://postalform.com/llms.txt
- group: other
  href: https://artifacts.apis.io/postalform-com/a2a/postalform-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/postalform-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/postalform-com/mcp/postalform-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/postalform-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/postalform-com/mcp/postalform-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/postalform-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/postalform-com/well-known/postalform-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postalform-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/postalform-com/well-known/postalform-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/postalform-com-api-catalog.json
- group: other
  href: https://artifacts.apis.io/postalform-com/well-known/postalform-com-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/postalform-com-robots.txt
- group: agent
  href: https://artifacts.apis.io/postalform-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/postalform-com/authentication/postalform-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postalform-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/conventions/postalform-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postalform-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/conventions/postalform-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postalform-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/errors/postalform-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postalform-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/lifecycle/postalform-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/postalform-com-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/postalform-com/sandbox/postalform-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/postalform-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/conformance/postalform-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postalform-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/data-model/postalform-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postalform-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/postalform-com/asyncapi/postalform-com-projects-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/postalform-com-projects-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/postalform-com/plans/postalform-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postalform-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/postalform-com/rate-limits/postalform-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postalform-com-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/postalform-com/packages/postalform-com-packages.yml
  title: ''
  type: Packages
  url: packages/postalform-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/postalform-com/agentic-access/postalform-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postalform-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/postalform-com/security/postalform-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postalform-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://postalform.com/privacy
created: '2026-09-19'
description: 'PostalForm is an online print-and-mail service operated by MindBike Technologies LLC that turns PDFs, letters, filled government and consumer forms, dispute packets, postcards and CSV bulk campaigns into real postal mail for twelve countries, with address validation, Certified Mail and electronic return receipts. It is built agent-first: a remote MCP server at https://postalform.com/mcp (12 tools, no credential to connect) creates reviewable hosted-checkout drafts; a 17-operation Machine Payments API lets autonomous runtimes validate, pay for and track orders through x402 (USDC on Base) or Stripe''s Machine Payments Protocol under an HTTP 402 challenge; an A2A 1.0 agent card, UCP and ACP checkout endpoints, an RFC 9727 api-catalog, an APIs.json index and an x402 manifest are served from /.well-known/. PostalForm Projects (25 operations) adds API-key workspaces with a free test mode, final-price quotes, Idempotency-Key orders, prepaid credits and signed webhooks.'
finops:
- has_sources: true
  method: derived
  name: Postalform Com Finops
  primary_unit: ''
  service_category: ''
  slug: postalform-com-finops
  template: true
image: https://postalform.com/og/default.png
layout: provider
mcp_servers:
- description: PostalForm operates ONE remote MCP server at https://postalform.com/mcp — the same host as its website, OpenAPI, A2A card and machine-payments REST API. It is Streamable HTTP (the developers page docu
  name: PostalForm MCP Server
  slug: postalform-com-mcp-yml
modified: '2026-09-19'
name: PostalForm
nav: Providers
network: true
overview: 'PostalForm publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api Keys API, Credits API, Documents API, and 8 more. Tagged areas include Physical Mail, Print & Mail, Postal Mail, Certified Mail, and Documents.


  The PostalForm catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PostalForm''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Postalform Com Plans Pricing
  plan_count: 3
  slug: postalform-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Postalform Com Rate Limits
  slug: postalform-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: PostalForm API Rules
  rule_count: 53
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 6
  slug: postalform-com-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 52.5
    developer_ergonomics: 48.8
    discoverability: 75.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 11.1
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/postalform-com/postalform-com-2026-10-11T112716.png
security:
- kind: authentication
  name: Postalform Com Authentication
  slug: postalform-com-authentication
  summary_line: http/none/payment-gated · 3 schemes
- kind: domain-security
  name: Postalform Com Domain Security
  slug: postalform-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: postalform-com-machine-order-x402-mpp
  slug: postalform-com-machine-order-x402-mpp
- name: postalform-com-projects-send-letter
  slug: postalform-com-projects-send-letter
slug: postalform-com
tags:
- Physical Mail
- Print & Mail
- Postal Mail
- Certified Mail
- Documents
- Agents
- Agentic Commerce
- MCP
- A2A
- x402
- Machine Payments
- Webhook
- Agent-Native
- United States
website: https://postalform.com/
---
