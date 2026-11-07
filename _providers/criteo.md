---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 114
  human_in_the_loop: 4
  name: Criteo Agentic Access
  operation_count: 219
  slug: criteo-agentic-access
  summary_line: 219 operations · 114 acting · 4 human-in-the-loop
api_count: 3
apis:
- description: 'Criteo operates two remote Model Context Protocol servers. The documentation server at developers.criteo.com/mcp is anonymous and was introspected live: three tools (search_criteo_docs, query_docs_fil'
  name: Criteo MCP Servers
  slug: criteo-mcp
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Accounts API from Criteo — 12 operation(s) for accounts.
  name: Criteo Accounts API
  slug: criteo-accounts-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Advertiser API from Criteo — 1 operation(s) for advertiser.
  name: Criteo Advertiser API
  slug: criteo-advertiser-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Analytics API from Criteo — 16 operation(s) for analytics.
  name: Criteo Analytics API
  slug: criteo-analytics-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Audience API from Criteo — 24 operation(s) for audience.
  name: Criteo Audience API
  slug: criteo-audience-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Balance API from Criteo — 8 operation(s) for balance.
  name: Criteo Balance API
  slug: criteo-balance-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Billing API from Criteo — 3 operation(s) for billing.
  name: Criteo Billing API
  slug: criteo-billing-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Campaign API from Criteo — 86 operation(s) for campaign.
  name: Criteo Campaign API
  slug: criteo-campaign-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Catalog API from Criteo — 2 operation(s) for catalog.
  name: Criteo Catalog API
  slug: criteo-catalog-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Creative API from Criteo — 9 operation(s) for creative.
  name: Criteo Creative API
  slug: criteo-creative-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Gateway API from Criteo — 3 operation(s) for gateway.
  name: Criteo Gateway API
  slug: criteo-gateway-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Reco API from Criteo — 8 operation(s) for reco.
  name: Criteo Reco API
  slug: criteo-reco-api
- baseURL: https://api.criteo.com/2026-07/retail-media
  baseurl_source: declared
  description: The Segment API from Criteo — 7 operation(s) for segment.
  name: Criteo Segment API
  slug: criteo-segment-api
artifact_total: 32
collections:
- collection_type: open
  name: Criteo API
  slug: open-criteo-commerce-grid-api
- collection_type: open
  name: Criteo API
  slug: open-criteo-marketing-solutions-api
- collection_type: open
  name: Criteo API
  slug: open-criteo-retail-media-api
- collection_type: open
  name: Criteo Retail Media API
  slug: open-criteo
common:
- group: other
  href: https://artifacts.apis.io/criteo/capabilities/criteo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/criteo-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/criteo/overlays/criteo-marketing-solutions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/criteo-marketing-solutions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/criteo/overlays/criteo-commerce-grid-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/criteo-commerce-grid-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/criteo/agentic-access/criteo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/criteo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/criteo/security/criteo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/criteo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/criteo/security/criteo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/criteo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/criteo/security/criteo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/criteo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/criteo/authentication/criteo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/criteo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/criteo/scopes/criteo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/criteo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/criteo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/criteo
- group: company
  title: ''
  type: Website
  url: https://www.criteo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.criteo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.criteo.com/retail-media/docs/welcome-to-criteo
- group: company
  title: ''
  type: Blog
  url: https://www.criteo.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.criteo.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.criteo.com/legal/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.criteo.com/llms.txt
- group: build
  href: https://artifacts.apis.io/criteo/packages/criteo-packages.yml
  title: ''
  type: Packages
  url: packages/criteo-packages.yml
- group: build
  href: https://artifacts.apis.io/criteo/packages/criteo-packages.yml
  title: ''
  type: SDKs
  url: packages/criteo-packages.yml
- group: agent
  href: https://artifacts.apis.io/criteo/well-known/criteo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/criteo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/criteo/well-known/criteo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/criteo-security.txt
- group: other
  href: https://artifacts.apis.io/criteo/a2a/criteo-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/criteo-a2a.yml
- group: agent
  href: https://artifacts.apis.io/criteo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/criteo/llms/criteo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/criteo-llms.txt
- group: design
  href: https://artifacts.apis.io/criteo/conformance/criteo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/criteo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.criteo.com/
- group: design
  href: https://artifacts.apis.io/criteo/errors/criteo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/criteo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/criteo/lifecycle/criteo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/criteo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.criteo.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.criteo.com/criteo-apis/docs/versioning-policy
