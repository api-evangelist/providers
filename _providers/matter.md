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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Matter Agentic Access
  operation_count: 17
  slug: matter-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 6
apis:
- description: Your user profile and API quota.
  name: Matter Account API
  slug: matter-account-api
- description: Highlights and notes on items.
  name: Matter Annotations API
  slug: matter-annotations-api
- description: Articles, podcasts, videos, PDFs, and tweets in your library.
  name: Matter Items API
  slug: matter-items-api
- description: Reading time history.
  name: Matter Reading Sessions API
  slug: matter-reading-sessions-api
- description: Full-text search across Matter.
  name: Matter Search API
  slug: matter-search-api
- description: Labels for organizing items.
  name: Matter Tags API
  slug: matter-tags-api
artifact_total: 12
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getmatter.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmatter.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getmatter.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getmatter.com/api/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/matter-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matter-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matter-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matter-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matter-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/matter-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matter-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matter-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/matter-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/matter-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matter-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matter-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matter-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matter-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/matter-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/matter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/matter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matter-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getmatterapp
- group: operate
  title: ''
  type: Support
  url: mailto:hello@getmatter.com
- group: start
  title: ''
  type: SignUp
  url: https://web.getmatter.com
- group: start
  title: ''
  type: Login
  url: https://web.getmatter.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getmatter.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmatter.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.getmatter.com
created: '2026-07-17'
description: Matter is a modern read-later application for people who take reading seriously — save articles, newsletters, podcasts, PDFs, and tweets from anywhere and read them in a clean, focused interface on iOS and the web, with highlighting, notes, tags, offline search, text-to-speech, and audio transcription of podcasts and videos. For Matter Pro subscribers, Matter ships a public REST API (api.getmatter.com/public/v1) to save, organize, search, and incrementally sync a reading library, secured with a personal Bearer token. It is complemented by a first-party CLI/TUI and official Obsidian, Roam, and Logseq highlight-export integrations. Matter is backed by GV (Google Ventures).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matter.png
layout: provider
mcp_servers:
- description: ''
  name: matter-mcp.yml
  slug: matter-mcpyml
modified: '2026-07-20'
name: Matter
nav: Providers
network: true
overview: 'Matter publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Annotations API, Items API, and 3 more. Tagged areas include Company, Consumer, Reading, Read Later, and Productivity.


  Matter''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, support, signup flow, and 23 more developer resources.'
random_paper: 79
rate_limits:
- limit_count: 6
  name: Matter Rate Limits
  slug: matter-rate-limits
score:
  band: developing
  composite: 52.7
  delta: -1.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.9
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matter/refs/heads/main/screenshots/matter-2026-07-25T230422.png
security:
- kind: authentication
  name: Matter Authentication
  slug: matter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Matter Domain Security
  slug: matter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Matter Vulnerability Disclosure
  slug: matter-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: matter
tags:
- Company
- Consumer
- Reading
- Read Later
- Productivity
- Content
- Highlights
- Bookmarking
website: https://www.getmatter.com
---
