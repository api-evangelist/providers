---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol server over Streamable HTTP at https://api.aircover.ai/mcp. An authenticated Aircover user's agent can list and read meetings and transcripts, ask questions across indexe
  name: Aircover MCP Server
  slug: aircover-mcp-server
- baseURL: https://api.aircover.ai/mcp
  baseurl_source: declared
  description: Machine-readable discovery metadata
  name: Aircover Discovery API
  slug: aircover-discovery-api
- baseURL: https://api.aircover.ai/mcp
  baseurl_source: declared
  description: Model Context Protocol server (Streamable HTTP transport)
  name: Aircover MCP API
  slug: aircover-mcp-api
- baseURL: https://api.aircover.ai/mcp
  baseurl_source: declared
  description: OAuth 2.0 authorization server (authorization code + PKCE, dynamic client registration)
  name: Aircover OAuth API
  slug: aircover-oauth-api
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://www.aircover.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aircover.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.aircover.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.aircover.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aircover.ai/developers
- group: operate
  title: ''
  type: Support
  url: https://www.aircover.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.aircover.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aircover
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aircover.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.aircover.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aircover.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aircover.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.aircover.ai/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.aircover.ai/trust-center
- group: company
  title: ''
  type: About
  url: https://www.aircover.ai/about
- group: company
  title: ''
  type: Careers
  url: https://www.aircover.ai/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aircover-ai
- group: agent
  href: https://artifacts.apis.io/aircover/llms/aircover-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aircover-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.aircover.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/aircover/mcp/aircover-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aircover-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aircover/mcp/aircover-server.json
  title: ''
  type: MCPServer
  url: mcp/aircover-server.json
- group: build
  href: https://artifacts.apis.io/aircover/mcp/aircover-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aircover-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aircover/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/Aircover/aircover-skills
- group: agent
  href: https://artifacts.apis.io/aircover/well-known/aircover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aircover-well-known.yml
- group: build
  href: https://artifacts.apis.io/aircover/packages/aircover-packages.yml
  title: ''
  type: Packages
  url: packages/aircover-packages.yml
- group: build
  href: https://artifacts.apis.io/aircover/packages/aircover-packages.yml
  title: ''
  type: SDKs
  url: packages/aircover-packages.yml
- group: build
  href: https://artifacts.apis.io/aircover/cli/aircover-cli.yml
  title: ''
  type: CLI
  url: cli/aircover-cli.yml
- group: operate
  href: https://artifacts.apis.io/aircover/changelog/aircover-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aircover-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Aircover/aircover-pipeline/blob/main/CHANGELOG.md
- group: auth
  href: https://artifacts.apis.io/aircover/authentication/aircover-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aircover-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aircover/scopes/aircover-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aircover-scopes.yml
- group: design
  href: https://artifacts.apis.io/aircover/conformance/aircover-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aircover-conformance.yml
- group: design
  href: https://artifacts.apis.io/aircover/conventions/aircover-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aircover-conventions.yml
- group: design
  href: https://artifacts.apis.io/aircover/errors/aircover-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aircover-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aircover/lifecycle/aircover-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aircover-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/aircover/plans/aircover-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aircover-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aircover/rate-limits/aircover-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aircover-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/aircover/overlays/aircover-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aircover-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/aircover/security/aircover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aircover-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/aircover/security/aircover-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aircover-trust-center.yml
- group: design
  href: https://artifacts.apis.io/aircover/data-model/aircover-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aircover-data-model.yml
- group: docs
  href: https://artifacts.apis.io/aircover/json-schema/aircover-pipeline-meetings-1.0.json
  title: ''
  type: JSONSchema
  url: json-schema/aircover-pipeline-meetings-1.0.json
- group: other
  href: https://artifacts.apis.io/aircover/regulatory/aircover-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/aircover-regulatory-posture.yml