- group: design
  href: https://artifacts.apis.io/criteo/conventions/criteo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/criteo-conventions.yml
- group: operate
  href: https://artifacts.apis.io/criteo/changelog/criteo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/criteo-changelog.yml
- group: design
  href: https://artifacts.apis.io/criteo/components/criteo-components.yml
  title: ''
  type: Components
  url: components/criteo-components.yml
- group: design
  href: https://artifacts.apis.io/criteo/data-model/criteo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/criteo-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/criteo/plans/criteo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/criteo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/criteo/rate-limits/criteo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/criteo-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://www.criteo.com/.well-known/security.txt
- group: commercial
  href: https://artifacts.apis.io/criteo/finops/criteo-finops.yml
  title: ''
  type: FinOps
  url: finops/criteo-finops.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/realcriteo/workspace/criteo/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.criteo.com/criteo-apis/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.criteo.com/criteo-apis/docs/connect-to-the-api
- group: operate
  title: ''
  type: Support
  url: https://help.criteo.com/
- group: start
  title: ''
  type: Login
  url: https://partners.criteo.com/
- group: other
  href: https://artifacts.apis.io/criteo/overlays/criteo-retail-media-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/criteo-retail-media-overlay.yaml
created: '2025-03-01'
description: 'Criteo is a global commerce media company whose Retail Media, Marketing Solutions and Commerce Grid platforms let retailers, brands, agencies and partners create, launch and measure onsite and offsite commerce advertising. Criteo publishes three live OpenAPI 3.0.1 documents at api.criteo.com covering 219 operations: campaign and line-item management, keyword and promoted-product targeting, audience segments and contact lists, retailer catalogs, account and brand hierarchies, balances and billing, creative and product-boost management, and demand-side and supply-side analytics. Authentication is OAuth 2.0 with client-credentials and authorization-code grants and 22 scopes of the form <Service>_<Domain>_<Level>. Criteo ships officially supported Python, PHP and Java SDKs, a public Postman workspace, an llms.txt docs index, an A2A agent card, a published Agent Skill, and two remote MCP servers — an anonymous documentation server and an OAuth-protected API server at mcp.criteo.com.'
finops:
- has_sources: true
  method: derived
  name: Criteo Finops
  primary_unit: ''
  service_category: ''
  slug: criteo-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/criteo.png
layout: provider
mcp_servers:
- description: Remote MCP server at developers.criteo.com; 3 tools listed.
  name: Criteo MCP Server
  slug: criteo-mcp-yml
modified: '2026-08-13'
name: Criteo
nav: Providers
network: true
overview: 'Criteo publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Advertiser API, Analytics API, and 10 more. Tagged areas include Advertising, Agent Skills, Analytics, Audiences, and Campaigns.


  The Criteo catalog on APIs.io includes 1 Spectral governance ruleset.


  Criteo''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, support, and 38 more developer resources.'
plans:
- name: Criteo Plans Pricing
  plan_count: 0
  slug: criteo-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Criteo Rate Limits
  slug: criteo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Criteo API Rules
  rule_count: 59
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 12
  slug: criteo-rules
scopes:
- name: Criteo Scopes
  scope_count: 22
  slug: criteo-scopes
  summary_line: 22 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 61.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 48.2
    developer_ergonomics: 63.7
    discoverability: 80.0
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 58.3
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/criteo/criteo-2026-06-20T175235.png
security:
- kind: authentication
  name: Criteo Authentication
  slug: criteo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Criteo Domain Security
  slug: criteo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Criteo Vulnerability Disclosure
  slug: criteo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Criteo Trust Center
  slug: criteo-trust-center
  summary_line: SOC 2, SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001
skill_count: 4
skills:
- name: Build an audience segment and target a line item or ad set with it
  slug: criteo-build-and-target-an-audience
- name: Fund a balance and launch a Retail Media campaign
  slug: criteo-fund-a-balance-and-launch-a-campaign
- name: Criteo
  slug: criteo-published-skill
- name: Run an async Retail Media report and collect the output
  slug: criteo-run-an-async-report
slug: criteo
tags:
- Advertising
- Agent Skills
- Analytics
- Audiences
- Campaigns
- Catalog
- Commerce
- Commerce Media
- Display Advertising
- Marketing
- MCP
- Media
- OAuth
- OpenAPI
- Reporting
- Retail
- Retail Media
- Sponsored Products
- A2A
- AdTech
- Authentication
website: https://www.criteo.com/
---
