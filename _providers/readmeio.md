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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The current ReadMe API for managing your project programmatically — API keys, API definitions, reference/guides/custom pages, categories, branches, changelog entries, recipes, images, fonts, Owlbot AI
  name: ReadMe API (v2)
  slug: readme-api-v2
- description: 'Read-only analytics over your ReadMe developer hub — page views (total, unique, by day, by user, by path), best/worst/top pages, average page quality, top search terms, users by search term, and page '
  name: Developer Metrics API
  slug: developer-metrics-api
- description: The legacy ReadMe API (HTTP Basic auth with an API key) for docs, categories, versions, custom pages, changelog, API specification upload, the API registry, and search. Not available to projects using
  name: ReadMe API (v1, Legacy)
  slug: readme-api-v1-legacy
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://readme.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.readme.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readme.com/main/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.readme.com/main/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.readme.com/main/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/readmeio-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://readme.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/readmeio
- group: commercial
  title: ''
  type: Pricing
  url: https://readme.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.readme.com/signup
- group: start
  title: ''
  type: Login
  url: https://dash.readme.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://readme.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://readme.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.readme.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.readme.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/readmeio-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/readmeio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/readmeio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/readmeio-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/readmeio-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/readmeio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/readmeio-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/readmeio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/readmeio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/readmeio-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/readmeio-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/readmeio-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/readmeio-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'ReadMe is a developer-experience platform that turns an OpenAPI definition into interactive, personalized API documentation and developer hubs — complete with a live API Explorer ("Try It!"), guides, recipes, a changelog, discussions, and Developer Metrics that show how real users call your API. Teams manage their docs as code (Git-synced, branch-based via ReadMe Refactored) and programmatically through the ReadMe API. This profile catalogs ReadMe''s own public APIs: the ReadMe API v2 (Bearer-token, RFC 9457 errors), the Developer Metrics API, and the Legacy API v1.'
image: https://readme.com/public/img/readme-og.png
layout: provider
mcp_servers:
- description: ''
  name: readmeio-mcp.yml
  slug: readmeio-mcpyml
modified: '2026-07-20'
name: ReadMe.io
nav: Providers
network: true
overview: 'ReadMe.io publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apis, Documentation, API Documentation, and Developer Experience.


  ReadMe.io''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 40.0
  delta: -1.6
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 41.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Readmeio Authentication
  slug: readmeio-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Readmeio Domain Security
  slug: readmeio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: readmeio
tags:
- Company
- Apis
- Documentation
- API Documentation
- Developer Experience
- Developer Portal
- OpenAPI
- Developer Hub
- API Metrics
website: https://readme.com
---
