---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://blazefeed.clipro.tv
  baseurl_source: declared
  description: The Feed API from WSC Sports — 7 operation(s) for feed.
  name: WSC Sports Feed API
  slug: wsc-sports-feed-api
artifact_total: 12
asyncapis:
- description: ''
  name: Wsc Sports Content Webhooks
  slug: wsc-sports-content-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://wsc-sports.com/feed/
- group: auth
  href: https://artifacts.apis.io/wsc-sports/security/wsc-sports-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wsc-sports-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wsc-sports.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.wsc-sports.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.wsc-sports.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dev.wsc-sports.com/reference/getstories
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.wsc-sports.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WSCSports
- group: company
  title: ''
  type: Blog
  url: https://wsc-sports.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://wsc-sports.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://wsc-sports.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wsc-sports.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wsc-sports.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/wsc-sports/llms/wsc-sports-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wsc-sports-llms.txt
- group: agent
  href: https://artifacts.apis.io/wsc-sports/mcp/wsc-sports-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wsc-sports-mcp.yml
- group: build
  href: https://artifacts.apis.io/wsc-sports/mcp/wsc-sports-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/wsc-sports-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/wsc-sports/packages/wsc-sports-packages.yml
  title: ''
  type: Packages
  url: packages/wsc-sports-packages.yml
- group: build
  href: https://artifacts.apis.io/wsc-sports/packages/wsc-sports-packages.yml
  title: ''
  type: SDKs
  url: packages/wsc-sports-packages.yml
- group: design
  href: https://artifacts.apis.io/wsc-sports/components/wsc-sports-components.yml
  title: ''
  type: Components
  url: components/wsc-sports-components.yml
- group: operate
  href: https://artifacts.apis.io/wsc-sports/changelog/wsc-sports-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wsc-sports-changelog.yml
- group: design
  href: https://artifacts.apis.io/wsc-sports/lifecycle/wsc-sports-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wsc-sports-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/wsc-sports/lifecycle/wsc-sports-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/wsc-sports-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wsc-sports/conventions/wsc-sports-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wsc-sports-conventions.yml
- group: design
  href: https://artifacts.apis.io/wsc-sports/conformance/wsc-sports-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wsc-sports-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wsc-sports/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/wsc-sports/plans/wsc-sports-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wsc-sports-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wsc-sports/rate-limits/wsc-sports-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wsc-sports-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/wsc-sports/asyncapi/wsc-sports-content-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wsc-sports-content-webhooks.yml
- group: other
  href: https://artifacts.apis.io/wsc-sports/overlays/wsc-sports-blaze-feed-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wsc-sports-blaze-feed-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/wsc-sports/data-model/wsc-sports-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wsc-sports-data-model.yml
- group: design
  href: https://artifacts.apis.io/wsc-sports/errors/wsc-sports-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wsc-sports-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/wsc-sports/authentication/wsc-sports-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wsc-sports-authentication.yml
- group: build
  href: https://artifacts.apis.io/wsc-sports/examples/wsc-sports-trending-recommendations.json
  title: ''
  type: Examples
  url: examples/wsc-sports-trending-recommendations.json
created: '2026-09-04'
description: 'WSC Sports Technologies is an Israeli sports-technology company whose AI platform automatically watches live sports broadcasts, identifies the moments that matter, and generates personalized short-form video — highlights, Stories and Moments — for leagues, broadcasters and rights holders. The developer surface is the Experiences product: a mobile-first embeddable SDK for iOS, Android, Web, React Native and Flutter that renders Stories, Moments and Videos inside a customer app, backed by the Arena CMS and the server-side Blaze Feed API, a read-only REST content-catalog and trending-recommendations API published as OpenAPI 3.0.1 at blazefeed.clipro.tv, complemented by outbound content-change webhooks and a public remote MCP server for AI coding assistants.'
examples:
- key_count: 5
  name: Wsc Sports Trending Recommendations
  slug: wsc-sports-trending-recommendations
finops:
- has_sources: true
  method: derived
  name: Wsc Sports Finops
  primary_unit: ''
  service_category: ''
  slug: wsc-sports-finops
  template: true
image: https://wsc-sports.com/wp-content/uploads/2024/05/Sharing-Image-1-1.png
layout: provider
mcp_servers:
- description: Remote MCP server at dev.wsc-sports.com; 6 tools listed.
  name: WSC Sports Experiences
  slug: wsc-sports-experiences
modified: '2026-10-06'
name: WSC Sports
nav: Providers
network: true
overview: 'WSC Sports publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Feed API. Tagged areas include Company, Sports, Video, Media, and Artificial Intelligence.


  The WSC Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WSC Sports'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Wsc Sports Plans Pricing
  plan_count: 0
  slug: wsc-sports-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Wsc Sports Rate Limits
  slug: wsc-sports-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: WSC Sports API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: wsc-sports-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.9
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 44.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/wsc-sports/wsc-sports-2026-10-11T195219.png
security:
- kind: authentication
  name: Wsc Sports Authentication
  slug: wsc-sports-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wsc Sports Domain Security
  slug: wsc-sports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: wsc-sports-sync-content-catalog
  slug: wsc-sports-sync-content-catalog
- name: wsc-sports-trending-content
  slug: wsc-sports-trending-content
slug: wsc-sports
tags:
- Company
- Sports
- Video
- Media
- Artificial Intelligence
- Content
- Streaming
- SDK
- Highlights
- Personalization
website: https://wsc-sports.com/
---
