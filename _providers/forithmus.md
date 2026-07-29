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
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 129
  human_in_the_loop: 3
  name: Forithmus Agentic Access
  operation_count: 213
  slug: forithmus-agentic-access
  summary_line: 213 operations · 129 acting · 3 human-in-the-loop
api_count: 25
apis:
- description: The 2fa API from Forithmus — 5 operation(s) for 2fa.
  name: Forithmus 2fa API
  slug: forithmus-2fa-api
- description: The admin API from Forithmus — 15 operation(s) for admin.
  name: Forithmus admin API
  slug: forithmus-admin-api
- description: The auth API from Forithmus — 13 operation(s) for auth.
  name: Forithmus auth API
  slug: forithmus-auth-api
- description: The challenges API from Forithmus — 7 operation(s) for challenges.
  name: Forithmus challenges API
  slug: forithmus-challenges-api
- description: The collections API from Forithmus — 15 operation(s) for collections.
  name: Forithmus collections API
  slug: forithmus-collections-api
- description: The credits API from Forithmus — 16 operation(s) for credits.
  name: Forithmus credits API
  slug: forithmus-credits-api
- description: The data-upload API from Forithmus — 8 operation(s) for data-upload.
  name: Forithmus data-upload API
  slug: forithmus-data-upload-api
- description: The forum API from Forithmus — 7 operation(s) for forum.
  name: Forithmus forum API
  slug: forithmus-forum-api
- description: The groups API from Forithmus — 10 operation(s) for groups.
  name: Forithmus groups API
  slug: forithmus-groups-api
- description: The Health API from Forithmus — 2 operation(s) for health.
  name: Forithmus Health API
  slug: forithmus-health-api
- description: The images API from Forithmus — 1 operation(s) for images.
  name: Forithmus images API
  slug: forithmus-images-api
- description: The leaderboard API from Forithmus — 2 operation(s) for leaderboard.
  name: Forithmus leaderboard API
  slug: forithmus-leaderboard-api
- description: The members API from Forithmus — 7 operation(s) for members.
  name: Forithmus members API
  slug: forithmus-members-api
- description: The messages API from Forithmus — 5 operation(s) for messages.
  name: Forithmus messages API
  slug: forithmus-messages-api
- description: The notifications API from Forithmus — 3 operation(s) for notifications.
  name: Forithmus notifications API
  slug: forithmus-notifications-api
- description: The pages API from Forithmus — 3 operation(s) for pages.
  name: Forithmus pages API
  slug: forithmus-pages-api
- description: The payments API from Forithmus — 6 operation(s) for payments.
  name: Forithmus payments API
  slug: forithmus-payments-api
- description: The phases API from Forithmus — 6 operation(s) for phases.
  name: Forithmus phases API
  slug: forithmus-phases-api
- description: The resources API from Forithmus — 5 operation(s) for resources.
  name: Forithmus resources API
  slug: forithmus-resources-api
- description: The roles API from Forithmus — 6 operation(s) for roles.
  name: Forithmus roles API
  slug: forithmus-roles-api
- description: The search API from Forithmus — 1 operation(s) for search.
  name: Forithmus search API
  slug: forithmus-search-api
- description: The submissions API from Forithmus — 18 operation(s) for submissions.
  name: Forithmus submissions API
  slug: forithmus-submissions-api
- description: The timeline API from Forithmus — 2 operation(s) for timeline.
  name: Forithmus timeline API
  slug: forithmus-timeline-api
- description: The uploads API from Forithmus — 1 operation(s) for uploads.
  name: Forithmus uploads API
  slug: forithmus-uploads-api
- description: The users API from Forithmus — 8 operation(s) for users.
  name: Forithmus users API
  slug: forithmus-users-api
artifact_total: 29
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forithmus-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forithmus-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://forithmus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://research.forithmus.com
- group: docs
  title: ''
  type: Documentation
  url: https://research.forithmus.com/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://research.forithmus.com/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forithmus
- group: company
  title: ''
  type: Blog
  url: https://forithmus.com/news/
- group: operate
  title: ''
  type: Support
  url: mailto:contact@forithmus.com
- group: start
  title: ''
  type: SignUp
  url: https://research.forithmus.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/forithmus-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/forithmus-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/forithmus-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/forithmus-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/forithmus-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/forithmus-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/forithmus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forithmus-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forithmus-llms.txt
created: '2026-07-17'
description: 'Forithmus builds foundation models for medical imaging (Zurich, Switzerland; pre-seed backed by Point Nine and e2vc). Its developer-facing product is the Forithmus Research Hub, a Challenge Platform where research teams host and enter medical-imaging benchmarks by submitting Docker containers or prediction files, with leaderboards, credits and compute tiers, collections, forums, and groups. The public REST API is served at https://research.forithmus.com/api and described by an OpenAPI 3.1.0 specification (172 paths, 213 operations across 24 tags: auth/2FA, challenges, phases, collections, submissions, leaderboard, credits, payments, forum, groups, and more). Authentication is Bearer JWT via email/password or Google OAuth, with a browser device flow used by the first-party `forithmus` CLI. Forithmus also publishes open model/dataset repositories (MR-RATE, VLM3D, FORA) on GitHub.'
image: https://forithmus.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: forithmus-mcp.yml
  slug: forithmus-mcpyml
modified: '2026-07-19'
name: Forithmus
nav: Providers
network: true
overview: 'Forithmus publishes 25 APIs on the [APIs.io](https://apis.io/) network, including 2fa API, admin API, auth API, and 22 more. Tagged areas include Medical Imaging, Radiology, Machine Learning, Foundation Models, and Healthcare AI.


  Forithmus'' developer surface includes documentation, getting-started guide, engineering blog, support, signup flow, authentication, CLI, and 13 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 36.3
  delta: -2.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 44.6
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forithmus/refs/heads/main/screenshots/forithmus-2026-07-25T214941.png
security:
- kind: authentication
  name: Forithmus Authentication
  slug: forithmus-authentication
  summary_line: http-bearer/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Forithmus Domain Security
  slug: forithmus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: forithmus
tags:
- Medical Imaging
- Radiology
- Machine Learning
- Foundation Models
- Healthcare AI
- Challenge Platform
- Benchmarks
- Research
- Developer Tools
- API
website: https://forithmus.com
---
