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
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: First-party hosted Model Context Protocol server (Streamable HTTP) at https://api.relmcrm.com/mcp. 41 typed tools covering every REST capability — schema discovery, search, list/get/create/update/dele
  name: Relm MCP Server
  slug: relm-mcp-server
- description: Agent2Agent (A2A 0.3.0) JSON-RPC endpoint at https://api.relmcrm.com/a2a. A message/send whose data part is {tool, arguments} runs one of the same 41 MCP tools synchronously and returns a terminal Tas
  name: Relm A2A Agent
  slug: relm-a2a-agent
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Activities API from Relm — 3 operation(s) for activities.
  name: Relm Activities API
  slug: relmcrm-com-activities-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Automations API from Relm — 3 operation(s) for automations.
  name: Relm Automations API
  slug: relmcrm-com-automations-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Batch API from Relm — 1 operation(s) for batch.
  name: Relm Batch API
  slug: relmcrm-com-batch-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Companies API from Relm — 3 operation(s) for companies.
  name: Relm Companies API
  slug: relmcrm-com-companies-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Connections API from Relm — 2 operation(s) for connections.
  name: Relm Connections API
  slug: relmcrm-com-connections-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Contacts API from Relm — 3 operation(s) for contacts.
  name: Relm Contacts API
  slug: relmcrm-com-contacts-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Deals API from Relm — 3 operation(s) for deals.
  name: Relm Deals API
  slug: relmcrm-com-deals-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: Self-describing schema, usage, settings.
  name: Relm Discovery API
  slug: relmcrm-com-discovery-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Pipelines API from Relm — 6 operation(s) for pipelines.
  name: Relm Pipelines API
  slug: relmcrm-com-pipelines-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: Custom fields, enums, object types.
  name: Relm Registry API
  slug: relmcrm-com-registry-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Search API from Relm — 1 operation(s) for search.
  name: Relm Search API
  slug: relmcrm-com-search-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Sequences API from Relm — 5 operation(s) for sequences.
  name: Relm Sequences API
  slug: relmcrm-com-sequences-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Templates API from Relm — 2 operation(s) for templates.
  name: Relm Templates API
  slug: relmcrm-com-templates-api
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: The Webhooks API from Relm — 3 operation(s) for webhooks.
  name: Relm Webhooks API
  slug: relmcrm-com-webhooks-api
artifact_total: 31
asyncapis:
- description: ''
  name: Relmcrm Com Webhooks
  slug: relmcrm-com-webhooks
common:
- group: other
  href: https://artifacts.apis.io/relmcrm-com/capabilities/relmcrm-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/relmcrm-com-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/relmcrm-com/security/relmcrm-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/relmcrm-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/relmcrm-com/security/relmcrm-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/relmcrm-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/relmcrm-com/security/relmcrm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relmcrm-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/relmcrm-com/authentication/relmcrm-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/relmcrm-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/relmcrm-com/scopes/relmcrm-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/relmcrm-com-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://relmcrm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://relmcrm.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://relmcrm.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://relmcrm.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://relmcrm.com/docs
- group: operate
  title: ''
  type: Support
  url: https://relmcrm.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://relmcrm.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.relmcrm.com/
- group: start
  title: ''
  type: Login
  url: https://app.relmcrm.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relmcrm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relmcrm.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://relmcrm.com/changelog
- group: operate
  href: https://artifacts.apis.io/relmcrm-com/changelog/relmcrm-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/relmcrm-com-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://relmcrm.com/status
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://relmcrm.com/security
- group: agent
  href: https://artifacts.apis.io/relmcrm-com/llms/relmcrm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/relmcrm-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://relmcrm.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/relmcrm-com/well-known/relmcrm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/relmcrm-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/relmcrm-com/well-known/relmcrm-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/relmcrm-com-security.txt
- group: other
  href: https://artifacts.apis.io/relmcrm-com/a2a/relmcrm-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/relmcrm-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/relmcrm-com/mcp/relmcrm-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/relmcrm-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/relmcrm-com/mcp/relmcrm-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/relmcrm-com-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/relmcrm-com/packages/relmcrm-com-packages.yml
  title: ''
  type: Packages
  url: packages/relmcrm-com-packages.yml
- group: build
  href: https://artifacts.apis.io/relmcrm-com/packages/relmcrm-com-packages.yml
  title: ''
  type: SDKs
  url: packages/relmcrm-com-packages.yml
