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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Padlet Agentic Access
  operation_count: 10
  slug: padlet-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 7
apis:
- description: The AI Recipe Boards API from Padlet — 2 operation(s) for ai recipe boards.
  name: Padlet AI Recipe Boards API
  slug: padlet-ai-recipe-boards-api
- description: The Boards API from Padlet — 1 operation(s) for boards.
  name: Padlet Boards API
  slug: padlet-boards-api
- description: The Comments API from Padlet — 1 operation(s) for comments.
  name: Padlet Comments API
  slug: padlet-comments-api
- description: The Organizations API from Padlet — 2 operation(s) for organizations.
  name: Padlet Organizations API
  slug: padlet-organizations-api
- description: The Posts API from Padlet — 2 operation(s) for posts.
  name: Padlet Posts API
  slug: padlet-posts-api
- description: The Reactions API from Padlet — 1 operation(s) for reactions.
  name: Padlet Reactions API
  slug: padlet-reactions-api
- description: The Users API from Padlet — 1 operation(s) for users.
  name: Padlet Users API
  slug: padlet-users-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/padlet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/padlet-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/padlet-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/padlet-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://padlet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.padlet.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.padlet.dev/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.padlet.dev/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.padlet.dev/reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://padlet.help/
- group: commercial
  title: ''
  type: Pricing
  url: https://padlet.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://padlet.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://padlet.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.padlet.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.padlet.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/padlet-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/padlet-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/padlet-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/padlet-security.txt
- group: auth
  title: ''
  type: Security
  url: https://padlet.com/.well-known/security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/padlet-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/padlet-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/padlet-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/padlet-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/padlet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/padlet-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/padlet-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Padlet is a collaborative visual platform of boards and canvases ("padlets") used across education and creative work to collect, organize, and share posts, images, links, and files. Its public REST API (api.padlet.dev, JSON:API) lets paying users read boards with their sections, posts, comments, and reactions, create posts, comments, and reactions, generate AI recipe boards, and read user and organization data — authenticated with an x-api-key header. Padlet also runs an official OAuth-protected MCP server at mcp.padlet.com for agent access.
image: https://elvis.padletcdn.com/1/atat/e_1/appBY8jxCUCf4JUUZ/tblANzywOAIDDHQsQ/recwXBCnX3ozCHYBU/fldKQAixAlmwWEnhk/0
layout: provider
mcp_servers:
- description: ''
  name: padlet-mcp.yml
  slug: padlet-mcpyml
modified: '2026-07-20'
name: Padlet
nav: Providers
network: true
overview: 'Padlet publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AI Recipe Boards API, Boards API, Comments API, and 4 more. Tagged areas include Collaboration, Education, Visual Collaboration, Content, and Boards.


  Padlet''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 74
rate_limits:
- limit_count: 1
  name: Padlet Rate Limits
  slug: padlet-rate-limits
score:
  band: developing
  composite: 53.8
  delta: 1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.7
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 52.7
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Padlet Authentication
  slug: padlet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Padlet Domain Security
  slug: padlet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Padlet Vulnerability Disclosure
  slug: padlet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: padlet
tags:
- Collaboration
- Education
- Visual Collaboration
- Content
- Boards
- Productivity
- JSON:API
- MCP
- EdTech
website: https://padlet.com/
---
