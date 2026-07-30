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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The Account API from RevenueBase — 2 operation(s) for account.
  name: RevenueBase Account API
  slug: revenuebase-account-api
- description: The Email API from RevenueBase — 2 operation(s) for email.
  name: RevenueBase Email API
  slug: revenuebase-email-api
- description: The Jobs API from RevenueBase — 4 operation(s) for jobs.
  name: RevenueBase Jobs API
  slug: revenuebase-jobs-api
- description: The Organization API from RevenueBase — 2 operation(s) for organization.
  name: RevenueBase Organization API
  slug: revenuebase-organization-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://revenuebase.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.revenuebase.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revenuebase.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.revenuebase.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.revenuebase.ai/docs/getting-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.revenuebase.ai/docs/getting-started/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/revenuebase-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revenuebase-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/revenuebase-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/revenuebase-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revenuebase-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revenuebase-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revenuebase-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revenuebase-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revenuebase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/revenuebase-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revenuebase.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/revenuebase-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revenuebase-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/revenuebase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/revenuebase-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revenuebase-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revenuebase-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.revenuebase.ai/api-reference/rate-limits
- group: company
  title: ''
  type: Blog
  url: https://revenuebase.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://revenuebase.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.revenuebase.ai/
- group: start
  title: ''
  type: Login
  url: https://app.revenuebase.ai/
- group: operate
  title: ''
  type: Support
  url: https://revenuebase.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revenuebase
- group: commercial
  title: ''
  type: TermsOfService
  url: https://revenuebase.ai/stc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revenuebase.ai/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenue-base/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/revenuebase
created: '2026-07-17'
description: RevenueBase is a B2B data infrastructure platform — "the trust layer for B2B data" — providing 390M+ continuously verified contacts and 60M+ companies delivered via Snowflake, S3, Gigasheet, or a REST API. Core capabilities include real-time and batch email verification, deterministic and semantic company matching/resolution, organization discovery, and record enrichment, with data filterable by headcount, revenue, funding stage, industry, job title, seniority, geography, and tech stack. The v2 REST API authenticates with an API key in the x-key header and meters usage in credits. Originally surfaced as a Bessemer Venture Partners portfolio company and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/69aeeb63d4c5075af2fb954d/69dcb129729f9ab3c0816e26_RevenueBase-Favicon-32x32px.png
layout: provider
mcp_servers:
- description: ''
  name: revenuebase-mcp.yml
  slug: revenuebase-mcpyml
modified: '2026-07-20'
name: RevenueBase
nav: Providers
network: true
overview: 'RevenueBase publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Email API, Jobs API, and 1 more. Tagged areas include Company, B2B Data, Data Enrichment, Email Verification, and Contact Data.


  RevenueBase''s developer surface includes documentation, API reference, getting-started guide, quickstart, authentication, changelog, engineering blog, and 28 more developer resources.'
random_paper: 25
score:
  band: developing
  composite: 52.3
  delta: -1.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.6
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 53.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Revenuebase Authentication
  slug: revenuebase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Revenuebase Domain Security
  slug: revenuebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revenuebase
tags:
- Company
- B2B Data
- Data Enrichment
- Email Verification
- Contact Data
- Company Data
- Lead Intelligence
- Sales Intelligence
website: https://revenuebase.ai/
---
