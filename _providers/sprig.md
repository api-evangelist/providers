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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.5
  scored_at: '2026-08-24'
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
artifact_total: 11
asyncapis:
- description: ''
  name: Sprig Webhooks
  slug: sprig-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sprig V1 API
  slug: open-sprig-v1-api
- collection_type: open
  name: Sprig V1 V2 API
  slug: open-sprig-v2-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sprig-api-overlay.yaml
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
  name: Sprig MCP Server
  slug: sprig-mcp-server
modified: '2026-07-21'
name: Sprig
nav: Providers
network: true
overview: 'Sprig publishes 2 APIs on the [APIs.io](https://apis.io/) network: V1 API and V2 API. Tagged areas include Company, Product Research, Surveys, User Insights, and Customer Experience.


  The Sprig catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sprig''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 3
scopes:
- name: Sprig Scopes
  scope_count: 5
  slug: sprig-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 16.7
    contract_quality: 67.8
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 52.7
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sprig/refs/heads/main/screenshots/sprig-2026-08-17T082046.png
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
- Artificial Intelligence
- Software-as-a-Service
website: https://sprig.com/
---
