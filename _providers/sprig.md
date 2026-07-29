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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sprig Agentic Access
  operation_count: 6
  slug: sprig-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 2
apis:
- description: Operations allowing export of survey data
  name: Sprig V1 API
  slug: sprig-v1-api
- description: The V2 API from Sprig — 3 operation(s) for v2.
  name: Sprig V2 API
  slug: sprig-v2-api
artifact_total: 8
asyncapis:
- description: ''
  name: Sprig Webhooks
  slug: sprig-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sprig.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sprig.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sprig.com/reference/sprig-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sprig.com/docs/installation/introduction-web/web-javascript
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sprig-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sprig.com/
- group: company
  title: ''
  type: Blog
  url: https://sprig.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://sprig.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sprig.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sprig.com/ssa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sprig.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@sprig.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UserLeap
- group: build
  title: ''
  type: Packages
  url: packages/sprig-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sprig-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sprig-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sprig-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sprig-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sprig-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sprig-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sprig-conventions.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sprig-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sprig-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sprig-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprig-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sprig-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sprig.com/
created: '2026-07-17'
description: Sprig is a continuous product-research platform that helps teams automatically capture user insights to improve their product, user experience, and marketing. Sprig delivers in-product studies and surveys to specific users at specific moments across web and mobile, then uses AI to synthesize responses into themes. For developers, Sprig ships a REST API (api.sprig.com) to export studies, responses, and themes and to manage users, web/mobile SDKs (JavaScript, iOS, Android, React Native, Flutter), a webhook event surface, and an official hosted MCP server for AI clients. Formerly UserLeap.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprig.png
layout: provider
mcp_servers:
- description: ''
  name: sprig-mcp.yml
  slug: sprig-mcpyml
modified: '2026-07-21'
name: Sprig
nav: Providers
network: true
overview: 'Sprig publishes 2 APIs on the [APIs.io](https://apis.io/) network: V1 API and V2 API. Tagged areas include Company, Product Research, Surveys, User Insights, and Customer Experience.


  The Sprig catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sprig''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 75
scopes:
- name: Sprig Scopes
  scope_count: 5
  slug: sprig-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 55.4
  delta: 0.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.9
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sprig Authentication
  slug: sprig-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sprig Domain Security
  slug: sprig-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sprig
tags:
- Company
- Product Research
- Surveys
- User Insights
- Customer Experience
- Analytics
- Product Analytics
- AI
- SaaS
website: https://sprig.com/
---