created: '2026-09-19'
description: 'Aircover is an AI-native revenue agent platform for sales teams: specialist AI agents work before, during and after every customer conversation, joining Zoom, Microsoft Teams, Google Meet and Webex calls to surface real-time coaching, objection handling, battlecards and technical answers from live transcription (no recording by default), then generating notes, follow-ups, MEDDPICC-style qualification scoring and CRM updates into Salesforce, HubSpot and ServiceNow. For developers and agents the company publishes a remote Model Context Protocol server at https://api.aircover.ai/mcp (Streamable HTTP, OAuth 2.0 with PKCE and RFC 7591 dynamic client registration, twelve read tools over meetings, transcripts, agent results, deals, teams, reports and documents), an OpenAPI 3.0.3 contract for the public agent API, an MCP registry server.json manifest, llms.txt, markdown content negotiation on every page, four open-source Claude/ChatGPT Skills and a PyPI-published Python pipeline CLI.
  The full customer REST API and webhooks are customer-only.'
finops:
- has_sources: true
  method: derived
  name: Aircover Finops
  primary_unit: ''
  service_category: ''
  slug: aircover-finops
  template: true
image: https://www.aircover.ai/assets/apple-touch-icon.png
json_schemas:
- name: Aircover Pipeline — agent-outputs/agent_<meeting_id>.json (v1.0)
  property_count: 5
  slug: aircover-pipeline-agent-output-1.0
- name: Aircover Pipeline — failures.json (v1.0)
  property_count: 0
  slug: aircover-pipeline-failures-1.0
- name: Aircover Pipeline — meetings.json (v1.0)
  property_count: 0
  slug: aircover-pipeline-meetings-1.0
- name: Aircover Pipeline — summary.json (v1.0)
  property_count: 14
  slug: aircover-pipeline-summary-1.0
layout: provider
mcp_servers:
- description: Aircover operates ONE remote Model Context Protocol server at https://api.aircover.ai/mcp (Streamable HTTP, OAuth 2.0 authorization code + PKCE with RFC 7591 dynamic client registration). It is the pr
  name: Aircover MCP Server
  slug: aircover-mcp-yml
- description: 'Query your Aircover sales-meeting data: meetings, transcripts, AI agent results, deal qualification (MEDDPICC and more), reports, and indexed documents. Real-time sales coaching platform data via MCP.'
  name: Aircover MCP Server
  slug: ai-aircover-mcp
- description: ''
  name: Aircover MCP Server
  slug: mcp-json
modified: '2026-09-19'
name: Aircover
nav: Providers
network: true
overview: 'Aircover publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, MCP API, OAuth API, and 1 more. Tagged areas include Sales Enablement, Conversation Intelligence, Sales Coaching, Revenue Intelligence, and AI Agents.


  The Aircover catalog on APIs.io includes 1 Spectral governance ruleset.


  Aircover''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, CLI, and 37 more developer resources.'
plans:
- name: Aircover Plans Pricing
  plan_count: 1
  slug: aircover-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Aircover Rate Limits
  slug: aircover-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Aircover API Rules
  rule_count: 70
  severity_counts:
    error: 68
    hint: 0
    info: 1
    warn: 1
  slug: aircover-rules
scopes:
- name: Aircover Scopes
  scope_count: 1
  slug: aircover-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 58.5
    catalog_earned_first_party: 8.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 75.0
    contract_governance: 31.8
    contract_quality: 60.5
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 61.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aircover/aircover-2026-10-11T093353.png
security:
- kind: authentication
  name: Aircover Authentication
  slug: aircover-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Aircover Domain Security
  slug: aircover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aircover Trust Center
  slug: aircover-trust-center
  summary_line: SOC 2 Type II, GDPR
skill_count: 4
skills:
- name: aircover-mutual-action-plan
  slug: aircover-mutual-action-plan
- name: path-to-quota
  slug: aircover-path-to-quota
- name: pre-call-prep
  slug: aircover-pre-call-prep
- name: product-sentiment-tracker
  slug: aircover-product-sentiment-tracker
slug: aircover
tags:
- Sales Enablement
- Conversation Intelligence
- Sales Coaching
- Revenue Intelligence
- AI Agents
- MCP
- Agent-Native
- CRM
- Meetings
- Transcription
- OAuth
- Authentication
website: https://www.aircover.ai/
---
