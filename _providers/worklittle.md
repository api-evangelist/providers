---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The Job Boards API from Worklittle — 8 operation(s) for job boards.
  name: Worklittle Job Boards API
  slug: worklittle-job-boards-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The consumer Jobs surface of the Worklittle API — 9 operations for market-wide job search, job detail, map clusters, suggestions, company search, market stats, account and profile resume upload.
  name: Worklittle Jobs API
  slug: worklittle-jobs-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The agent-documents API from Worklittle — 4 operation(s) for agent-documents.
  name: Worklittle Agent Documents API
  slug: worklittle-agent-documents-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The apply API from Worklittle — 5 operation(s) for apply.
  name: Worklittle Apply API
  slug: worklittle-apply-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The attendance API from Worklittle — 1 operation(s) for attendance.
  name: Worklittle Attendance API
  slug: worklittle-attendance-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The billing API from Worklittle — 1 operation(s) for billing.
  name: Worklittle Billing API
  slug: worklittle-billing-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The candidates API from Worklittle — 3 operation(s) for candidates.
  name: Worklittle Candidates API
  slug: worklittle-candidates-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The documents API from Worklittle — 1 operation(s) for documents.
  name: Worklittle Documents API
  slug: worklittle-documents-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The email-offers API from Worklittle — 3 operation(s) for email-offers.
  name: Worklittle Email Offers API
  slug: worklittle-email-offers-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The employees API from Worklittle — 2 operation(s) for employees.
  name: Worklittle Employees API
  slug: worklittle-employees-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The employer-jobs API from Worklittle — 1 operation(s) for employer-jobs.
  name: Worklittle Employer Jobs API
  slug: worklittle-employer-jobs-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The job-listings API from Worklittle — 2 operation(s) for job-listings.
  name: Worklittle Job Listings API
  slug: worklittle-job-listings-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The organization API from Worklittle — 2 operation(s) for organization.
  name: Worklittle Organization API
  slug: worklittle-organization-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The people API from Worklittle — 3 operation(s) for people.
  name: Worklittle People API
  slug: worklittle-people-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The surveys API from Worklittle — 2 operation(s) for surveys.
  name: Worklittle Surveys API
  slug: worklittle-surveys-api
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The webhooks API from Worklittle — 2 operation(s) for webhooks.
  name: Worklittle Webhooks API
  slug: worklittle-webhooks-api
artifact_total: 39
asyncapis:
- description: ''
  name: Worklittle Webhooks
  slug: worklittle-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://worklittle.com/feed.xml
- group: other
  href: https://artifacts.apis.io/worklittle/capabilities/worklittle-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/worklittle-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/worklittle/authentication/worklittle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/worklittle-authentication.yml
- group: auth
  href: https://artifacts.apis.io/worklittle/security/worklittle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worklittle-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/worklittle/mcp/worklittle-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/worklittle-mcp.yml
- group: agent
  href: https://artifacts.apis.io/worklittle/llms/worklittle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/worklittle-llms.txt
- group: other
  href: https://artifacts.apis.io/worklittle/a2a/worklittle-agent-manifest.json
  title: ''
  type: AgentManifest
  url: a2a/worklittle-agent-manifest.json
- group: company
  title: ''
  type: Website
  url: https://worklittle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.worklittle.com
- group: build
  href: https://artifacts.apis.io/worklittle/packages/worklittle-packages.yml
  title: ''
  type: Packages
  url: packages/worklittle-packages.yml
- group: build
  href: https://artifacts.apis.io/worklittle/packages/worklittle-packages.yml
  title: ''
  type: SDKs
  url: packages/worklittle-packages.yml
- group: build
  href: https://artifacts.apis.io/worklittle/cli/worklittle-cli.yml
  title: ''
  type: CLI
  url: cli/worklittle-cli.yml
- group: agent
  href: https://artifacts.apis.io/worklittle/well-known/worklittle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/worklittle-well-known.yml
- group: build
  href: https://artifacts.apis.io/worklittle/mcp/worklittle-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/worklittle-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/worklittle/scopes/worklittle-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/worklittle-scopes.yml
- group: design
  href: https://artifacts.apis.io/worklittle/conformance/worklittle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/worklittle-conformance.yml
- group: design
  href: https://artifacts.apis.io/worklittle/errors/worklittle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/worklittle-problem-types.yml
- group: design
  href: https://artifacts.apis.io/worklittle/lifecycle/worklittle-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/worklittle-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.worklittle.com/business/resources/status
