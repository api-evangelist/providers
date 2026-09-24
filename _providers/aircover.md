---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Remote Model Context Protocol server over Streamable HTTP at https://api.aircover.ai/mcp. An authenticated Aircover user's agent can list and read meetings and transcripts, ask questions across indexe
  name: Aircover MCP Server
  slug: aircover-mcp-server
- baseURL: https://api.aircover.ai
  baseurl_source: declared
  description: 'The public, agent-facing API surface of Aircover described by an OpenAPI 3.0.3 contract: the OAuth 2.0 authorization server (authorize, token, dynamic client registration, revocation), the RFC 8414 an'
  name: Aircover Public Agent API
  slug: aircover-public-agent-api
artifact_total: 16
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
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/llms/aircover-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aircover-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.aircover.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/mcp/aircover-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aircover-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/mcp/aircover-server.json
  title: ''
  type: MCPServer
  url: mcp/aircover-server.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/mcp/aircover-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aircover-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/Aircover/aircover-skills
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/well-known/aircover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aircover-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/packages/aircover-packages.yml
  title: ''
  type: Packages
  url: packages/aircover-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/packages/aircover-packages.yml
  title: ''
  type: SDKs
  url: packages/aircover-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/cli/aircover-cli.yml
  title: ''
  type: CLI
  url: cli/aircover-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/changelog/aircover-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aircover-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Aircover/aircover-pipeline/blob/main/CHANGELOG.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/authentication/aircover-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aircover-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/scopes/aircover-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aircover-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/conformance/aircover-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aircover-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/conventions/aircover-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aircover-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/errors/aircover-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aircover-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/lifecycle/aircover-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aircover-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/plans/aircover-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aircover-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/rate-limits/aircover-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aircover-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/overlays/aircover-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aircover-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/security/aircover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aircover-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/security/aircover-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aircover-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/data-model/aircover-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aircover-data-model.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/json-schema/aircover-pipeline-meetings-1.0.json
  title: ''
  type: JSONSchema
  url: json-schema/aircover-pipeline-meetings-1.0.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aircover/refs/heads/main/regulatory/aircover-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/aircover-regulatory-posture.yml
created: '2026-09-19'
description: 'Aircover is an AI-native revenue agent platform for sales teams: specialist AI agents work before, during and after every customer conversation, joining Zoom, Microsoft Teams, Google Meet and Webex calls to surface real-time coaching, objection handling, battlecards and technical answers from live transcription (no recording by default), then generating notes, follow-ups, MEDDPICC-style qualification scoring and CRM updates into Salesforce, HubSpot and ServiceNow. For developers and agents the company publishes a remote Model Context Protocol server at https://api.aircover.ai/mcp (Streamable HTTP, OAuth 2.0 with PKCE and RFC 7591 dynamic client registration, twelve read tools over meetings, transcripts, agent results, deals, teams, reports and documents), an OpenAPI 3.0.3 contract for the public agent API, an MCP registry server.json manifest, llms.txt, markdown content negotiation on every page, four open-source Claude/ChatGPT Skills and a PyPI-published Python pipeline CLI.
  The full customer REST API and webhooks are customer-only.'
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
- description: ''
  name: Aircover MCP Server
  slug: aircover-mcp-server
- description: ''
  name: Aircover MCP Server
  slug: aircover-mcp-server-2
- description: 'Query your Aircover sales-meeting data: meetings, transcripts, AI agent results, deal qualification (MEDDPICC and more), reports, and indexed documents. Real-time sales coaching platform data via MCP.'
  name: Aircover MCP Server
  slug: aircover-mcp-server-3
- description: ''
  name: Aircover MCP Server
  slug: aircover-mcp-server-4
modified: '2026-09-19'
name: Aircover
nav: Providers
network: true
overview: 'Aircover publishes 1 API on the [APIs.io](https://apis.io/) network: Public Agent API. Tagged areas include Sales Enablement, Conversation Intelligence, Sales Coaching, Revenue Intelligence, and AI Agents.


  Aircover''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, CLI, and 37 more developer resources.'
plans:
- name: Aircover Plans Pricing
  plan_count: 0
  slug: aircover-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Aircover Rate Limits
  slug: aircover-rate-limits
scopes:
- name: Aircover Scopes
  scope_count: 1
  slug: aircover-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 53.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Authentication
website: https://www.aircover.ai/
---
