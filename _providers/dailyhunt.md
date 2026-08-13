---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Dailyhunt Agentic Access
  operation_count: 15
  slug: dailyhunt-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 8
apis:
- description: Create and read a vendor catalog.
  name: Dailyhunt Catalog API
  slug: dailyhunt-catalog-api
- description: Discovery of the content channels a partner is entitled to consume.
  name: Dailyhunt Channels API
  slug: dailyhunt-channels-api
- description: Paginated retrieval of the content cards inside a channel, plus keyword search.
  name: Dailyhunt Content Fetch API
  slug: dailyhunt-content-fetch-api
- description: Live cricket match score and commentary streaming.
  name: Dailyhunt Cricket API
  slug: dailyhunt-cricket-api
- description: Fetch the feedback options to display to a user and submit the user's selection.
  name: Dailyhunt Feedback API
  slug: dailyhunt-feedback-api
- description: The languages Dailyhunt's content feeds support.
  name: Dailyhunt Languages API
  slug: dailyhunt-languages-api
- description: Batch create, update and delete products inside a catalog, and poll batch status.
  name: Dailyhunt Products API
  slug: dailyhunt-products-api
- description: Partner callback reporting which cards a user actually saw.
  name: Dailyhunt Tracking API
  slug: dailyhunt-tracking-api
artifact_total: 13
collections:
- collection_type: postman
  name: Dailyhunt Content Syndication
  slug: postman-dailyhunt-content-syndication
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: dailyhunt-mcp.yml
  slug: dailyhunt-mcpyml
modified: '2026-08-04'
name: Dailyhunt
nav: Providers
network: true
overview: 'Dailyhunt publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Channels API, Content Fetch API, and 5 more. Tagged areas include Company, News, Media, Content Syndication, and Content.


  Dailyhunt''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.2
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