- group: design
  href: https://artifacts.apis.io/worklittle/conventions/worklittle-conventions.yml
  title: ''
  type: Conventions
  url: conventions/worklittle-conventions.yml
- group: operate
  href: https://artifacts.apis.io/worklittle/changelog/worklittle-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/worklittle-changelog.yml
- group: design
  href: https://artifacts.apis.io/worklittle/data-model/worklittle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/worklittle-data-model.yml
- group: design
  href: https://artifacts.apis.io/worklittle/asyncapi/worklittle-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/worklittle-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/worklittle/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/worklittle/plans/worklittle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/worklittle-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/worklittle/rate-limits/worklittle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/worklittle-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/worklittle/overlays/worklittle-jobs-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/worklittle-jobs-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/worklittle/overlays/worklittle-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/worklittle-platform-api-overlay.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.worklittle.com/jobs/get-started/overview
- group: operate
  title: ''
  type: Support
  url: https://docs.worklittle.com/help/privacy-safety/contact-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worklittle
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.worklittle.com/jobs/get-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://worklittle.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worklittle.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worklittle.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.worklittle.com
created: '2026-08-24'
description: 'Worklittle is a workforce-intelligence platform covering job discovery, auto-apply, embedded careers boards, ATS sync and sourcing over one API. It splits into two halves: Jobs, the market-wide index plus candidate-facing apply and document tools including commute search on a geocoded job map, and Business, an employer hiring workspace with postings, an ATS pipeline, employees, HR documents and webhooks. The public contract is a $ref-based OpenAPI 3.1 document served from docs.worklittle.com/openapi/openapi.yaml resolving to 47 paths across jobs, platform and job-board surfaces on api.worklittle.com, with bearer sk-wl-api01 authentication plus an OAuth 2.0 authorization server (RFC 8414, PKCE, dynamic registration) backing MCP Connect. Worklittle operates a live remote MCP server at mcp.worklittle.com (101 documented tools, 13 anonymously introspectable), ships first-party TypeScript and Python SDKs and a CLI on npm, PyPI and Homebrew, and publishes a 99KB llms.txt plus a docs
  agent manifest.'
finops:
- has_sources: true
  method: derived
  name: Worklittle Finops
  primary_unit: 1m input tokens
  service_category: ''
  slug: worklittle-finops
  template: false
image: https://docs.worklittle.com/social-banner.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.worklittle.com over HTTP requiring an API key; 13 tools listed.
  name: Worklittle MCP Server
  slug: worklittle
modified: '2026-10-06'
name: Worklittle
nav: Providers
network: true
overview: 'Worklittle publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Job Boards API, Jobs API, Agent Documents API, and 13 more. Tagged areas include Job Search, Applicant Tracking, Recruiting, Workforce Intelligence, and Job Board.


  The Worklittle catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Worklittle''s developer surface includes authentication, CLI, changelog, getting-started guide, support, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Worklittle Plans Pricing
  plan_count: 5
  slug: worklittle-plans-pricing
- name: Worklittle Price Estimates
  plan_count: 0
  slug: worklittle-price-estimates
random_paper: 1
rate_limits:
- limit_count: 10
  name: Worklittle Rate Limits
  slug: worklittle-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Worklittle API Rules
  rule_count: 50
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 2
  slug: worklittle-rules
scopes:
- name: Worklittle Scopes
  scope_count: 11
  slug: worklittle-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 42.9
    discoverability: 80.0
    operational_transparency: 57.9
  previous_composite: 56.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/worklittle/worklittle-2026-09-02T170938.png
security:
- kind: authentication
  name: Worklittle Authentication
  slug: worklittle-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Worklittle Domain Security
  slug: worklittle-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 13
skills:
- name: apply-with-ai
  slug: apply-with-ai
- name: candidates
  slug: candidates
- name: capability-map
  slug: capability-map
- name: employees
  slug: employees
- name: job-alerts
  slug: job-alerts
- name: job-search
  slug: job-search
- name: market-stats
  slug: market-stats
- name: mcp-install
  slug: mcp-install
- name: people-search
  slug: people-search
- name: post-a-job
  slug: post-a-job
- name: resume-cover-letter
  slug: resume-cover-letter
- name: worklittle-best-practices
  slug: worklittle-best-practices
- name: worklittle-docs
  slug: worklittle-docs
slug: worklittle
tags:
- Job Search
- Applicant Tracking
- Recruiting
- Workforce Intelligence
- Job Board
- Webhook
- MCP
website: https://worklittle.com
---
