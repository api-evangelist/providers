---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Dailyhunt Agentic Access
  operation_count: 15
  slug: dailyhunt-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 2
apis:
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Create and read a vendor catalog.
  name: Dailyhunt Catalog API
  slug: dailyhunt-catalog-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Discovery of the content channels a partner is entitled to consume.
  name: Dailyhunt Channels API
  slug: dailyhunt-channels-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Paginated retrieval of the content cards inside a channel, plus keyword search.
  name: Dailyhunt Content Fetch API
  slug: dailyhunt-content-fetch-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Live cricket match score and commentary streaming.
  name: Dailyhunt Cricket API
  slug: dailyhunt-cricket-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Fetch the feedback options to display to a user and submit the user's selection.
  name: Dailyhunt Feedback API
  slug: dailyhunt-feedback-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: The languages Dailyhunt's content feeds support.
  name: Dailyhunt Languages API
  slug: dailyhunt-languages-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Batch create, update and delete products inside a catalog, and poll batch status.
  name: Dailyhunt Products API
  slug: dailyhunt-products-api
- baseURL: http://feed.dailyhunt.in/api/v2/syndication
  baseurl_source: declared
  description: Partner callback reporting which cards a user actually saw.
  name: Dailyhunt Tracking API
  slug: dailyhunt-tracking-api
artifact_total: 21
collections:
- collection_type: postman
  name: Dailyhunt Content Syndication
  slug: postman-dailyhunt-content-syndication
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dailyhunt E-Commerce Shopping Catalog API
  slug: open-dailyhunt-catalog-api
- collection_type: open
  name: Dailyhunt Content Syndication Channels API
  slug: open-dailyhunt-channels-api
- collection_type: open
  name: Dailyhunt Content Syndication Content Fetch API
  slug: open-dailyhunt-content-fetch-api
- collection_type: open
  name: Dailyhunt Content Syndication Cricket API
  slug: open-dailyhunt-cricket-api
- collection_type: open
  name: Dailyhunt Content Syndication Feedback API
  slug: open-dailyhunt-feedback-api
- collection_type: open
  name: Dailyhunt Content Syndication Languages API
  slug: open-dailyhunt-languages-api
- collection_type: open
  name: Dailyhunt E-Commerce Shopping Catalog Products API
  slug: open-dailyhunt-products-api
- collection_type: open
  name: Dailyhunt Content Syndication Tracking API
  slug: open-dailyhunt-tracking-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dailyhunt-content-syndication-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.dailyhunt.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dailyhunt.in/ads/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dailyhunt.in/ads/
- group: docs
  title: ''
  type: APIReference
  url: https://api-syndication.dailyhunt.in/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-syndication.dailyhunt.in/
- group: company
  title: ''
  type: Blog
  url: http://developer.dailyhunt.in/ads/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dailyhunt
- group: operate
  title: ''
  type: Support
  url: https://verse.in/contact-us.php
- group: start
  title: ''
  type: SignUp
  url: https://direct.dailyhunt.in/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://direct.dailyhunt.in/help/v2/ad-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://m.dailyhunt.in/privacy
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/8670292/SVmzsvnm
- group: auth
  title: ''
  type: Authentication
  url: authentication/dailyhunt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dailyhunt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dailyhunt-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dailyhunt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dailyhunt-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dailyhunt-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dailyhunt-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dailyhunt-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/dailyhunt-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/dailyhunt-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dailyhunt-well-known.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/dailyhunt-unified-metrics.proto
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dailyhunt-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dailyhunt-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dailyhunt-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dailyhunt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dailyhunt-domain-security.yml
created: '2026-08-04'
description: 'Dailyhunt is India''s largest local-language content and news aggregation platform, operated by VerSe Innovation (Bengaluru). It aggregates news, video, and short-form "DailyShare" cards from more than 600 publisher partners across fourteen Indian languages and distributes them through its own apps, mobile web and PWA, and — for approved partners — through a signed Content Syndication API that pushes the same catalogue into partner apps, OEM device home screens and browsers. Alongside syndication, Dailyhunt runs an advertising stack: the Dailyhunt Direct self-serve ad platform, a JavaScript Tracker SDK (with a Google Tag Manager path) for down-funnel conversion tracking on advertiser sites, and an E-Commerce Shopping Catalog API for vendors to batch-upload product feeds. VerSe Innovation also operates the Josh short-video app. API access is partner-gated: keys, secrets and partner codes are provisioned during onboarding rather than self-service, and the production feed host
  is not publicly resolvable.'
image: https://m.dailyhunt.in/favicon.ico
layout: provider
modified: '2026-08-04'
name: Dailyhunt
nav: Providers
network: true
overview: 'Dailyhunt publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Channels API, Content Fetch API, and 5 more. Tagged areas include Company, News, Media, Content Syndication, and Content.


  Dailyhunt''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 13.9
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dailyhunt/refs/heads/main/screenshots/dailyhunt-2026-08-07T164025.png
security:
- kind: authentication
  name: Dailyhunt Authentication
  slug: dailyhunt-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Dailyhunt Domain Security
  slug: dailyhunt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dailyhunt
tags:
- Company
- News
- Media
- Content Syndication
- Content
- Advertising
- Video
- Localization
- India
- Mobile
website: https://www.dailyhunt.in/
---
