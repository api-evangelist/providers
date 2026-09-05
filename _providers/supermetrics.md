---
access_model:
  confidence: high
  label: Self-serve signup with a 14-day free trial; Data API access is a paid extra
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://supermetrics.com/pricing
  - https://docs.supermetrics.com/docs/how-to-start-a-supermetrics-free-trial.md
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST Product API (v2) to query marketing data from connected data sources, with synchronous and asynchronous query execution, plus a Management API for API keys, saved queries, teams, data-source logi
  name: Supermetrics API
  slug: supermetrics-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://supermetrics.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://supermetrics.com/products/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supermetrics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.supermetrics.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.supermetrics.com/apidocs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.supermetrics.com/docs/about-supermetrics-support.md
- group: company
  title: ''
  type: Blog
  url: https://supermetrics.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supermetrics-public
- group: commercial
  title: ''
  type: Pricing
  url: https://supermetrics.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://supermetrics.com/start-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supermetrics.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supermetrics.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.supermetrics.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/supermetrics-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/supermetrics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.supermetrics.com/docs/system-updates.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/supermetrics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/supermetrics-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/supermetrics-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/supermetrics-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/supermetrics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/supermetrics-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/supermetrics-cli.yml
- group: design
  title: ''
  type: Components
  url: components/supermetrics-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/supermetrics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supermetrics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supermetrics-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/supermetrics-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/supermetrics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.supermetrics.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/supermetrics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supermetrics-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supermetrics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://supermetrics.com/.well-known/security.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/supermetrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/supermetrics-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/supermetrics-data-model.yml
created: '2026-07-17'
description: Supermetrics is a marketing intelligence platform that automates the pipeline of marketing and advertising data from 100+ sources (Google Ads, Facebook/Meta Ads, TikTok, Google Analytics, LinkedIn Ads, and more) into spreadsheets, BI tools, and data warehouses. Its public Product API (v2) lets developers query that data programmatically over REST, run long-running extracts asynchronously, and manage teams, saved queries, data-source logins, and Data Warehouse backfills via a Management API. Authentication is by API key (Bearer) or a full OAuth2/OIDC flow, and Supermetrics also ships an official Python SDK, a Go CLI, an n8n node, and a hosted MCP server for connecting AI assistants to live marketing data.
image: https://supermetrics.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Supermetrics MCP Server
  slug: supermetrics-mcp-server
modified: '2026-08-13'
name: Supermetrics
nav: Providers
network: true
overview: 'Supermetrics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Analytics, Advertising, and Data.


  Supermetrics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Supermetrics Plans Pricing
  plan_count: 3
  slug: supermetrics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Supermetrics Rate Limits
  slug: supermetrics-rate-limits
scopes:
- name: Supermetrics Scopes
  scope_count: 13
  slug: supermetrics-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 53.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supermetrics/refs/heads/main/screenshots/supermetrics-2026-08-17T082204.png
security:
- kind: authentication
  name: Supermetrics Authentication
  slug: supermetrics-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Supermetrics Domain Security
  slug: supermetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Supermetrics Vulnerability Disclosure
  slug: supermetrics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Supermetrics Trust Center
  slug: supermetrics-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: supermetrics
tags:
- Company
- Marketing
- Analytics
- Advertising
- Data
- Reporting
- Business Intelligence
- Data Warehouse
website: https://supermetrics.com
---
