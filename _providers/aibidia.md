---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-09-15'
api_count: 3
apis:
- baseURL: https://otpm-api.aibidia.com
  baseurl_source: declared
  description: The deliberately-public integration surface of Aibidia's OTP Management solution. It accepts automated multi-level segmentation data injections for a given year, month and Extract Type, and returns th
  name: Aibidia Public OTP Management API
  slug: aibidia-public-otp-management-api
- baseURL: https://tpai-api.aibidia.com
  baseurl_source: declared
  description: Backend service for the Aibidia TP AI solution surfaced at platform.aibidia.com/tpai/. It serves an OpenAPI 3.1.0 document anonymously at https://tpai-api.aibidia.com/openapi.json describing a healthc
  name: Aibidia TP AI API
  slug: aibidia-tp-ai-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.aibidia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aibidia.my.site.com/help/support
- group: operate
  title: ''
  type: Support
  url: https://aibidia.my.site.com/help/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://aibidia.my.site.com/help/support
- group: docs
  title: ''
  type: APIReference
  url: https://otpm-api.aibidia.com/swagger/index.html
- group: start
  title: ''
  type: Login
  url: https://platform.aibidia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aibidia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aibidia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aibidia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aibidia.com/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/llms/aibidia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aibidia-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/well-known/aibidia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aibidia-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/authentication/aibidia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aibidia-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/conventions/aibidia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aibidia-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/lifecycle/aibidia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aibidia-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/conformance/aibidia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aibidia-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/conformance/aibidia-conformance.yml
  title: ''
  type: Compliance
  url: conformance/aibidia-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/security/aibidia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibidia-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/errors/aibidia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aibidia-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/data-model/aibidia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aibidia-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/rate-limits/aibidia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aibidia-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/plans/aibidia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aibidia-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/packages/aibidia-packages.yml
  title: ''
  type: Packages
  url: packages/aibidia-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/changelog/aibidia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aibidia-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.aibidia.com/product-news
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/mcp/aibidia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aibidia-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aibidia/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-13'
description: 'Aibidia is a Helsinki-based transfer pricing technology company whose cloud platform lets multinational enterprises manage transfer pricing policy, intercompany transaction data, documentation and country-by-country reporting in one place. The platform is delivered as a set of solution modules — TPDoc (documentation), CbCR, OTP Management, Strategic TP Management, Value Chain Analysis, Data Studio, Horizon and TP AI — behind a single Azure AD B2C sign-in at platform.aibidia.com, each backed by its own first-party API service on an aibidia.com subdomain. Aibidia publishes a small deliberately-public integration surface: the Public OTP Management API, which accepts automated multi-level segmentation data injections from a customer''s ERP or finance stack using an X-DATAINGESTION-API-KEY header. There is no open developer portal, no public API reference and no self-serve signup; the platform is sold to enterprise tax teams and the help centre and release notes sit behind client-rendered
  portals.'
image: https://cdn.prod.website-files.com/652d101c1d03208622e683de/65686f3212a45fa956dd35a9_Social%20Share%20Aibidia.png
layout: provider
mcp_servers:
- description: ''
  name: Aibidia MCP Server
  slug: aibidia-mcp-server
modified: '2026-09-13'
name: Aibidia
nav: Providers
network: true
overview: 'Aibidia publishes 2 APIs on the [APIs.io](https://apis.io/) network: Public OTP Management API and TP AI API. Tagged areas include Company, Transfer Pricing, Tax Technology, Tax Compliance, and Regulatory Reporting.


  Aibidia''s developer surface includes documentation, support, API reference, engineering blog, authentication, changelog, and 21 more developer resources.'
plans:
- name: Aibidia Plans Pricing
  plan_count: 0
  slug: aibidia-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Aibidia Rate Limits
  slug: aibidia-rate-limits
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 45.9
    developer_ergonomics: 37.5
    discoverability: 81.5
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 42.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aibidia Authentication
  slug: aibidia-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Aibidia Domain Security
  slug: aibidia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aibidia
tags:
- Company
- Transfer Pricing
- Tax Technology
- Tax Compliance
- Regulatory Reporting
- Country-by-Country Reporting
- Financial Data
- Enterprise Software
- Data Ingestion
- Finland
website: https://www.aibidia.com/
---
