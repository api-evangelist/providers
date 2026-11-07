---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'First-party hosted Model Context Protocol server that exposes the same ad index to AI assistants (Claude, Codex, Cursor, Gemini). Streamable HTTP at https://api.adsmom.com/mcp, protected by OAuth 2.0 '
  name: Adsmom MCP Server
  slug: adsmom-mcp-server
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Account API from Adsmom Inc. — 1 operation(s) for account.
  name: Adsmom Inc. Account API
  slug: adsmom-inc-account-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Analytics · Google API from Adsmom Inc. — 7 operation(s) for analytics · google.
  name: Adsmom Inc. Analytics · Google API
  slug: adsmom-inc-analytics-google-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Analytics · Meta API from Adsmom Inc. — 7 operation(s) for analytics · meta.
  name: Adsmom Inc. Analytics · Meta API
  slug: adsmom-inc-analytics-meta-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Analytics · TikTok API from Adsmom Inc. — 9 operation(s) for analytics · tiktok.
  name: Adsmom Inc. Analytics · TikTok API
  slug: adsmom-inc-analytics-tiktok-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Explore · Google Ads API from Adsmom Inc. — 2 operation(s) for explore · google ads.
  name: Adsmom Inc. Explore · Google Ads API
  slug: adsmom-inc-explore-google-ads-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Explore · LinkedIn Ads API from Adsmom Inc. — 6 operation(s) for explore · linkedin ads.
  name: Adsmom Inc. Explore · LinkedIn Ads API
  slug: adsmom-inc-explore-linkedin-ads-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Explore · Meta Ads API from Adsmom Inc. — 4 operation(s) for explore · meta ads.
  name: Adsmom Inc. Explore · Meta Ads API
  slug: adsmom-inc-explore-meta-ads-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Explore · TikTok Ads API from Adsmom Inc. — 6 operation(s) for explore · tiktok ads.
  name: Adsmom Inc. Explore · TikTok Ads API
  slug: adsmom-inc-explore-tiktok-ads-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Insights · Google API from Adsmom Inc. — 4 operation(s) for insights · google.
  name: Adsmom Inc. Insights · Google API
  slug: adsmom-inc-insights-google-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Insights · Instagram Organic API from Adsmom Inc. — 4 operation(s) for insights · instagram organic.
  name: Adsmom Inc. Insights · Instagram Organic API
  slug: adsmom-inc-insights-instagram-organic-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Insights · LinkedIn API from Adsmom Inc. — 4 operation(s) for insights · linkedin.
  name: Adsmom Inc. Insights · LinkedIn API
  slug: adsmom-inc-insights-linkedin-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Insights · Meta API from Adsmom Inc. — 4 operation(s) for insights · meta.
  name: Adsmom Inc. Insights · Meta API
  slug: adsmom-inc-insights-meta-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Insights · TikTok API from Adsmom Inc. — 4 operation(s) for insights · tiktok.
  name: Adsmom Inc. Insights · TikTok API
  slug: adsmom-inc-insights-tiktok-api
- baseURL: https://api.adsmom.com
  baseurl_source: declared
  description: The Insights · TikTok Organic API from Adsmom Inc. — 4 operation(s) for insights · tiktok organic.
  name: Adsmom Inc. Insights · TikTok Organic API
  slug: adsmom-inc-insights-tiktok-organic-api
artifact_total: 28
common:
- group: other
  href: https://artifacts.apis.io/adsmom-inc/capabilities/adsmom-inc-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adsmom-inc-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://adsmom.com
- group: docs
  title: ''
  type: Documentation
  url: https://adsmom.com/product/api
- group: docs
  title: ''
  type: APIReference
  url: https://adsmom.com/product/api
- group: docs
  href: https://artifacts.apis.io/adsmom-inc/openapi/_original/adsmom-inc-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/adsmom-inc-openapi.json
- group: agent
  href: https://artifacts.apis.io/adsmom-inc/mcp/adsmom-inc-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adsmom-inc-mcp.yml
- group: build
  href: https://artifacts.apis.io/adsmom-inc/mcp/adsmom-inc-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adsmom-inc-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/adsmom-inc/well-known/adsmom-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsmom-inc-well-known.yml
- group: auth
  href: https://artifacts.apis.io/adsmom-inc/authentication/adsmom-inc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adsmom-inc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adsmom-inc/scopes/adsmom-inc-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adsmom-inc-scopes.yml
- group: design
  href: https://artifacts.apis.io/adsmom-inc/errors/adsmom-inc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adsmom-inc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adsmom-inc/conventions/adsmom-inc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adsmom-inc-conventions.yml
- group: design
  href: https://artifacts.apis.io/adsmom-inc/data-model/adsmom-inc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adsmom-inc-data-model.yml
