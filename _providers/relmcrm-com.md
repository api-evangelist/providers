---
access_model:
  confidence: high
  label: Self-serve signup · free tier · no-account test widget
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - pricing
  - sandbox
  - authentication
  trial: true
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.2
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://api.relmcrm.com/v1
  baseurl_source: declared
  description: REST surface for the whole Relm workspace — contacts, companies, deals, activities (full CRUD with soft delete + restore), pipelines and stages, custom fields / enum values / object types, automations
  name: Relm CRM REST API
  slug: relm-crm-rest-api
- description: First-party hosted Model Context Protocol server (Streamable HTTP) at https://api.relmcrm.com/mcp. 41 typed tools covering every REST capability — schema discovery, search, list/get/create/update/dele
  name: Relm MCP Server
  slug: relm-mcp-server
- description: Agent2Agent (A2A 0.3.0) JSON-RPC endpoint at https://api.relmcrm.com/a2a. A message/send whose data part is {tool, arguments} runs one of the same 41 MCP tools synchronously and returns a terminal Tas
  name: Relm A2A Agent
  slug: relm-a2a-agent
artifact_total: 12
asyncapis:
- description: ''
  name: Relmcrm Com Webhooks
  slug: relmcrm-com-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/security/relmcrm-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/relmcrm-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/security/relmcrm-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/relmcrm-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/security/relmcrm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relmcrm-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/authentication/relmcrm-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/relmcrm-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/scopes/relmcrm-com-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/changelog/relmcrm-com-changelog.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/llms/relmcrm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/relmcrm-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://relmcrm.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/well-known/relmcrm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/relmcrm-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/well-known/relmcrm-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/relmcrm-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/a2a/relmcrm-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/relmcrm-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/mcp/relmcrm-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/relmcrm-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/mcp/relmcrm-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/relmcrm-com-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/packages/relmcrm-com-packages.yml
  title: ''
  type: Packages
  url: packages/relmcrm-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/packages/relmcrm-com-packages.yml
  title: ''
  type: SDKs
  url: packages/relmcrm-com-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/plans/relmcrm-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/relmcrm-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/rate-limits/relmcrm-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/relmcrm-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/sandbox/relmcrm-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/relmcrm-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/conventions/relmcrm-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/relmcrm-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/conventions/relmcrm-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/relmcrm-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/errors/relmcrm-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/relmcrm-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/data-model/relmcrm-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/relmcrm-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/lifecycle/relmcrm-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/relmcrm-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/conformance/relmcrm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/relmcrm-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/asyncapi/relmcrm-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/relmcrm-com-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/overlays/relmcrm-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/relmcrm-com-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/skills/_index.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/relmcrm-com/refs/heads/main/regulatory/relmcrm-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/relmcrm-com-regulatory-posture.yml
created: '2026-09-19'
description: 'Relm is an API-first CRM built for LLMs and AI agents, operated by ASP FZE LLC (Sharjah, UAE) with data hosted in Helsinki, Finland. Contacts, companies, deals, activities, pipelines, automations, drip sequences, templates and webhooks are exposed three ways over one workspace key: a 72-operation OpenAPI 3.1 REST API at https://api.relmcrm.com/v1, a hosted Streamable-HTTP MCP server at https://api.relmcrm.com/mcp whose 41 typed tools answer an anonymous tools/list, and an A2A 0.3.0 agent card at https://relmcrm.com/.well-known/agent-card.json backed by a JSON-RPC endpoint at https://api.relmcrm.com/a2a. Auth is a workspace bearer key (relm_live_ / free isolated relm_test_) or OAuth 2.1 with PKCE and RFC 7591 dynamic client registration; errors are RFC 9457 problem+json carrying valid_options and a suggestion so an agent self-corrects; writes carry Idempotency-Key on the core creates and If-Match optimistic concurrency on updates. Priced per API request (Free 1,000/mo, Pro $29
  for 100,000, Scale $249 for 2,000,000) rather than per seat. The web dashboard is described by the provider as "the thin part".'
image: https://relmcrm.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: Relm MCP Server
  slug: relm-mcp-server
- description: ''
  name: Live MCP endpoint (Streamable HTTP)
  slug: live-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Relm
nav: Providers
network: true
overview: 'Relm publishes 1 API on the [APIs.io](https://apis.io/) network: CRM REST API. Tagged areas include CRM, Sales, Contacts, Deals, and Sales Pipeline.


  The Relm catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Relm''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Relmcrm Com Plans Pricing
  plan_count: 3
  slug: relmcrm-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Relmcrm Com Rate Limits
  slug: relmcrm-com-rate-limits
scopes:
- name: Relmcrm Com Scopes
  scope_count: 1
  slug: relmcrm-com-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 63.1
    developer_ergonomics: 70.8
    discoverability: 75.9
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 60.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
