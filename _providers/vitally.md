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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Vitally Agentic Access
  operation_count: 31
  slug: vitally-agentic-access
  summary_line: 31 operations · 14 acting
api_count: 9
apis:
- description: The Accounts API from Vitally — 3 operation(s) for accounts.
  name: Vitally Accounts API
  slug: vitally-accounts-api
- description: The Admins API from Vitally — 1 operation(s) for admins.
  name: Vitally Admins API
  slug: vitally-admins-api
- description: The Conversations API from Vitally — 1 operation(s) for conversations.
  name: Vitally Conversations API
  slug: vitally-conversations-api
- description: The Custom Objects API from Vitally — 1 operation(s) for custom objects.
  name: Vitally Custom Objects API
  slug: vitally-custom-objects-api
- description: The Notes API from Vitally — 2 operation(s) for notes.
  name: Vitally Notes API
  slug: vitally-notes-api
- description: The NPS Responses API from Vitally — 2 operation(s) for nps responses.
  name: Vitally NPS Responses API
  slug: vitally-nps-responses-api
- description: The Organizations API from Vitally — 2 operation(s) for organizations.
  name: Vitally Organizations API
  slug: vitally-organizations-api
- description: The Tasks API from Vitally — 2 operation(s) for tasks.
  name: Vitally Tasks API
  slug: vitally-tasks-api
- description: The Users API from Vitally — 3 operation(s) for users.
  name: Vitally Users API
  slug: vitally-users-api
artifact_total: 17
asyncapis:
- description: ''
  name: Vitally Webhooks
  slug: vitally-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/vitally-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://vitally.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vitally.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vitally.io/en/articles/9880649-rest-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vitally.io/en/articles/11048953-getting-started-with-vitally-as-an-admin
- group: operate
  title: ''
  type: Support
  url: https://docs.vitally.io/
- group: company
  title: ''
  type: Blog
  url: https://www.vitally.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vitally.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.vitally.io/demo-request
- group: start
  title: ''
  type: Login
  url: https://login.vitally.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vitally.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vitally.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://vitally.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vitally-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vitally-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vitally-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/vitally-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vitally-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vitally-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vitally-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vitally-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vitally-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.vitally.io/security
- group: auth
  title: ''
  type: Security
  url: https://www.vitally.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/vitally-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vitally-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitally-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vitally-agentic-access.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vitally-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/vitally-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vitally-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vitally-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/vitally-components.yml
created: '2026-07-17'
description: Vitally is an AI-powered Customer Success platform (CSP) that unifies customer data, health scores, and revenue context with workflow automation — Hubs, automated Playbooks, Docs, Projects, and NPS and custom surveys — plus Vitally AI (Copilot, Summaries, Meeting Recorder). Its public REST API exposes the core Customer Success objects (accounts, organizations, users, tasks, notes, conversations, NPS responses, custom objects) over HTTP Basic auth with cursor pagination and RateLimit headers, and an official remote MCP server (Beta) connects MCP-compatible AI clients to a Vitally workspace.
image: https://cdn.prod.website-files.com/63d3e5f547ca0a274b2e07e1/65456c4b07c63e23bfaedbea_logo-vitally.png
layout: provider
mcp_servers:
- description: ''
  name: vitally-mcp.yml
  slug: vitally-mcpyml
modified: '2026-07-21'
name: Vitally
nav: Providers
network: true
overview: 'Vitally publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Admins API, Conversations API, and 6 more. Tagged areas include Company, Customer Success, SaaS, CRM, and NPS.


  The Vitally catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vitally''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 77
rate_limits:
- limit_count: 1
  name: Vitally Rate Limits
  slug: vitally-rate-limits
score:
  band: strong
  composite: 60.8
  delta: -1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.2
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 71.1
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Vitally Authentication
  slug: vitally-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vitally Domain Security
  slug: vitally-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vitally Vulnerability Disclosure
  slug: vitally-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Vitally Trust Center
  slug: vitally-trust-center
  summary_line: SOC 2, GDPR
slug: vitally
tags:
- Company
- Customer Success
- SaaS
- CRM
- NPS
- Surveys
- Analytics
- Artificial Intelligence
website: https://vitally.io/
---
