---
agent_readiness:
  band: agent-ready
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
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://blazefeed.clipro.tv
  baseurl_source: declared
  description: Server-side pull API for the WSC Sports Experiences content catalog. Seven read-only GET operations return Stories, Moments and Videos metadata — filtered by title, labels, status, geo, live state, cr
  name: WSC Sports Blaze Feed API
  slug: wsc-sports-blaze-feed-api
artifact_total: 8
asyncapis:
- description: ''
  name: Wsc Sports Content Webhooks
  slug: wsc-sports-content-webhooks
common:
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/wsc-sports-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wsc-sports-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/wsc-sports-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/wsc-sports-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wsc-sports-packages.yml
- group: design
  title: ''
  type: Components
  url: components/wsc-sports-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wsc-sports-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wsc-sports-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/wsc-sports-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wsc-sports-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wsc-sports-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wsc-sports-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wsc-sports-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wsc-sports-content-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wsc-sports-blaze-feed-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/wsc-sports-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wsc-sports-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wsc-sports-authentication.yml
- group: build
  title: ''
  type: Examples
  url: examples/wsc-sports-trending-recommendations.json
created: '2026-09-04'
description: 'WSC Sports Technologies is an Israeli sports-technology company whose AI platform automatically watches live sports broadcasts, identifies the moments that matter, and generates personalized short-form video — highlights, Stories and Moments — for leagues, broadcasters and rights holders. The developer surface is the Experiences product: a mobile-first embeddable SDK for iOS, Android, Web, React Native and Flutter that renders Stories, Moments and Videos inside a customer app, backed by the Arena CMS and the server-side Blaze Feed API, a read-only REST content-catalog and trending-recommendations API published as OpenAPI 3.0.1 at blazefeed.clipro.tv, complemented by outbound content-change webhooks and a public remote MCP server for AI coding assistants.'
examples:
- key_count: 5
  name: Wsc Sports Trending Recommendations
  slug: wsc-sports-trending-recommendations
image: https://wsc-sports.com/wp-content/uploads/2024/05/Sharing-Image-1-1.png
layout: provider
mcp_servers:
- description: ''
  name: WSC Sports Experiences
  slug: wsc-sports-experiences
modified: '2026-09-04'
name: WSC Sports
nav: Providers
network: true
overview: 'WSC Sports publishes 1 API on the [APIs.io](https://apis.io/) network: Blaze Feed API. Tagged areas include Company, Sports, Video, Media, and Artificial Intelligence.


  The WSC Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WSC Sports'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 25 more developer resources.'
plans:
- name: Wsc Sports Plans Pricing
  plan_count: 0
  slug: wsc-sports-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Wsc Sports Rate Limits
  slug: wsc-sports-rate-limits
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 50.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 44.9
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Wsc Sports Authentication
  slug: wsc-sports-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wsc Sports Domain Security
  slug: wsc-sports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
