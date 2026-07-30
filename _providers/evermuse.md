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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Evermuse Agentic Access
  operation_count: 3
  slug: evermuse-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Send data to Evermuse
  name: Evermuse ingestion API
  slug: evermuse-ingestion-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://evermuse.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evermuse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evermuse.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evermuse.com/api-reference/index
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evermuse.com/
- group: company
  title: ''
  type: Blog
  url: https://www.evermuse.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.evermuse.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evermuse.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.evermuse.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evermuse.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evermuse.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://evermuse.checkly-status-page.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/evermuse-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evermuse-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evermuse-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/evermuse-scopes.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/evermuse-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evermuse-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evermuse-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evermuse-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evermuse-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.evermuse.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/evermuse-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.evermuse.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/evermuse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evermuse-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evermuse-agentic-access.yml
created: '2026-07-17'
description: Evermuse is an AI advisor for product teams that turns every customer signal — sales and success calls, support conversations, meeting notes, emails, surveys, and reviews — into code-ready, well-researched feature specifications. Its Ingestion API accepts records wrapped in a canonical Integration Envelope (JSON or NDJSON), validates, normalizes, deduplicates, and stores them in the Evermuse Data Lake for AI analysis into user needs, feature requests, and prioritized opportunities. Evermuse also publishes a hosted, OAuth 2.1-protected Model Context Protocol (MCP) server that plugs Claude, ChatGPT, Cursor, and other agents directly into a workspace's real customer evidence and live roadmap.
image: https://www.evermuse.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: evermuse-mcp.yml
  slug: evermuse-mcpyml
modified: '2026-07-19'
name: Evermuse
nav: Providers
network: true
overview: 'Evermuse publishes 1 API on the [APIs.io](https://apis.io/) network: ingestion API. Tagged areas include Company, Product Management, Customer Feedback, Voice of Customer, and Artificial Intelligence.


  Evermuse''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 56
scopes:
- name: Evermuse Scopes
  scope_count: 3
  slug: evermuse-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 56.2
  delta: 0.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evermuse/refs/heads/main/screenshots/evermuse-2026-07-25T213734.png
security:
- kind: authentication
  name: Evermuse Authentication
  slug: evermuse-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Evermuse Domain Security
  slug: evermuse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Evermuse Vulnerability Disclosure
  slug: evermuse-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Evermuse Trust Center
  slug: evermuse-trust-center
  summary_line: SOC 2, GDPR
slug: evermuse
tags:
- Company
- Product Management
- Customer Feedback
- Voice of Customer
- Artificial Intelligence
- Data Ingestion
- Product Analytics
- MCP
- Developer Tools
website: https://evermuse.com
---
