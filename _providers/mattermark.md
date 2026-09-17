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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mattermark Agentic Access
  operation_count: 11
  slug: mattermark-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 2
apis:
- description: 'GraphQL access to the Mattermark dataset using the Mattermark Search Filter Language (MSFL) for complex company and investor queries. Read-only: the published schema declares 57 types under a single R'
  name: Mattermark GraphQL API
  slug: mattermark-graphql-api
- baseURL: https://api.mattermark.com/
  baseurl_source: declared
  description: The Companies API from Mattermark — 5 operation(s) for companies.
  name: Mattermark Companies API
  slug: mattermark-companies-api
- baseURL: https://api.mattermark.com/
  baseurl_source: declared
  description: The Complex Queries API from Mattermark — 1 operation(s) for complex queries.
  name: Mattermark Complex Queries API
  slug: mattermark-complex-queries-api
- baseURL: https://api.mattermark.com/
  baseurl_source: declared
  description: The Funding Events API from Mattermark — 1 operation(s) for funding events.
  name: Mattermark Funding Events API
  slug: mattermark-funding-events-api
- baseURL: https://api.mattermark.com/
  baseurl_source: declared
  description: The Investors API from Mattermark — 2 operation(s) for investors.
  name: Mattermark Investors API
  slug: mattermark-investors-api
- baseURL: https://api.mattermark.com/
  baseurl_source: declared
  description: The Search API from Mattermark — 1 operation(s) for search.
  name: Mattermark Search API
  slug: mattermark-search-api
- baseURL: https://api.mattermark.com/
  baseurl_source: declared
  description: The Utilities API from Mattermark — 1 operation(s) for utilities.
  name: Mattermark Utilities API
  slug: mattermark-utilities-api
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/agentic-access/mattermark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mattermark-agentic-access.yml
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
  url: https://mattermark.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://mattermark.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mattermark
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/llms/mattermark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mattermark-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/authentication/mattermark-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mattermark-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/conventions/mattermark-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mattermark-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/errors/mattermark-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mattermark-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/rate-limits/mattermark-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mattermark-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/lifecycle/mattermark-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mattermark-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/changelog/mattermark-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mattermark-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/mcp/mattermark-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mattermark-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/mcp/mattermark-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mattermark-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/packages/mattermark-packages.yml
  title: ''
  type: Packages
  url: packages/mattermark-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/conformance/mattermark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mattermark-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/data-model/mattermark-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mattermark-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/security/mattermark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mattermark-domain-security.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/openapi/_original/mattermark-rest-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/mattermark-rest-api-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/graphql/mattermark.graphql
  title: ''
  type: GraphQL
  url: graphql/mattermark.graphql
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/overlays/mattermark-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mattermark-rest-api-overlay.yaml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/sandbox/mattermark-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mattermark-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/plans/mattermark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mattermark-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mattermark is a business-intelligence platform for data-driven deal making, providing profiles on roughly four million companies and twenty million key contacts along with their investors, funding events, and news. Relaunched as an independent company, Mattermark exposes its dataset through a REST API (api.mattermark.com) and a GraphQL API (eapi.mattermark.com), both authenticated with a Bearer API key and queryable with the Mattermark Search Filter Language (MSFL). Originally an a16z / Slow Ventures / Version One Ventures-backed startup, it is tracked in the API Evangelist network as a company profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mattermark.png
layout: provider
modified: '2026-09-16'
name: Mattermark
nav: Providers
network: true
overview: 'Mattermark publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Complex Queries API, Funding Events API, and 3 more. Tagged areas include Company, Business Intelligence, Company Data, Investor, and Funding.


  Mattermark''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, authentication, changelog, and 23 more developer resources.'
plans:
- name: Mattermark Plans Pricing
  plan_count: 4
  slug: mattermark-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Mattermark Rate Limits
  slug: mattermark-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 56.9
    developer_ergonomics: 51.8
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 47.0
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/mattermark/refs/heads/main/screenshots/mattermark-2026-07-25T230426.png
security:
- kind: authentication
  name: Mattermark Authentication
  slug: mattermark-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mattermark Domain Security
  slug: mattermark-domain-security
  summary_line: TLSv1.3
slug: mattermark
tags:
- Company
- Business Intelligence
- Company Data
- Investor
- Funding
- Sales Intelligence
- Market Research
website: https://mattermark.com
---