- group: commercial
  href: https://artifacts.apis.io/relmcrm-com/plans/relmcrm-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/relmcrm-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/relmcrm-com/rate-limits/relmcrm-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/relmcrm-com-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/relmcrm-com/sandbox/relmcrm-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/relmcrm-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/conventions/relmcrm-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/relmcrm-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/conventions/relmcrm-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/relmcrm-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/errors/relmcrm-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/relmcrm-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/data-model/relmcrm-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/relmcrm-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/lifecycle/relmcrm-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/relmcrm-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/conformance/relmcrm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/relmcrm-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/relmcrm-com/asyncapi/relmcrm-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/relmcrm-com-webhooks.yml
- group: other
  href: https://artifacts.apis.io/relmcrm-com/overlays/relmcrm-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/relmcrm-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/relmcrm-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://relmcrm.com/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://relmcrm.com/privacy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://relmcrm.com/privacy
- group: other
  title: ''
  type: ExitAssistance
  url: https://relmcrm.com/terms
- group: other
  href: https://artifacts.apis.io/relmcrm-com/regulatory/relmcrm-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/relmcrm-com-regulatory-posture.yml
created: '2026-09-19'
description: 'Relm is an API-first CRM built for LLMs and AI agents, operated by ASP FZE LLC (Sharjah, UAE) with data hosted in Helsinki, Finland. Contacts, companies, deals, activities, pipelines, automations, drip sequences, templates and webhooks are exposed three ways over one workspace key: a 72-operation OpenAPI 3.1 REST API at https://api.relmcrm.com/v1, a hosted Streamable-HTTP MCP server at https://api.relmcrm.com/mcp whose 41 typed tools answer an anonymous tools/list, and an A2A 0.3.0 agent card at https://relmcrm.com/.well-known/agent-card.json backed by a JSON-RPC endpoint at https://api.relmcrm.com/a2a. Auth is a workspace bearer key (relm_live_ / free isolated relm_test_) or OAuth 2.1 with PKCE and RFC 7591 dynamic client registration; errors are RFC 9457 problem+json carrying valid_options and a suggestion so an agent self-corrects; writes carry Idempotency-Key on the core creates and If-Match optimistic concurrency on updates. Priced per API request (Free 1,000/mo, Pro $29
  for 100,000, Scale $249 for 2,000,000) rather than per seat. The web dashboard is described by the provider as "the thin part".'
finops:
- has_sources: true
  method: derived
  name: Relmcrm Com Finops
  primary_unit: requests
  service_category: ''
  slug: relmcrm-com-finops
  template: false
image: https://relmcrm.com/og.png
layout: provider
mcp_servers:
- description: 'Relm ships a first-party hosted MCP server at https://api.relmcrm.com/mcp (Streamable HTTP). The tool catalog is deliberately public: an anonymous initialize and tools/list both answer HTTP 200 with t'
  name: Relm MCP Server
  slug: relm
modified: '2026-09-19'
name: Relm
nav: Providers
network: true
overview: 'Relm publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Automations API, Batch API, and 13 more. Tagged areas include CRM, Sales, Contacts, Deals, and Sales Pipeline.


  The Relm catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Relm''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 40 more developer resources.'
plans:
- name: Relmcrm Com Plans Pricing
  plan_count: 3
  slug: relmcrm-com-plans-pricing
- name: Relmcrm Com Price Estimates
  plan_count: 0
  slug: relmcrm-com-price-estimates
random_paper: 14
rate_limits:
- limit_count: 0
  name: Relmcrm Com Rate Limits
  slug: relmcrm-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Relm API Rules
  rule_count: 63
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 3
  slug: relmcrm-com-rules
scopes:
- name: Relmcrm Com Scopes
  scope_count: 1
  slug: relmcrm-com-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 59.0
    developer_ergonomics: 49.4
    discoverability: 75.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 67.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 52.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/relmcrm-com/relmcrm-com-2026-10-11T125109.png
security:
- kind: authentication
  name: Relmcrm Com Authentication
  slug: relmcrm-com-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Relmcrm Com Domain Security
  slug: relmcrm-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Relmcrm Com Vulnerability Disclosure
  slug: relmcrm-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 4
skills:
- name: Create a contact and open a deal
  slug: relmcrm-com-create-contact-and-open-deal
- name: Import leads in batch
  slug: relmcrm-com-import-leads-in-batch
- name: Move a deal and log the activity
  slug: relmcrm-com-move-deal-and-log-activity
- name: Subscribe to and verify webhooks
  slug: relmcrm-com-subscribe-and-verify-webhooks
slug: relmcrm-com
tags:
- CRM
- Sales
- Contacts
- Deals
- Sales Pipeline
- Automation
- Webhook
- MCP
- A2A
- AI Agents
- Agent-Native
- United Arab Emirates
website: https://relmcrm.com/
---
