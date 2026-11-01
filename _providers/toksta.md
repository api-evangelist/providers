---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://www.toksta.com/#pricing
  - https://help.toksta.com/public-api/pricing-and-plans
  - https://help.toksta.com/public-api/authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hosted remote Model Context Protocol server exposing 18 Toksta tools — campaigns, creator discovery, lists, enrichment, content-fit and audience-fit analysis, and job control — to Claude and ChatGPT c
  name: Toksta MCP Server
  slug: toksta-mcp-server
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Account API from toksta — 1 operation(s) for account.
  name: toksta Account API
  slug: toksta-account-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Analysis API from toksta — 6 operation(s) for analysis.
  name: toksta Analysis API
  slug: toksta-analysis-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Campaigns API from toksta — 2 operation(s) for campaigns.
  name: toksta Campaigns API
  slug: toksta-campaigns-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Creator Lists API from toksta — 2 operation(s) for creator lists.
  name: toksta Creator Lists API
  slug: toksta-creator-lists-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Creators API from toksta — 4 operation(s) for creators.
  name: toksta Creators API
  slug: toksta-creators-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Enrichment API from toksta — 2 operation(s) for enrichment.
  name: toksta Enrichment API
  slug: toksta-enrichment-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Evidence API from toksta — 1 operation(s) for evidence.
  name: toksta Evidence API
  slug: toksta-evidence-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The Jobs API from toksta — 4 operation(s) for jobs.
  name: toksta Jobs API
  slug: toksta-jobs-api
- baseURL: https://api.toksta.com
  baseurl_source: declared
  description: The System API from toksta — 4 operation(s) for system.
  name: toksta System API
  slug: toksta-system-api
artifact_total: 23
collections:
- collection_type: open
  name: Toksta Public API
  slug: open-toksta-public-api
common:
- group: other
  href: https://artifacts.apis.io/toksta/overlays/toksta-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/toksta-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.toksta.com
- group: company
  title: ''
  type: Blog
  url: https://www.toksta.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://hub.toksta.com/signup
- group: start
  title: ''
  type: Login
  url: https://hub.toksta.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.toksta.com/public-api/toksta-public-api
- group: docs
  title: ''
  type: Documentation
  url: https://help.toksta.com/public-api/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://help.toksta.com/public-api/toksta-public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.toksta.com/public-api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.toksta.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.toksta.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.toksta.com/#pricing
- group: agent
  href: https://artifacts.apis.io/toksta/mcp/toksta-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/toksta-mcp.yml
- group: agent
  href: https://artifacts.apis.io/toksta/llms/toksta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toksta-llms.txt
- group: agent
  href: https://artifacts.apis.io/toksta/well-known/toksta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/toksta-well-known.yml
- group: auth
  href: https://artifacts.apis.io/toksta/authentication/toksta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toksta-authentication.yml
- group: auth
  href: https://artifacts.apis.io/toksta/scopes/toksta-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/toksta-scopes.yml
- group: design
  href: https://artifacts.apis.io/toksta/conventions/toksta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toksta-conventions.yml
- group: design
  href: https://artifacts.apis.io/toksta/errors/toksta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toksta-problem-types.yml
- group: design
  href: https://artifacts.apis.io/toksta/data-model/toksta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/toksta-data-model.yml
- group: operate
  href: https://artifacts.apis.io/toksta/rate-limits/toksta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/toksta-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/toksta/plans/toksta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toksta-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/toksta/lifecycle/toksta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/toksta-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/toksta/conformance/toksta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toksta-conformance.yml
- group: agent
  href: https://artifacts.apis.io/toksta/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/toksta/security/toksta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toksta-domain-security.yml
created: '2026-07-17'
description: 'Toksta is a B2B influencer marketing intelligence platform that uses AI agents to research, filter, and match creators at scale for enterprise brands. It runs a vetted B2B creator database with LinkedIn and YouTube influencer search, automated relevance scoring (AI Match), granular vetting benchmarks (Deep Metrics), campaign management, brand monitoring, and reporting. Toksta ships two machine surfaces: the Toksta Public API v1 at api.toksta.com — a credit-metered REST API with a published OpenAPI 3.0.3 document and Swagger UI, covering creator search and discovery, enrichment, content-match and audience-match analysis jobs, post evidence, campaigns, creator lists and account usage — and a hosted, OAuth-protected MCP server at mcp.toksta.com exposing 18 tools to Claude and ChatGPT custom connectors. Async work is polling-only; there are no webhooks in v1. Toksta is a portfolio company of Seedcamp.'
finops:
- has_sources: true
  method: derived
  name: Toksta Finops
  primary_unit: workspace
  service_category: ''
  slug: toksta-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toksta.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.toksta.com over HTTP requiring OAuth; 18 tools listed.
  name: toksta MCP Server
  slug: toksta-mcp
modified: '2026-08-13'
name: toksta
nav: Providers
network: true
overview: 'toksta publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analysis API, Campaigns API, and 7 more. Tagged areas include Company, Influencer Marketing, Marketing, B2B, and Creator Discovery.


  toksta''s developer surface includes engineering blog, signup flow, documentation, API reference, getting-started guide, support, pricing, and 19 more developer resources.'
plans:
- name: Toksta Plans Pricing
  plan_count: 5
  slug: toksta-plans-pricing
- name: Toksta Price Estimates
  plan_count: 0
  slug: toksta-price-estimates
random_paper: 14
rate_limits:
- limit_count: 5
  name: Toksta Rate Limits
  slug: toksta-rate-limits
scopes:
- name: Toksta Scopes
  scope_count: 0
  slug: toksta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 58.9
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 43.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/toksta/toksta-2026-08-17T082400.png
security:
- kind: authentication
  name: Toksta Authentication
  slug: toksta-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Toksta Domain Security
  slug: toksta-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: Discover and shortlist B2B creators
  slug: toksta-discover-and-shortlist-creators
- name: Enrich creators and read the bill
  slug: toksta-enrich-creators
- name: Run a thought-leader discovery job
  slug: toksta-run-a-thought-leader-discovery-job
- name: Score creator fit for a campaign
  slug: toksta-score-creator-fit-for-a-campaign
slug: toksta
tags:
- Company
- Influencer Marketing
- Marketing
- B2B
- Creator Discovery
- AI Agents
- LinkedIn
- YouTube
- Software-as-a-Service
- Creator Data
- MCP
- Brand Monitoring
website: https://www.toksta.com
---