- group: operate
  href: https://artifacts.apis.io/adsmom-inc/rate-limits/adsmom-inc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adsmom-inc-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/adsmom-inc/lifecycle/adsmom-inc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adsmom-inc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/adsmom-inc/conformance/adsmom-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adsmom-inc-conformance.yml
- group: other
  href: https://artifacts.apis.io/adsmom-inc/overlays/adsmom-inc-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adsmom-inc-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/adsmom-inc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/adsmom-inc/llms/adsmom-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adsmom-inc-llms.txt
- group: auth
  href: https://artifacts.apis.io/adsmom-inc/security/adsmom-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsmom-inc-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://adsmom.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adsmom.com/pricing
- group: commercial
  href: https://artifacts.apis.io/adsmom-inc/plans/adsmom-inc-plans.yml
  title: ''
  type: Plans
  url: plans/adsmom-inc-plans.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.adsmom.com/
- group: start
  title: ''
  type: Login
  url: https://app.adsmom.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsmom.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsmom.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adsmom
created: '2026-07-17'
description: Adsmom (SIA Adsmom) is a Latvia-based AI-powered ad intelligence platform that indexes 200M+ ads from Meta, TikTok and Google, decodes them with AI, and gives brands, agencies and research teams a clear read on what competitors are running and what is actually working. The platform covers ad search across a competitor library, spend and creative-strategy insights, an AI chat analyst ("Sense"), real-time competitor alerts, and branded reporting. Adsmom exposes its ad index programmatically via both a hosted Model Context Protocol (MCP) server — for connecting AI assistants such as Claude, Codex, Cursor and Gemini — and a REST API for server-to-server pipelines, internal tools and scheduled jobs. API and MCP access are included on all paid tiers. The REST API publishes a public OpenAPI 3.0.0 description at api.adsmom.com covering 78 operations across four paid-ad platforms (Meta, TikTok, Google, LinkedIn) plus TikTok and Instagram organic accounts, grouped into Explore (ad search
  and hydration), Insights (tracked-advertiser management, AI summaries, weekly reports) and Analytics (reach, activity, share of voice, runtime, creative mix, targeting). Adsmom is a 500 Global portfolio company and raised ~$610K in early 2025.
finops:
- has_sources: true
  method: derived
  name: Adsmom Inc Finops
  primary_unit: ''
  service_category: ''
  slug: adsmom-inc-finops
  template: true
image: https://adsmom.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.adsmom.com over streamable HTTP.
  name: Adsmom MCP Server
  slug: adsmom
modified: '2026-09-16'
name: Adsmom
nav: Providers
network: true
overview: 'Adsmom publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Inc. Account API, Inc. Analytics · Google API, Inc. Analytics · Meta API, and 12 more. Tagged areas include Company, Advertising, Ad Intelligence, Competitive Intelligence, and Marketing.


  The Adsmom catalog on APIs.io includes 1 Spectral governance ruleset.


  Adsmom''s developer surface includes documentation, API reference, authentication, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Adsmom Inc Plans
  plan_count: 3
  slug: adsmom-inc-plans
- name: Adsmom Inc Price Estimates
  plan_count: 0
  slug: adsmom-inc-price-estimates
random_paper: 16
rate_limits:
- limit_count: 1
  name: Adsmom Inc Rate Limits
  slug: adsmom-inc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Adsmom API Rules
  rule_count: 52
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 4
  slug: adsmom-inc-rules
scopes:
- name: Adsmom Inc Scopes
  scope_count: 4
  slug: adsmom-inc-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 55.5
    catalog_earned_first_party: 12.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 40.1
    developer_ergonomics: 32.7
    discoverability: 75.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - latvia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 43.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adsmom-inc/adsmom-inc-2026-07-25T181702.png
security:
- kind: authentication
  name: Adsmom Inc Authentication
  slug: adsmom-inc-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Adsmom Inc Domain Security
  slug: adsmom-inc-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Analyze TikTok creative strategy
  slug: adsmom-inc-analyze-tiktok-creative-strategy
- name: Pull a competitor's ads and their reach
  slug: adsmom-inc-pull-a-competitors-ads-and-reach
- name: Start tracking a competitor
  slug: adsmom-inc-start-tracking-a-competitor
- name: Build a weekly competitive briefing
  slug: adsmom-inc-weekly-competitive-briefing
slug: adsmom-inc
tags:
- Company
- Advertising
- Ad Intelligence
- Competitive Intelligence
- Marketing
- Artificial Intelligence
- MCP
- Software-as-a-Service
- OpenAPI
- REST
- Analytics
- Social Media
- Agent-Native
website: https://adsmom.com
---
