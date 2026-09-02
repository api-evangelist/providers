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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Revenuebase Agentic Access
  operation_count: 10
  slug: revenuebase-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 2
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
- description: The health API from RevenueBase — 2 operation(s) for health.
  name: RevenueBase Health API
  slug: revenuebase-health-api
- description: The v2 API from RevenueBase — 1 operation(s) for v2.
  name: RevenueBase V2 API
  slug: revenuebase-v2-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Revenuebase API v2 Account API
  slug: open-revenuebase-account-api
- collection_type: open
  name: Revenuebase API v2 Account Email API
  slug: open-revenuebase-email-api
- collection_type: open
  name: Revenuebase API v2 Account Jobs API
  slug: open-revenuebase-jobs-api
- collection_type: open
  name: Revenuebase API v2 Account Organization API
  slug: open-revenuebase-organization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revenuebase-agentic-access.yml
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
  url: https://docs.revenuebase.ai/api-reference/v2/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.revenuebase.ai/docs/getting-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.revenuebase.ai/api-reference/v2/make-first-call
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
  url: openapi/_original/revenuebase-openapi.json
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
  url: rate-limits/revenuebase-rate-limits.yml
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
  url: https://revenuebase.ai/stc-01-14-2024
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
- group: other
  title: ''
  type: AgentCard
  url: a2a/revenuebase-a2a.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/revenuebase-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/revenuebase-provider-skill.md
- group: commercial
  title: ''
  type: Plans
  url: plans/revenuebase-plans-pricing.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.revenuebase.ai/docs/release-notes
created: '2026-07-17'
description: RevenueBase is a B2B data infrastructure platform — "the trust layer for B2B data" — providing 400M+ continuously verified contacts (399M as of the August 2026 release notes) and 65M+ companies delivered via Snowflake, S3, Gigasheet, or a REST API. Core capabilities include real-time and batch email verification, deterministic and semantic company matching/resolution, organization discovery, and record enrichment, with data filterable by headcount, revenue, funding stage, industry, job title, seniority, geography, and tech stack. The v2 REST API authenticates with an API key in the x-key header and meters usage in credits. Originally surfaced as a Bessemer Venture Partners portfolio company and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/69aeeb63d4c5075af2fb954d/69dcb129729f9ab3c0816e26_RevenueBase-Favicon-32x32px.png
layout: provider
mcp_servers:
- description: ''
  name: RevenueBase
  slug: revenuebase
modified: '2026-08-13'
name: RevenueBase
nav: Providers
network: true
overview: 'RevenueBase publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Email API, Jobs API, and 3 more. Tagged areas include Company, B2B Data, Data Enrichment, Email Verification, and Contact Data.


  RevenueBase''s developer surface includes documentation, API reference, getting-started guide, quickstart, authentication, changelog, engineering blog, and 34 more developer resources.'
plans:
- name: Revenuebase Plans Pricing
  plan_count: 5
  slug: revenuebase-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Revenuebase Rate Limits
  slug: revenuebase-rate-limits
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 25
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revenuebase/refs/heads/main/screenshots/revenuebase-2026-08-17T081544.png
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
