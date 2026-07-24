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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 76.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Stellaconnect Agentic Access
  operation_count: 14
  slug: stellaconnect-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 6
apis:
- description: The Coaching API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for coaching.
  name: Stella Connect (Medallia Agent Connect) Coaching API
  slug: stellaconnect-coaching-api
- description: The Data API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for data.
  name: Stella Connect (Medallia Agent Connect) Data API
  slug: stellaconnect-data-api
- description: The Employees API from Stella Connect (Medallia Agent Connect) — 5 operation(s) for employees.
  name: Stella Connect (Medallia Agent Connect) Employees API
  slug: stellaconnect-employees-api
- description: The Qa API from Stella Connect (Medallia Agent Connect) — 3 operation(s) for qa.
  name: Stella Connect (Medallia Agent Connect) Qa API
  slug: stellaconnect-qa-api
- description: The Recoveries API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for recoveries.
  name: Stella Connect (Medallia Agent Connect) Recoveries API
  slug: stellaconnect-recoveries-api
- description: The Requests API from Stella Connect (Medallia Agent Connect) — 1 operation(s) for requests.
  name: Stella Connect (Medallia Agent Connect) Requests API
  slug: stellaconnect-requests-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stellaconnect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stellaconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stellaconnect.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.medallia.com/en/agent-connect
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medallia.com/en/agent-connect/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.medallia.com/en/agent-connect/api/requests/request-from-any-system
- group: auth
  title: ''
  type: Authentication
  url: authentication/stellaconnect-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stellaconnect-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stellaconnect-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://agentconnect.status.medallia.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stellaconnect-lifecycle.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.medallia.com/en/agent-connect/technical-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stellaservice
- group: start
  title: ''
  type: Login
  url: https://stellaconnect.net
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medallia.com/about/legal/terms/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medallia.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.medallia.com/en/agent-connect/security-policies-and-controls/policies-compliance-and-certification
- group: design
  title: ''
  type: Conformance
  url: conformance/stellaconnect-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stellaconnect-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stellaconnect-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stellaconnect-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stellaconnect-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stellaconnect-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stellaconnect-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stellaconnect-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stellaconnect-requests-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/stellaconnect-data-return-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/stellaconnect-user-management-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stellaconnect-trigger-feedback-survey.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stellaconnect-export-feedback-and-qa-data.md
created: '2026-07-17'
description: Stella Connect, built by StellaService and acquired by Medallia in 2020, is now Medallia Agent Connect — a customer service team platform that pairs real-time customer feedback with agent coaching, quality assurance (QA), and recognition for contact center front-line teams. The product still runs on stellaconnect.net, and its Agent Connect API at api.stellaconnect.net exposes a Requests API for triggering feedback and service recovery surveys from any CRM or helpdesk, a Data Return API for pulling feedback, coaching sessions, QA reviews, audits, and calibrations, and a User Management API for employee lifecycle operations, secured with API keys and HMAC-signed JWTs.
image: https://docs-assets.medallia.com/icons/medallia.svg
layout: provider
mcp_servers:
- description: ''
  name: stellaconnect-mcp.yml
  slug: stellaconnect-mcpyml
modified: '2026-07-21'
name: Stella Connect (Medallia Agent Connect)
nav: Providers
network: true
overview: 'Stella Connect (Medallia Agent Connect) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Coaching API, Data API, Employees API, and 3 more. Tagged areas include Customer Service, Customer Feedback, Quality Assurance, Coaching, and Contact Centers.


  Stella Connect (Medallia Agent Connect)''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, sandbox, and 23 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 5
  name: Stellaconnect Rate Limits
  slug: stellaconnect-rate-limits
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 50.3
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 52.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Stellaconnect Authentication
  slug: stellaconnect-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Stellaconnect Domain Security
  slug: stellaconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stellaconnect
tags:
- Customer Service
- Customer Feedback
- Quality Assurance
- Coaching
- Contact Centers
- Surveys
- Customer Experience
- SaaS
website: https://stellaconnect.com
---
