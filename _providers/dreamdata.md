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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Segment-compatible event tracking API for capturing B2B customer journey events. Server-side events are POSTed as a batch to the HTTP endpoint with HTTP Basic auth (source API key as username, empty p
  name: Dreamdata Event Tracking API
  slug: dreamdata-event-tracking-api
artifact_total: 10
asyncapis:
- description: ''
  name: Dreamdata Webhook Syncs
  slug: dreamdata-webhook-syncs
common:
- group: company
  title: ''
  type: Website
  url: https://dreamdata.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dreamdata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dreamdata.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dreamdata.io/client-side/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dreamdata.io/
- group: company
  title: ''
  type: Blog
  url: https://dreamdata.io/blog
- group: operate
  title: ''
  type: Support
  url: https://dreamdata.io/support
- group: commercial
  title: ''
  type: Pricing
  url: https://dreamdata.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.dreamdata.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dreamdata.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dreamdata.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dreamdata-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dreamdata.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dreamdata.io/
- group: auth
  title: ''
  type: Compliance
  url: https://dreamdata.io/security
- group: auth
  title: ''
  type: Security
  url: https://dreamdata.io/security/bounty-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamdata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dreamdata-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dreamdata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dreamdata-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dreamdata-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/dreamdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dreamdata-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dreamdata-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dreamdata-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dreamdata-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dreamdata-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dreamdata-webhook-syncs.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dreamdata-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dreamdata-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dreamdata-error-codes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dreamdata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dreamdata-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Dreamdata is a B2B revenue attribution and go-to-market data platform founded in 2018 in Copenhagen. It connects every marketing and sales touchpoint — from anonymous web visits and ad clicks to CRM opportunities and closed-won revenue — into one clean, account-based customer journey data model. The platform delivers multi-touch attribution, pipeline and revenue analytics, AI-powered audience building, and activation that syncs audiences to ad networks and downstream tools. For developers Dreamdata exposes a Segment-compatible event tracking API (client-side JavaScript and a server-side HTTP batch endpoint), a data warehouse model, outbound webhook syncs, first-party Node.js and Go SDKs, and a hosted remote MCP server secured with OAuth 2.1 PKCE for agent access.
image: http://static1.squarespace.com/static/60880c8985e48a388d33bd16/t/6821cbca7c756751d5f1473a/1748866920123/Activation+and+Attribution+for+B2B+Marketing.png?format=1500w
layout: provider
mcp_servers:
- description: ''
  name: Dreamdata MCP Server
  slug: dreamdata-mcp-server
modified: '2026-08-13'
name: Dreamdata
nav: Providers
network: true
overview: 'Dreamdata publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B Attribution, Revenue Attribution, Marketing Analytics, and Customer Journey.


  The Dreamdata catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dreamdata''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Dreamdata Plans Pricing
  plan_count: 2
  slug: dreamdata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Dreamdata Rate Limits
  slug: dreamdata-rate-limits
scopes:
- name: Dreamdata Scopes
  scope_count: 5
  slug: dreamdata-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 53.8
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 53.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dreamdata/refs/heads/main/screenshots/dreamdata-2026-07-25T212356.png
security:
- kind: authentication
  name: Dreamdata Authentication
  slug: dreamdata-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Dreamdata Domain Security
  slug: dreamdata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dreamdata Vulnerability Disclosure
  slug: dreamdata-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Dreamdata Trust Center
  slug: dreamdata-trust-center
  summary_line: SOC 2 Type II, GDPR, US Privacy
slug: dreamdata
tags:
- Company
- B2B Attribution
- Revenue Attribution
- Marketing Analytics
- Customer Journey
- Event Tracking
- Audience Activation
- Analytics
- MCP
website: https://dreamdata.io
---
