---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
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
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The Externally recorded demos API from Demodesk — 3 operation(s) for externally recorded demos.
  name: Demodesk Externally recorded demos API
  slug: demodesk-externally-recorded-demos-api
- description: Endpoints to discover recordings and fetch related artifacts.
  name: Demodesk Recordings API
  slug: demodesk-recordings-api
- description: Endpoints regarding user management.
  name: Demodesk Users API
  slug: demodesk-users-api
artifact_total: 15
asyncapis:
- description: Event notifications Demodesk POSTs to a subscriber endpoint.
  name: Demodesk Webhooks
  slug: demodesk-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API V1 Externally recorded demos API
  slug: open-demodesk-externally-recorded-demos-api
- collection_type: open
  name: API V1 Externally recorded demos Recordings API
  slug: open-demodesk-recordings-api
- collection_type: open
  name: API V1 Externally recorded demos Users API
  slug: open-demodesk-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/demodesk-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demodesk-v2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://demodesk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://demodesk.com/api/docs/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.demodesk.com/en/collections/3177803-api-integrations
- group: docs
  title: ''
  type: APIReference
  url: https://help.demodesk.com/en/articles/8518816-api-reference
- group: operate
  title: ''
  type: Support
  url: https://help.demodesk.com
- group: company
  title: ''
  type: Blog
  url: https://demodesk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://demodesk.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://demodesk.com/manage/auth/register?seatType=ci
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demodesk.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demodesk.com/legal/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demodesk
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demodesk.com
- group: operate
  title: ''
  type: Roadmap
  url: https://demodesk.com/blog
- group: auth
  title: ''
  type: Authentication
  url: authentication/demodesk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/demodesk-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/demodesk-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/demodesk-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/demodesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demodesk-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demodesk-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demodesk-mcp-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/demodesk-packages.yml
- group: design
  title: ''
  type: Components
  url: components/demodesk-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/demodesk-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/demodesk-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/demodesk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.demodesk.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demodesk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/demodesk-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demodesk-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/demodesk-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Demodesk is an AI Sales Agent platform for B2B revenue teams, founded in 2018 in Munich, Germany. Four AI agents (Assistant, Coach, Analyst, CRM Concierge) plus a custom AI Agent Builder record and transcribe sales conversations, generate summaries and scorecards, update CRMs (Salesforce, HubSpot, Pipedrive), coach reps, and flag at-risk deals. The company exposes a public REST API (v2, OpenAPI 3.1) for recordings, transcripts, AI summaries, scorecards, and users, authenticated with Bearer API keys, plus a webhook event surface for meeting and recording lifecycle events and an official hosted MCP server (OAuth2) at demodesk.com/mcp. GDPR-native with EU-only data residency (Azure Frankfurt) and ISO 27001:2022 certification.
image: https://demodesk.com/favicon.ico
layout: provider
mcp_servers:
- description: 'Official hosted, read-only MCP server. Exposes Demodesk meeting recordings, transcripts, AI summaries and coaching scorecards to any MCP client. The company runs a dedicated microsite for it at https:'
  name: Demodesk MCP Server
  slug: demodesk-mcp-server
modified: '2026-08-14'
name: Demodesk
nav: Providers
network: true
overview: 'Demodesk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Externally recorded demos API, Recordings API, and Users API. Tagged areas include Company, Sales, Artificial Intelligence, Conversation Intelligence, and Video Conferencing.


  The Demodesk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Demodesk''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Demodesk Plans Pricing
  plan_count: 3
  slug: demodesk-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Demodesk Rate Limits
  slug: demodesk-rate-limits
scopes:
- name: Demodesk Scopes
  scope_count: 1
  slug: demodesk-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.3
  delta: 1.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 16.7
    contract_quality: 59.7
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 60.5
  previous_composite: 59.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demodesk/refs/heads/main/screenshots/demodesk-2026-07-25T211714.png
security:
- kind: authentication
  name: Demodesk Authentication
  slug: demodesk-authentication
  summary_line: apiKey/http/oauth2 · 2 schemes
- kind: domain-security
  name: Demodesk Domain Security
  slug: demodesk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Demodesk Trust Center
  slug: demodesk-trust-center
  summary_line: ISO 27001, GDPR
slug: demodesk
tags:
- Company
- Sales
- Artificial Intelligence
- Conversation Intelligence
- Video Conferencing
- CRM
- Transcription
- Webhook
- MCP
website: https://demodesk.com/
---
