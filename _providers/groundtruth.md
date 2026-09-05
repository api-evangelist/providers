---
access_model:
  confidence: high
  label: Credentials issued on request
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://api-docs.groundtruth.com/welcome-824669m0
  - https://help.groundtruth.com/hc/en-us/articles/4402393255315-Can-I-set-up-external-reporting-API
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
  score: 31.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Groundtruth Agentic Access
  operation_count: 318
  slug: groundtruth-agentic-access
  summary_line: 318 operations · 63 acting
api_count: 4
apis:
- description: Model Context Protocol endpoint served on the GroundTruth developer documentation host. It answers MCP JSON-RPC on /mcp but returns error -32001 "Authorization required" to anonymous initialize and to
  name: GroundTruth Documentation MCP Server
  slug: groundtruth-documentation-mcp-server
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Accounts API from GroundTruth — 6 operation(s) for accounts.
  name: GroundTruth Accounts API
  slug: groundtruth-accounts-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Ad Groups API from GroundTruth — 6 operation(s) for ad groups.
  name: GroundTruth Ad Groups API
  slug: groundtruth-ad-groups-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Audiences API from GroundTruth — 2 operation(s) for audiences.
  name: GroundTruth Audiences API
  slug: groundtruth-audiences-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Campaigns API from GroundTruth — 6 operation(s) for campaigns.
  name: GroundTruth Campaigns API
  slug: groundtruth-campaigns-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Creative Assets API from GroundTruth — 2 operation(s) for creative assets.
  name: GroundTruth Creative Assets API
  slug: groundtruth-creative-assets-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Creatives API from GroundTruth — 5 operation(s) for creatives.
  name: GroundTruth Creatives API
  slug: groundtruth-creatives-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: Demand API documentation
  name: GroundTruth Demand API
  slug: groundtruth-demand-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Direct Mail API from GroundTruth — 1 operation(s) for direct mail.
  name: GroundTruth Direct Mail API
  slug: groundtruth-direct-mail-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Health API from GroundTruth — 1 operation(s) for health.
  name: GroundTruth Health API
  slug: groundtruth-health-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Jobs API from GroundTruth — 9 operation(s) for jobs.
  name: GroundTruth Jobs API
  slug: groundtruth-jobs-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Miscellaneous API from GroundTruth — 1 operation(s) for miscellaneous.
  name: GroundTruth Miscellaneous API
  slug: groundtruth-miscellaneous-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Organizations API from GroundTruth — 2 operation(s) for organizations.
  name: GroundTruth Organizations API
  slug: groundtruth-organizations-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Reporting API from GroundTruth — 160 operation(s) for reporting.
  name: GroundTruth Reporting API
  slug: groundtruth-reporting-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Search API from GroundTruth — 18 operation(s) for search.
  name: GroundTruth Search API
  slug: groundtruth-search-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Static API from GroundTruth — 12 operation(s) for static.
  name: GroundTruth Static API
  slug: groundtruth-static-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Tenants API from GroundTruth — 1 operation(s) for tenants.
  name: GroundTruth Tenants API
  slug: groundtruth-tenants-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Upload API from GroundTruth — 1 operation(s) for upload.
  name: GroundTruth Upload API
  slug: groundtruth-upload-api
- baseURL: https://api-public.groundtruth.com
  baseurl_source: declared
  description: The Users API from GroundTruth — 4 operation(s) for users.
  name: GroundTruth Users API
  slug: groundtruth-users-api
artifact_total: 28
collections:
- collection_type: open
  name: Ads Manager API
  slug: open-groundtruth-ads-manager
- collection_type: open
  name: Groundtruth Reporting API
  slug: open-groundtruth-reporting
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groundtruth-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/groundtruth-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.groundtruth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.groundtruth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.groundtruth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.groundtruth.com/
- group: start
  title: ''
  type: SignUp
  url: https://ads.groundtruth.com/login?sign_up=1
- group: start
  title: ''
  type: Login
  url: https://ads.groundtruth.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.groundtruth.com/insight/category/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.groundtruth.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.groundtruth.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.groundtruth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.groundtruth.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.groundtruth.com/get-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/groundtruth-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groundtruth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groundtruth-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/groundtruth-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groundtruth-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groundtruth-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groundtruth-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/groundtruth-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/groundtruth-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groundtruth-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groundtruth-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/groundtruth-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/groundtruth-ads-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/groundtruth-reporting-overlay.yaml
created: '2026-07-17'
description: 'GroundTruth is a location-intelligence performance advertising platform (formerly xAd) that helps brands and agencies plan, launch, and measure omnichannel ad campaigns tied to real-world behavior. Its Ads Manager, proprietary Blueprints location-mapping technology, and Dynamic Intent Prediction AI turn visitation, behavioral, and demographic signals into targeting and store-visit and sales attribution across verticals including QSR/restaurants, CPG, auto, retail, healthcare, education, travel, and political. GroundTruth is backed by Emergence Capital and IVP and became part of ZeroToOne.AI in 2026. GroundTruth publishes two public REST API surfaces: the Ads Manager Public API at api-public.groundtruth.com (259 operations across accounts, organizations, tenants, campaigns, ad groups, creatives, audiences, jobs, uploads, search and reporting, with a live OpenAPI 3.1 document and Swagger UI at /docs), and the Groundtruth Reporting API at reporting.groundtruth.com (59 read-only
  demand-reporting operations described by an OpenAPI 3.0.1 document). Both authenticate with the paired X-GT-USER-ID and X-GT-API-KEY headers; credentials are issued on request rather than self-serve.'
image: https://www.groundtruth.com/wp-content/uploads/2026/06/GroundTruth-Featured-Image.webp
layout: provider
mcp_servers:
- description: ''
  name: GroundTruth MCP Server
  slug: groundtruth-mcp-server
- description: ''
  name: GroundTruth MCP Server
  slug: groundtruth-mcp-server-2
modified: '2026-08-12'
name: GroundTruth
nav: Providers
network: true
overview: 'GroundTruth publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Ad Groups API, Audiences API, and 15 more. Tagged areas include Company, MarTech, Advertising, Location Intelligence, and Marketing.


  GroundTruth''s developer surface includes documentation, API reference, signup flow, engineering blog, support, getting-started guide, authentication, and 22 more developer resources.'
plans:
- name: Groundtruth Plans Pricing
  plan_count: 0
  slug: groundtruth-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Groundtruth Rate Limits
  slug: groundtruth-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 56.6
    developer_ergonomics: 57.7
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groundtruth/refs/heads/main/screenshots/groundtruth-2026-07-25T220343.png
security:
- kind: authentication
  name: Groundtruth Authentication
  slug: groundtruth-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Groundtruth Domain Security
  slug: groundtruth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groundtruth
tags:
- Company
- MarTech
- Advertising
- Location Intelligence
- Marketing
- AdTech
- Location-Based Marketing
- Advertising API
- Campaign Management
- Ad Reporting
- Attribution
- Geofencing
- Digital Out Of Home
- CTV
website: https://www.groundtruth.com
---
