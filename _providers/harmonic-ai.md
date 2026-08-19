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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Harmonic Ai Agentic Access
  operation_count: 113
  slug: harmonic-ai-agentic-access
  summary_line: 113 operations · 70 acting
api_count: 2
apis:
- description: 'REST API for company search, enrichment, saved searches, list management, and bulk operations, plus a full GraphQL endpoint for flexible queries across companies, people, investors, lists, and custom '
  name: Harmonic REST & GraphQL API
  slug: harmonic-rest-graphql-api
- description: Hosted, agent-native MCP server exposing 40+ tools for enrichment, search, saved searches, lists, investors, network mapping, batch lookup, custom fields, and team. Listed in the Claude Connector stor
  name: Harmonic MCP Server
  slug: harmonic-mcp-server
artifact_total: 22
asyncapis:
- description: ''
  name: Harmonic Ai Event Surface
  slug: harmonic-ai-event-surface
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harmonic.ai Public attachments API
  slug: open-harmonic-ai-attachments-api
- collection_type: open
  name: Harmonic.ai Public companies API
  slug: open-harmonic-ai-companies-api
- collection_type: open
  name: Harmonic.ai Public email_enrichment API
  slug: open-harmonic-ai-email-enrichment-api
- collection_type: open
  name: Harmonic.ai Public enrichment API
  slug: open-harmonic-ai-enrichment-api
- collection_type: open
  name: Harmonic.ai Public investors API
  slug: open-harmonic-ai-investors-api
- collection_type: open
  name: Harmonic.ai Public people API
  slug: open-harmonic-ai-people-api
- collection_type: open
  name: Harmonic.ai Public persons API
  slug: open-harmonic-ai-persons-api
- collection_type: open
  name: Harmonic.ai Public saved_searches API
  slug: open-harmonic-ai-saved-searches-api
- collection_type: open
  name: Harmonic.ai Public search API
  slug: open-harmonic-ai-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harmonic-ai-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.harmonic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://console.harmonic.ai/docs/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://console.harmonic.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://console.harmonic.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.harmonic.ai/
- group: company
  title: ''
  type: Blog
  url: https://harmonic.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://harmonic.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.harmonic.ai/signup
- group: start
  title: ''
  type: Login
  url: https://console.harmonic.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harmonic.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harmonic.ai/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/harmonic-ai/harmonic/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harmonic.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://console.harmonic.ai/docs/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harmonic-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmonic-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/harmonic-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harmonic-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/harmonic-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harmonic-ai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harmonic-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harmonic-ai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmonic-ai-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/harmonic-ai-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harmonic-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/harmonic-ai-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/harmonic-ai-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harmonic-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/harmonic-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/harmonic-ai-conformance.yml
created: '2026-07-22'
description: Startup discovery and intelligence platform built on a proprietary database of 30M+ companies and 200M+ people, offering real-time funding data, headcount/traction metrics, team composition, and investor relationships via REST, GraphQL, and a hosted MCP server. Used by venture capital, growth equity, corporate development, and go-to-market teams to find, research, and qualify startups programmatically or through the console web app, Chrome extension, bulk data exports (BigQuery/Snowflake/S3), and CRM integrations (Salesforce/HubSpot/Affinity).
image: https://cdn.prod.website-files.com/6107b1101d4d3e748743f234/65f31ad2b4ac6cf0cb8bd691_og-img.png
layout: provider
mcp_servers:
- description: ''
  name: harmonic-ai-mcp.yml
  slug: harmonic-ai-mcpyml
- description: ''
  name: mcp.api.harmonic.ai
  slug: mcpapiharmonicai
modified: '2026-08-14'
name: Harmonic.ai
nav: Providers
network: true
overview: 'Harmonic.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Harmonic REST & GraphQL API. Tagged areas include startup-intelligence, venture-capital, company-data, people-data, and investor-data.


  The Harmonic.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Harmonic.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Harmonic Ai Plans Pricing
  plan_count: 3
  slug: harmonic-ai-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 0
  name: Harmonic Ai Rate Limits
  slug: harmonic-ai-rate-limits
scopes:
- name: Harmonic Ai Scopes
  scope_count: 2
  slug: harmonic-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 49.0
  delta: -11.1
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 30.3
    contract_quality: 54.9
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/harmonic-ai/refs/heads/main/screenshots/harmonic-ai-2026-07-25T220821.png
security:
- kind: authentication
  name: Harmonic Ai Authentication
  slug: harmonic-ai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Harmonic Ai Domain Security
  slug: harmonic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Harmonic Ai Vulnerability Disclosure
  slug: harmonic-ai-vulnerability-disclosure
  summary_line: Hackerone
slug: harmonic-ai
tags:
- startup-intelligence
- venture-capital
- company-data
- people-data
- investor-data
- funding-data
- data-enrichment
- sales-intelligence
- market-intelligence
- graphql
- mcp
- agent-native
website: https://console.harmonic.ai/
---
