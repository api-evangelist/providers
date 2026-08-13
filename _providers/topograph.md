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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 10
  human_in_the_loop: 10
  name: Topograph Agentic Access
  operation_count: 22
  slug: topograph-agentic-access
  summary_line: 22 operations · 10 acting · 10 human-in-the-loop
api_count: 7
apis:
- description: The Billing API from Topograph — 1 operation(s) for billing.
  name: Topograph Billing API
  slug: topograph-billing-api
- description: The Billing Notifications API from Topograph — 3 operation(s) for billing notifications.
  name: Topograph Billing Notifications API
  slug: topograph-billing-notifications-api
- description: The Data API from Topograph — 3 operation(s) for data.
  name: Topograph Data API
  slug: topograph-data-api
- description: The Monitors API from Topograph — 3 operation(s) for monitors.
  name: Topograph Monitors API
  slug: topograph-monitors-api
- description: The Pricing API from Topograph — 1 operation(s) for pricing.
  name: Topograph Pricing API
  slug: topograph-pricing-api
- description: The Search API from Topograph — 1 operation(s) for search.
  name: Topograph Search API
  slug: topograph-search-api
- description: The Workspaces API from Topograph — 3 operation(s) for workspaces.
  name: Topograph Workspaces API
  slug: topograph-workspaces-api
arazzos:
- description: Start monitoring a company, review its change logs, then stop monitoring.
  name: Monitor a company for register changes
  slug: topograph-monitor-company
- description: Search for a company, request its data and documents, then poll for the result.
  name: Resolve a company and retrieve KYB data
  slug: topograph-resolve-and-retrieve
artifact_total: 16
asyncapis:
- description: ''
  name: Topograph Monitoring Webhooks
  slug: topograph-monitoring-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.topograph.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.topograph.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.topograph.co/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.topograph.co/quickstart
- group: company
  title: ''
  type: Blog
  url: https://topograph.co/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://topograph.co/blog/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://topograph.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.topograph.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://topograph.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://topograph.co/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/topograph-data/
- group: company
  title: ''
  type: Website
  url: http://topograph.co
- group: agent
  title: ''
  type: MCPServer
  url: mcp/topograph-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/topograph-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/topograph-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/topograph-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/topograph-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/topograph-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/topograph-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/topograph-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/topograph-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/topograph-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/topograph-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/topograph-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/topograph-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.topograph.co/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/topograph-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/topograph-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/topograph-monitoring-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/topograph-resolve-and-retrieve.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/topograph-monitor-company.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/topograph-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/topograph-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/topograph-domain-security.yml
created: '2026-07-17'
description: Topograph is a KYB (Know Your Business) data platform that connects directly to official European and international business registers (35+ countries) for real-time company verification. It provides company data and official documents with source-traceable provenance, ownership-graph analysis across shareholders, ultimate beneficial owners and subsidiaries, cross-border entity resolution, and continuous change monitoring delivered over webhooks. Built for fintechs, neobanks and compliance software vendors, Topograph is exposed as a REST API (x-api-key) with a published MCP server, an x402 agentic-commerce surface, and pay-per-request pricing, backed by SOC 2 Type 2 and ISO 27001:2022 certifications.
image: https://www.topograph.co/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: topograph-mcp.yml
  slug: topograph-mcpyml
modified: '2026-07-21'
name: Topograph
nav: Providers
network: true
overview: 'Topograph publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Billing Notifications API, Data API, and 4 more. Tagged areas include Company, KYB, Company Data, Business Registers, and Compliance.


  The Topograph catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Topograph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 28 more developer resources.'
random_paper: 20
scopes:
- name: Topograph Scopes
  scope_count: 7
  slug: topograph-scopes
  summary_line: 7 scopes · authorizationCode/refreshToken
score:
  band: strong
  composite: 57.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.5
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Topograph Authentication
  slug: topograph-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Topograph Domain Security
  slug: topograph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Topograph Trust Center
  slug: topograph-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type 2, Penetration test certification
slug: topograph
tags:
- Company
- KYB
- Company Data
- Business Registers
- Compliance
- Identity Verification
- Beneficial Ownership
- AML
- Due Diligence
- Fintech
website: http://topograph.co
---
