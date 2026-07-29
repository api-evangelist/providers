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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: RESTful access to Mattermark company, investor, funding-event, news and personnel data, with page-based pagination and MSFL query endpoints.
  name: Mattermark REST API
  slug: mattermark-rest-api
- description: GraphQL access to the Mattermark dataset using the Mattermark Search Filter Language (MSFL) for complex company and investor queries.
  name: Mattermark GraphQL API
  slug: mattermark-graphql-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://mattermark.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mattermark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mattermark.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mattermark.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mattermark.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://mattermark.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mattermark.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mattermark.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://mattermark.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mattermark
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mattermark-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mattermark-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mattermark-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mattermark-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mattermark-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mattermark-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mattermark-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mattermark-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/mattermark-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mattermark-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mattermark-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mattermark-domain-security.yml
created: '2026-07-17'
description: Mattermark is a business-intelligence platform for data-driven deal making, providing profiles on roughly four million companies and twenty million key contacts along with their investors, funding events, and news. Relaunched as an independent company, Mattermark exposes its dataset through a REST API (api.mattermark.com) and a GraphQL API (eapi.mattermark.com), both authenticated with a Bearer API key and queryable with the Mattermark Search Filter Language (MSFL). Originally an a16z / Slow Ventures / Version One Ventures-backed startup, it is tracked in the API Evangelist network as a company profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mattermark.png
layout: provider
mcp_servers:
- description: ''
  name: mattermark-mcp.yml
  slug: mattermark-mcpyml
modified: '2026-07-20'
name: Mattermark
nav: Providers
network: true
overview: 'Mattermark publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Intelligence, Company Data, Investors, and Funding.


  Mattermark''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, authentication, changelog, and 15 more developer resources.'
random_paper: 53
rate_limits:
- limit_count: 0
  name: Mattermark Rate Limits
  slug: mattermark-rate-limits
score:
  band: thin
  composite: 28.1
  delta: -1.5
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 29.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/screenshots/mattermark-2026-07-25T230426.png
security:
- kind: authentication
  name: Mattermark Authentication
  slug: mattermark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mattermark Domain Security
  slug: mattermark-domain-security
  summary_line: TLSv1.3
slug: mattermark
tags:
- Company
- Business Intelligence
- Company Data
- Investors
- Funding
- Sales Intelligence
- Market Research
website: https://mattermark.com
---
