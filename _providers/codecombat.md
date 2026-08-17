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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: The Auth API from CodeCombat — 1 operation(s) for auth.
  name: CodeCombat Auth API
  slug: codecombat-auth-api
- description: The Clans API from CodeCombat — 1 operation(s) for clans.
  name: CodeCombat Clans API
  slug: codecombat-clans-api
- description: The Classrooms API from CodeCombat — 6 operation(s) for classrooms.
  name: CodeCombat Classrooms API
  slug: codecombat-classrooms-api
- description: The Default API from CodeCombat — 1 operation(s) for default.
  name: CodeCombat Default API
  slug: codecombat-default-api
- description: The Stats API from CodeCombat — 2 operation(s) for stats.
  name: CodeCombat Stats API
  slug: codecombat-stats-api
- description: The Users API from CodeCombat — 10 operation(s) for users.
  name: CodeCombat Users API
  slug: codecombat-users-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CodeCombat Auth API
  slug: open-codecombat-auth-api
- collection_type: open
  name: CodeCombat Auth Clans API
  slug: open-codecombat-clans-api
- collection_type: open
  name: CodeCombat Auth Classrooms API
  slug: open-codecombat-classrooms-api
- collection_type: open
  name: CodeCombat Auth  API
  slug: open-codecombat-default-api
- collection_type: open
  name: CodeCombat Auth Stats API
  slug: open-codecombat-stats-api
- collection_type: open
  name: CodeCombat Auth Users API
  slug: open-codecombat-users-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codecombat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codecombat-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.codecombat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.codecombat.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.codecombat.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codecombat
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codecombat.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://codecombat.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codecombat.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codecombat.com/legal
- group: operate
  title: ''
  type: Support
  url: https://codecombat.com/help
- group: company
  title: ''
  type: Blog
  url: https://codecombat.com/blog
- group: build
  title: ''
  type: Packages
  url: packages/codecombat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/codecombat-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/codecombat/codecombat-postman
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codecombat-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codecombat-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/codecombat-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/codecombat-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codecombat-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codecombat-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codecombat-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: CodeCombat is a game-based computer science platform where students learn to code by playing a real programming game, writing Python or JavaScript to control heroes through levels. Its Partner API (a Fern-generated REST API at https://codecombat.com/api, secured with HTTP Basic authentication) lets learning platforms and school districts provision and manage users, create and administer classrooms, enroll students in courses, grant and shorten licenses and Home subscriptions, link OAuth2 SSO identities, manage clans, and pull playtime, license, and per-member progress statistics. CodeCombat is backed by a16z and Y Combinator and publishes official Node, Python, Java, and Go SDKs plus a Postman collection generated from its public OpenAPI description.
image: https://avatars.githubusercontent.com/u/5795842?v=4
layout: provider
mcp_servers:
- description: ''
  name: codecombat-mcp.yml
  slug: codecombat-mcpyml
modified: '2026-07-18'
name: CodeCombat
nav: Providers
network: true
overview: 'CodeCombat publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Clans API, Classrooms API, and 3 more. Tagged areas include Company, Education, EdTech, Coding, and Learning.


  CodeCombat''s developer surface includes authentication, documentation, API reference, pricing, support, engineering blog, and 17 more developer resources.'
random_paper: 147
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 55.2
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 43.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codecombat/refs/heads/main/screenshots/codecombat-2026-07-25T205918.png
security:
- kind: authentication
  name: Codecombat Authentication
  slug: codecombat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Codecombat Domain Security
  slug: codecombat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: codecombat
tags:
- Company
- Education
- EdTech
- Coding
- Learning
- Classroom
- Students
- Gamification
- SSO
- Developer Tools
website: https://api-docs.codecombat.com/
---
